import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import mysql.connector
from mysql.connector import Error

class Auto_entry():
    def __init__(self, server_address):

        self.__root = Tk()
        self.__root.geometry('350x200+50+50')
        self.server_address = server_address
        self.log_in = False
        self.Top_Frame = Frame(
            self.__root, relief=RIDGE, border=1)
        self.Top_Frame.pack(fill=BOTH, expand=YES)
        self.user_name_lbl = Label(self.Top_Frame, text='User Name', width=15)
        self.user_name_lbl.grid(row=1, column=0, padx=10, pady=10)
        self.user_name_inp = Entry(self.Top_Frame,  width=20)
        self.user_name_inp.grid(row=1, column=1, padx=10, pady=10)
        # self.user_name_inp.insert(0, 'Sheryar Arif Khan')
        self.login_lbl = Label(self.Top_Frame, text='Login ID', width=15)
        self.login_lbl.grid(row=2, column=0, padx=10, pady=10)
        self.login_inp = Entry(self.Top_Frame,  width=20)
        # self.login_inp.insert(0, 'shehryarak@gmail.com')
        self.login_inp.grid(row=2, column=1, padx=10, pady=10)

        self.password_lbl = Label(self.Top_Frame, text='Passowrd', width=15)
        self.password_lbl.grid(row=3, column=0, padx=10, pady=10)
        self.password_inp = Entry(self.Top_Frame,  width=20, show='*')
        self.password_inp.grid(row=3, column=1, padx=10, pady=10)
        # self.password_inp.insert(0, 'approver@123')

        self.login_btn = Button(self.Top_Frame, text='Login',
                                width=15, command=self.check_login)
        self.login_btn.grid(row=4, column=0, padx=10, pady=10)
        self.exit_btn = Button(self.Top_Frame, text='Exit',
                               width=15, command=self.__root.destroy)
        self.exit_btn.grid(row=4, column=1, padx=10, pady=10)
        self.driver = webdriver.Chrome()
        self.driver.get('https://admin-icta.nitb.gov.pk/login')

    def open_con(self):

        self.con = mysql.connector.connect(host='{}'.format(self.server_address.strip()),
                                           database='domicile_reports',
                                           user='superadmin',
                                           password='Superadmin')
        try:
            if self.con.is_connected():
                self.conection_status = 'connected'
            else:
                self.conection_status = 'not connected'
        except Error as e:
            print('error while connecting to db ', e)

    def close_con(self):
        self.con.close()

    def exec_query(self, query, query_type, dictionary):
        if self.conection_status == 'connected':
            if dictionary == True:
                self.cur = self.con.cursor(dictionary=True)
            else:
                self.cur = self.con.cursor()
            if query_type == 'get':
                self.cur.execute(query)
                data = self.cur.fetchall()

                return data
            elif query_type == 'update':
                self.cur.execute(query)
                self.cur.execute('commit')

                return 'update succeded'
            else:
                return 'query type error'

        else:
            return 'not connected to db'

    def check_login(self):
        if len(self.user_name_inp.get()) == 0:
            # Sheryar Arif Khan
            return messagebox.showerror('Error', 'Please Provide User Name')
        if len(self.login_inp.get()) == 0:
            return messagebox.showerror('Error', 'Please Provide login id')
        if len(self.password_inp.get()) == 0:
            return messagebox.showerror('Error', 'Please Provide Password')

        email_elem = self.driver.find_element(By.NAME, 'email')
        email_elem.send_keys("{}".format(self.login_inp.get()))
        pass_elem = self.driver.find_element(By.NAME, 'password')
        pass_elem.send_keys("{}".format(self.password_inp.get()))
        submit_btn = self.driver.find_element(By.CLASS_NAME, 'btn-sign-in')
        submit_btn.click()
        self.driver.get('https://admin-icta.nitb.gov.pk/domicile/applications')
        # Login Check
        a = 0
        for span in self.driver.find_elements(By.TAG_NAME, 'span'):
            if len(span.text) != 0:
                a = a + 1
                if a == 1 and span.text == self.user_name_inp.get():
                    self.log_in = True
                    break

        if self.log_in == True:
            self.main_window()
        else:
            messagebox.showerror('Error', 'Login Failed')

    def main_window(self):
        self.__root.geometry('800x700+50+50')
        self.password_lbl.forget()
        self.password_inp.forget()
        self.login_btn.forget()
        self.exit_btn.forget()
        self.Top_Frame.forget()
        self.Top_Frame = Frame(
            self.__root, relief=RIDGE, border=1)
        self.Top_Frame.pack(fill=BOTH, expand=YES)
        self.Top_label = Label(
            self.Top_Frame, text='Javascript Generator', border=1, font=('Bell', 18, 'bold'))
        self.Top_label.grid(row=0, column=0, columnspan=7, padx=10, pady=10)
        self.Label_CNIC = Label(
            self.Top_Frame, text='CNIC', border=1, font=('Bell', 12))
        self.Label_CNIC.grid(row=1, column=0, padx=10, pady=10)
        self.Entry_CNIC = Entry(self.Top_Frame, font=('Bell', 12))

        self.Entry_CNIC.grid(row=1, column=1, padx=10, pady=10)
        self.Js_Text = Text(self.Top_Frame, height=20, font=('Bell', 12))
        self.Js_Text.grid(row=3, column=0, columnspan=7, padx=10, pady=10)
        self.Js_child_Text = Text(self.Top_Frame, height=10, font=('Bell', 12))
        self.Js_child_Text.grid(
            row=4, column=0, columnspan=7, padx=10, pady=10)
        self.Entry_CNIC.bind('<Return>', self.check_event)
        self.Gen_JS_Button = Button(
            self.Top_Frame, text='Generate Js', width=15, command=self.generate, font=('Bell', 12))
        self.Gen_JS_Button.grid(row=2, column=0, padx=10, pady=10)
        self.Gen_JS_Button = Button(
            self.Top_Frame, text='New Application', width=15, command=self.new_application, font=('Bell', 12))
        self.Gen_JS_Button.grid(row=2, column=1, padx=10, pady=10)
        self.Clear_Button = Button(
            self.Top_Frame, text='Clear Text', width=15, command=self.clear_text, font=('Bell', 12))
        self.Clear_Button.grid(row=2, column=2, padx=10, pady=10)

    def run(self):
        self.__root.mainloop()

    def new_application(self):
        self.driver.get(
            'https://admin-icta.nitb.gov.pk/domicile/application/create')

        if self.get_data() is not None:
            for row in self.data:

                txt = "document.getElementById('first_name').value = '{}';".format(
                    row["First_Name"])
                self.driver.execute_script(txt)
                txt = "document.getElementById('last_name').value = '{}';".format(
                    row['Last_Name'])
                self.driver.execute_script(txt)
                txt = "document.getElementById('cnic').value = '{}';".format(
                    row['CNIC'])
                self.driver.execute_script(txt)
                txt = "document.getElementById('place_of_birth').value = '{}';".format(
                    row['Placeofbirth'])
                self.driver.execute_script(txt)
                txt = "document.getElementById('father_name').value = '{}';".format(
                    row['Father_Name'])
                self.driver.execute_script(txt)
                txt = "document.getElementById('spouse_name').value = '{}';".format(
                    row['Spouse_Name'])
                self.driver.execute_script(txt)
                txt = "document.getElementById('temp_address').value = '{}';".format(
                    row['Present_Address'])
                self.driver.execute_script(txt)
                txt = "document.getElementById('temp_province_id').value = '{}';".format(
                    row['Pres_Province'])
                self.driver.execute_script(txt)
                txt = "document.getElementById('temp_district_id').value = '{}';".format(
                    row['Pres_District'])
                self.driver.execute_script(txt)
                txt = "document.getElementById('temp_tehsil_id').value = '{}';".format(
                    row['Pres_Tehsil'])
                self.driver.execute_script(txt)
                txt = "document.getElementById('permanent_address').value = '{}';".format(
                    row['Permenant_Address'])
                self.driver.execute_script(txt)
                txt = "document.getElementById('permanent_province_id').value = '{}';".format(
                    row['Perm_Province'])
                self.driver.execute_script(txt)
                txt = "document.getElementById('permanent_district_id').value = '{}';".format(
                    row['Perm_District'])
                self.driver.execute_script(txt)
                txt = "document.getElementById('permanent_tehsil_id').value = '{}';".format(
                    row['Perm_Tehsil'])
                self.driver.execute_script(txt)
                txt = "document.getElementById('contact').value = '{}';".format(
                    row['Contact'])
                self.driver.execute_script(txt)
                txt = "document.getElementById('date_of_birth').value = '{}';".format(
                    row['Date_of_Birth'])
                self.driver.execute_script(txt)
                txt = "document.getElementById('arrival_date').value = '{}';".format(
                    row['Arrival_Date'])
                self.driver.execute_script(txt)
                txt = "document.getElementById('gender_id').value = '{}';".format(
                    row['Gender'])
                self.driver.execute_script(txt)
                txt = "document.getElementById('religion').value = '{}';".format(
                    row['Religon'])
                self.driver.execute_script(txt)
                txt = "document.getElementById('marital_status_id').value = '{}';".format(
                    row['Marital_Status'])
                self.driver.execute_script(txt)
                txt = "document.getElementById('qualification_id').value = '{}';".format(
                    row['Qualification'])
                self.driver.execute_script(txt)
                txt = "document.getElementById('occupation_id').value = '{}';".format(
                    row['Occupation'])
                self.driver.execute_script(txt)
                txt = "document.getElementById('applicant_type_id').value = '{}';".format(
                    row['Application_Type'])
                self.driver.execute_script(txt)
                txt = "document.getElementById('request_type_id').value = '{}';".format(
                    row['Request_Type'])
                self.driver.execute_script(txt)
                txt = "document.getElementById('service_type_id').value = '{}';".format(
                    row['Service_Type'])
                self.driver.execute_script(txt)
                txt = "document.getElementById('payment_type_id').value = '{}';".format(
                    row['Payment_Type'])
                self.driver.execute_script(txt)
                txt = "document.getElementById('docs-cnic-front').checked = {};".format(
                    self.Convert_Boolean(row['cnic_front']))
                self.driver.execute_script(txt)

                txt = "document.getElementById('docs[cnic_back]').checked = {};".format(
                    self.Convert_Boolean(row['cnic_back']))
                self.driver.execute_script(txt)
                txt = "document.getElementById('docs[cnic_guardian]').checked = {};".format(
                    self.Convert_Boolean(row['cnic_guardian']))
                self.driver.execute_script(txt)
                txt = "document.getElementById('docs[proof_of_residence]').checked = {};".format(
                    self.Convert_Boolean(row['Residance_Prof']))
                self.driver.execute_script(txt)
                txt = "document.getElementById('docs[utility_bill]').checked = {};".format(
                    self.Convert_Boolean(row['utility_bill']))
                self.driver.execute_script(txt)
                txt = "document.getElementById('docs[educational_certificate]').checked = {};".format(
                    self.Convert_Boolean(row['educational_certificate']))
                self.driver.execute_script(txt)
                txt = "document.getElementById('docs[marriage_registration_certificate]').checked = {};".format(
                    self.Convert_Boolean(row['marriage_registration_certificate']))
                self.driver.execute_script(txt)
                txt = "document.getElementById('docs[form_b]').checked = {};".format(
                    self.Convert_Boolean(row['form_b']))

                self.driver.execute_script(txt)
                txt = "document.getElementById('docs[domicile_of_guardian]').checked = {};".format(
                    self.Convert_Boolean(row['domicile_of_guardian']))

                self.driver.execute_script(txt)
                txt = "document.getElementById('docs[noc_from_concerned_district]').checked = {};".format(
                    self.Convert_Boolean(row['noc_from_concerned_district']))

                self.driver.execute_script(txt)
                txt = "document.getElementById('docs[affidavit_domicile]').checked = {};".format(
                    self.Convert_Boolean(row['affidavit_domicile']))

                self.driver.execute_script(txt)
                txt = "document.getElementById('docs[affidavit_voterlist]').checked = {};".format(
                    self.Convert_Boolean(row['affidavit_voterlist']))

                self.driver.execute_script(txt)
                txt = "document.getElementById('docs[voter_list]').checked = {};".format(
                    self.Convert_Boolean(row['voter_list']))

                self.driver.execute_script(txt)
                txt = "document.getElementById('docs[domicile_challan]').checked = {};".format(
                    self.Convert_Boolean(row['domicile_challan']))
                self.driver.execute_script(txt)
                vari = 97
                cnt = 0
                if self.child_data is not None:
                    for row in self.child_data:
                        txt = "var {} = document.getElementsByName('children[{}][first_name]');".format(
                            chr(vari), cnt)
                        self.driver.execute_script(txt)
                        txt = chr(vari) + "[0].value = '" + \
                            row["Child_Name"] + "';"
                        self.driver.execute_script(txt)
                        var = vari + 1
                        txt = "var {} = document.getElementsByName('children[" + str(
                            cnt) + "][date_of_birth]');".format(chr(vari))
                        self.driver.execute_script(txt)
                        txt = chr(vari) + \
                            "[0].value = '{}';".format(row["Child_dob"])
                        self.driver.execute_script(txt)
                        cnt = cnt + 1
                        vari = vari + 1

    def clear_text(self):
        self.Js_Text.delete('1.0', 'end')
        self.Js_child_Text.delete('1.0', 'end')

    def check_event(self, event):
        if event.keysym == 'Return':
            self.generate()
            self.Js_Text.focus_set()
            self.Js_Text.tag_add(SEL, "1.0", END)
            self.Js_Text.mark_set(INSERT, "1.0")
            self.Js_Text.see(INSERT)
            return 'break'

    def Convert_Boolean(self, val):
        if val == 0:
            return 'false'
        elif val == -1:
            return 'true'

    def get_data(self):
        if len(self.Entry_CNIC.get()) != 13:
            messagebox.showerror('showerror', 'Incorrect CNIC')
            self.Entry_CNIC.focus_set()
            return
        if self.Entry_CNIC.get().isnumeric():
            pass
        else:
            messagebox.showerror('showerror', 'Invalid CNIC')
            self.Entry_CNIC.focus_set()
            return
        self.open_con()
        Query = "Select * from domicile Where CNIC='{}'".format(
            self.Entry_CNIC.get())
        self.data = self.exec_query(Query, 'get', True)
        Query = "Select * from Childern Where Father_CNIC='{}'".format(
            self.Entry_CNIC.get())
        self.child_data = self.exec_query(Query, 'get', True)
        self.con.close()
        if len(self.data) == 0:
            messagebox.showerror('showerror', 'Nothing Found')
            self.Entry_CNIC.focus_set()
            return
        else:
            return self.data

    def generate(self):

        if self.get_data() is not None:

            for row in self.data:

                txt = "document.getElementById('first_name').value = '{}';".format(
                    row["First_Name"])
                self.Js_Text.insert(END, txt + '\n')
                txt = "document.getElementById('last_name').value = '{}';".format(
                    row['Last_Name'])
                self.Js_Text.insert(END, txt + '\n')
                txt = "document.getElementById('cnic').value = '{}';".format(
                    row['CNIC'])
                self.Js_Text.insert(END, txt + '\n')
                txt = "document.getElementById('place_of_birth').value = '{}';".format(
                    row['Placeofbirth'])
                self.Js_Text.insert(END, txt + '\n')
                txt = "document.getElementById('father_name').value = '{}';".format(
                    row['Father_Name'])
                self.Js_Text.insert(END, txt + '\n')
                txt = "document.getElementById('spouse_name').value = '{}';".format(
                    row['Spouse_Name'])
                self.Js_Text.insert(END, txt + '\n')
                txt = "document.getElementById('temp_address').value = '{}';".format(
                    row['Present_Address'])
                self.Js_Text.insert(END, txt + '\n')
                txt = "document.getElementById('temp_province_id').value = '{}';".format(
                    row['Pres_Province'])
                self.Js_Text.insert(END, txt + '\n')
                txt = "document.getElementById('temp_district_id').value = '{}';".format(
                    row['Pres_District'])
                self.Js_Text.insert(END, txt + '\n')
                txt = "document.getElementById('temp_tehsil_id').value = '{}';".format(
                    row['Pres_Tehsil'])
                self.Js_Text.insert(END, txt + '\n')
                txt = "document.getElementById('permanent_address').value = '{}';".format(
                    row['Permenant_Address'])
                self.Js_Text.insert(END, txt + '\n')
                txt = "document.getElementById('permanent_province_id').value = '{}';".format(
                    row['Perm_Province'])
                self.Js_Text.insert(END, txt + '\n')
                txt = "document.getElementById('permanent_district_id').value = '{}';".format(
                    row['Perm_District'])
                self.Js_Text.insert(END, txt + '\n')
                txt = "document.getElementById('permanent_tehsil_id').value = '{}';".format(
                    row['Perm_Tehsil'])
                self.Js_Text.insert(END, txt + '\n')
                txt = "document.getElementById('contact').value = '{}';".format(
                    row['Contact'])
                self.Js_Text.insert(END, txt + '\n')
                txt = "document.getElementById('date_of_birth').value = '{}';".format(
                    row['Date_of_Birth'])
                self.Js_Text.insert(END, txt + '\n')
                txt = "document.getElementById('arrival_date').value = '{}';".format(
                    row['Arrival_Date'])
                self.Js_Text.insert(END, txt + '\n')
                txt = "document.getElementById('gender_id').value = '{}';".format(
                    row['Gender'])
                self.Js_Text.insert(END, txt + '\n')
                txt = "document.getElementById('religion').value = '{}';".format(
                    row['Religon'])
                self.Js_Text.insert(END, txt + '\n')
                txt = "document.getElementById('marital_status_id').value = '{}';".format(
                    row['Marital_Status'])
                self.Js_Text.insert(END, txt + '\n')
                txt = "document.getElementById('qualification_id').value = '{}';".format(
                    row['Qualification'])
                self.Js_Text.insert(END, txt + '\n')
                txt = "document.getElementById('occupation_id').value = '{}';".format(
                    row['Occupation'])
                self.Js_Text.insert(END, txt + '\n')
                txt = "document.getElementById('applicant_type_id').value = '{}';".format(
                    row['Application_Type'])
                self.Js_Text.insert(END, txt + '\n')
                txt = "document.getElementById('request_type_id').value = '{}';".format(
                    row['Request_Type'])
                self.Js_Text.insert(END, txt + '\n')
                txt = "document.getElementById('service_type_id').value = '{}';".format(
                    row['Service_Type'])
                self.Js_Text.insert(END, txt + '\n')
                txt = "document.getElementById('payment_type_id').value = '{}';".format(
                    row['Payment_Type'])
                self.Js_Text.insert(END, txt + '\n')
                txt = "document.getElementById('docs-cnic-front').checked = {};".format(
                    self.Convert_Boolean(row['cnic_front']))
                self.Js_Text.insert(END, txt + '\n')

                txt = "document.getElementById('docs[cnic_back]').checked = {};".format(
                    self.Convert_Boolean(row['cnic_back']))
                self.Js_Text.insert(END, txt + '\n')
                txt = "document.getElementById('docs[cnic_guardian]').checked = {};".format(
                    self.Convert_Boolean(row['cnic_guardian']))
                self.Js_Text.insert(END, txt + '\n')
                txt = "document.getElementById('docs[proof_of_residence]').checked = {};".format(
                    self.Convert_Boolean(row['Residance_Prof']))
                self.Js_Text.insert(END, txt + '\n')
                txt = "document.getElementById('docs[utility_bill]').checked = {};".format(
                    self.Convert_Boolean(row['utility_bill']))
                self.Js_Text.insert(END, txt + '\n')
                txt = "document.getElementById('docs[educational_certificate]').checked = {};".format(
                    self.Convert_Boolean(row['educational_certificate']))
                self.Js_Text.insert(END, txt + '\n')
                txt = "document.getElementById('docs[marriage_registration_certificate]').checked = {};".format(
                    self.Convert_Boolean(row['marriage_registration_certificate']))
                self.Js_Text.insert(END, txt + '\n')
                txt = "document.getElementById('docs[form_b]').checked = {};".format(
                    self.Convert_Boolean(row['form_b']))

                self.Js_Text.insert(END, txt + '\n')
                txt = "document.getElementById('docs[domicile_of_guardian]').checked = {};".format(
                    self.Convert_Boolean(row['domicile_of_guardian']))

                self.Js_Text.insert(END, txt + '\n')
                txt = "document.getElementById('docs[noc_from_concerned_district]').checked = {};".format(
                    self.Convert_Boolean(row['noc_from_concerned_district']))

                self.Js_Text.insert(END, txt + '\n')
                txt = "document.getElementById('docs[affidavit_domicile]').checked = {};".format(
                    self.Convert_Boolean(row['affidavit_domicile']))

                self.Js_Text.insert(END, txt + '\n')
                txt = "document.getElementById('docs[affidavit_voterlist]').checked = {};".format(
                    self.Convert_Boolean(row['affidavit_voterlist']))

                self.Js_Text.insert(END, txt + '\n')
                txt = "document.getElementById('docs[voter_list]').checked = {};".format(
                    self.Convert_Boolean(row['voter_list']))

                self.Js_Text.insert(END, txt + '\n')
                txt = "document.getElementById('docs[domicile_challan]').checked = {};".format(
                    self.Convert_Boolean(row['domicile_challan']))
                vari = 97
                cnt = 0
                if self.child_data is not None:
                    for row in self.child_data:
                        txt = "var {} = document.getElementsByName('children[{}][first_name]');".format(
                            chr(vari), cnt)
                        self.Js_child_Text.insert(END, txt + '\n')
                        txt = chr(vari) + "[0].value = '" + \
                            row["Child_Name"] + "';"
                        self.Js_child_Text.insert(END, txt + '\n')
                        var = vari + 1
                        txt = "var {} = document.getElementsByName('children[" + str(
                            cnt) + "][date_of_birth]');".format(chr(vari))
                        self.Js_child_Text.insert(END, txt + '\n')
                        txt = chr(vari) + \
                            "[0].value = '{}';".format(row["Child_dob"])
                        self.Js_child_Text.insert(END, txt + '\n')
                        cnt = cnt + 1
                        vari = vari + 1

    # self.Entry_CNIC.bind('<Return>', check_event)
    # self.Gen_JS_Button = Button(
    #     self.Top_Frame, text='Generate Js', command=generate, font=('Bell', 12))
    # self.Gen_JS_Button.place(x=300, y=50)
    # self.Clear_Button = Button(
    #     self.Top_Frame, text='Clear Text', command=clear_text, font=('Bell', 12))
    # self.Clear_Button.place(x=430, y=50)
if __name__ == '__main__':
    obj = Auto_entry('25.48.184.239')
    obj.run()
