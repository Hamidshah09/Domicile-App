from tkinter import Tk, ttk
def first_function():
    print("first Function")
def second_function():
    print("Second Function")
window  =Tk()
window.geometry("300x300")
entry = ttk.Entry(window)
entry.bind('<Tab>', lambda event:[first_function(), second_function()])
# entry.bind('<Tab>', second_function)
entry.pack()
window.mainloop()