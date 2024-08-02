from tkinter import *
from tkinter import ttk, messagebox
from DataEntry_Mysql import dataentry, Sysentry
from Monthly_Report import Monthly_Report
from NOC_Letter import NOC
from black_list import Black_List
from Cash_Report import Cash_Report
from NOC_for_ICT import NOC_ICT
from Cancellation_Letter import Canelation
from Verification_Letter import Verification
from Update_status import Update_Status
# from SystemEntry import Auto_entry
from settings import settings
from splash_screen_gui import splashscreen
from login import Login
# from PIL import ImageTk, Image
import json
import os
from tools import open_con

obj = splashscreen()
obj.run()
obj1 = Login()
obj1.login()
obj1.root.mainloop()
if obj1.login_status == False:
    exit()
window = Tk()
width_of_window = 610
screen_width = window.winfo_screenwidth()
left_cord = (screen_width/2)-(width_of_window/2)
window.geometry("610x680+{}+50".format(int(left_cord)))
window.title('CFC APP Verion 3.5')
f = open("config.json", "r")
j_obj = json.load(f)
f.close()
path = os.getcwd()
# path = path+r"\theme"

main_frame = Frame(window)  # 4c618f #bg='#24304a'
main_frame.pack(fill=BOTH, expand=1)
top_frame = Frame(main_frame)  # 4c618f #bg='#24304a'
top_frame.pack(fill=X, expand=1)
bottom_frame = Frame(main_frame)  # 4c618f #bg='#24304a'
bottom_frame.pack(fill=BOTH, expand=1)
# image_a = ImageTk.PhotoImage(Image.open(
#     r'C:\Users\Hamid Shah\Desktop\blck_galaxy.jpg'))

# background_label = Label(bottom_frame, image=image_a)
# background_label.place(x=0, y=0)  # relwidth=1, relheight=1
# 4c618f #bg='#24304a'78
# left1_frame = Frame(bottom_frame)
# left1_frame.pack(side=LEFT, fill=Y, expand=1)
# 4c618f #bg='#24304a'
# left2_frame = Frame(bottom_frame)
# left2_frame.pack(side=LEFT, fill=Y, expand=1)
# bottom_frame = Frame(bottom_frame)  # 4c618f #bg='#24304a'
# left3_frame.pack(side=LEFT, fill=Y, expand=1)
# background_image = PhotoImage(
#     'C:\\Users\\Hamid Shah\\Desktop\\blck_galaxy.png')
window.tk.call("source", "azure.tcl")
window.tk.call("set_theme", "light")

# window.tk.call('lappend', 'auto_path',
#                path)
# window.tk.call('package', 'require', 'awdark')
style = ttk.Style(window)
# style.theme_use('awdark')

# style.configure('TButton', foreground="white", background="#24304a", highlightthickness=2,
#                 highlightbackground='#4c618f', highlightforeground="black",
#                 activebackground="#24304a")
# frame1 = Frame(main_frame, width=15)
# frame1.grid(row=0, column=0, rowspan=12)
style.configure("TButton", font=("Courier", 14, 'bold'))
top_label = Label(top_frame, text='CFC App',
                  justify=CENTER, width=50,  font=("Game Of Squids", 32))  # bg='#24304a', foreground='#ffffff',
top_label.pack(padx=10, pady=10, anchor=E)


def check_server():
    con, cur  = open_con()
    try:
        if con.isconnected():
                # print('{} Connected'.format(server_address))
            con.close()
            return 'Connected'
            
    except Exception as e:
        messagebox.showinfo("Db Connection Status" , "Can not connect to db. {}".format(e))
        return 'Not Connected'


def cash_report():
    obj = Cash_Report()
    obj.run()


def setting_obj():
    obj = Black_List(obj1.user_data)
    # return messagebox.showinfo('Under Construction', 'Setting Module will be available soon')
    # obj = settings()
    obj.window.mainloop()


def imp_exp():
    obj = Update_Status()
    obj.root.mainloop()


def data_obj():
    obj = dataentry(obj1.user_data)
    obj.mainloop()


def noc_other():
    obj = NOC(obj1.session, obj1.user_data)
    obj.mainloop()


def noc_ict():
    obj = NOC_ICT()
    obj.mainloop()


def verification():
    obj = Verification(obj1.session)
    obj.mainloop()


def cancellation():
    obj = Canelation()
    obj.run()


def export_nitb():
    obj = Sysentry()
    obj.mainloop()


def mon_report():
    obj = Monthly_Report()
    obj.mainloop()

def update_passwrod():
    obj1.change_password(obj1.user_data['user_login'])
def app_settings():
    messagebox.showerror('Under construction', 'This part is under construction')

btn = ttk.Button(bottom_frame, text='Domicile\nReports',
                 command=cash_report, width=15)
btn.grid(row=0, column=1, ipady=10)
btn1 = ttk.Button(bottom_frame, command=setting_obj,
                  text='Black List \n  CNICs', width=15)
btn1.grid(row=1, column=0, ipady=10, padx=10)
btn11 = ttk.Button(bottom_frame, command=imp_exp,
                   text='Update Files Status', width=15)
btn11.grid(row=1, column=2, ipady=10)

btn1 = ttk.Button(bottom_frame, text=' Domicile\nData Entry',
                  command=data_obj, width=15)
btn1.grid(row=2, column=1, ipady=10)

btn2 = ttk.Button(
    bottom_frame, text=' NOC Letter to\nOther Districts', width=15, command=noc_other)
btn2.grid(row=3, column=0, ipady=10, padx=10)

btn3 = ttk.Button(bottom_frame, text='NOC Letter for\n ICT Domicile',
                  width=15, command=noc_ict)
btn3.grid(row=3, column=2, ipady=10)

btn4 = ttk.Button(bottom_frame, text='Verification\n   Letter',
                  width=15, command=verification)
btn4.grid(row=4, column=1, ipady=10)

btn5 = ttk.Button(bottom_frame, text='Cancellation\nof Domicile',
                  width=15, command=cancellation)
btn5.grid(row=5, column=0, ipady=10, padx=10)

btn6 = ttk.Button(bottom_frame, text='Export\nto NITB',
                  width=15, command=export_nitb)
btn6.grid(row=5, column=2, ipady=10)

btn7 = ttk.Button(bottom_frame, text='  Monthly Report',
                  width=15, command=mon_report)
btn7.grid(row=6, column=1, ipady=10)

btn8 = ttk.Button(bottom_frame, text='Change Password',
                  width=15, command=update_passwrod)
btn8.grid(row=7, column=0, ipady=10)

btn9 = ttk.Button(bottom_frame, text='Settings',
                  width=15, command=app_settings)
btn9.grid(row=7, column=2, ipady=10)

# _status = check_server()
# if _status == 'Not Connected':
#     messagebox.showerror('Error', 'Server Not Connected')
#     window.destroy()
window.mainloop()
