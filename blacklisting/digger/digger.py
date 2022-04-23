import sqlite3
import pydig
import socket


class Digger:
    def __init__(self):
        super().__init__()
        self.con = sqlite3.connect('CMShark.db')

    def ReadPoolList(self):
        myCursor = self.con.cursor()
        myCursor.execute('SELECT pool_name FROM pools WHERE 1')
        return myCursor.fetchall()

    def Dig(self):
        pools = self.ReadPoolList()

        myCursor = self.con.cursor()
        myCursor.execute('DELETE FROM nsblacklist WHERE 1')
        myCursor.execute('UPDATE sqlite_sequence SET seq=0 WHERE name="nsblacklist"')

        print('digger started!')
        for pool in pools:
            self.WriteNSBlacklist(myCursor, pydig.query(pool[0], 'A'))
            self.WriteNSBlacklist(myCursor, pydig.query('www.'+pool[0], 'A'))
        
        myCursor.close()
        self.con.close()
        print('ip deging compelited!')



    def WriteNSBlacklist(self, myCursor, pool):

        for i in range(0, len(pool)):
            try:
                myCursor.execute(
                    'INSERT INTO nsblacklist(nsblackword_word) VALUES("'+pool[i]+'")')
                self.con.commit()
                print(pool[i])
            except sqlite3.IntegrityError:
                pass

    def IPCheck(self, input):
        try:
            socket.inet_aton(addr)
            return True
        except socket.error:
            return False


digger = Digger()
digger.Dig()
