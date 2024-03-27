import mysql.connector
global my_dict
my_dict = {}


def Columns_dict():
    global my_dict
    try:
        con = mysql.connector.connect(host='25.48.184.239',
                                           database='domicile_reports',
                                           user='superadmin',
                                           password='Superadmin')
        if con.is_connected():
            cur = con.cursor(dictionary=True)
            cur.execute("SHOW COLUMNS FROM domicile;")
            data = cur.fetchall()
            my_dict = {}
            for row in data:
                my_dict[row['Field']] = ''

    except Exception as e:
        print('error while connecting to db ', e)


def Write_column():
    global my_dict
    with open('Columns.txt', 'w') as f:
        for item in my_dict:
            f.write("dict_name['{}'] =".format(item))
            f.write('\n')


def match_column():
    global my_dict
    with open(r'F:\Docs\OneDrive\Documents\sqlite_columns.txt', 'r') as f:
        content = f.read()
        column_list = content.split(',')
        columns = []
        for item in column_list:
            columns.append(item.strip())
        indx = 0
        for item in my_dict:
            # columns.append(item.strip())

            if item not in columns:
                print(item)


Columns_dict()
# Write_column()
match_column()
