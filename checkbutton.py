from tkinter import *
from tkinter import ttk
window = Tk()
window.geometry("500x500")
window.tk.call("source", "azure.tcl")
window.tk.call("set_theme", "dark")
# window.tk.call('lappend', 'auto_path',r'')
# window.tk.call('package', 'require', 'awdark')
# window.theme_style = ttk.Style(window)
# self.theme_style.theme_use('awdark')
chk_val = IntVar()
chk = ttk.Checkbutton(window, variable=chk_val,
                      text='Select', onvalue=1, offvalue=0)
chk.pack()


def select():

    chk_val.set(1)


def unselect():
    chk_val.set(0)


btn1 = ttk.Button(window, text='Click to Select',
                  style="Accent.TButton", command=select)
btn1.pack()
btn2 = ttk.Button(window, text='Click to Un Select',
                  style="Accent.TButton", command=unselect)
btn2.pack()

window.mainloop()
