import sqlite3
con = sqlite3.connect('office.db')
cur = con.cursor()
cur.execute(
    'Select * from Childern;')
no_of_rows = 0
data = cur.fetchall()
for row in data:
    no_of_rows = no_of_rows + 1
print(no_of_rows)
# f = Open ('Childern_Data.txt', 'w')
# for row in data:
#     qur = 'Insert Into Childern'
#     f.write(qur)
# f.close()
