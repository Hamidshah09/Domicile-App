import json
from bs4 import BeautifulSoup
import requests
from tools import open_con
from tkinter import Listbox, Tk, Toplevel, ttk, messagebox

class Login():
    def __init__(self):
        self.root = Tk()
        left = int((self.root.winfo_screenwidth() / 2) -200)
        top = int((self.root.winfo_screenheight() / 2) -170)
        self.root.title("Login")
        self.root.geometry(f"400x300+{left}+{top}")
        self.login_status = False
        self.session_status = False
        self.app_style = ttk.Style(master=self.root)
        self.app_style.configure("Main.TLabel", font=('Century Gothic', 14, 'bold'))
        self.app_style.configure("TLabel", font=('Century Gothic', 12, 'bold'))
        self.app_style.configure("TButton", font=('Century Gothic', 12), width=30)
    def login(self):    
        self.top_label = ttk.Label(self.root, text='Login', anchor='center', style="Main.TLabel")
        self.top_label.pack(fill='x', padx=5, pady=10, ipadx=10)
        self.widget_frame = ttk.Frame(self.root)
        self.widget_frame.pack(fill='both', expand=True)

        self.user_label = ttk.Label(self.widget_frame, text='Login ID')
        self.user_label.grid(row=0, column=0, padx=60, pady='5 0', sticky='sw')
        self.user_entry = ttk.Entry(self.widget_frame, font=('Century Gothic', 12), width=30)
        self.user_entry.grid(row=1, column=0, padx=60, pady='0 5',ipady=5)

        self.password_label = ttk.Label(self.widget_frame, text='Password')
        self.password_label.grid(row=2, column=0, padx=60, pady='5 0', sticky='sw')
        self.password_entry = ttk.Entry(self.widget_frame, show='*', font=('Century Gothic', 12), width=30)
        self.password_entry.grid(row=3, column=0, padx=60, pady='0 5', ipady=5)
        self.password_entry.bind('<Return>', self.submit_login)

        self.login_btn = ttk.Button(self.widget_frame, text='Login', command=self.submit_login)
        self.login_btn.grid(row=4, column=0, padx=60, pady=10, ipady=5)
        try:
            with open('username.txt', 'r') as f:
                uname = f.read()
                self.user_entry.insert(0, uname)
        except Exception:
            pass
    def change_password(self, userlogin):
        change_pass_window = Toplevel()
        left = int((change_pass_window.winfo_screenwidth() / 2) -200)
        top = int((change_pass_window.winfo_screenheight() / 2) -200)
        change_pass_window.title("Login")
        change_pass_window.geometry(f"400x450+{left}+{top}")
        app_style = ttk.Style(master=change_pass_window)
        app_style.configure("Main.TLabel", font=('Century Gothic', 14, 'bold'))
        app_style.configure("TLabel", font=('Century Gothic', 12, 'bold'))
        app_style.configure("TButton", font=('Century Gothic', 12), width=30)
        top_label = ttk.Label(change_pass_window, text='Update Password', anchor='center', style="Main.TLabel")
        top_label.pack(fill='x', padx=5, pady=10, ipadx=10)
        widget_frame = ttk.Frame(change_pass_window)
        widget_frame.pack(fill='both', expand=True)

        user_label = ttk.Label(widget_frame, text='Login ID')
        user_label.grid(row=0, column=0, padx=60, pady='5 0', sticky='sw')
        user_entry = ttk.Entry(widget_frame, font=('Century Gothic', 12), width=30)
        user_entry.grid(row=1, column=0, padx=60, pady='0 5',ipady=5)
        user_entry.insert(0, userlogin)
        user_entry.config(state='readonly')

        password_label = ttk.Label(widget_frame, text='Old Password')
        password_label.grid(row=2, column=0, padx=60, pady='5 0', sticky='sw')
        password_entry = ttk.Entry(widget_frame, show='*', font=('Century Gothic', 12), width=30)
        password_entry.grid(row=3, column=0, padx=60, pady='0 5', ipady=5)

        password1_label = ttk.Label(widget_frame, text='New Password')
        password1_label.grid(row=4, column=0, padx=60, pady='5 0', sticky='sw')
        password1_entry = ttk.Entry(widget_frame, show='*', font=('Century Gothic', 12), width=30)
        password1_entry.grid(row=5, column=0, padx=60, pady='0 5', ipady=5)

        password2_label = ttk.Label(widget_frame, text='Confirm Password')
        password2_label.grid(row=6, column=0, padx=60, pady='5 0', sticky='sw')
        password2_entry = ttk.Entry(widget_frame, show='*', font=('Century Gothic', 12), width=30)
        password2_entry.grid(row=7, column=0, padx=60, pady='0 5', ipady=5)

        def update_pass():
            if len(password_entry.get().strip()) ==0 or len(password1_entry.get().strip()) ==0 or len(password2_entry.get().strip()) ==0:
                messagebox.showerror('Empty Password', 'Password input cannot be empty')
                return change_pass_window.focus()
            if password1_entry.get() != password2_entry.get():
                messagebox.showerror('Error', 'Password miss matched')
                return change_pass_window.focus()
            con, cur = open_con(False)
            cur.execute("select user_login from users where user_login = %s and user_pass = %s;", [userlogin.lower(), password_entry.get()])
            data = cur.fetchall()
            if data:
                cur.execute("update users set user_pass = %s where user_login = %s;", [password1_entry.get(), userlogin.lower().lower()])
                con.commit()
                cur.close()
                con.close()
                messagebox.showinfo('Success', 'Password Updated')
                change_pass_window.destroy()
            else:
                messagebox.showerror('Old Password Error', 'Old Password is Not Correct')
                return change_pass_window.focus()
        update_btn = ttk.Button(widget_frame, text='Update Password', command=update_pass)
        update_btn.grid(row=8, column=0, padx=60, pady=10, ipady=5)
        change_pass_window.focus()
        change_pass_window.mainloop()
    def nitb_login(self,id, passw):
        self.session = requests.session()
        url = f'https://admin-icta.nitb.gov.pk/login'
        try:
            page = self.session.get(url)
        except Exception as e:
            messagebox.showerror('Connection Error', e)
            return False
        soup = BeautifulSoup(page.content, 'html.parser')
        for links in soup.find_all('input', type='hidden'):
            _token = links.attrs['value']
            break
        payload = {'_token':_token, 'email':id, 'password':passw, 'submit':'login'}
        update_url = 'https://admin-icta.nitb.gov.pk/login'
        responce = self.session.post(update_url, data=payload)
        if responce.url == 'https://admin-icta.nitb.gov.pk/dashboard':
            self.login_status = True
            return True
        else:
            messagebox.showerror('Different Password', 'Your Password for NITB appliantion is differnt than local application')
            return False
    def submit_login(self, event=None):
        if len(self.user_entry.get().strip()) ==0 or len(self.password_entry.get().strip()) ==0:
            return messagebox.showerror('Input Error', 'Pease provide user id and password')
        con, cur = open_con(True)
        if type(cur) is str:
            return messagebox.showerror('Connection Error', 'Unable to Connect to Db')
        cur.execute("Select user_id, user_name, user_login, role, user_status from users where user_login = %s and user_pass = %s", [self.user_entry.get().lower(), self.password_entry.get()])
        self.user_data = cur.fetchone()
        if self.user_data:    
            if self.user_data['user_status'] != 'Active':
                return messagebox.showerror('User Status', "User is not Active")
            else:
                self.login_status = True #at this point user authenticated and is active in local database
                try: #reading config file
                    f = open("config.json", "r")
                    j_obj = json.load(f)
                    f.close()
                except Exception:
                    messagebox.showerror('File Not Found', 'Config.json File not found in current directory')
                    return
                with open('username.txt', 'w') as f:
                    f.write(f'{self.user_entry.get()}')
                try: #trying to extra nitb login from config file
                    nitb_login = j_obj['nitb_login']
                    cur.execute("Select user_login, user_pass from users where user_login = %s", [nitb_login])
                    nitb_login_data = cur.fetchone()
                    if nitb_login_data:
                        if self.nitb_login(j_obj['nitb_login'], nitb_login_data['user_pass']) == False:
                            messagebox.showerror('Authentication Error', 'Incorrect Username and Password for NITB Application.\n Incharge Domicile may update his username and password as per NITB Application')
                            self.root.destroy()
                        else:
                            self.session_status = True
                            self.root.destroy()
                    else:
                        messagebox.showerror('NITB Login Error', f'unable to find data for NITB user login "{nitb_login}" in local db')
                        self.session_status = False
                        self.root.destroy()
                except KeyError:
                    messagebox.showerror('Configuration Error', 'Config file does not contain valid NITB login')
                    return
        
        else:
            messagebox.showerror('Invalid Username or password', 'Invalid username or password')    
            self.login_status = False
            return
            
            
class LocalLogin(Login):
    def __init__(self):
        super().__init__()
    def submit_login(self, event=None):
        if len(self.user_entry.get().strip()) ==0 or len(self.password_entry.get().strip()) ==0:
            return messagebox.showerror('Input Error', 'Pease provide user id and password')
        con, cur = open_con(True)
        if type(cur) is str:
            return messagebox.showerror('Connection Error', 'Unable to Connect to Db')
        
        #incase its not new user, therefore it will be checked that this user_id or passwrod exist
        cur.execute("Select user_id, user_name, role, user_status from users where user_login = %s and user_pass = %s", [self.user_entry.get().lower(), self.password_entry.get()])
        self.user_data = cur.fetchone()
        print(self.user_data)
        if self.user_data:
            if self.user_data['user_status'] != 'Active':
                return messagebox.showerror('User Status', "User is not Active")
            else:
                self.login_status = True
                self.root.destroy()

        else:
            messagebox.showerror('Error', 'Invalid user login or password for local application')
        
class SaveLogin(Login):
    def __init__(self):
        super().__init__()
        self.root.title('Save Login')
    def submit_login(self, event=None):
        if len(self.user_entry.get().strip()) ==0 or len(self.password_entry.get().strip()) ==0:
            return messagebox.showerror('Input Error', 'Pease provide user id and password')
        con, cur = open_con(True)
        if type(cur) is str:
            return messagebox.showerror('Connection Error', 'Unable to Connect to Db')
        cur.execute("insert into users (user_name, user_pass, user_status, user_type) values (%s, %s, 'Active', 'Main User');", [self.user_entry.get().lower(), self.password_entry.get()])
        con.commit()
        self.root.destroy()

class TempLogin(Login):
    def __init__(self):
        super().__init__()
    def submit_login(self, event=None):
        self.top_label.config(text='Temp Login')
        self.top_label.update()
        if len(self.user_entry.get().strip()) ==0 or len(self.password_entry.get().strip()) ==0:
            return messagebox.showerror('Input Error', 'Pease provide user id and password')
        con, cur = open_con(True)
        if type(cur) is str:
            return messagebox.showerror('Connection Error', 'Unable to Connect to Db')
        
        #incase its not new user, therefore it will be checked that this user_id or passwrod exist
        cur.execute("Select user_id, user_name, main_user_id, user_status from users where user_login = %s and user_pass = %s", [self.user_entry.get().lower(), self.password_entry.get()])
        self.temp_user_data = cur.fetchone()
        if self.temp_user_data:
            if self.temp_user_data['user_status'] != 'Active':
                return messagebox.showerror('User Status', "User is not Active")
            else:
                cur.execute("Select user_id, user_login, user_name, user_pass from users where user_id = %s;", [self.temp_user_data['main_user_id']])
                self.user_data = cur.fetchone()
                if self.user_data:
                    if self.nitb_login(self.user_data['user_login'], self.user_data['user_pass']) == True:
                        self.login_status = True
                        self.root.destroy()
                    else:
                        messagebox.showerror('NITB Login Error', 'User Name and Password for NITB login are incorrect')
                else:
                    messagebox.showerror('User Type Error', 'Main user for temporary user is not defined')
        else:
            messagebox.showerror('Error', 'Invalid user login or password for local application')
        
if __name__ == '__main__':
    obj = Login()
    obj.login()
    obj.root.mainloop()
    print(obj.login_status)
    print(obj.session_status)
    
