import mysql.connector
connectionstring = mysql.connector.connect(host='25.48.184.239',
                                           database='domicile_reports',
                                           user='superadmin',
                                           password='Superadmin')
con = connectionstring
try:

    if con.is_connected():
        Query = "Select last_insert_id();"
        cur = con.cursor()
        cur.execute(Query)
        data = cur.fetchall()
        print(data[0][0])

        con.close()
except Exception as e:
    print("Can not connect to db. {} Occured".format(e))
