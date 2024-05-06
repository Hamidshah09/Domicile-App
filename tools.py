from http import server
import socket
import mysql.connector
from mysql.connector import Error
import json
from tkinter import messagebox
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    local_ip = s.getsockname()[0]
    s.close()
    return local_ip

def open_con(dictionary):
    try:
        f = open("config.json", "r")
        j_obj = json.load(f)
        f.close()
        local_ip = get_local_ip()
        local_subnet = local_ip.split('.')[2]
        server_subnet = j_obj['server_1'].split('.')[2]
        if local_subnet != server_subnet:
            return "Your not on server network subnet.\nPlease check your config file", "Error"
        con = mysql.connector.connect(host='{}'.format(j_obj['server_1']),
                                            database='domicile_reports',
                                            user='superadmin',
                                            password='Superadmin')
                                            #password='28910203@dimaH'
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
if __name__ == '__main__':
    con, cur = open_con(False)
    if type(cur) is str:
        print(con)
# Query = "Select dispatch_id, dispatch_no, letter_id from dispatch_dairy where dispatch_id = 0;"
# cur.execute(Query)
# data = cur.fetchall()
# print(data)
# id = 11911
# for row in data:
#     id += 1
#     Query = "Update dispatch_dairy set dispatch_id = %s where dispatch_no = %s and letter_id = %s;"
#     cur.execute(Query, [id, row[1], row[2]])
#     con.commit()