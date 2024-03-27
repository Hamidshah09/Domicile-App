import sqlite3
import mysql.connector
from mysql.connector import Error
con = sqlite3.connect('office.db')
cur = con.cursor()
cur.execute(
    'Select * from Childern where Father_CNIC in (Select CNIC from Domicile)')
tehsil_data = cur.fetchall()
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='domicile_reports',
                                         user='root',
                                         password='2891dimah')
    if connection.is_connected():
        cursor = connection.cursor()
        a = 0
        for data in tehsil_data:
            a += 1
            cursor.execute(
                "Insert Into Childern (Father_CNIC, Child_Name, Child_dob) values ('{}', '{}', '{}');".format(data[1], data[2], data[3]))
            cursor.execute('commit;')
        connection.close()
        print('{} Records Inserted'.format(a))
except Error as e:
    print(data[1], data[2])
    print("Error while connecting to MySQL", e)
