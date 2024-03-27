import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from datetime import date
from fpdf.fonts import FontFace
from fpdf import FPDF

from Validation import validate_CNIC, validate_date
import mysql.connector
from mysql.connector import Error
import os
from tools import open_con

class Canelation():
    def __init__(self):
        self.__root = Tk()
        # self.__root.attributes('-fullscreen', True)
        self.rec_id = 0
        self.__font = ('Cambria', 14, 'bold')
        self.__root.geometry('1400x700+50+50')
        self.__root.title("Cancelation Letter")
        self.btn_font = ('Cambria', 12)

        self.top_frame = Frame(self.__root, relief=RIDGE,
                               borderwidth=2)
        self.top_frame.pack(side=TOP, fill=X)
        self.top_frame1 = Frame(self.__root, relief=RIDGE,
                                borderwidth=2)
        self.top_frame1.pack(side=TOP, fill=X)

        self.filter_type = Listbox(self.top_frame1, height=1, bg='#272727',
                                   font=self.btn_font, exportselection=0)
        self.filter_type.grid(row=1, column=1, padx=10, pady=10)
        self.filter_type.insert(0, 'CNIC')
        self.filter_type.insert(1, 'Name')
        self.filter_type.insert(2, 'Father Name')
        self.filter_type.insert(3, 'Domicile No')
        self.filter_type.insert(4, 'Domicile Date')
        self.filter_type.insert(5, 'Letter Date')
        self.filter_type.insert(6, 'Dispatch No')
        self.filter_type.select_set(0)

        self.filter_input = Entry(self.top_frame1, font=self.btn_font)
        self.filter_input.grid(row=1, column=2, padx=10, pady=10)
        self.filter_input.bind('<Return>', lambda event: self.search(self.filter_type.get(self.filter_type.curselection()), self.filter_input.get(), 'None'))
        self.left_frame = Frame(self.__root, relief=RIDGE, borderwidth=2)
        self.left_frame.pack(side=LEFT, fill=Y)
        self.right_frame = Frame(self.__root, relief=RIDGE, borderwidth=2)
        self.right_frame.pack(side=LEFT, fill=Y)

        self.title_label = Label(
            self.top_frame, text='Domicile Cancellation', font=self.__font)
        self.title_label.pack()

        self.cnic_label = Label(
            self.left_frame, text='CNIC', font=self.btn_font)
        self.cnic_label.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)
        self.cnic_input = Entry(self.left_frame, font=self.btn_font)
        self.cnic_input.grid(row=1, column=2, padx=10, pady=10)

        self.name_label = Label(
            self.left_frame, text='Name', font=self.btn_font)
        self.name_label.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)
        self.name_input = Entry(self.left_frame, font=self.btn_font)
        self.name_input.grid(row=2, column=2, padx=10, pady=10)
        self.relation_label = Label(
            self.left_frame, text='Relation', font=self.btn_font)
        self.relation_label.grid(
            column=1, row=3, padx=10, pady=10, sticky=tk.W)
        self.relation = Listbox(
            self.left_frame, width=20, height=1, selectmode='single', exportselection=0, font=self.btn_font)
        self.relation.grid(column=2, row=3, padx=10, pady=10, sticky=tk.W)
        self.relation.insert(0, 's/o')
        self.relation.insert(1, 'd/o')
        self.relation.insert(2, 'w/o')
        self.relation.bind('<KeyPress>', self.select_keysym_value)
        self.fathername_label = Label(
            self.left_frame, text='Father Name', font=self.btn_font)
        self.fathername_label.grid(
            row=4, column=1, padx=10, pady=10, sticky=tk.W)
        self.fathername_input = Entry(self.left_frame, font=self.btn_font)
        self.fathername_input.grid(row=4, column=2, padx=10, pady=10)

        self.address_label = Label(
            self.left_frame, text='Address', font=self.btn_font)
        self.address_label.grid(row=5, column=1, padx=10, pady=10, sticky=tk.W)
        self.address_input = Entry(self.left_frame, font=self.btn_font)
        self.address_input.grid(row=5, column=2, padx=10, pady=10)
        # 3rd Row
        self.domicile_no_label = Label(
            self.left_frame, text='Domicile No', font=self.btn_font)
        self.domicile_no_label.grid(
            row=6, column=1, padx=10, pady=10, sticky=tk.W)
        self.domicile_no_input = Entry(self.left_frame,  font=self.btn_font)
        self.domicile_no_input.grid(
            row=6, column=2, padx=10, pady=10, sticky=tk.W)
        # 4th Row
        self.domicile_date_label = Label(
            self.left_frame, text='Domicile Date', font=self.btn_font)
        self.domicile_date_label.grid(
            row=7, column=1, padx=10, pady=10, sticky=tk.W)
        self.domicile_date_input = Entry(self.left_frame,  font=self.btn_font)
        self.domicile_date_input.grid(
            row=7, column=2, padx=10, pady=10, sticky=tk.W)

        self.save_btn = Button(self.left_frame, text='Save New',
                               width=15, command=self.save, font=self.btn_font)
        self.save_btn.grid(row=10, column=2, padx=10, sticky=tk.W)

        can_style = ttk.Style()

        can_style.configure('Treeview',
                            rowheight=36, font=self.btn_font)
        can_style.configure("Treeview.Heading",
                            font=self.__font, background="blue")
        self.trv = ttk.Treeview(
            self.right_frame, selectmode='browse', height=7)
        self.trv.pack(fill=BOTH, expand=TRUE)
        # , "7", "8", "9")
        self.trv["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8")
        self.trv['show'] = 'headings'
        self.trv.column("1", width=50, anchor='center')
        self.trv.column("2", width=120, anchor='center')
        self.trv.column("3", width=100, anchor='center')
        self.trv.column("4", width=150, anchor='w')
        self.trv.column("5", width=250, anchor='w')
        self.trv.column("6", width=250, anchor='w')
        self.trv.column("7", width=150, anchor='center')
        self.trv.column("8", width=150, anchor='center')
        

        self.trv.heading("1", text="ID", anchor='center')
        self.trv.heading("2", text="Dispatch No", anchor='center')
        self.trv.heading("3", text="Date", anchor='center')
        self.trv.heading("4", text="CNIC", anchor='w')
        self.trv.heading("5", text="Name", anchor='w')
        self.trv.heading("6", text="Father Name", anchor='w')
        self.trv.heading("7", text="Domicile No", anchor='center')
        self.trv.heading("8", text="Domicile Date", anchor='center')

        self.trv.bind("<Button 1>", self.trv_click)
        self.Search_btn = Button(self.top_frame1, text='Search', command=lambda: self.search(self.filter_type.get(self.filter_type.curselection()), self.filter_input.get(), 'None'),
                                 font=self.btn_font, width=15)
        self.Search_btn.grid(row=1, column=3, padx=10, pady=10)
        self.update_btn = Button(self.top_frame1, text='Update', state='disabled', command=self.update,
                                 font=self.btn_font, width=15)
        self.update_btn.grid(row=1, column=4, padx=10, pady=10)
        self.Issue_letter_btn = Button(self.top_frame1, text='Issue Letter', command=self.issue_cancellation_letter,
                                       font=self.btn_font, width=15)
        self.Issue_letter_btn.grid(row=1, column=5, padx=10, pady=10)
        self.clear_btn = Button(self.top_frame1, text='Clear', command=self.clear,
                                font=self.btn_font, width=15)
        self.clear_btn.grid(row=1, column=6, padx=10, pady=10)
        self.exit_btn = Button(self.top_frame1, text='Exit', command=self.__root.destroy,
                               font=self.btn_font, width=15)
        self.exit_btn.grid(row=1, column=7, padx=10, pady=10)
        self.search('None', 'None', 'All')

    def select_keysym_value(self, event):

        for itm in range(event.widget.size()):
            if event.keysym.lower() == event.widget.get(itm)[:1]:
                event.widget.selection_clear(0, END)
                event.widget.select_set(itm)
                event.widget.see(itm)
                event.widget.activate(itm)
                break
    def trv_click(self, event):
        for item in self.trv.selection():
            selected_item = self.trv.item(item, 'values')
            # record = selected_item['values']
            self.update_btn.config(state='normal')
            self.save_btn.config(state='disabled')
            self.display_in_fields(selected_item[0])
            self.rec_id = selected_item[0]

    def search(self, keyword, value, query_type):

        if len(value) == 0 or value == 'None':
            query_type = 'All'
        else:
            query_type = 'None'

        if keyword == "CNIC":
            query_part = "c.CNIC like '%{}%'".format(value)
        elif keyword == "Name":
            query_part = "c.Applicant_Name like '%{}%'".format(value)
        elif keyword == "Father Name":
            query_part = "c.Father_Name like '%{}%'".format(value)
        elif keyword == "Domicile No":
            query_part = "c.Domicile_No like '%{}%'".format(value)
        elif keyword == "Dispatch No":
            query_part = "d.Dispatch_No = '{}'".format(value)
        elif keyword == "Domicile Date":
            if value.find(' ') != -1:
                val1, val2 = value.split(' ')
                query_part = "c.Domicile_Date Between '{}' and '{}'".format(
                    val1, val2)
            else:
                query_part = "c.Domicile_Date = '{}'".format(value)
        elif keyword == "c.Letter Date":
            if value.find(' ') != -1:
                val1, val2 = value.split(' ')
                query_part = "c.Letter_Date Between '{}' and '{}'".format(
                    val1, val2)
            else:
                query_part = "c.Letter_Date = '{}'".format(value)
        self.trv.delete(*self.trv.get_children())
        
        Query = """SELECT 
                c.Letter_ID,
                d.Dispatch_No,
                c.Letter_Date,
                c.CNIC,
                c.Applicant_Name,
                c.Relation,
                c.Father_Name,
                c.Address,
                c.Domicile_No,
                c.Domicile_Date
            FROM cancellation as c
            inner Join dispatch_dairy as d
            on c.Letter_ID = d.Letter_ID and d.Letter_Type = 'Cancellation Letter' """
        if query_type == 'All':
            Query  = Query + "order by Letter_ID Desc Limit 200;"
        else:
            Query = Query + " Where " + \
                query_part + " order by Letter_ID Desc;"
        con, cur = open_con(True)
        cur.execute(Query)
        self.agr_data = cur.fetchall()
        for row in self.agr_data:
            self.trv.insert("", 'end', values=(
                row['Letter_ID'], row['Dispatch_No'], row['Letter_Date'], row['CNIC'], row['Applicant_Name'], row['Father_Name'], row['Domicile_No'], row['Domicile_Date']))
        con.close()

    def display_in_fields(self, id):

        Query = "Select * from Cancellation Where Letter_ID = %s;"
        con, cur = open_con(True)
        cur.execute(Query, [id])
        self.agr_data = cur.fetchall()
        for row in self.agr_data:
            self.cnic_input.delete(0, 'end')
            self.cnic_input.insert(0, str(row['CNIC']))
            self.name_input.delete(0, 'end')
            self.name_input.insert(0, row['Applicant_Name'])
            if row['Relation'] is not None:
                lst_index = self.relation.get(
                    0, 'end').index(str(row['Relation']))
                self.relation.select_set(lst_index)
                self.relation.see(lst_index)
            self.fathername_input.delete(0, 'end')
            self.fathername_input.insert(0, str(row['Father_Name']))
            self.address_input.delete(0, 'end')
            self.address_input.insert(0, str(row['Address']))

            self.domicile_no_input.delete(0, 'end')
            self.domicile_no_input.insert(0, str(row['Domicile_No']))
            self.domicile_date_input.delete(0, 'end')
            self.domicile_date_input.insert(
                0, str(row['Domicile_Date']))

        con.close()

    def run(self):
        self.__root.mainloop()

    def save(self):
        widget_list = [self.cnic_input.get().strip(), self.name_input.get().strip(), self.fathername_input.get().strip(
        ), self.address_input.get().strip(), self.domicile_no_input.get().strip(), self.domicile_date_input.get().strip()]
        for widgt in widget_list:
            if widgt.upper().find('UPDATE') != -1 or widgt.upper().find('DELETE') != -1 or widgt.upper().find('INSERT') != -1:
                return messagebox.showerror('Invalid CNIC', 'Milicious Word Found in Widget')
        validation_result = validate_CNIC(self.cnic_input.get().strip())
        if validation_result != 'valid':
            return messagebox.showerror('Invalid CNIC', validation_result)
        if len(self.name_input.get().strip()) == 0:
            return messagebox.showerror(('Error', 'Name Not Provided'))
        if len(self.fathername_input.get().strip()) == 0:
            return messagebox.showerror(('Error', 'Father Name Not Provided'))
        if len(self.relation.curselection()) == 0:
            return messagebox.showerror(('Error', 'Relation Not selected'))
        elif len(self.relation.curselection()) > 1:
            return messagebox.showerror(('Error', 'Please Select Relation Properly'))
        if len(self.address_input.get().strip()) == 0:
            return messagebox.showerror(('Error', 'Address Not Provided'))
        if len(self.domicile_no_input.get().strip()) == 0:
            return messagebox.showerror(('Error', 'Domicile Number Not Provided'))
        if len(self.domicile_date_input.get().strip()) == 0:
            return messagebox.showerror(('Error', 'Domicile Date Not Provided'))
        else:
            validation_result = validate_date(
                self.domicile_date_input.get())
            if validation_result != 'valid':
                return messagebox.showerror('Error', validation_result)
        con, cur = open_con(False)
        # Query = "Select CNIC FROM Cancellation WHERE CNIC = %s;"
        # cur.execute(Query, [self.cnic_input.get()])
        # data = cur.fetchall()
        # if len(data) > 0:
        #     con.close()
        #     return messagebox.showerror('Error', 'Cancelation Letter already issued against {}'.format(self.cnic_input.get()))
        Query = "Insert into Cancellation (CNIC, Applicant_Name, Relation, Father_name, Address, Domicile_No, Domicile_Date) values (%s,%s,%s,%s,%s,%s,%s) ;"
        parm_list = [self.cnic_input.get(), self.name_input.get(), self.relation.get(self.relation.curselection()), self.fathername_input.get(), self.address_input.get(), self.domicile_no_input.get(), self.domicile_date_input.get()]
        cur.execute(Query, parm_list)
        con.commit()
        cur.execute('Select last_insert_id();')
        last_letter_id = cur.fetchall()
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
        Query = "Insert Into dispatch_dairy (Dispatch_No, Letter_Type, Letter_ID) values (%s, 'Cancellation Letter', %s);"
        parm_list = [last_dispatch, last_letter_id[0][0]]
        cur.execute(Query, parm_list)
        con.commit()
        self.clear()
        con.close()
        messagebox.showinfo('Updated', "New Record Saved")
        self.search('None', 'None', 'All')

    def clear(self):
        self.cnic_input.delete(0, 'end')
        self.name_input.delete(0, 'end')
        self.fathername_input.delete(0, 'end')
        self.address_input.delete(0, 'end')
        self.domicile_no_input.delete(0, 'end')
        self.domicile_date_input.delete(0, 'end')
        self.update_btn.config(state='disabled')
        self.save_btn.config(state='normal')

    def update(self):
        validation_result = validate_CNIC(self.cnic_input.get().strip())
        if validation_result != 'valid':
            return messagebox.showerror('Invalid CNIC', validation_result)
        if len(self.name_input.get().strip()) == 0:
            return messagebox.showerror('Error', 'Name Not Provided')
        if len(self.fathername_input.get().strip()) == 0:
            return messagebox.showerror('Error', 'Father Name Not Provided')

        if len(self.relation.curselection()) == 0:
            return messagebox.showerror('Error', 'Relation Not selected')
        elif len(self.relation.curselection()) > 1:
            return messagebox.showerror('Error', 'Please select single value from relation')
        if len(self.address_input.get().strip()) == 0:
            return messagebox.showerror('Error', 'Address Not Provided')
        if len(self.domicile_no_input.get().strip()) == 0:
            return messagebox.showerror('Error', 'Domicile Number Not Provided')
        if len(self.domicile_date_input.get().strip()) == 0:
            return messagebox.showerror('Error', 'Domicile Date Not Provided')
        else:
            validation_result = validate_date(
                self.domicile_date_input.get())
            if validation_result != 'valid':
                return messagebox.showerror('Error', validation_result)
        if self.rec_id != 0:
            Query = "Update Cancellation Set CNIC = %s, Applicant_Name = %s, Father_Name = %s, Relation=%s, Address = %s, Domicile_No = %s, Domicile_Date = %s Where Letter_ID = %s;"
            parm_list = [self.cnic_input.get(), self.name_input.get(), self.fathername_input.get(), self.relation.get(self.relation.curselection()), self.address_input.get(), self.domicile_no_input.get(), self.domicile_date_input.get(), self.rec_id]
            con, cur = open_con(False)
            cur.execute(Query, parm_list)
            con.commit()
            cur.close()
            con.close()
            messagebox.showinfo('Updated', "Record Updated")
            self.update_btn.config(state='disabled')
            self.save_btn.config(state='normal')
            self.cnic_input.delete(0, 'end')
            self.name_input.delete(0, 'end')
            self.fathername_input.delete(0, 'end')
            self.address_input.delete(0, 'end')
            self.domicile_no_input.delete(0, 'end')
            self.domicile_date_input.delete(0, 'end')
            self.update_btn.config(state='disabled')
            self.save_btn.config(state='normal')

    def issue_cancellation_letter(self):

        if self.rec_id == 0:
            return messagebox.showerror('Error', 'Nothing Selected')
        Query = """SELECT a.Letter_ID, d.Dispatch_No, a.Letter_Date,  a.CNIC, a.Applicant_Name, a.Relation, a.Father_Name, a.Address, a.Domicile_No, a.Domicile_Date 
                            FROM cancellation as a                                
                            Inner Join dispatch_dairy as d
                            on d.Letter_ID = a.Letter_ID
                            Where a.Letter_ID = %s And d.Letter_Type = 'Cancellation Letter';"""

        con, cur = open_con(True)
        cur.execute(Query, [self.rec_id])
        data = cur.fetchall()
        cur.close()
        con.close()

        pdf = FPDF()
        pdf.add_page()
        pdf.set_left_margin(15)
        pdf.set_right_margin(15)
        pdf.set_font('courier', 'B', size=16)
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
        pdf.set_font('courier', size=14)
        pdf.ln(8)
        pdf.cell(10, 6, text='')
        pdf.cell(20, 6, text='From:', align='L')
        pdf.cell(30, 6, text='The District Magistrate',
                 new_x="LMARGIN", new_y="NEXT", align='L')
        pdf.cell(30, 6, text='')
        pdf.cell(30, 6, text='ICT, Islamabad',
                 new_x="LMARGIN", new_y="NEXT", align='L')
        pdf.ln(8)
        pdf.cell(10, 6, text='')
        pdf.cell(20, 6, text='To:', align='L')
        pdf.cell(30, 6, text='Mr./Miss. {}'.format(data[0]['Applicant_Name']),
                 new_x="LMARGIN", new_y="NEXT", align='L')
        if data[0]['Father_Name'] is not None:
            pdf.cell(30, 6, text='')
            pdf.cell(35, 6, text='{} {},'.format(data[0]['Relation'], data[0]['Father_Name']),
                     new_x="LMARGIN", new_y="NEXT", align='L')
        pdf.cell(30, 6, text='')
        pdf.multi_cell(100, 6, text='{}'.format(data[0]['Address']), align='L')
        pdf.ln(8)
        
        pdf.cell(
            20, 6, text='No.{}/Domicile'.format(data[0]['Dispatch_No']), align='L')
        # pdf.cell(15, 6, text='', align='L')
        pdf.cell(0, 6, text='Dated: {}'.format(
            data[0]['Letter_Date']), new_x="LMARGIN", new_y="NEXT",  align='R')
        pdf.ln(8)

        
        pdf.cell(15, 6, text='Subject:', align='L')
        pdf.cell(15, 6, text='')
        pdf.set_font('courier', 'BU', size=14)
        pdf.cell(40, 6, text='CANCELLATION OF DOMICILE CERTIFICATE',
                 new_x="LMARGIN", new_y="NEXT", align='L')

        pdf.set_font('courier', size=14)
        pdf.multi_cell(
            0, 10, text='          Referance to your application on the subject cited above.',new_x="LMARGIN", new_y="NEXT")
        pdf.multi_cell(
            0, 10, text='2.       Your domicile certificate issued from this office vide Domicile No. {}, Dated {} is hereby cancelled on your own request and this office has no objection if the applicant applies for Domicile Certificate from any other district.'.format(data[0]['Domicile_No'], data[0]['Domicile_Date']), new_x="LMARGIN", new_y="NEXT")
        pdf.ln(6)
        pdf.ln(6)

        pdf.set_font('courier', size=14)
        # signature
        pdf.set_font('courier', 'B', size=14)
        pdf.cell(70, 6, text='')
        pdf.cell(0, 6, text='Incharge Domicile Branch', align='C', new_x="LMARGIN", new_y="NEXT")
        pdf.cell(70, 6, text='')
        pdf.cell(0, 6, text='ICT, Islamabad', align='C', new_x="LMARGIN", new_y="NEXT")

        pdf.output('Letter.pdf')

        path = 'Letter.pdf'
        os.system(path)


if __name__ == '__main__':
    can_letter = Canelation()
    can_letter.run()
