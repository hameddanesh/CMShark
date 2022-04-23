import sqlite3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time
import re


class MiningPoolStats:
    def __init__(self, browser='firefox'):
        super().__init__()
        self.con = sqlite3.connect('CMShark.db')
        self.myCursor = self.con.cursor()

        self.coinLinks = []
        self.coinNames = []
        self.coinSymbols = []

        if browser == 'firefox':
            self.driver = webdriver.Firefox(
                executable_path='./geckodriver')

        elif browser == 'chrome':
            self.driver = webdriver.Chrome('./chromedriver')
        else:
            print('browser not supported!')
            return

    def ReadCoinNames(self):
        self.driver.get('https://miningpoolstats.stream/')

        try:
            # wait for page to load
            coinLength = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "coins_length")))

            # select the all coin option on the target website
            coinSelect = Select(coinLength.find_element_by_tag_name("select"))
            coinSelect.select_by_visible_text('All')

        except:
            print("an error happend!")
            self.driver.quit()

        self.driver.implicitly_wait(5)  # wait for ajax to load coin data
        coinTable = self.driver.find_element_by_id('coins')
        coins = coinTable.find_elements(By.TAG_NAME, 'a')
        symbols = coinTable.find_elements(By.CLASS_NAME, 'homesymbol')

        # self.UpdatePoolList('https://miningpoolstats.stream/bitcoin')
        for i in range(0, (len(coins)-1)):
            print(str(str(i+1)+"  -  " +
                  coins[i+1].get_attribute('href'))+" ----- " + symbols[i].text)
            self.UpdateBlacklist(
                str(coins[i+1].get_attribute('href')).split('/')[3])
            self.UpdateBlacklist(coins[i].text)
            self.UpdateBlacklist(symbols[i].text)

            self.UpdatePoolList(coins[i+1].get_attribute('href'))

        self.driver.close()

    def UpdateBlacklist(self, _word):
        word = _word.lower()
        self.myCursor.execute(
            'SELECT COUNT(blackword_id) FROM blacklist WHERE blackword_word="'+word+'"')
        exists = self.myCursor.fetchone()

        if exists[0] == 0:
            self.myCursor.execute(
                'INSERT INTO blacklist(blackword_word) VALUES("'+word+'")')
            self.con.commit()

    def UpdatePoolList(self, URL):
        self.driver.execute_script("window.open('about:blank', 'secondtab');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(URL)

        poolTable = self.driver.find_element_by_id('pools')
        pools = poolTable.find_elements_by_tag_name('a')

        for pool in pools:
            temp = pool.text.strip()
            if temp != "" and len(temp.split('.')) >= 2:

                _poolUrl = pool.get_attribute('href').split(
                    '/')[2].replace('www.', '').split(':')[0].split('.')
                poolUrl = _poolUrl[len(_poolUrl)-2] + \
                    "."+_poolUrl[len(_poolUrl)-1]
                # print(poolUrl)

                self.myCursor.execute(
                    'SELECT COUNT(pool_id) FROM pools WHERE pool_name="'+poolUrl.lower()+'"')
                exists = self.myCursor.fetchone()

                if exists[0] == 0:
                    self.myCursor.execute(
                        'INSERT INTO pools(pool_name) VALUES("'+poolUrl.lower()+'")')
                    self.con.commit()
                    print('\tpool: '+poolUrl+' saved successfuly')

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])


miningpoolstats = MiningPoolStats()
miningpoolstats.ReadCoinNames()
