# importing library
from tkinter import *
from tkinter import font
from PIL import ImageTk, Image

import json
import mysql.connector
from mysql.connector.errors import Error
import threading


class splashscreen():
    def __init__(self):

        self.w = Tk()
        f = open("config.json", "r")
        j_obj = json.load(f)
        f.close()
        self.server_1 = j_obj['server_1']
        self.server_2 = j_obj['server_2']
        self.server_1_status = 'Not Connected'
        self.server_2_status = 'Not Connected'
        width_of_window = 427
        height_of_window = 250
        screen_width = self.w.winfo_screenwidth()
        screen_height = self.w.winfo_screenheight()
        x_coordinate = (screen_width/2)-(width_of_window/2)
        y_coordinate = (screen_height/2)-(height_of_window/2)
        self.w.geometry("%dx%d+%d+%d" %
                        (width_of_window, height_of_window, x_coordinate, y_coordinate))
        # self.w.configure(bg='#ED1B76')
        self.w.overrideredirect(1)  # for hiding titlebar
        self.image_a = ImageTk.PhotoImage(Image.open('c2.png'))
        self.image_b = ImageTk.PhotoImage(Image.open('c1.png'))
        # new window to open

        Frame(self.w, width=427, height=250, bg='#272727').place(x=0, y=0)
        self.label1 = Label(self.w, text='CFC App', fg='white',
                            bg='#272727')  # decorate it
        # You need to install this font in your PC or try another one
        self.label1.configure(font=("Game Of Squids", 24, "bold"))
        self.label1.place(x=130, y=90)

        self.label2 = Label(self.w, text='Loading...', fg='white',
                            bg='#272727')  # decorate it
        self.label2.configure(font=("Calibri", 11))
        self.label2.place(x=10, y=215)
        self.counter = 0
        self.count = 0
        # self.check_server(self.server_2)
        self.label1.after(1000, self.check_server1)
        self.label2.after(500, self.animate)
        self.w.mainloop()

    def check_server1(self):
        self.server_1_status = self.check_server(self.server_1)

    def check_server2(self):
        self.server_2_status = self.check_server(self.server_2)

    def thred(self):
        t1 = threading.Thread(target=self.check_server1)

        t2 = threading.Thread(target=self.check_server2)

        # print('starting thread 1')
        t1.start()
        # print('starting thread 2')
        try:
            t2.start()
        except Exception as e:
            print('Error {} occured'.format(e))
        t1.join()
        # print('Thred 1 completed')
        t2.join()
        # print('Thred 2 completed')
        # print("Server 1 Status:-", self.server_1_status)
        # print("Server 2 Status:-", self.server_2_status)

    def check_server(self, server_address):
        try:
            con = mysql.connector.connect(host='{}'.format(server_address),
                                          database='domicile_reports',
                                          user='superadmin',
                                          password='Superadmin')
            if con.is_connected():
                # print('{} Connected'.format(server_address))
                return 'Connected'
            con.close()
        except Error as e:
            print("Can not connect to db. {} Occured".format(e))
            return 'Not Connected'

    # making animation

    def animate(self):
        self.count += 1
        if self.count == 1:
            l1 = Label(self.w, image=self.image_a, border=0,
                       relief=SUNKEN).place(x=180, y=145)
            l2 = Label(self.w, image=self.image_b, border=0,
                       relief=SUNKEN).place(x=200, y=145)
            l3 = Label(self.w, image=self.image_b, border=0,
                       relief=SUNKEN).place(x=220, y=145)
            l4 = Label(self.w, image=self.image_b, border=0,
                       relief=SUNKEN).place(x=240, y=145)
            self.w.update_idletasks()
        elif self.count == 2:

            l1 = Label(self.w, image=self.image_b, border=0,
                       relief=SUNKEN).place(x=180, y=145)
            l2 = Label(self.w, image=self.image_a, border=0,
                       relief=SUNKEN).place(x=200, y=145)
            l3 = Label(self.w, image=self.image_b, border=0,
                       relief=SUNKEN).place(x=220, y=145)
            l4 = Label(self.w, image=self.image_b, border=0,
                       relief=SUNKEN).place(x=240, y=145)
            self.w.update_idletasks()
        elif self.count == 3:

            l1 = Label(self.w, image=self.image_b, border=0,
                       relief=SUNKEN).place(x=180, y=145)
            l2 = Label(self.w, image=self.image_b, border=0,
                       relief=SUNKEN).place(x=200, y=145)
            l3 = Label(self.w, image=self.image_a, border=0,
                       relief=SUNKEN).place(x=220, y=145)
            l4 = Label(self.w, image=self.image_b, border=0,
                       relief=SUNKEN).place(x=240, y=145)
            self.w.update_idletasks()
        elif self.count == 4:

            l1 = Label(self.w, image=self.image_b, border=0,
                       relief=SUNKEN).place(x=180, y=145)
            l2 = Label(self.w, image=self.image_b, border=0,
                       relief=SUNKEN).place(x=200, y=145)
            l3 = Label(self.w, image=self.image_b, border=0,
                       relief=SUNKEN).place(x=220, y=145)
            l4 = Label(self.w, image=self.image_a, border=0,
                       relief=SUNKEN).place(x=240, y=145)
            self.w.update_idletasks()
        else:
            self.w.destroy()
        if self.count < 5:
            self.label2.after(500, self.animate)

    def run(self):
        self.w.mainloop


    # def run(self):
if __name__ == '__main__':
    obj = splashscreen()
    obj.run()
    import CFC_APP_Main
