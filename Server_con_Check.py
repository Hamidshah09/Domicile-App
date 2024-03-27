import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
#from DataEntry_sqlite3 import dataentry, Sysentry, Collection_Report
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
    top_label.config(text='Please locate config file.')
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
