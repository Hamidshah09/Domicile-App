from tkinter import Tk, Label, Frame, Entry, Button, messagebox, ttk, PhotoImage, Toplevel
import tkinter as tk
from tools import open_con
from PIL import Image, ImageTk


class Login_form():
    def __init__(self):
        self.root = Tk()
        self.root.geometry("800x685+300+0")
        self.root.title("Login")
        self.root.resizable(False, False)
        img = Image.open(r'Pictures/back_ground.jpg')
        # img_resize = img.resize((800, 600))
        final_image = ImageTk.PhotoImage(img)
        # self.bgpic = PhotoImage(
        #     file=r'back_ground.png', master=self.root)
        self.btn_font = ('Century Gothic', 12)

        
        self.main_label = Label(self.root, image=final_image)
        self.main_label.image = final_image
        self.main_label.pack(fill='both', expand=True)
        update_pass_image = PhotoImage(
            file=r'Pictures/update_pass.png', master=self.root)
        self.update_label = Label(self.main_label, image=update_pass_image)
        self.update_label.image = update_pass_image
        self.update_label.place(x=550, y=10)
        self.update_label.bind('<Button 1>', self.change_pass)

        self.login_status = ""
        self.login_data = ""
        # self.user_login_label = Label(
        #     self.main_label, text='User Login', font=('Century Gothic', 12))
        # self.user_login_label.grid(
        #     row=0, column=0, padx=10, pady=10, sticky=tk.W)
        self.user_login_entry = Entry(
            self.main_label, bg='#D2D2D2',  bd=0, font=('Century Gothic', 14))
        self.user_login_entry.place(x=280, y=305)
        
        # self.user_password_label = Label(
        #     self.main_label, text='User password', font=('Century Gothic', 12))
        # self.user_password_label.grid(
        #     row=1, column=0, padx=10, pady=10, sticky=tk.W)
        self.user_password_entry = Entry(
            self.main_label, show='*', bg='#D2D2D2',  bd=0, font=('Century Gothic', 14))
        self.user_password_entry.place(x=280, y=385)
        self.user_password_entry.bind('<Return>', self.login)
        # img1 = Image.open(r'images\EXPn2.png')
        # img2 = ImageTk.PhotoImage(img1)
        self.btn_img = PhotoImage(
            file=r'Pictures/login_button.png', master=self.root)
        # self.btn_img_hr = PhotoImage(
        #     file=r'images\login_hr.png', master=self.root)
        # self.cur_img = self.btn_img
        # self.pass_button = Button(
        #     self.main_label, image=self.btn_img, relief='solid', bd=0, font=('Century Gothic', 12), command=self.login)
        # self.pass_button.image = self.btn_img
        # self.pass_button.place(x=560, y=480)
        self.label_btn = Label(
            self.main_label, image=self.btn_img, bd=0, borderwidth=0, font=('Century Gothic', 12))
        self.label_btn.place(x=190, y=440)
        self.label_btn.bind('<Button 1>', self.login)

        # self.label_btn.bind('<Enter>', self.hover)
        # self.label_btn.bind('<Leave>', self.normal)
        # self.label_btn.image = self.cur_img
        self.get_username()
        self.user_login_entry.focus()

        # exit_btn_img = PhotoImage(
        #     file=r'C:\Users\Hamid Shah\Desktop\login_btn.png', master=self.root)
        # exit_btn = Label(
        #     self.main_label, image=self.exit_btn_img, bd=0, borderwidth=0, font=('Century Gothic', 12))
        # exit_btn.place(x=565, y=500)
        # exit_btn.bind('<Button 1>', self.exit_)
        # self.exit_btn.image = self.exit_btn_img
        # self.cancil_button = Button(
        #     self.main_label, text='Cancil', width=15, font=('Century Gothic', 12), command=self.root.destroy)
        # self.cancil_button.grid(row=2, column=1, padx=10, pady=10)
    #     self.root.after(1000, self.resizer)
        # self.exit_label_btn = Label(
        #     self.main_label, bd=0, borderwidth=0, font=('Century Gothic', 12))
        # self.exit_label_btn.place(x=560, y=500)
        # self.exit_label_btn.bind('<Button 1>', self.root.destroy)
    # def resizer(self):
    #     # print(event.width, event.height)
    #     self.resized_img = self.img.resize((event.width, event.height))
    #     self.new_img = ImageTk.PhotoImage(self.resized_img)
    #     self.main_label.config(image=self.new_img)

    # def hover(self, event):
    #     self.label_btn.config(image=self.btn_img_hr)
    #     self.cur_img = self.btn_img_hr
    #     self.label_btn.image = self.cur_img
    #     return

    # def normal(self, event):
    #     self.label_btn.config(image=self.btn_img)
    #     self.cur_img = self.btn_img
    #     self.label_btn.image = self.cur_img

    #     return
    
    def exit_(self, event):
        self.root.destroy()
    def get_username(self):
        try:
            with open('username.txt', 'r') as f:
                username = f.read()
                self.user_login_entry.insert(0, username)
        except Exception:
            return
    def change_pass(self, event):
        change_pass_window = Toplevel(self.root)
        change_pass_window.geometry("500x350")
        change_pass_window.title("Change Password")

        user_name_label = ttk.Label(change_pass_window, text='User Name')
        user_name_label.grid(row=0, column=0, padx='20 0', pady=10, sticky='w')
        user_name_entry = ttk.Entry(change_pass_window, font=self.btn_font)
        user_name_entry.grid(row=0, column=1, padx=10, pady=10, sticky='w')
        # user_name_entry.insert(0, self.login_data['user_name'])
        # user_name_entry.config(state='readonly')

        user_id_label = ttk.Label(change_pass_window, text='User ID')
        user_id_label.grid(row=1, column=0, padx='20 0', pady=10, sticky='w')
        user_id_entry = ttk.Entry(change_pass_window, font=self.btn_font)
        user_id_entry.grid(row=1, column=1, padx=10, pady=10, sticky='w')
        # user_id_entry.insert(0, self.login_data['user_login'])
        # user_id_entry.config(state='readonly')

        old_pass_label = ttk.Label(change_pass_window, text='Old Password')
        old_pass_label.grid(row=2, column=0, padx='20 0', pady=10, sticky='w')
        old_pass_entry = ttk.Entry(change_pass_window, show='*',font=self.btn_font)
        old_pass_entry.grid(row=2, column=1, padx=10, pady=10, sticky='w')

        new_pass_label = ttk.Label(change_pass_window, text='New Password')
        new_pass_label.grid(row=3, column=0, padx='20 0', pady=10, sticky='w')
        new_pass_entry = ttk.Entry(change_pass_window, show='*', font=self.btn_font)
        new_pass_entry.grid(row=3, column=1, padx=10, pady=10, sticky='w')

        retype_new_pass_label = ttk.Label(change_pass_window, text='Re-type New Password')
        retype_new_pass_label.grid(row=4, column=0, padx='20 0', pady=10, sticky='w')
        retype_new_pass_entry = ttk.Entry(change_pass_window, show='*', font=self.btn_font)
        retype_new_pass_entry.grid(row=4, column=1, padx=10, pady=10, sticky='w')
        
        def update_pass():
            if len(old_pass_entry.get().strip()) == 0 or len(new_pass_entry.get().strip()) == 0 or len(retype_new_pass_entry.get().strip()) == 0:
                messagebox.showerror('Error', 'Please Provide Old, new and retype-new password')
                return change_pass_window.lift()
            if old_pass_entry.get().strip() == self.login_data['user_pass']:
                if new_pass_entry.get().strip() == retype_new_pass_entry.get().strip():
                    
                    try:
                        con, cur = open_con(True)
                        if con.is_connected:
                            cur = con.cursor(dictionary=True)
                            cur.execute('Update users set user_pass = %s where user_id = %s;', [new_pass_entry.get().strip(), self.login_data['user_id']])
                            con.commit()
                            self.login_data['user_pass'] = new_pass_entry.get().strip()
                            cur.close()
                            con.close()
                            messagebox.showinfo('Password Changed', 'Password Updated')
                            change_pass_window.destroy()
                    except Exception as e:
                        messagebox.showerror('Error', f"{e} accured. Connection not established")
                        change_pass_window.lift()
                        return
                else:
                    messagebox.showerror('Error', 'New and retype-new password mismatched')
                    return change_pass_window.lift()
            else:
                messagebox.showerror('Error', 'Old password mismatched')            
                return change_pass_window.lift()
        update_pass_btn = ttk.Button(change_pass_window, text='Update', style="Accent.TButton", command=update_pass)
        update_pass_btn.grid(row=5, column=1, padx=10, pady=10)
        change_pass_window.mainloop()

    def login(self, *args):
        if len(self.user_login_entry.get().strip()) == 0 or len(self.user_password_entry.get().strip()) == 0:
            return messagebox.showerror('Error', 'Type something in both boxes')
        widget_list = [self.user_login_entry, self.user_password_entry]
        for item in widget_list:
            if item.get().upper().find('UPDATE') != -1 or item.get().upper().find('INSERT') != -1 or item.get().upper().find('DELETE') != -1:
                return messagebox.showerror('Error', 'Milisous Word Found in entry widget')
        con, cur = open_con(True)
        Query = "Select user_id, user_name, user_pass, role from users where user_login = %s;"
        parm_list = []
        parm_list.append(self.user_login_entry.get())
        cur.execute(Query, parm_list)
        data = cur.fetchall()
        if len(data) == 0:
            return messagebox.showerror('Error', 'Invalid User')
        else:
            if data[0]['user_pass'] != self.user_password_entry.get().strip():
                messagebox.showerror('Error', 'Invalid password')
                return
            else:
                
                parm_list = []
                parm_list.append(data[0]['user_id'])
                parm_list.append('User Loged In')
                
                cur.close()
                con.close()
                
                self.login_status = "Successfull"
                self.login_data = data[0]
                with open('username.txt', 'w') as f:
                    f.write(self.user_login_entry.get())
                self.root.destroy()
                return

    def run(self):
        self.root.mainloop()

    def exit(self):
        self.root.destroy()


if __name__ == '__main__':
    obj = Login_form()
    obj.run()
