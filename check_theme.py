# Import module
from splash_screen_gui import splashscreen
from tkinter import *
# obj = splashscreen()
# Create object
root = Tk()
# Adjust size
root.geometry("1024x573")
root.title("Main Menue")


def click_me(event):
    print("Hellow World")


def mouse_over(event):
    lbl.config(image=bg1)


# Add image file
bg = PhotoImage(file="btn.png")
bg1 = PhotoImage(file="btn1.png")
btn = Button(root, text='Click Me', width=15)
btn.place(x=10, y=10)
lbl = Label(root, image=bg)
lbl.place(x=100, y=100)
lbl.bind('<Button 1>', click_me)
lbl.bind('Motion', mouse_over)
# Execute tkinter
root.mainloop()
