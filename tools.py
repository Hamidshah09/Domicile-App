import mysql.connector
from mysql.connector import Error
import json
def open_con(dictionary):
    try:
        f = open("config.json", "r")
        j_obj = json.load(f)
        f.close()
        con = mysql.connector.connect(host='{}'.format(j_obj['server_1']),
                                            database='domicile_reports',
                                            user='superadmin',
                                            password='Superadmin')
                                            #password='Superadmin12345'
        if con.is_connected:
            if dictionary == True:
                cur = con.cursor(dictionary=True)
            else:
                cur = con.cursor()
        return con, cur
    except Error as e:
        return e, 'Error'
def search_dict(dict_data_set, key_for_search, value, return_key):
    result = None
    for i in range(len(dict_data_set)):
        if dict_data_set[i][key_for_search] == value:
            result = dict_data_set[i][return_key]
            break

    return result, i