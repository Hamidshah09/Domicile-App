import shutil
import os
from tkinter import *
import time
root = Tk()
root.geometry('350x200')
root.title('Domicile App Updater')
Main_Label = Label(root, text='Updating', font=('Courier', 18, 'bold'))
Main_Label.place(x=120, y=25)
Prog_bar_Label = Label(root, text='', bg='green',
                       font=('Courier', 14, 'bold'))
Prog_bar_Label.place(x=50, y=70)
global a
a = 0
global brek
brek = FALSE


def update_label():
    global a, brek
    a = a + 1
    if a == 1:
        if brek == TRUE:
            return
        else:
            Prog_bar_Label.config(text='   30%   ')
            Main_Label.after(1000, update_label)
    elif a == 2:
        if brek == TRUE:
            return
        else:
            Prog_bar_Label.config(text='    40%    ')
            Main_Label.after(1000, update_label)
        # Prog_bar_Label.config(width=a*2)
    elif a == 3:
        if brek == TRUE:
            return
        else:
            Prog_bar_Label.config(text='     50%     ')
            Main_Label.after(1000, update_label)
        # Prog_bar_Label.config(width=a*2)
    elif a == 4:
        if brek == TRUE:
            return
        else:
            Prog_bar_Label.config(text='      60%      ')
            Main_Label.after(1000, update_label)
        # Prog_bar_Label.config(width=a*2)
    elif a == 5:
        if brek == TRUE:
            return
        else:
            Prog_bar_Label.config(text='       70%       ')
            Main_Label.after(1000, update_label)
    elif a == 6:
        if brek == TRUE:
            return
        else:
            Prog_bar_Label.config(text='        80%        ')
            Main_Label.after(1000, update_label)
    elif a == 7:
        if brek == TRUE:
            return
        else:
            Prog_bar_Label.config(text='        90%        ')
            Main_Label.after(1000, update_label)
        a = 0
        return


def update_now():
    global brek
    update_label()
    src = r'\\HAMID-PC\Domicile_App'
    dest = os.getcwd()
    file_name = '\\Domicile_App.exe'
    try:

        shutil.copy(src+file_name, dest+file_name)
        brek = TRUE
        Prog_bar_Label.config(text='        100%        ')
        Main_Label.config(text='Updated')

    except Exception as e:
        err = '{} Occured'.format(e.__class__())
        Main_Label.config(text=err)
        Main_Label.after(3000, root.destroy)


Prog_bar_Label.config(text='  20%  ')
root.after(1000, update_now)
root.mainloop()
