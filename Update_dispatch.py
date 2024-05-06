
import mysql.connector
from mysql.connector import Error
from Validation import validate_date
import os
def open_con(dictionary):
    try:
        con = mysql.connector.connect(host=ip,
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
def get_input(inpt_text):
    inp = input(inpt_text)
    return inp

def get_date():
    letter_date =  ''
    validate_result = ''
    while validate_result != 'valid':
        letter_date = get_input("Enter Letter Issuance Date:-")
        validate_result = validate_date(letter_date)        
        if validate_result != 'valid':
            print(validate_result)
            print("valid format is 'yyyy-mm-dd'")
    return letter_date
def get_subject():
    subject = ''
    for i in range(101):
        subject += " "
    while len(subject) > 99:
        subject = get_input("Enter Letter Subject:-")        
        if len(subject) > 99:
            print("Subject shall be less than 99 characters")
        else:
            break
    return subject
def letter_to():
    to=''
    while len(to) < 10:
        to = get_input("Letter Addressed to:-")        
        if len(to) < 9:
            print("Letter address shall be atleast 10 characters")
        else:
            break
    return to
def add():
    
    
    letter_date = get_date()
    subject= get_subject()
    to = letter_to()
    print(f"--------------------------")
    print(f"Letter Date : {letter_date}")
    print(f"Subject     : {subject}")
    print(f"Letter To   : {to}")
    print(f"--------------------------")
    yesno = input("is above information correct? Procceding to Save?(y/n)")
    if yesno.upper() == 'Y':
        con, cur = open_con(False)
        if type(cur) is not str:
            cur.execute("Insert into office_letters (letter_date, subject, letter_to) values (%s, %s, %s);", [letter_date, subject, to])
            con.commit()
            cur.execute("Select office_letter_id from office_letters order by office_letter_id desc limit 1")
            l_id = cur.fetchone()
            cur.execute("Select Dispatch_No from dispatch_dairy order by Dispatch_ID desc Limit 1;")
            last_d_no = cur.fetchone()
            cur.execute("Insert into dispatch_dairy (Dispatch_No, Letter_Type, Letter_ID) values (%s, %s, %s);", [last_d_no[0]+1, 'Office Letter', l_id[0]])
            con.commit()
            print(f"Your Letter Dispatch No is {last_d_no[0]+1}")
        else:
            print(con)
def last_dispatch():
    con, cur = open_con(False)
    if type(cur) is not str:
        cur.execute("Select Dispatch_No from dispatch_dairy order by Dispatch_ID desc Limit 1;")
        last_d_no = cur.fetchone()
        print(f"Your last Dispatch No is {last_d_no[0]}")
    else:
        print(con)
def update(edit_input, letter_id, con, cur):
    
    if edit_input =='1':
        letter_date = get_date()
        query = "Update office_letters set letter_date = %s where office_letter_id = %s"
        cur.execute(query, [letter_date, letter_id])
        con.commit()
        print("Letter Date Updated.")
    elif edit_input =='2':
        subject = get_subject()
        query = "Update office_letters set subject = %s where office_letter_id = %s"
        cur.execute(query, [subject, letter_id])
        print("Subject Updated")
    elif edit_input =='3':
        letter_addressed = letter_to()
        query = "Update office_letters set letter_to = %s where office_letter_id = %s"
        cur.execute(query, [letter_addressed, letter_id])
        print("Letter Addressed to Updated.")

def edit():
    dispatch_no = ''
    while dispatch_no.isnumeric() == False:
        dispatch_no = get_input("Enter Dispatch No:-")
        if dispatch_no.isnumeric() == True:
            con, cur = open_con(False)
            Query = """select office_letter_id, letter_date, subject, letter_to 
                    from office_letters 
                    Join dispatch_dairy 
                    on dispatch_dairy.Letter_ID = office_letters.office_letter_id and dispatch_dairy.Letter_Type = 'Office Letter' 
                    where dispatch_dairy.Dispatch_No = %s;"""
            cur.execute(Query, [dispatch_no])
            data = cur.fetchall()
            if data is not None:
                if len(data) !=0:
                    for row in data:
                        print("------------------------------------------")
                        print("Letter Issuance Date     :     ", row[1])
                        print("Subject                  :     ",row[2])
                        print("Letter Addressed to      :     ",row[3])
                        print("------------------------------------------")
                        letter_id = row[0]
                    print("Enter 1 to update letter issuance date.")
                    print("Enter 2 to update subject.")
                    print("Enter 3 to update Letter addressed to.")
                    print("Enter 0 to exit from update")
                    print("------------------------------------------")
                    edit_input = 4
                    while edit_input != '0':
                        edit_input = get_input("Enter Choice:-")
                        update(edit_input, letter_id, con, cur)
                else:
                    print("Record not found.")
            else:
                print("Record not found.")            
        else:
            print("Dispatch No shall be digits.")
def help():
    print("add:                      To insert new dispatch number for any office letter")
    print("edit:                     To update a record")
    print("last:                     To check last dispatch number")
    print("help:                     To see the commands help")
    print("show ip:                  To see the server ip")
    print("set ip:                   To set new ip")
    print("check connection:         To test a database connection")
    print("exit:                     To exit from current programme")

def show_ip():
    print(f"Server Ip is {ip}")
def set_ip():
    print(f"Current Server Ip is {ip}")
    os.system('cmd /c "ipconfig > ip_.txt"')
    with open('ip_.txt', 'r') as f:
        for line in f.readlines():
            if line.find('192.168.') != -1:
                start_pos = line.find("192.168.")
                end_pos = line.find(".", start_pos+8)
                gateway = line[start_pos:end_pos]
                break
    new_ip= input(f"Please Provide New IP {gateway.strip()[:-1]}")
    if len(new_ip.strip()) != 0:
        return gateway.strip()[:-1] + new_ip
    else:
        return None
try:
    with open('server_ip.txt') as ip_file:
        ip = ip_file.read()
except Exception:
    ip = '192.168.18.14'
print("Dispatch Register Utility [Version 2.1]")
print("All Rights Reserved. H-Soft Corporation")
print(f"Server IP is {ip}")
print("type 'help' to see the command list")
inp =''
while inp!='exit':
    inp = input("Dispacher:-")
    if inp.lower() == 'add':
        add()
    elif inp.lower() == 'last':
        last_dispatch()
    elif inp.lower() == 'edit':
        edit()
    elif inp.lower() == 'help':
        help()
    elif inp.lower() == 'show ip':
        show_ip()
    elif inp.lower() == 'set ip':
        result = set_ip()
        if result is not None:
            with open('server_ip.txt', 'w') as f:
                f.write(result)
            print("Server Ip Updated")
            ip = result
    elif inp.lower() == 'check connection':
        con, cur = open_con(False)
        if type(cur) is str:
            print(con)
        else:
            print("Connection Ok")