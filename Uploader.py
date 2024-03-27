import sqlite3
con = sqlite3.connect('office.db')
cur = con.cursor()
f = open('F:\Docs\OneDrive\Documents\childer.txt', 'r')
linenumber = 0
for line in f:
    cur.execute(line)
    cur.execute('commit')
    linenumber = linenumber + 1
    print(linenumber)
f.close()
con.close()
