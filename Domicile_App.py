import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
from DataEntry_sqlite3 import dataentry, Sysentry, Collection_Report
from tkinter import filedialog as fd
import os
import subprocess
import shutil
import time

global inst
inst = FALSE


root = Tk()
root.geometry('300x150')
root.title('Setting Up...')
font_style = ('Book Antiqua', 14, 'bold')
btn_style = ttk.Style()
btn_style.configure('TButton', font=('Book Antiqua', 14, 'bold'))
top_frame = Frame(root, height=4)
top_frame.pack(fill=BOTH, expand=TRUE)
bot_frame = Frame(root, height=4)
bot_frame.pack(fill=BOTH, expand=TRUE)

blank_label = ttk.Label(top_frame).pack()

top_label = ttk.Label(top_frame, text='Initializing..', font=font_style)
top_label.pack()


def update_config_file():

    filetypes = (('database files', '*.db'), ('All files', '*.*'))
    fil = fd.askopenfilename(filetypes=filetypes)
    if len(fil) == 0:
        messagebox.showerror(
            'showerror', 'You did not select database file. exiting now...')
        exit()
    else:
        filepath = fil
        f = open("config.txt", "w")
        f.write(fil)
        f.close()
        root.destroy()


def update_splash():
    top_label.config(text='Please locate database file.')
    browse_btn = ttk.Button(bot_frame, text='Browse',
                            command=update_config_file)
    browse_btn.pack()


def check_db_file():
    global filepath
    filepath = ''
    if os.path.exists('config.txt') == True:
        f = open('config.txt', 'r')
        filepath = f.read()
        f.close()
        if os.path.exists(filepath) == False:
            if messagebox.askyesno(
                    'askyesno', 'Database file not found at {}. Are you want to update database path?'.format(filepath)) == True:
                update_config_file()
            else:
                exit()
        else:
            root.destroy()
    else:
        update_splash()


top_label.after(1000, check_db_file)
root.mainloop()


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.btn_var = StringVar()
        self.geometry('1450x700+10+10')
        self.title('Domicile Application')
        self.main_label = ttk.Label(
            self, text='Domicile Application', font=('MT Bell', 24, 'bold'))
        self.main_label.pack()

        def dataentryform():
            global filepath
            data_window = dataentry(filepath)
            data_window.mainloop

        def JS_form():
            global filepath
            JS_Window = Sysentry(filepath)
            JS_Window.mainloop

        def update_now():
            global inst
            src = r'\\HAMID-PC\Domicile_App'
            dest = os.getcwd()
            file_name = '\\Installer.exe'
            print('copy from', src, ' to ', dest)
            shutil.copy(src+file_name, dest+file_name)
            print('copy complete')
            # time.sleep(2)
            inst = TRUE

            app.after(2000, app.destroy())

        def report():
            global filepath
            Rpt_Window = Collection_Report(filepath)
            Rpt_Window.mainloop()
        self.Data_Entry_lbl = tk.Label(
            self, text='Data Entry', width=20, height=2, borderwidth=1, relief=GROOVE, font=('Bell', 14, 'bold'))
        self.Data_Entry_lbl.place(x=40, y=50)

        self.Data_Entry_Btn = Button(self, text='New Data Entry', width=20,
                                     height=1, borderwidth=1, relief=RIDGE, command=dataentryform, font=('Bell', 14))
        self.Data_Entry_Btn.place(x=150, y=110)
        self.Data_Entry_JS = Button(self, text='Java Script Gen', width=20,
                                    height=1, borderwidth=1, relief=RIDGE, command=JS_form, font=('Bell', 14))
        self.Data_Entry_JS.place(x=150, y=160)
        self.Data_Entry_JS = Button(self, text='Daily Collection Report', width=20,
                                    height=1, borderwidth=1, relief=RIDGE, command=report, font=('Bell', 14))
        self.Data_Entry_JS.place(x=150, y=210)
        # second label
        self.Data_Entry_lbl = tk.Label(
            self, text='NOC', width=20, height=2, borderwidth=1, relief=GROOVE, font=('Bell', 14, 'bold'))
        self.Data_Entry_lbl.place(x=40, y=260)
        self.Btn_Update = Button(self, text='Update Now', width=20,
                                 height=1, borderwidth=1, relief=RIDGE, command=update_now, font=('Bell', 14))
        self.Btn_Update.place(x=1200, y=50)


app = App()
app.mainloop()
if inst == TRUE:
    subprocess.Popen('installer.exe', shell=True,
                     stdout=subprocess.PIPE).stdout.read()
