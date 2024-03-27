from tkinter import *
from tkinter.ttk import *
from tkinter import ttk

root = Tk()
root.geometry('800x800')
style = ttk.Style()
style.configure('Treeview', font=('Helvetica', 12))
style.configure("Treeview.Heading", font=('Helvetica', 12))
trv = ttk.Treeview(root, selectmode='browse')
trv.grid(row=1, column=1, columnspan=4, padx=20, pady=20)
trv["columns"] = ("1", "2")
trv['show'] = 'headings'
trv.column("1", width=100, anchor='w')
trv.column("2", width=100, anchor='w')
trv.heading("1", text="Child Name", anchor='w')
trv.heading("2", text="Date of Birth", anchor='w')
i = 1
trv.insert("", 'end', iid=i,
           values=('Ahmed', '2021-02-03'))
i = 2
trv.insert("", 'end', iid=i,
           values=('Sami', '2022-04-07'))
root.mainloop()
