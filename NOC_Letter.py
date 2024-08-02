from ast import List
from tkinter import Toplevel, ttk, messagebox, Tk, Listbox, Variable
from turtle import mode
from bs4 import BeautifulSoup
from fpdf import FPDF
import os
import Validation
from tools import open_con
from fpdf.fonts import FontFace

class NOC(Tk):
    def __init__(self, session, user_data):
        super().__init__()
        self.geometry('1000x750+50+50')
        self.title('NOC to Other Districts')
        self.session = session
        self.user_data = user_data
        self.letter_font = 'Courier'
        self.letter_font_size = 12
        # self.tk.call('lappend', 'auto_path',
        #              r'C:\Users\Hamid Shah\Desktop\newtheam\awthemes-10.4.0')
        # self.tk.call('package', 'require', 'awarc')
        # style = ttk.Style(self)
        # style.theme_use('awarc')
        self.tk.call("source", "azure.tcl")
        self.tk.call("set_theme", "light")
        noc_style = ttk.Style(self)
        noc_style.configure('Treeview', font=(self.letter_font, 14))
        noc_style.configure("Treeview.Heading", font=(self.letter_font, 14, 'bold'))
        noc_style.configure('TButton', font=(self.letter_font, 14, 'bold'))
        noc_style.configure('TLabel', font=(self.letter_font, 14))
        noc_style.configure('TEntry', font=(self.letter_font, 14), width=40)
        noc_style.configure('Heading.TLabel', font=(self.letter_font, 14, 'bold'))
        self.Top_Frame = ttk.Frame(
            self, relief='ridge', border=1)
        self.Top_Frame.pack(fill='x')
        self.Top_label = ttk.Label(
            self.Top_Frame, text='NOC to Other Districts', border=1, font=(self.letter_font, 18, 'bold'))
        self.Top_label.pack(padx=10, pady=10, side='top')
        self.Middle_Frame = ttk.Frame(
            self, relief='ridge', border=1, height=10)
        self.Middle_Frame.pack(fill='both', expand=1)
        self.Bottom_Frame = ttk.Frame(
            self, relief='ridge', border=1, height=10)
        self.Bottom_Frame.pack(fill='x')
        self.edit_mode = False
        self.child_edit_mode = False
        self.old_cnic = ''
        self.letter_date_label = ttk.Label(
            self.Middle_Frame, text='NOC Issuance Date', font=(self.letter_font, 14, 'bold'))
        self.letter_date_label.grid(
            column=0, row=1, padx=10, pady=10, sticky='w')
        self.letter_date_entry = ttk.Entry(
            self.Middle_Frame, state='readonly', font=(self.letter_font, 14))
        self.letter_date_entry.grid(
            column=1, row=1, pady=10, sticky='w')

        self.letter_to_label = ttk.Label(
            self.Middle_Frame, text='NOC Issued To', font=(self.letter_font, 14, 'bold'))
        self.letter_to_label.grid(column=2, row=1, padx=10, pady=10, sticky='w')
        # self.letter_to_1 = Label(
        #     self.Middle_Frame, width=20, text='Deputy Commissioner/', font=('Bell', 12, 'bold'))
        # self.letter_to_1.grid(column=1, row=2, pady=10, sticky='w')
        # self.letter_to_2 = Label(
        #     self.Middle_Frame, width=20, text='Assistant Commissioner', font=('Bell', 12, 'bold'))
        # self.letter_to_2.grid(column=1, row=3, sticky='w')
        self.Districts = ttk.Entry(
            self.Middle_Frame, font=(self.letter_font, 14,))

        self.Districts.grid(column=3, pady=10, row=1, sticky='w')
        self.Districts.bind('<KeyRelease>', self.list_search)
        self.cnic_label = ttk.Label(
            self.Middle_Frame, text='CNIC', font=(self.letter_font, 14, 'bold'))
        self.cnic_label.grid(column=0, row=2, padx=20, pady=10, sticky='w')
        self.name_label = ttk.Label(
            self.Middle_Frame, text='Name', font=(self.letter_font, 14, 'bold'))
        self.name_label.grid(column=2, row=2, padx=20, sticky='w')
        self.relation_label = ttk.Label(
            self.Middle_Frame, text='Relation', font=(self.letter_font, 14, 'bold'))
        self.relation_label.grid(column=0, row=3, padx=20, sticky='w')
        self.father_name_label = ttk.Label(
            self.Middle_Frame, text='Father Name', font=(self.letter_font, 14, 'bold'))
        self.father_name_label.grid(column=2, row=3, padx=20, sticky='w')
        self.cnic_entry = ttk.Entry(
            self.Middle_Frame, font=(self.letter_font, 14, 'bold'))
        self.cnic_entry.grid(column=1, row=2, pady=10, sticky='w')
        self.cnic_entry.bind('<Tab>', self.check_already_issued)
        self.name_entry = ttk.Entry(self.Middle_Frame, font=(self.letter_font, 14))
        self.name_entry.grid(column=3, row=2, pady=10, sticky='w')
        self.relation = Listbox(
            self.Middle_Frame, width=20, height=1, selectmode='single', exportselection=0, font=(self.letter_font, 14, 'bold'))
        self.relation.grid(column=1, row=3, pady=10, sticky='w')
        self.relation.insert(0, 's/o')
        self.relation.insert(1, 'd/o')
        self.relation.insert(2, 'w/o')
        self.relation.bind('<KeyPress>', self.select_keysym_value)
        self.father_name_entry = ttk.Entry(
            self.Middle_Frame, font=(self.letter_font, 14))
        self.father_name_entry.bind('<Return>', self.add)
        self.father_name_entry.grid(
            column=3, row=3, pady=10, sticky='w')
        
        self.remarks_label = ttk.Label(
            self.Middle_Frame, text='Remarks', font=(self.letter_font, 14, 'bold'))
        self.remarks_label.grid(column=0, row=4, padx=20, sticky='w')
        self.remarks_entry = ttk.Entry(
            self.Middle_Frame, font=(self.letter_font, 14), width=60)
        self.remarks_entry.bind('<Return>', self.add)
        self.remarks_entry.grid(
            column=1, row=4, columnspan=4, pady=10, sticky='w')

        self.trv = ttk.Treeview(
            self.Middle_Frame, selectmode='browse')
        self.trv.grid(row=5, column=0, columnspan=6, padx=20, pady=10)
        self.trv.bind("<Button-1>", self.self_trv_click)
        self.trv.bind('<Return>', self.self_trv_click)
        self.trv["columns"] = ("1", "2", "3", "4", "5")
        self.trv['show'] = 'headings'
        self.trv.column("1", width=120, anchor='w')
        self.trv.column("2", width=150, anchor='w')
        self.trv.column("3", width=250, anchor='w')
        self.trv.column("4", width=100, anchor='w')
        self.trv.column("5", width=250, anchor='w')
        self.trv.heading("1", text="ID", anchor='w')
        self.trv.heading("2", text="CNIC", anchor='w')
        self.trv.heading("3", text="Name", anchor='w')
        self.trv.heading("4", text="Relation", anchor='w')
        self.trv.heading("5", text="Father Name", anchor='w')
        self.Bottom1_Frame = ttk.Frame(self.Middle_Frame)
        self.Bottom1_Frame.grid(column=0, row=6, columnspan=6, ipady=5)
        self.Add_Btn = ttk.Button(self.Bottom1_Frame, command=self.add,
                                  text='Add Applicant', width=13)
        self.Add_Btn.grid(column=0, row=0, padx=10, pady=10)
        self.Del_Btn = ttk.Button(self.Bottom1_Frame, text='Del Applicant',
                                  command=self.del_child, width=13)
        self.Del_Btn.grid(column=1, row=0, padx=10, pady=10)

        self.save_Btn = ttk.Button(self.Bottom_Frame, text='Save Record',
                                   command=self.Save_data, width=13)
        self.save_Btn.grid(column=0, row=0, padx=10, pady=10)
        self.edit_Btn = ttk.Button(self.Bottom_Frame, text='Edit Records',
                                   command=self.edit_records, width=13)
        self.edit_Btn.grid(column=1, row=0, padx=10, pady=10)
        self.letter_Btn = ttk.Button(self.Bottom_Frame, text='Issue Letter',
                                     command=self.issue_letter, width=13)
        self.letter_Btn.grid(column=2, row=0, padx=10, pady=10)
        self.font_set = ttk.Button(self.Bottom_Frame, text='Font Settings',
                                   command=self.font_settings, width=13)
        self.font_set.grid(column=3, row=0, padx=10, pady=10)
        self.exit_Btn = ttk.Button(self.Bottom_Frame, text='Exit',
                                   command=self.destroy, width=13)
        self.exit_Btn.grid(column=4, row=0, columnspan=2, padx=10, pady=10)
        
        con, cur = open_con(False)
        if type(cur) is str:
            messagebox.showerror("DB Connection Error", "Could Not Connect to Database")
        else:
            cur.execute (
                "SELECT Teh_name FROM tehsils Union Select Dis_name from districts;")
            self.Teh_Dist_names = cur.fetchall()
            cur.close()
            con.close()

    def list_search(self, event):
        # Exempted keys upon which no action would be taken
        if event.keysym == "BackSpace" or event.keysym == "Tab" or event.keysym == "Enter":
            return
        elif event.keysym == "Space":
            return
        elif event.keysym[0:5] == "Shift":
            return
        # checking, atleast one character to serach list

        if event.widget.get():
            text_lenth = len(event.widget.get())
            filtered = filter(lambda dat: dat[0][:text_lenth].upper(
            ) == event.widget.get().upper(), self.Teh_Dist_names)
            filtered_list = list(filtered)

            if len(filtered_list) != 0:
                event.widget.delete(0, 'end')
                event.widget.insert(0, filtered_list[0][0])
                event.widget.selection_range(text_lenth, 'end')



    def check_already_issued(self, *args):
        
        cnic = self.cnic_entry.get().strip()
        try:
            responce = self.session.get(f'https://admin-icta.nitb.gov.pk/domicile/applications?keyword={cnic}&from=&to=&status=')
            if responce.url == 'https://admin-icta.nitb.gov.pk/login':
                messagebox.showerror('Session Expired', 'Your NITB Session is expired. Please relogin to create new session')
                return
        except Exception as e:
            messagebox.showerror('Server Error', e)
            return
        soup = BeautifulSoup(responce.content, 'html.parser')
        notfound = soup.find('div', class_ = 'alert alert-info alert-dismissable fade show has-icon')
        if notfound is not None:
            Query = "Select CNIC from NOC_Applicants Where CNIC = %s"
            con, cur = open_con(False)
            cur.execute(Query, [cnic])
            data = cur.fetchall()
            cur.close()
            con.close()
            if data:
                messagebox.showerror(
                    'Error', "NOC already issued to this applicant")
                return 'already noc issued'
            else:
                return 'noc not issued'
        else:
            messagebox.showerror(
                'Error', "Domicile already issued")
            return 'Domicile already issued'

    def add(self, *args):

        if len(self.cnic_entry.get()) == 0:
            return messagebox.showerror('Error', "Please Provide Applicant's CNIC")
        if len(self.cnic_entry.get()) != 13:
            return messagebox.showerror('Error', "CNIC lenth is not 13 digit")
        # if self.edit_mode == False:
        #     check_result = self.check_already_issued()
        #     if check_result == 'already noc issued' or check_result == 'Domicile already issued':
        #         return
        if len(self.relation.curselection()) == 0:
            return messagebox.showerror('Error', 'Relation Not selected')
        elif len(self.relation.curselection()) > 1:
            return messagebox.showerror('Error', 'Please Select Single value from Relation \n instead of multiple values')
        if len(self.name_entry.get()) == 0:
            return messagebox.showerror('Error', "Please Provide Applicant's Name")
        if len(self.father_name_entry.get()) == 0:
            return messagebox.showerror('Error', "Please Provide Applicant's Father Name")
        if self.child_edit_mode == False:
            for line in self.trv.get_children():
                if str(self.trv.item(line)['values'][1]) == self.cnic_entry.get():
                    return messagebox.showerror('Error', 'CNIC Already exist')
            self.trv.insert("", 'end',
                            values=(0, self.cnic_entry.get(), self.name_entry.get(), self.relation.get(self.relation.curselection()), self.father_name_entry.get()))
            self.cnic_entry.delete('0', 'end')
            self.name_entry.delete('0', 'end')
            # self.father_name_entry.delete('0', 'end')
            self.cnic_entry.focus_set()
        else:

            selectedItem = self.trv.selection()[0]

            val_tpl = tuple(("{}".format(self.trv.item(selectedItem)['values'][0]), "{}".format(self.cnic_entry.get()), "{}".format(self.name_entry.get()), "{}".format(
                self.relation.get(self.relation.curselection())), "{}".format(self.father_name_entry.get())))

            self.trv.item(selectedItem, text='', values=val_tpl)
            self.child_edit_mode = False
            self.Add_Btn.config(text='Add Applicant')

    def self_trv_click(self, *args):

        if len(self.trv.selection()) == 0:
            return
        self.child_edit_mode = True
        self.Add_Btn.config(text='Update Child')
        self.cnic_entry.delete('0', 'end')
        self.name_entry.delete('0', 'end')
        self.father_name_entry.delete('0', 'end')
        selectedItem = self.trv.selection()[0]

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

    def del_child(self):
        self.trv.delete(self.trv.selection())
        self.cnic_entry.delete('0', 'end')
        self.name_entry.delete('0', 'end')
        self.father_name_entry.delete('0', 'end')
        self.child_edit_mode = False
        self.Add_Btn.config(text='Add Applicant')
    
    def select_keysym_value(self, event):
        for itm in range(event.widget.size()):
            if event.keysym.lower() == event.widget.get(itm)[:1]:
                event.widget.selection_clear(0, 'end')
                event.widget.select_set(itm)
                event.widget.see(itm)
                event.widget.activate(itm)
                break
    def Save_data(self):
        if self.edit_mode == False:
            
            con, cur = open_con(False)
            self.data_list = []
            for line in self.trv.get_children():
                self.data_list.append(self.trv.item(line)['values'])
            if len(self.data_list) == 0:
                return messagebox.showerror('Error', 'Nothing to Save')

            Query = "Insert Into NOC_Letters (Letter_Date, NOC_Issued_To, Remarks) values (curdate(), %s, %s);"

            cur.execute(Query, [self.Districts.get(), self.remarks_entry.get()])
            con.commit()
            cur.execute("Select Letter_ID from NOC_Letters order by Letter_ID desc Limit 1;")
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
            Query = "Insert Into dispatch_dairy (Dispatch_No, Letter_Type, Letter_ID) values (%s, 'NOC Letter', %s);"
            parm_list = [last_dispatch, last_letter_id]
            cur.execute(Query, parm_list)
            con.commit()

            for row in self.data_list:
                print(row)
                Query = "Insert Into NOC_Applicants (Letter_ID,CNIC,Applicant_Name,Relation,Applicant_FName) values (%s, %s, %s, %s, %s);"
                parm_list = [last_letter_id, row[1], row[2], row[3], row[4]]

                cur.execute(Query, parm_list)
                con.commit()
            messagebox.showinfo(
                'Success', "New Record Saved with Dispatch No:-{}".format(last_dispatch))
            
            cur.close()
            con.close()
            self.cnic_entry.delete('0', 'end')
            self.name_entry.delete('0', 'end')
            self.father_name_entry.delete('0', 'end')
            self.remarks_entry.delete('0', 'end')
            self.trv.delete(*self.trv.get_children())
            return
        else:
            if self.letter_id == 0:
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
            # print("Addition List:-", self.addition_list)
            # print("Updation List:-", self.updation_list)
            # print("Deletion List:-", self.deletion_list)
            con, cur = open_con(False)
            Query = "Update NOC_Letters Set Letter_Date = %s, NOC_Issued_To = %s, Remarks=%s Where Letter_ID = %s;"
            parm_list = [self.letter_date_entry.get(),self.Districts.get(), self.remarks_entry.get(), self.letter_id]
            cur.execute(Query, parm_list)
            con.commit()
            if len(self.updation_list) != 0:
                for row in self.updation_list:
                    Query = "Update NOC_Applicants Set CNIC = %s, Applicant_Name = %s, Relation = %s, Applicant_FName = %s Where App_ID = %s;"
                    parm_list = [str(row[1]), row[2], row[3], row[4], row[0]]
                    cur.execute(Query, parm_list)
                    con.commit()
            if len(self.addition_list) != 0:
                for row in self.addition_list:
                    Query = "Insert Into NOC_Applicants (Letter_ID,CNIC,Applicant_Name,Relation,Applicant_FName) values (%s,%s,%s, %s,%s);"
                    parm_list = [self.letter_id, str(row[1]), row[2], row[3], row[4]]
                    cur.execute(Query, parm_list)
                    con.commit()
            if len(self.deletion_list) != 0:
                for row in self.deletion_list:
                    Query = "Delete From NOC_Applicants Where App_ID = %s;"

                    cur.execute(Query, [row])
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
            self.letter_id = 0
            self.letter_date_entry.delete('0', 'end')
            self.Districts.delete('0', 'end')
            self.cnic_entry.delete('0', 'end')
            self.name_entry.delete('0', 'end')
            self.father_name_entry.delete('0', 'end')
        self.letter_date_entry.config(state='readonly')

    def load_data(self):

        if self.letter_id != 0:
            Query = """SELECT l.Letter_ID, d.Dispatch_No, l.Letter_Date, l.NOC_Issued_To, l.Remarks, a.App_ID, a.CNIC, a.Applicant_Name, a.Relation, a.Applicant_FName 
                            FROM noc_letters as l 
                            Left Join noc_applicants as a
                            On l.Letter_ID = a.Letter_ID
                            Inner Join dispatch_dairy as d
                            on d.Letter_ID = l.Letter_ID
                            Where l.Letter_ID = %s And d.Letter_Type = 'NOC Letter';"""
            con, cur = open_con(True)
            cur.execute(Query, [self.letter_id])
            data = cur.fetchall()
            cur.close()
            con.close()
            self.letter_date_entry.delete(0, 'end')
            self.Districts.delete(0, 'end')
            self.cnic_entry.delete(0, 'end')
            self.name_entry.delete(0, 'end')
            self.father_name_entry.delete(0, 'end')
            self.remarks_entry.delete('0', 'end')
            loop = 0
            self.old_child_list = []
            self.cnic_entry.get()
            self.trv.delete(*self.trv.get_children())
            for row in data:
                loop += 1
                if loop == 1:
                    self.Districts.insert(
                        0, row['NOC_Issued_To'])
                    self.letter_date_entry.config(state='normal')
                    self.letter_date_entry.delete(0, 'end')
                    self.letter_date_entry.insert(
                        0, row['Letter_Date'])
                    self.remarks_entry.insert(0, str(row['Remarks']))
                    self.letter_date_entry.config(state='readonly')
                if row['App_ID'] is not None:
                    self.trv.insert("", 'end',
                                    values=(row['App_ID'], int(row['CNIC']), row['Applicant_Name'], row['Relation'], row['Applicant_FName']))
                    lst = list((int(row['CNIC']), "{}".format(row['Applicant_Name']), "{}".format(
                        row['Relation']), "{}".format(row['Applicant_FName'])))
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
                Query = """SELECT l.Letter_ID, d.Dispatch_No, l.Letter_Date, l.NOC_Issued_To, a.CNIC, a.Applicant_Name, a.Relation, a.Applicant_FName 
                        FROM noc_letters as l 
                        Inner Join noc_applicants as a
                        On l.Letter_ID = a.Letter_ID
                        Inner Join dispatch_dairy as d
                        on d.Letter_ID = l.Letter_ID
                        Where l.Letter_Date = %s And d.Letter_Type = 'NOC Letter';"""
                parm_list = [search_input.get()]
            elif search_type.get(search_type.curselection()) == 'Dispatch No':
                if search_input.get().isnumeric():
                    Query = """SELECT l.Letter_ID, d.Dispatch_No, l.Letter_Date, l.NOC_Issued_To, a.CNIC, a.Applicant_Name, a.Relation, a.Applicant_FName 
                            FROM noc_letters as l 
                            Inner Join noc_applicants as a
                            On l.Letter_ID = a.Letter_ID
                            Inner Join dispatch_dairy as d
                            on d.Letter_ID = l.Letter_ID
                            Where d.Dispatch_No = %s And d.Letter_Type = 'NOC Letter';"""
                    parm_list = [search_input.get()]
                else:
                    return messagebox.showerror('Error', "Dispatch No shall be a number")
            elif search_type.get(search_type.curselection()) == 'CNIC':
                if len(search_input.get()) != 13:
                    return messagebox.showerror('Error', "CNIC Number lenth shall be 13 digit without dashes")
                if search_input.get().isnumeric():
                    Query = """SELECT l.Letter_ID, d.Dispatch_No, l.Letter_Date, l.NOC_Issued_To, a.CNIC, a.Applicant_Name, a.Relation, a.Applicant_FName 
                            FROM noc_letters as l 
                            Inner Join noc_applicants as a
                            on l.Letter_ID = a.Letter_ID
                            Inner Join dispatch_dairy as d
                            on d.Letter_ID = l.Letter_ID
                            Where a.CNIC = %s And d.Letter_Type = 'NOC Letter';"""
                    parm_list = [search_input.get()]
                else:
                    return messagebox.showerror('Error', "Input for CNIC search shall be a number")
            else:
                return messagebox.showerror(
                    'Error', "Please Select Search Type from List")
            con, cur = open_con(True)
            cur.execute(Query, parm_list)
            data = cur.fetchall()
            cur.close()
            con.close()
            trv.delete(*trv.get_children())
            lett_id = 0
            for row in data:
                if lett_id != row['Letter_ID']:
                    trv.insert("", 'end',
                               values=(row['Letter_ID'], row['Letter_Date'], row['Dispatch_No'], row['NOC_Issued_To'], row['CNIC'], row['Applicant_Name']))
                lett_id = row['Letter_ID']

        def start_up():
            Query = """SELECT l.Letter_ID, d.Dispatch_No, l.Letter_Date, l.NOC_Issued_To, a.CNIC, a.Applicant_Name, a.Relation, a.Applicant_FName 
                            FROM noc_letters as l 
                            Left Join noc_applicants as a
                            on l.Letter_ID = a.Letter_ID
                            Inner Join dispatch_dairy as d
                            on d.Letter_ID = l.Letter_ID
                            Where d.Letter_Type = 'NOC Letter' order by l.Letter_ID Desc Limit 50;"""
            con, cur = open_con(True)
            cur.execute (Query)
            data = cur.fetchall()
            cur.close()
            con.close()
            trv.delete(*trv.get_children())
            lett_id = 0
            for row in data:
                if lett_id != row['Letter_ID']:
                    trv.insert("", 'end',
                               values=(row['Letter_ID'], row['Letter_Date'], row['Dispatch_No'], row['NOC_Issued_To'], row['CNIC'], row['Applicant_Name']))
                lett_id = row['Letter_ID']

        def cancel():
            self.letter_id = 0
            self.edit_window.quit()
            self.edit_window.destroy()

        def trv_click(*args):
            if len(trv.selection()) == 0:
                return messagebox.showerror('Error', 'Nothing Selected')
            selectedItem = trv.selection()[0]

            self.letter_id = trv.item(selectedItem)['values'][0]
            self.edit_window.quit()
            self.edit_window.destroy()

        self.letter_id = 0
        self.edit_window = Toplevel()
        self.edit_window.geometry("800x400")
        self.edit_window.title('Record Selection')
        Top_Frame = ttk.Frame(self.edit_window)
        Top_Frame.pack(fill='x')
        search_type = Listbox(
            Top_Frame, width=15, height=1, exportselection=0, font=('Bell', 12))
        search_type.grid(row=1, column=0, padx=10, pady=10)
        search_type.insert(0, "Dispatch No")
        search_type.insert(1, "Date")
        search_type.insert(2, "CNIC")
        search_type.select_set(0)
        search_type.see(0)
        search_input = ttk.Entry(Top_Frame, width=15, font=('Bell, 12'))
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
        trv.heading("4", text="NOC_Issued_To", anchor='w')
        trv.heading("5", text="Applicant CNIC", anchor='w')
        trv.heading("6", text="Applicant Name", anchor='w')
        trv.bind("<Double-1>", trv_click)

        search_btn = ttk.Button(Top_Frame, width=15,
                            text='Search', command=Search)
        search_btn.grid(row=1, column=3)
        cancel_btn = ttk.Button(Top_Frame, width=15, text='Cancel',
                             command=cancel)
        cancel_btn.grid(row=1, column=4, padx=10, pady=10)

        start_up()
        self.edit_window.mainloop()

    def edit_records(self):
        self.Record_Selector()
        self.load_data()
        self.letter_date_entry.config(state='normal')

    def font_settings(self):
        setting_window = Toplevel()
        setting_window.geometry("300x200+300+300")
        font_list = ["Courier", "Helvetica", "Times"]
        font_size_list = [11, 12, 13, 14, 15, 16]
        list_box_var = Variable(value = font_list)
        list_box_var2 = Variable(value = font_size_list)
        ttk.Label(setting_window, text='Font', anchor='w').grid(row=0, column=0, padx=10, pady=10)
        self.font_list_box = Listbox(
            setting_window, width=15, height=1, selectmode='browes', listvariable=list_box_var, exportselection=0, font=(self.letter_font, 14, 'bold'))
        self.font_list_box.grid(row=0, column=1, padx=10, pady=10)
        # self.font_list_box.select_set(0)
        # self.font_list_box.see(0)
        ttk.Label(setting_window, text='Font Size', anchor='w').grid(row=1, column=0, padx=10, pady=10)
        self.font_size_list_box = Listbox(
            setting_window, width=15, height=1, selectmode='browes', listvariable=list_box_var2, exportselection=0, font=(self.letter_font, 14, 'bold'))
        self.font_size_list_box.grid(row=1, column=1, padx=10, pady=10)
        # self.font_size_list_box.select_set(0)
        # self.font_size_list_box.see(0)
        indx = font_list.index(self.letter_font)
        self.font_list_box.select_set(indx)
        self.font_list_box.see(indx)

        indx = font_size_list.index(self.letter_font_size)
        self.font_size_list_box.select_set(indx)
        self.font_size_list_box.see(indx)
        def update_setting():
            if len(self.font_list_box.curselection()) != 1:
                return messagebox.showerror("Reselect", "Please re-select one value from font list")
            if len(self.font_size_list_box.curselection()) != 1:
                return messagebox.showerror("Reselect", "Please re-select one value from font size list")
            self.letter_font = self.font_list_box.get(self.font_list_box.curselection())
            self.letter_font_size = int(self.font_size_list_box.get(self.font_size_list_box.curselection()))
            setting_window.destroy()
        ttk.Button(setting_window, text='Update', command=update_setting).grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        
        
        
    def issue_letter(self):
        self.Record_Selector()
        if self.letter_id == 0:
            return messagebox.showerror('Error', 'Nothing Selected')

        Query = """SELECT l.Letter_ID, d.Dispatch_No, l.Letter_Date, l.NOC_Issued_To, a.CNIC, a.Applicant_Name, a.Relation, a.Applicant_FName 
                    FROM noc_letters as l 
                    Inner Join noc_applicants as a
                    on l.Letter_ID = a.Letter_ID
                    Inner Join dispatch_dairy as d
                    on d.Letter_ID = l.Letter_ID
                    Where l.Letter_ID = %s And d.Letter_Type = 'NOC Letter';"""
        con, cur = open_con(True)
        cur.execute(Query, [self.letter_id])
        data = cur.fetchall()
        cur.close()
        con.close()
        if len(data) != 0:
            pdf = FPDF()
            pdf.add_page()

            # pdf.add_font(self.letter_font, '', "c:\WINDOWS\FONTS\courier.ttf", uni=True)
            # pdf.add_font(self.letter_font, 'B', "c:\WINDOWS\FONTS\courier.ttf", uni=True)
            pdf.set_left_margin(15)
            pdf.set_right_margin(15)
            pdf.set_font(self.letter_font, 'B', size=self.letter_font_size+1)
            pdf.set_fill_color(211, 211, 211)
            #pdf.image('govt_logo.png', x=10, y=10, w=30, h=30)
            pdf.ln(7)
            #pdf.cell(20, 6, text='', align='C')
            pdf.cell(0, 6, text='OFFICE OF THE DISTRICT MAGISTRATE',
                     new_x="LMARGIN", new_y="NEXT", align='C')
            #pdf.cell(20, 6, text='', align='C')
            pdf.cell(0, 6, text='ISLAMABAD CAPITAL TERRITORY',
                     new_x="LMARGIN", new_y="NEXT", align='C')
            #pdf.cell(20, 6, text='', align='C')
            pdf.cell(0, 6, text='ISLAMABAD',
                     new_x="LMARGIN", new_y="NEXT", align='C')
            pdf.set_font(self.letter_font, size=self.letter_font_size)
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
            pdf.cell(30, 6, text='The Deputy Commissioner/',
                     new_x="LMARGIN", new_y="NEXT", align='L')
            pdf.cell(40, 6, text='')
            pdf.cell(35, 6, text='Assistant Commissioner,',
                     new_x="LMARGIN", new_y="NEXT", align='L')
            pdf.cell(40, 6, text='')
            pdf.cell(30, 6, text='{}'.format(data[0]['NOC_Issued_To']),
                     new_x="LMARGIN", new_y="NEXT", align='L')
            pdf.ln(8)
            if data[0]['Dispatch_No'] is not None:
                pdf.cell(
                    20, 6, text='No.{}/Domicile'.format(data[0]['Dispatch_No']), align='L')
            # pdf.cell(15, 6, text='', align='L')
            pdf.cell(0, 6, text='Dated: {}'.format(
                data[0]['Letter_Date']), new_x="LMARGIN", new_y="NEXT",  align='R')
            pdf.ln(8)

            
            pdf.cell(15, 6, text='Subject:', align='L')
            pdf.cell(15, 6, text='')
            pdf.set_font(self.letter_font, 'BU', size=self.letter_font_size)
            pdf.cell(40, 6, text='ISSUANCE OF NO OBJECTION CERTIFICATE',
                     new_x="LMARGIN", new_y="NEXT", align='L')

            pdf.set_font(self.letter_font, size=self.letter_font_size)
            
            pdf.multi_cell(
                0, 10, text='          The Computerized record has been inspected. As per compuerized record, No domicile issued in favour of following persons from this office:-')
            pdf.ln(4)
            
            pdf.set_font(self.letter_font, size=self.letter_font_size)
            #lst = [[1, '61101-1234596-8', 'Manha Hamid Kakakhel', 'Syed M Hamid Shah Kaka Khel'], [2, '61101-1234586-8', 'Maira Hamid Jehangir Shah Kakakhel', 'Hamid Shah'], [3, '61101-1234596-8', 'Habiba Hamid Shah Kaka Khel', 'Hamid Shah']]
            sl = 0
            grey = (128, 128, 128)
            white = (255, 255, 255)
            headings_style = FontFace(emphasis="BOLD", fill_color=grey)
            table_style = FontFace(fill_color=white)
            with pdf.table(headings_style=headings_style, first_row_as_headings=False, line_height=7, padding=2, text_align=("CENTER", "CENTER", "LEFT", "LEFT"), col_widths=(11, 28, 39, 40)) as table:
                row = table.row()
                row.cell("S.No")
                row.cell("CNIC")
                row.cell("Name")
                row.cell("Father/Husband Name")
                for data_row in data:
                    row = table.row(style=table_style)
                    sl += 1
                    row.cell(str(sl))
                    row.cell(str(data_row["CNIC"]))
                    row.cell(str(data_row["Applicant_Name"]))
                    row.cell(str(data_row["Applicant_FName"]))
            pdf.ln(4)
            pdf.multi_cell(
                0, 10, text='2.        It is not possible to check the manual record. However, applicant has/have submitted an affidavit regarding non-issuance of domicile from Islamabad.')

            pdf.ln(8)
            pdf.ln(8)
            # signature
            pdf.set_font(self.letter_font, 'B', size=self.letter_font_size)
            pdf.cell(70, 6, text='')
            pdf.cell(0, 6, text='Incharge Domicile Branch', align='C', new_x="LMARGIN", new_y="NEXT")
            pdf.cell(70, 6, text='')
            pdf.cell(0, 6, text='ICT, Islamabad', align='C', new_x="LMARGIN", new_y="NEXT")
            pdf.output('Letter.pdf')

            path = 'Letter.pdf'
            os.system(path)
        else:
            return messagebox.showerror('Error', 'Record Not Complete')


if __name__ == '__main__':
    # Obj = NOC('25.48.184.239')
    # Obj.mainloop()
    session = 'dumy object'
    user_data = {'user_id':3}
    Obj = NOC(session, user_data)
    Obj.mainloop()
