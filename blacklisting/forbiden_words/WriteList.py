import sqlite3

con=sqlite3.connect('CMShark.db')

myCursor=con.cursor();
fileHandler=open("blacklisting/forbiden_words/forbiden-words.csv","r")
for recored in fileHandler:
   myCursor.execute('INSERT into blacklist(blackword_word) values("'+recored.rstrip()+'")')
   print(recored.rstrip())

con.commit()
myCursor.close()
con.close()