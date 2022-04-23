import sqlite3
import time


class Adder:
    def __init__(self):
        super().__init__()
        self.con = sqlite3.connect('CMShark.db')

    def Add(self):
        myFile=open("./blacklisting/cmtracker_cjlist/cryptojacking_domain_list.csv","r")
        cjlist=myFile.readlines()

        myCursor = self.con.cursor()

        for _cj in cjlist:
            cj=_cj.strip("\n")
            
            myCursor.execute('SELECT COUNT(pool_name) FROM pools WHERE pool_name="'+cj+'"')
            exists = myCursor.fetchone()

            if exists[0] == 0:
                myCursor2 = self.con.cursor()
                myCursor2.execute(
                'INSERT INTO pools(pool_name) VALUES("'+cj+'")')

    
if __name__=="__main__":
    adder=Adder()
    adder.Add()


