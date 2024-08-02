
from tkinter import Tk, ttk, messagebox, Listbox, Toplevel, IntVar
from fpdf import FPDF
from fpdf.fonts import FontFace
import os
import Validation
from tools import open_con
import json
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import threading

class Verification(Tk):
    def __init__(self, session):
        super().__init__()
        self.session = session
        self.geometry('1200x800+50+50')
        f = open("config.json", "r")
        self.j_obj = json.load(f)
        f.close()
        self.tk.call("source", "{}".format(self.j_obj['theme_source']))
        self.tk.call("set_theme", "{}".format(self.j_obj['theme_mode']))
        self.title('Verification Letter')
        # self.tk.call('lappend', 'auto_path',
        #              r'C:\Users\Hamid Shah\Desktop\newtheam\awthemes-10.4.0')
        # self.tk.call('package', 'require', 'awarc')
        # style = ttk.Style(self)
        # style.theme_use('awarc')
        veri_style = ttk.Style(self)
        veri_style.configure('Treeview', font=(
            ''.format(self.j_obj['font_name']), 12))
        veri_style.configure("Treeview.Heading", font=(
            ''.format(self.j_obj['font_name']), 12, 'bold'))
        veri_style.configure('TButton', font=(
            ''.format(self.j_obj['font_name']), 12, 'bold'))
        veri_style.map('TButton',
                       foreground=[('pressed', 'red'),
                                   ('active', 'blue')])

        veri_style.configure('TLabel', font=(
            ''.format(self.j_obj['font_name']), 13, 'bold'))
        veri_style.configure('TEntry', font=(
            ''.format(self.j_obj['font_name']), 12), width=60)
        veri_style.configure('Heading.TLabel', font=(
            ''.format(self.j_obj['font_name']), 13, 'bold'))
        self.checkbutton_var = IntVar()
        self.label_heading_font = (self.j_obj['font_name'], 14, 'bold')
        self.label_font = (self.j_obj['font_name'], 13, 'bold')
        self.entry_font = (self.j_obj['font_name'], 12)
        self.Top_Frame = ttk.Frame(
            self, relief='ridge', border=1)
        self.Top_Frame.pack(fill='x')
        self.Top_label = ttk.Label(
            self.Top_Frame, text='Verification Letter', border=1, font=self.label_heading_font)
        self.Top_label.pack(padx=10, pady=10, side='top')
        self.Middle_Frame1 = ttk.Frame(
            self, relief='ridge')
        self.Middle_Frame1.pack(fill='both')
        self.Middle_Frame = ttk.Frame(
            self, relief='ridge')
        self.Middle_Frame.pack(fill='both')
        self.Bottom_Frame1 = ttk.Frame(
            self, relief='ridge')
        self.Bottom_Frame1.pack(fill='both')
        self.Bottom_Frame = ttk.Frame(
            self, relief='ridge', border=1)
        self.Bottom_Frame.pack(fill='x')
        self.edit_mode = False
        self.child_edit_mode = False
        self.old_cnic = ''

        self.letter_no_label = ttk.Label(
            self.Middle_Frame1, text='Received Letter No', font=self.label_font)
        self.letter_no_label.grid(
            column=0, row=0, padx=20, pady=10, sticky='w')
        self.letter_no_entry = ttk.Entry(
            self.Middle_Frame1, font=self.entry_font)
        self.letter_no_entry.grid(
            column=1, row=0, pady=10, sticky='w')

        self.letter_date_label = ttk.Label(
            self.Middle_Frame1, text='Received Letter/\nApplication Date', font=self.label_font)
        self.letter_date_label.grid(
            column=2, row=0, padx=20, pady=10, sticky='w')
        self.letter_date_entry = ttk.Entry(
            self.Middle_Frame1, font=self.entry_font)
        self.letter_date_entry.grid(
            column=3, row=0, pady=10, sticky='w')

        self.letter_to_label = ttk.Label(
            self.Middle_Frame1, text='Reply to', font=self.label_font)
        self.letter_to_label.grid(column=0, row=1, padx=20, sticky='w')
        self.sender = ttk.Entry(self.Middle_Frame1, font=self.entry_font)
        self.sender.grid(column=1, row=1, sticky='w')
        self.sender_designation_lable = ttk.Label(
            self.Middle_Frame1, text='Designation', font=self.label_font)
        self.sender_designation_lable.grid(column=2, row=1, padx=20, sticky='w')
        self.sender_designation_entry = ttk.Entry(
            self.Middle_Frame1, font=self.entry_font)
        self.sender_designation_entry.grid(column=3, row=1, sticky='w')

        self.sender_address_lable = ttk.Label(
            self.Middle_Frame1, text='Sender Address', font=self.label_font)
        self.sender_address_lable.grid(
            column=0, row=2, padx=20, pady=20, sticky='w')
        self.sender_address_entry = ttk.Entry(
            self.Middle_Frame1, font=self.entry_font)
        self.sender_address_entry.grid(column=1, row=2, columnspan=4, sticky='w')

        self.sender_address_entry1 = ttk.Entry(
            self.Middle_Frame1, font=self.entry_font)
        self.sender_address_entry1.grid(column=2, row=2, columnspan=4, sticky='w')

        self.sender_address_entry2 = ttk.Entry(
            self.Middle_Frame1, font=self.entry_font)
        self.sender_address_entry2.grid(column=3, row=2, columnspan=4, sticky='w')

        self.sender_address_entry3 = ttk.Entry(
            self.Middle_Frame1, font=self.entry_font)
        self.sender_address_entry3.grid(column=4, row=2, columnspan=4, sticky='w')

        self.remarks_lable = ttk.Label(
            self.Middle_Frame1, text='Remarks', font=self.label_font)
        self.remarks_lable.grid(
            column=0, row=3, padx=20, pady=5, sticky='w')
        self.remarks_entry = ttk.Entry(
            self.Middle_Frame1, font=self.entry_font, width=60)
        self.remarks_entry.grid(column=1, row=3, columnspan=4, pady=5, sticky='w')

        self.cnic_label = ttk.Label(
            self.Middle_Frame, text='CNIC', font=self.label_font)
        self.cnic_label.grid(column=0, row=0, padx=20, pady=20, sticky='w')
        self.name_label = ttk.Label(
            self.Middle_Frame, text='Domicile Holder Name', font=self.label_font)
        self.name_label.grid(column=2, row=0, padx=20, sticky='w')
        self.relation_label = ttk.Label(
            self.Middle_Frame, text='Relation', font=self.label_font)
        self.relation_label.grid(column=0, row=1, padx=20, sticky='w')
        
        self.father_name_label = ttk.Label(
            self.Middle_Frame, text='Father/Husband Name', font=self.label_font)
        self.father_name_label.grid(column=2, row=1, padx=20, sticky='w')
        self.cnic_entry = ttk.Entry(self.Middle_Frame, font=self.entry_font)
        self.cnic_entry.grid(column=1, row=0, pady=20, sticky='w')
        self.cnic_entry.bind('<Tab>', lambda event: [self.check_already_issued(), self.fetch_rec()])
        self.name_entry = ttk.Entry(self.Middle_Frame)
        self.name_entry.grid(column=3, row=0, sticky='w')
        self.relation = Listbox(
            self.Middle_Frame, width=20, height=1, selectmode='single', exportselection=0, font=self.entry_font)
        self.relation.grid(column=1, row=1, pady=10, sticky='w')
        self.relation.insert(0, 's/o')
        self.relation.insert(1, 'd/o')
        self.relation.insert(2, 'w/o')
        self.relation.bind('<KeyPress>', self.select_keysym_value)
        self.father_name_entry = ttk.Entry(
            self.Middle_Frame, font=self.entry_font)
        self.father_name_entry.bind('<Return>', self.add)
        self.father_name_entry.grid(
            column=3, row=1, pady=10, sticky='w')
        self.address_label = ttk.Label(
            self.Middle_Frame, text='Address', font=self.label_font)
        self.address_label.grid(column=0, row=3, padx=20, pady=10, sticky='w')
        self.address_entry = ttk.Entry(
            self.Middle_Frame, width=63, font=self.entry_font)
        self.address_entry.grid(
            column=1, row=3, columnspan=4, pady=10, sticky='w')

        self.domicile_label = ttk.Label(
            self.Middle_Frame, text='Domicile No', font=self.label_font)
        self.domicile_label.grid(column=0, row=4, padx=20, pady=10, sticky='w')
        self.domicile_entry = ttk.Entry(
            self.Middle_Frame, width=20, font=self.entry_font)
        self.domicile_entry.grid(column=1, row=4, pady=10, sticky='w')

        self.domicile_date_label = ttk.Label(
            self.Middle_Frame, text='Domicile Date', font=self.label_font)
        self.domicile_date_label.grid(
            column=2, row=4, padx=20, pady=10, sticky='w')
        self.domicile_date_entry = ttk.Entry(
            self.Middle_Frame, width=20, font=self.entry_font)
        self.domicile_date_entry.grid(
            column=3, row=4, pady=10, sticky='w')

        self.trv = ttk.Treeview(
            self.Bottom_Frame1, height=7, selectmode='browse', style='Treeview')
        self.trv.pack(fill='x')
        self.trv.bind("<Button-1>", self.self_trv_click)
        self.trv.bind('<Return>', self.self_trv_click)
        self.trv["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8")
        self.trv['show'] = 'headings'
        self.trv.column("1", width=50, anchor='w')
        self.trv.column("2", width=150, anchor='w')
        self.trv.column("3", width=250, anchor='w')
        self.trv.column("4", width=100, anchor='w')
        self.trv.column("5", width=250, anchor='w')
        self.trv.column("6", width=120, anchor='w')
        self.trv.column("7", width=120, anchor='w')
        self.trv.column("8", width=250, anchor='w')

        self.trv.heading("1", text="App_ID", anchor='w')
        self.trv.heading("2", text="CNIC", anchor='w')
        self.trv.heading("3", text="Name", anchor='w')
        self.trv.heading("4", text="Relation", anchor='w')
        self.trv.heading("5", text="Father Name", anchor='w')
        self.trv.heading("6", text="Domicile No", anchor='w')
        self.trv.heading("7", text="Domicile Date", anchor='w')
        self.trv.heading("8", text="Address", anchor='w')
        self.Add_Btn = ttk.Button(self.Bottom_Frame, command=self.add,
                                  text='Add Applicant', width=15)
        self.Add_Btn.grid(column=0, row=1, padx=10, pady=10)
        self.Del_Btn = ttk.Button(self.Bottom_Frame, text='Del Applicant',
                                  command=self.del_child, width=15)
        self.Del_Btn.grid(column=1, row=1, padx=10, pady=10)

        self.save_Btn = ttk.Button(self.Bottom_Frame, text='Save Record',
                                   command=self.Save_data, width=15)
        self.save_Btn.grid(column=2, row=1, padx=10, pady=10)
        self.edit_Btn = ttk.Button(self.Bottom_Frame, text='Edit Records',
                                   command=self.edit_records, width=15)
        self.edit_Btn.grid(column=3, row=1, padx=10, pady=10)
        self.letter_Btn = ttk.Button(self.Bottom_Frame, text='Issue Letter',
                                     command=self.issue_letter, width=15)
        self.letter_Btn.grid(column=4, row=1, padx=10, pady=10)
        self.exit_Btn = ttk.Button(self.Bottom_Frame, text='Exit',
                                   command=self.destroy, width=15)
        self.exit_Btn.grid(column=5, row=1, padx=10, pady=10)
    def fetch_rec(self, event):
        if len(self.cnic_entry.get().strip()) != 13:
            return
        try:
            responce = self.session.get(f'https://admin-icta.nitb.gov.pk/domicile/applications?keyword={self.cnic_entry.get()}&from=&to=&status=')
            if responce.url == 'https://admin-icta.nitb.gov.pk/login':
                messagebox.showerror('Session Expired', 'Your NITB Session is expired. Please relogin to create new session')
                return
        except Exception as e:
            messagebox.showerror('Error', e)
            return
        soup = BeautifulSoup(responce.content, 'html.parser')
        notfound = soup.find('div', class_ = 'alert alert-info alert-dismissable fade show has-icon')
        if notfound is None:
            for links in soup.find_all('a', href=True, class_='dropdown-item'):
                data_link = links['href']
            details_page = self.session.get(data_link)
            soup = BeautifulSoup(details_page.content, 'html.parser')
            data_dict = {}
            address = False
            for row in soup.find_all('div', class_='row mb-2'):
                if row.text.find(':') != -1:
                    if row.text[:13].strip() == 'Payment Paid':
                        pass
                    else:
                        attrib, val = row.text.split(":")
                        if row.text[:8].strip() == 'Address':
                            data_dict[attrib.strip()] = val.strip()
                            address = True
                        if address == True:
                            address = False
                            pass
                        else:
                            data_dict[attrib.strip()] = val.strip()
            self.name_entry.delete(0, 'end')
            self.name_entry.insert(0, data_dict['Name'])
            self.father_name_entry.delete(0, 'end')
            self.father_name_entry.insert(0, data_dict['Father/Husband Name'])
            self.address_entry.delete(0, 'end')
            self.address_entry.insert(0, data_dict['Address'])
            self.domicile_entry.delete(0, 'end')
            self.domicile_entry.insert(0, data_dict['Application Number'])
            self.domicile_date_entry.delete(0, 'end')
            self.domicile_date_entry.insert(0, data_dict['Payment Due Date'])
    def create_session(self):
        self.session = requests.session()
        url = f'https://admin-icta.nitb.gov.pk/login'
        try:
            page = self.session.get(url)
        except Exception as e:
            messagebox.showerror('Connection Error', e)
            return
        soup = BeautifulSoup(page.content, 'html')
        for links in soup.find_all('input', type='hidden'):
            _token = links.attrs['value']
            break
        payload = {'_token':_token, 'email':'hamidshah09@gmail.com', 'password':'2891dimah', 'submit':'login'}
        try:
            responce = self.session.post(url, data=payload)
        except Exception as e:
            messagebox.showerror('Authentication Error', e)
            return
        if responce.status_code == 200:
            self.session_status = True
        else:
            self.session_status = False    

    def check_already_issued(self, *args):
        con, cur = open_con(False)
        cnic = self.cnic_entry.get().strip()
        Query = "Select CNIC from verification_applicants Where CNIC = %s;"
        cur.execute(Query, [cnic])
        data = cur.fetchall()
        print(data)
        if data:
            messagebox.showerror(
                'Error', "Verificatin Letter already issued to this applicant")
            con.close()
            return 'verification already issued'
        else:
            con.close()
            return 'verification not issued'

    def add(self, *args):
        if self.sender.get().find("'") != -1:
            return messagebox.showerror("String Error", "Special Character (') not allowed.")
        if len(self.cnic_entry.get()) == 0:
            return messagebox.showerror('Error', "Please Provide Applicant's CNIC")
        if len(self.cnic_entry.get()) != 13:
            return messagebox.showerror('Error', "CNIC lenth is not 13 digit")
        if len(self.relation.curselection()) == 0:
            return messagebox.showerror('Error', 'Relation Not selected')
        elif len(self.relation.curselection()) > 1:
            return messagebox.showerror('Error', 'Please Select Single value from Relation \n instead of multiple values')
        if len(self.name_entry.get()) == 0:
            return messagebox.showerror('Error', "Please Provide Applicant's Name")
        if len(self.father_name_entry.get()) == 0:
            return messagebox.showerror('Error', "Please Provide Applicant's Father Name")
        if len(self.domicile_entry.get()) == 0:
            return messagebox.showerror('Error', "Please Provide Domicile No")
        if len(self.domicile_date_entry.get()) == 0:
            return messagebox.showerror('Error', "Please Provide Domicile Date")
        else:
            validation_result = Validation.validate_date(
                self.domicile_date_entry.get())
            if validation_result != 'valid':
                return messagebox.showerror('Error', validation_result)
        if self.child_edit_mode == False:
            for line in self.trv.get_children():
                if str(self.trv.item(line)['values'][1]) == self.cnic_entry.get():
                    return messagebox.showerror('Error', 'CNIC Already exist')
            self.check_already_issued()
            self.trv.insert("", 'end',
                            values=(0, self.cnic_entry.get(), self.name_entry.get(), self.relation.get(self.relation.curselection()), self.father_name_entry.get(), self.domicile_entry.get(), self.domicile_date_entry.get(), self.address_entry.get()))
            self.cnic_entry.delete('0', 'end')
            self.name_entry.delete('0', 'end')
            self.father_name_entry.delete('0', 'end')
            self.address_entry.delete('0', 'end')
            self.domicile_entry.delete('0', 'end')
            self.domicile_date_entry.delete('0', 'end')
            self.cnic_entry.focus_set()
        else:

            selectedItem = self.trv.selection()[0]

            val_tpl = tuple(("{}".format(self.trv.item(selectedItem)['values'][0]), "{}".format(self.cnic_entry.get()), "{}".format(self.name_entry.get()), "{}".format(
                self.relation.get(self.relation.curselection())), "{}".format(self.father_name_entry.get()), "{}".format(self.domicile_entry.get()), "{}".format(self.domicile_date_entry.get()), "{}".format(self.address_entry.get())))
            self.cnic_entry.delete('0', 'end')
            self.name_entry.delete('0', 'end')
            self.father_name_entry.delete('0', 'end')
            self.address_entry.delete('0', 'end')
            self.domicile_entry.delete('0', 'end')
            self.domicile_date_entry.delete('0', 'end')
            self.trv.item(selectedItem, text='', values=val_tpl)
            self.child_edit_mode = False
            self.Add_Btn.config(text='Add Applicant')

    def self_trv_click(self, *args):

        if len(self.trv.selection()) == 0:
            return
        self.child_edit_mode = True
        self.Add_Btn.config(text='Update Child')

        selectedItem = self.trv.selection()[0]
        self.cnic_entry.delete('0', 'end')
        self.name_entry.delete('0', 'end')
        self.father_name_entry.delete('0', 'end')
        self.address_entry.delete('0', 'end')
        self.domicile_entry.delete('0', 'end')
        self.domicile_date_entry.delete('0', 'end')
        self.cnic_entry.insert(0, self.trv.item(selectedItem)['values'][1])
        self.old_cnic = self.trv.item(selectedItem)['values'][1]
        self.name_entry.insert(0, self.trv.item(selectedItem)['values'][2])
        self.father_name_entry.insert(
            0, self.trv.item(selectedItem)['values'][4])
        if self.trv.item(selectedItem)['values'][3] == 's/o':
            self.relation.select_set(0)
            self.relation.see(0)
        elif self.trv.item(selectedItem)['values'][3] == 'd/o':
            self.relation.select_set(1)
            self.relation.see(1)
        elif self.trv.item(selectedItem)['values'][3] == 'w/o':
            self.relation.select_set(2)
            self.relation.see(2)
        self.domicile_entry.insert(0, self.trv.item(selectedItem)['values'][5])
        self.domicile_date_entry.insert(
            0, self.trv.item(selectedItem)['values'][6])
        self.address_entry.insert(0, self.trv.item(selectedItem)['values'][7])

    def del_child(self):
        self.trv.delete(self.trv.selection())
        self.clear_form()
        self.child_edit_mode = False
        self.Add_Btn.config(text='Add Applicant')

    def Save_data(self):
        if len(self.letter_date_entry.get()) != 0:
            try:
                letter_date = datetime.strptime(self.letter_date_entry.get(), "%Y-%m-%d").date()
            except ValueError:
                messagebox.showerror('Date Format Error', 'Please Provide date in yyyy-mm-dd')
                return
        else:
            return messagebox.showerror('Error', 'Please Provide Letter Date')
        if len(self.letter_no_entry.get()) == 0:
            return messagebox.showerror('Error', 'Please Provide Letter No')
        if len(self.sender.get()) == 0:
            return messagebox.showerror('Error', 'Please Provide Letter Sender Name')
        if len(self.sender_designation_entry.get()) == 0:
            return messagebox.showerror('Error', 'Please Provide Letter Sender Designation')

        if self.edit_mode == False:
            self.data_list = []

            for line in self.trv.get_children():
                self.data_list.append(self.trv.item(line)['values'])
            if len(self.data_list) == 0:
                return messagebox.showerror('Error', 'Nothing to Save')
            sender_address = self.sender_address_entry.get()
            if  len(self.sender_address_entry1.get()) != 0:
                sender_address = sender_address + ">" + self.sender_address_entry1.get()
            if  len(self.sender_address_entry2.get()) != 0:
                sender_address = sender_address + ">" + self.sender_address_entry2.get()
            if  len(self.sender_address_entry3.get()) != 0:
                sender_address = sender_address + ">" + self.sender_address_entry3.get()
            Query = "Insert Into verification_letters (Letter_Date, Letter_No, Letter_Sent_by, Designation, sender_address, Remarks) values (%s,%s, %s,%s, %s, %s);"
            parm_list = [letter_date, self.letter_no_entry.get(), self.sender.get(), self.sender_designation_entry.get(), sender_address, self.remarks_entry.get()]

            con, cur = open_con(False)
            cur.execute(Query, parm_list)
            con.commit()
            Query = 'Select Letter_ID from verification_letters order by Letter_ID desc Limit 1;'
            cur.execute(Query)
            let_id_data = cur.fetchall()
            last_letter_id = let_id_data[0][0]
            Query = "SELECT Dispatch_No, Year(timestamp) as Last_Year, Year(curdate()) as Cur_Year FROM dispatch_dairy order by Dispatch_ID desc;"
            cur.execute(Query)
            Last_Dispatch_data = cur.fetchall()

            if Last_Dispatch_data is not None:
                if Last_Dispatch_data[0][1] != Last_Dispatch_data[0][2]:
                    last_dispatch = 1
                else:
                    last_dispatch = 1 + Last_Dispatch_data[0][0]
            else:
                last_dispatch = 1
            Query = "Insert Into dispatch_dairy (Dispatch_No, Letter_Type, Letter_ID) values (%s, 'Verification Letter', %s);"
            parm_list= [last_dispatch, last_letter_id]
            cur.execute(Query, parm_list)
            con.commit()
            for row in self.data_list:
                Query = "Insert Into verification_Applicants (Letter_ID,CNIC,Applicant_Name,Relation,Applicant_FName, address, Domicile_No, Domicile_Date) values (%s,%s,%s, %s,%s,%s, %s,%s);"
                parm_list = [last_letter_id, row[1], row[2], row[3], row[4], row[7], row[5], row[6]]

                cur.execute(Query, parm_list)
                con.commit()
            messagebox.showinfo('Success', "New Record Saved")
            con.close()
            self.clear_form()
            return
        else:
            if self.letter_id['letter_id'] == 0:
                return messagebox.showerror('Error', 'No Record ID to Update')
            self.updated_data_list = []
            for line in self.trv.get_children():
                self.updated_data_list.append(
                    self.trv.item(line)['values'])
            # for addition entries
            self.addition_list = []
            self.updation_list = []
            for item in self.updated_data_list:
                if item[0] not in self.old_child_list:
                    self.addition_list.append(item)
                else:
                    self.updation_list.append(item)

            # for deletion entries
            self.updated_id_list = []
            for item in self.updated_data_list:
                self.updated_id_list.append(item[0])
            self.deletion_list = []
            for item in self.old_child_list:
                if item not in self.updated_id_list:
                    if item != 0:
                        self.deletion_list.append(item)
            print("Addition List:-", self.addition_list)
            print("Updation List:-", self.updation_list)
            print("Deletion List:-", self.deletion_list)
            sender_address = self.sender_address_entry.get()
            if  len(self.sender_address_entry1.get()) != 0:
                sender_address = sender_address + ">" + self.sender_address_entry1.get()
            if  len(self.sender_address_entry2.get()) != 0:
                sender_address = sender_address + ">" + self.sender_address_entry2.get()
            if  len(self.sender_address_entry3.get()) != 0:
                sender_address = sender_address + ">" + self.sender_address_entry3.get()
            con, cur = open_con(False)
            Query = "Update verification_letters Set Letter_Date=%s, Letter_No=%s, Letter_Sent_by = %s, Designation=%s, sender_address=%s , Remarks=%s Where Letter_ID = %s;"
            parm_list = [self.letter_date_entry.get(), self.letter_no_entry.get(), self.sender.get(), self.sender_designation_entry.get(), sender_address, self.remarks_entry.get(), self.letter_id['letter_id']]
            cur.execute(Query, parm_list)
            con.commit()
            if len(self.updation_list) != 0:
                for row in self.updation_list:
                    Query = "Update verification_Applicants Set CNIC = %s, Applicant_Name = %s, Relation = %s, Applicant_FName = %s, address=%s, Domicile_No = %s, Domicile_Date = %s Where App_ID = %s;"
                    parm_list = [str(row[1]), row[2], row[3], row[4], row[7], row[5], row[6], row[0]]
                    cur.execute(Query, parm_list)
                    con.commit()
                    
            if len(self.addition_list) != 0:
                for row in self.addition_list:
                    Query = "Insert Into verification_Applicants (Letter_ID,CNIC,Applicant_Name,Relation,Applicant_FName, address, Domicile_No, Domicile_Date) values (%s,%s,%s, %s,%s,%s,%s,%s);"
                    parm_list=[self.letter_id['letter_id'], str(row[1]), row[2], row[3], row[4], row[7], row[5], row[6]]
                    cur.execute(Query, parm_list)
                    con.commit()
            if len(self.deletion_list) != 0:
                for row in self.deletion_list:
                    Query = "Delete From verification_Applicants Where App_ID = %s;"
                    cur.execute(Query, [row[0]])
                    con.commit()
            messagebox.showinfo('Success', "Record Updated")
            con.close()
            self.edit_mode = False
            self.save_Btn.config(text='Save Record')
            self.child_edit_mode = False
            self.Add_Btn.config(text='Add Applicant')
            self.addition_list = []
            self.deletion_list = []
            self.trv.delete(*self.trv.get_children())
            self.letter_id = {'letter_id':0, 'reply_type':'official'}
            self.clear_form()

    def clear_form(self):
        self.letter_no_entry.delete('0', 'end')
        self.sender.delete('0', 'end')
        self.letter_date_entry.delete('0', 'end')
        self.sender_designation_entry.delete('0', 'end')
        self.sender_address_entry.delete('0', 'end')
        self.sender_address_entry1.delete('0', 'end')
        self.sender_address_entry2.delete('0', 'end')
        self.sender_address_entry3.delete('0', 'end')
        self.cnic_entry.delete('0', 'end')
        self.name_entry.delete('0', 'end')
        self.father_name_entry.delete('0', 'end')
        self.address_entry.delete('0', 'end')
        self.domicile_entry.delete('0', 'end')
        self.domicile_date_entry.delete('0', 'end')
        self.trv.delete(*self.trv.get_children())
        self.remarks_entry.delete('0', 'end')

    def load_data(self):

        if self.letter_id['letter_id'] != 0:
            Query = """SELECT l.Letter_ID, d.Dispatch_No, l.Letter_Date, l.Letter_No, l.Letter_Sent_by, l.Designation, l.sender_address, l.Remarks,
                            a.App_ID, a.CNIC, a.Applicant_Name, a.Relation, a.Applicant_FName, a.Domicile_No, a.Domicile_Date, a.address
                            FROM verification_letters as l 
                            Left Join verification_applicants as a
                            On l.Letter_ID = a.Letter_ID
                            Inner Join dispatch_dairy as d
                            on d.Letter_ID = l.Letter_ID
                            Where l.Letter_ID = %s And d.Letter_Type = 'Verification Letter';"""
            con, cur = open_con(True)
            cur.execute(Query, [self.letter_id['letter_id']])
            data = cur.fetchall()
            con.close()
            self.clear_form()
            loop = 0
            self.old_child_list = []
            self.cnic_entry.get()
            self.trv.delete(*self.trv.get_children())
            for row in data:
                loop += 1
                if loop == 1:
                    self.clear_form()
                    self.letter_no_entry.insert(0, row['Letter_No'])
                    self.letter_date_entry.insert(0, row['Letter_Date'])
                    self.sender.insert(0, row['Letter_Sent_by'])
                    self.sender_designation_entry.insert(
                        0, str(row['Designation']))
                    a = 0
                    for address_item in row['sender_address'].split('>'):
                        a +=1
                        if a==1:
                            self.sender_address_entry.insert(0, str(address_item))
                        elif a==2:
                            self.sender_address_entry1.insert(0, str(address_item))
                        elif a==3:
                            self.sender_address_entry2.insert(0, str(address_item))
                        elif a==4:
                            self.sender_address_entry3.insert(0, str(address_item))
                    self.remarks_entry.insert('0', str(row['Remarks']))
                if row['App_ID'] is not None:
                    self.trv.insert("", 'end',
                                    values=(row['App_ID'], int(row['CNIC']), row['Applicant_Name'], row['Relation'], row['Applicant_FName'], row['Domicile_No'], row['Domicile_Date'], row['address']))
                    # lst = list((int(row['CNIC']), "{}".format(row['Applicant_Name']), "{}".format(
                    #     row['Relation']), "{}".format(row['Applicant_FName']), "{}".format(row['Applicant_FName'])))
                    self.old_child_list.append(row['App_ID'])

                self.edit_mode = True
                self.save_Btn.config(text='Update Record')
        else:
            print('Record ID Not available')

    def Record_Selector(self):
        def Search(*args):
            if len(search_input.get()) == 0:
                return messagebox.showerror(
                    'Error', 'Please Provide Search Input')
            if search_type.get(search_type.curselection()) == 'Date':
                validation_result = Validation.validate_date(
                    search_input.get())
                if validation_result != 'valid':
                    return messagebox.showerror('Error', validation_result)
                Query = """SELECT l.Letter_ID, d.Dispatch_No, l.Letter_No, l.Letter_Date, l.Letter_Sent_by, a.CNIC, a.Applicant_Name, a.Relation, a.Applicant_FName 
                        FROM verification_letters as l 
                        Inner Join verification_applicants as a
                        On l.Letter_ID = a.Letter_ID
                        Inner Join dispatch_dairy as d
                        on d.Letter_ID = l.Letter_ID
                        Where l.Letter_Date = '{}' And d.Letter_Type = 'Verification Letter';""".format(search_input.get())
            elif search_type.get(search_type.curselection()) == 'Dispatch No':
                if search_input.get().isnumeric():
                    Query = """SELECT l.Letter_ID, d.Dispatch_No, l.Letter_No, l.Letter_Date, l.Letter_Sent_by, a.CNIC, a.Applicant_Name, a.Relation, a.Applicant_FName 
                            FROM verification_letters as l 
                            Inner Join verification_applicants as a
                            On l.Letter_ID = a.Letter_ID
                            Inner Join dispatch_dairy as d
                            on d.Letter_ID = l.Letter_ID
                            Where d.Dispatch_No = {} And d.Letter_Type = 'Verification Letter';""".format(search_input.get())
                else:
                    return messagebox.showerror('Error', "Dispatch No shall be a number")
            elif search_type.get(search_type.curselection()) == 'CNIC':
                if len(search_input.get()) != 13:
                    return messagebox.showerror('Error', "CNIC Number lenth shall be 13 digit without dashes")
                if search_input.get().isnumeric():
                    Query = """SELECT l.Letter_ID, d.Dispatch_No, l.Letter_No, l.Letter_Date, l.Letter_Sent_by, a.CNIC, a.Applicant_Name, a.Relation, a.Applicant_FName 
                            FROM verification_letters as l 
                            Inner Join verification_applicants as a
                            on l.Letter_ID = a.Letter_ID
                            Inner Join dispatch_dairy as d
                            on d.Letter_ID = l.Letter_ID
                            Where a.CNIC = {} And d.Letter_Type = 'Verification Letter';""".format(search_input.get())
                else:
                    return messagebox.showerror('Error', "Input for CNIC search shall be a number")
            else:
                return messagebox.showerror(
                    'Error', "Please Select Search Type from List")
            con, cur = open_con(True)
            cur.execute(Query)
            data = cur.fetchall()
            con.close()
            trv.delete(*trv.get_children())
            lett_id = 0
            for row in data:
                if lett_id != row['Letter_ID']:
                    trv.insert("", 'end',
                               values=(row['Letter_ID'], row['Letter_Date'], row['Dispatch_No'], row['Letter_Sent_by'], row['CNIC'], row['Applicant_Name']))
                lett_id = row['Letter_ID']

        def start_up():
            Query = """SELECT l.Letter_ID, d.Dispatch_No, l.Letter_Date, l.Letter_No, l.Letter_Sent_by, a.CNIC, a.Applicant_Name, a.Relation, a.Applicant_FName 
                            FROM verification_letters as l 
                            Left Join verification_applicants as a
                            on l.Letter_ID = a.Letter_ID
                            Inner Join dispatch_dairy as d
                            on d.Letter_ID = l.Letter_ID
                            Where d.Letter_Type = 'Verification Letter' order by l.Letter_ID Desc Limit 50;"""
            con, cur = open_con(True)
            cur.execute(Query)
            if type(cur) is str:
                return messagebox.showerror('Db Connection Error', 'Looks Like Data base is not connected')
            data = cur.fetchall()
            con.close()
            trv.delete(*trv.get_children())
            lett_id = 0
            for row in data:
                if lett_id != row['Letter_ID']:
                    trv.insert("", 'end',
                               values=(row['Letter_ID'], row['Letter_Date'], row['Dispatch_No'], row['Letter_Sent_by'], row['CNIC'], row['Applicant_Name']))
                lett_id = row['Letter_ID']

        def cancel():
            self.letter_id = {'letter_id':0, 'reply_type':'personal'}
            self.edit_window.quit()
            self.edit_window.destroy()

        def trv_click(*args):
            if len(trv.selection()) == 0:
                return messagebox.showerror('Error', 'Nothing Selected')
            selectedItem = trv.selection()[0]
            self.cnic_entry.delete('0', 'end')
            self.name_entry.delete('0', 'end')
            self.father_name_entry.delete('0', 'end')
            self.address_entry.delete('0', 'end')
            self.domicile_entry.delete('0', 'end')
            self.domicile_date_entry.delete('0', 'end')
            if self.checkbutton_var.get() == 1:
                self.letter_id = {'letter_id':trv.item(selectedItem)['values'][0], 'reply_type':'personal'}
            else:
                self.letter_id = {'letter_id':trv.item(selectedItem)['values'][0], 'reply_type':'official'}                
            self.edit_window.quit()
            self.edit_window.destroy()

        self.letter_id = {'letter_id':0, 'reply_type':'official'}
        self.edit_window = Toplevel()
        self.edit_window.geometry("1000x400")
        self.edit_window.title('Record Selection')
        Top_Frame = ttk.Frame(self.edit_window)
        Top_Frame.pack(fill='x')
        search_type = Listbox(
            Top_Frame, width=15, height=1, exportselection=0)
        search_type.grid(row=1, column=0, padx=10, pady=10)
        search_type.insert(0, "Dispatch No")
        search_type.insert(1, "Date")
        search_type.insert(2, "CNIC")
        search_type.select_set(0)
        search_type.see(0)
        search_input = ttk.Entry(Top_Frame, width=15, font=self.label_font)
        search_input.grid(row=1, column=1, padx=10, pady=10)
        search_input.bind('<Return>', Search)
        Bottom_Frame = ttk.Frame(self.edit_window)
        Bottom_Frame.pack(fill='x', expand=1)
        trv = ttk.Treeview(Bottom_Frame, selectmode='browse', height=15)
        trv.pack(fill='both', expand=True, padx=10, pady=10)
        trv["columns"] = ("1", "2", "3", "4", "5", "6")
        trv['show'] = 'headings'
        trv.column("1", width=50, anchor='w')
        trv.column("2", width=80, anchor='w')
        trv.column("3", width=100, anchor='w')
        trv.column("4", width=120, anchor='w')
        trv.column("5", width=120, anchor='w')
        trv.column("6", width=150, anchor='w')

        trv.heading("1", text="Letter ID", anchor='w')
        trv.heading("2", text="Letter Date", anchor='w')
        trv.heading("3", text="Dispatch No", anchor='w')
        trv.heading("4", text="Letter_Sent_by", anchor='w')
        trv.heading("5", text="Applicant CNIC", anchor='w')
        trv.heading("6", text="Applicant Name", anchor='w')
        trv.bind("<Double-1>", trv_click)

        search_btn = ttk.Button(Top_Frame, width=15,
                            text='Search', command=Search)
        search_btn.grid(row=1, column=3)
        cancel_btn = ttk.Button(Top_Frame, width=15, text='Cancel', command=cancel)
        cancel_btn.grid(row=1, column=4, padx=10, pady=10)
        self.reply_type = ttk.Checkbutton(Top_Frame, text = "Reply to applicant", variable = self.checkbutton_var,
                onvalue = 1, offvalue = 0)
        self.reply_type.grid(row=1, column=5, padx=10, pady=10)
        start_up()
        self.edit_window.mainloop()

    def edit_records(self):
        self.Record_Selector()
        self.load_data()
    def select_keysym_value(self, event):

        for itm in range(event.widget.size()):
            if event.keysym.upper() == event.widget.get(itm)[:1]:
                event.widget.selection_clear(0, 'end')
                event.widget.select_set(itm)
                event.widget.see(itm)
                event.widget.activate(itm)
                break
    def issue_letter(self):
        self.Record_Selector()
        if self.letter_id['letter_id'] == 0:
            return messagebox.showerror('Error', 'Nothing Selected')

        Query = """SELECT l.timestamp, l.Letter_ID, d.Dispatch_No, l.Letter_No, l.Letter_Date, l.Letter_Sent_by, l.Designation, l.sender_address, 
                    a.CNIC, a.Applicant_Name, a.Relation, a.Applicant_FName, a.address, a.Domicile_No, a.Domicile_Date 
                    FROM verification_letters as l 
                    Inner Join verification_applicants as a
                    on l.Letter_ID = a.Letter_ID
                    Inner Join dispatch_dairy as d
                    on d.Letter_ID = l.Letter_ID
                    Where l.Letter_ID = %s And d.Letter_Type = 'Verification Letter';"""
        con, cur = open_con(True)
        cur.execute(Query, [self.letter_id['letter_id']])
        data = cur.fetchall()
        if len(data) != 0:

            pdf = FPDF()
            pdf.add_page()
            pdf.set_left_margin(15)
            pdf.set_right_margin(15)
            # pdf.add_font('courier', '', "c:\WINDOWS\FONTS\courier.ttf", uni=True)
            # pdf.add_font('courier', 'B', "c:\WINDOWS\FONTS\courier.ttf", uni=True)
            pdf.set_font('courier', 'B', size=16)
            pdf.set_fill_color(211, 211, 211)
            # pdf.image('govt_logo.png', x=10, y=10, w=30, h=30)
            pdf.ln(7)
            # pdf.cell(20, 6, text='', align='C')
            pdf.cell(0, 6, text='OFFICE OF THE DISTRICT MAGISTRATE',
                     new_x="LMARGIN", new_y="NEXT", align='C')
            # pdf.cell(20, 6, text='', align='C')
            pdf.cell(0, 6, text='ISLAMABAD CAPITAL TERRITORY',
                     new_x="LMARGIN", new_y="NEXT", align='C')
            # pdf.cell(20, 6, text='', align='C')
            pdf.cell(0, 6, text='ISLAMABAD',
                     new_x="LMARGIN", new_y="NEXT", align='C')
            pdf.set_font('courier', size=14)
            pdf.ln(8)
            pdf.cell(10, 6, text='')
            pdf.cell(20, 6, text='From:', align='L')
            pdf.cell(10, 6, text='')
            pdf.cell(30, 6, text='The District Magistrate',
                     new_x="LMARGIN", new_y="NEXT", align='L')
            pdf.cell(40, 6, text='')
            pdf.cell(30, 6, text='ICT, Islamabad',
                     new_x="LMARGIN", new_y="NEXT", align='L')
            pdf.ln(8)
            pdf.cell(10, 6, text='')
            pdf.cell(20, 6, text='To:', align='L')
            pdf.cell(10, 6, text='')
            pdf.cell(0, 6, text='{},'.format(
                data[0]['Letter_Sent_by']), align='L', new_x="LMARGIN", new_y="NEXT")
            pdf.cell(40, 6, text='')
            pdf.cell(0, 6, text='{},'.format(
                data[0]['Designation']), align='L', new_x="LMARGIN", new_y="NEXT")
            for address in data[0]['sender_address'].split(">"):
                pdf.cell(40, 6, text='')
                pdf.cell(0, 6, text=f'{address}', align='L', new_x="LMARGIN", new_y="NEXT")

            pdf.ln(8)
            if data[0]['Dispatch_No'] is not None:
                pdf.cell(
                    20, 6, text='No.{}/Domicile'.format(data[0]['Dispatch_No']), align='L')
            # pdf.cell(15, 6, text='', align='L')
            issuance_date = data[0]['timestamp'].strftime('%d-%m-%Y')
            pdf.cell(0, 6, text='Dated: {}'.format(
                issuance_date), new_x="LMARGIN", new_y="NEXT",  align='R')
            pdf.ln(8)

            
            pdf.cell(15, 6, text='Subject:', align='L')
            pdf.cell(15, 6, text='')
            pdf.set_font('courier', 'BU', size=14)
            pdf.cell(40, 6, text='VERIFICATION OF DOMICILE',
                     new_x="LMARGIN", new_y="NEXT", align='L')

            pdf.set_font('courier', size=14)
            #Letter No. {}
            if self.letter_id['reply_type'] == 'official':
                starter_text = '         Kindly refer to your office Letter No {}, Dated {}, on the subject noted above.'.format(data[0]['Letter_No'], data[0]['Letter_Date'].strftime('%d-%m-%Y'))
            else:
                starter_text = '         Kindly refer to your application, Dated {}, on the subject noted above.'.format(data[0]['Letter_Date'].strftime('%d-%m-%Y'))
            pdf.multi_cell(
                0, 10, text=starter_text, new_x="LMARGIN", new_y="NEXT")
            pdf.multi_cell(0, 10, text='2.      The record reveals that the following domicile certificate has been issued by this office:-')
            
            pdf.ln(4)
            sl = 0
            grey = (128, 128, 128)
            white = (255, 255, 255)
            headings_style = FontFace(emphasis="BOLD", fill_color=grey)
            table_style = FontFace(fill_color=white)
            with pdf.table(headings_style=headings_style, first_row_as_headings=False, line_height=7, padding=2, text_align=("CENTER", "LEFT", "CENTER", "CENTER"), col_widths=(10, 41, 23, 18)) as table:
                row = table.row()
                row.cell("S.No")
                row.cell("Name & Address")
                row.cell("Domicile No")
                row.cell("Issuance Date")
                for data_row in data:
                    row = table.row(style=table_style)
                    sl += 1
                    row.cell(str(sl))
                    row.cell(str(data_row["Applicant_Name"]) + " " + str(data_row["Relation"]) + " " + str(data_row["Applicant_FName"]) + " R/o " + str(data_row["address"]))
                    row.cell(str(data_row["Domicile_No"]))
                    row.cell(str(data_row["Domicile_Date"]))
            pdf.ln(4)
            pdf.ln(8)
            pdf.ln(8)
            # signature
            pdf.set_font('courier', 'B', size=14)
            pdf.cell(70, 6, text='')
            pdf.cell(0, 6, text='Incharge Domicile Branch', align='C', new_x="LMARGIN", new_y="NEXT")
            pdf.cell(70, 6, text='')
            pdf.cell(0, 6, text='ICT, Islamabad', align='C', new_x="LMARGIN", new_y="NEXT")

            pdf.output('Letter.pdf')
            path = 'Letter.pdf'
            os.system(path)
        else:
            return messagebox.showerror('Error', 'Record Not Complete')

    def select_keysym_value(self, event):
        for itm in range(event.widget.size()):
            if event.keysym.lower() == event.widget.get(itm)[:1]:
                event.widget.selection_clear(0, 'end')
                event.widget.select_set(itm)
                event.widget.see(itm)
                event.widget.activate(itm)
                break
if __name__ == '__main__':
    # Obj = Verification('25.33.21.56')
    # Obj.mainloop()
    Obj = Verification()
    Obj.mainloop()
