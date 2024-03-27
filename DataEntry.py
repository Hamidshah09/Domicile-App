
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from datetime import date
from datetime import datetime
from datetime import timedelta
from fpdf import FPDF
# import sqlite3
import mysql.connector
from mysql.connector import Error
import os


class dataentry(tk.Tk):
    def __init__(self):
        super().__init__()
        self.connectionstring = mysql.connector.connect(host='25.48.184.239',
                                                        database='domicile_reports',
                                                        user='superadmin',
                                                        password='Superadmin')
        self.geometry('1400x750+50+50')
        self.widget_name = ''
        self.Top_Frame = Frame(
            self, relief=RIDGE, border=1, height=10)
        self.Top_Frame.pack(fill=X)
        self.Top_label = ttk.Label(
            self.Top_Frame, text='New Domicile Application', border=1, font=('Bell', 18, 'bold'))
        self.Top_label.pack()
        self.Grid_Frame = Frame(self, relief=RIDGE, border=1)
        self.Grid_Frame.pack(fill=BOTH, expand=TRUE)
        self.Bottom_Frame = Frame(self, relief=RIDGE, border=1)
        self.Bottom_Frame.pack(fill=BOTH, expand=TRUE)
        self.Status_Frame = Frame(self, relief=RIDGE, border=1)
        self.Status_Frame.pack(fill=BOTH, expand=TRUE)
        # Creating Labels
        self.Lbl_CNIC = ttk.Label(self.Grid_Frame, text='CNIC', font=('Bell', 14, 'bold')).grid(
            column=0, row=0, padx=10, pady=10, sticky=tk.W)
        self.Lbl_First_Name = ttk.Label(self.Grid_Frame, text='First Name', font=(
            'Bell', 14, 'bold')).grid(column=2, row=0, padx=10, pady=10, sticky=tk.W)
        self.Lbl_Last_Name = ttk.Label(self.Grid_Frame, text='Last Name', font=(
            'Bell', 14, 'bold')).grid(column=4, row=0, padx=10, pady=10, sticky=tk.W)
        self.Lbl_Father_Name = ttk.Label(self.Grid_Frame, text='Father Name', font=(
            'Bell', 14, 'bold')).grid(column=0, row=1, padx=10, pady=10, sticky=tk.W)
        self.Lbl_Spouse_Name = ttk.Label(self.Grid_Frame, text='Spouse Name', font=(
            'Bell', 14, 'bold')).grid(column=2, row=1, padx=10, pady=10, sticky=tk.W)
        self.Lbl_Contact = ttk.Label(self.Grid_Frame, text='Contact', font=(
            'Bell', 14, 'bold')).grid(column=4, row=1, padx=10, pady=10, sticky=tk.W)
        self.Lbl_Placeofbirth = ttk.Label(self.Grid_Frame, text='Place of birth', font=(
            'Bell', 14, 'bold')).grid(column=0, row=2, padx=10, pady=10, sticky=tk.W)
        self.Lbl_Date_of_Birth = ttk.Label(self.Grid_Frame, text='Date of Birth', font=(
            'Bell', 14, 'bold')).grid(column=2, row=2, padx=10, pady=10, sticky=tk.W)
        self.Lbl_Arrival_Date = ttk.Label(self.Grid_Frame, text='Arrival Date', font=(
            'Bell', 14, 'bold')).grid(column=4, row=2, padx=10, pady=10, sticky=tk.W)

        self.Lbl_Pre_Tehsil = ttk.Label(self.Grid_Frame, text='Present Tehsil', font=(
            'Bell', 14, 'bold')).grid(column=0, row=3, padx=10, pady=10, sticky=tk.W)
        self.Label_Pre_District = ttk.Label(self.Grid_Frame, text='Present District', font=(
            'Bell', 14, 'bold')).grid(column=2, row=3, padx=10, pady=10, sticky=tk.W)
        self.Lbl_Present_Province = ttk.Label(self.Grid_Frame, text='Present Province', font=(
            'Bell', 14, 'bold')).grid(column=4, row=3, padx=10, pady=10, sticky=tk.W)
        self.Lbl_Present_Address = ttk.Label(self.Grid_Frame, text='Present Address', font=(
            'Bell', 14, 'bold')).grid(column=0, row=5, padx=10, pady=10, sticky=tk.W)

        self.Lbl_Prme_Tehsil = ttk.Label(self.Grid_Frame, text='Permenent Tehsil', font=(
            'Bell', 14, 'bold')).grid(column=0, row=6, padx=10, pady=10, sticky=tk.W)
        self.Label_Prme_District = ttk.Label(self.Grid_Frame, text='Permenent District', font=(
            'Bell', 14, 'bold')).grid(column=2, row=6, padx=10, pady=10, sticky=tk.W)
        self.Lbl_Perm_Province = ttk.Label(self.Grid_Frame, text='Permenent Province', font=(
            'Bell', 14, 'bold')).grid(column=4, row=6, padx=10, pady=10, sticky=tk.W)
        self.Lbl_Permenent_Address = ttk.Label(self.Grid_Frame, text='Permenent Address', font=(
            'Bell', 14, 'bold')).grid(column=0, row=8, padx=10, pady=10, sticky=tk.W)
        self.Lbl_Gender = ttk.Label(self.Grid_Frame, text='Gender', font=(
            'Bell', 14, 'bold')).grid(column=0, row=9, padx=10, pady=10, sticky=tk.W)
        self.Lbl_Religion = ttk.Label(self.Grid_Frame, text='Religion', font=(
            'Bell', 14, 'bold')).grid(column=2, row=9, padx=10, pady=10, sticky=tk.W)
        self.Lbl_Marital_Status = ttk.Label(self.Grid_Frame, text='Marital Status', font=(
            'Bell', 14, 'bold')).grid(column=4, row=9, padx=10, pady=10, sticky=tk.W)
        self.Lbl_Qulification = ttk.Label(self.Grid_Frame, text='Qulification', font=(
            'Bell', 14, 'bold')).grid(column=0, row=10, padx=10, pady=10, sticky=tk.W)
        self.Lbl_Occupation = ttk.Label(self.Grid_Frame, text='Occupation', font=(
            'Bell', 14, 'bold')).grid(column=2, row=10, padx=10, pady=10, sticky=tk.W)
        self.Lbl_Process_type = ttk.Label(self.Grid_Frame, text='Proccess Type', font=(
            'Bell', 14, 'bold')).grid(column=4, row=10, padx=10, pady=10, sticky=tk.W)
        self.Lbl_Request_Type = ttk.Label(self.Grid_Frame, text='Request Type', font=(
            'Bell', 14, 'bold')).grid(column=0, row=11, padx=10, pady=10, sticky=tk.W)
        self.Lbl_Application_Type = ttk.Label(self.Grid_Frame, text='Application Type', font=(
            'Bell', 14, 'bold')).grid(column=2, row=11, padx=10, pady=10, sticky=tk.W)
        self.Lbl_Service_Type = ttk.Label(self.Grid_Frame, text='Service Type', font=(
            'Bell', 14, 'bold')).grid(column=4, row=11, padx=10, pady=10, sticky=tk.W)
        self.Lbl_Payment_Type = ttk.Label(self.Grid_Frame, text='Payment Type', font=(
            'Bell', 14, 'bold')).grid(column=0, row=12, padx=10, pady=10, sticky=tk.W)
        self.Lbl_Approver = ttk.Label(self.Grid_Frame, text='Approver', font=(
            'Bell', 14, 'bold')).grid(column=2, row=12, padx=10, pady=10, sticky=tk.W)

        self.Entry_CNIC = ttk.Entry(self.Grid_Frame, font=('Bell', 14))
        self.Entry_CNIC.grid(column=1, row=0, padx=10, pady=10, sticky=tk.W)

        self.Entry_First_Name = ttk.Entry(self.Grid_Frame, font=('Bell', 14))
        self.Entry_First_Name.grid(
            column=3, row=0, padx=10, pady=10, sticky=tk.W)

        self.Entry_Last_Name = ttk.Entry(self.Grid_Frame, font=('Bell', 14))
        self.Entry_Last_Name.grid(column=5, row=0, padx=10,
                                  pady=10, sticky=tk.W)

        self.Entry_Father_Name = ttk.Entry(self.Grid_Frame, font=('Bell', 14))
        self.Entry_Father_Name.grid(
            column=1, row=1, padx=10, pady=10, sticky=tk.W)

        self.Entry_Spouse_Name = ttk.Entry(self.Grid_Frame, font=('Bell', 14))
        self.Entry_Spouse_Name.grid(
            column=3, row=1, padx=10, pady=10, sticky=tk.W)

        self.Entry_Contact = ttk.Entry(self.Grid_Frame, font=('Bell', 14))
        self.Entry_Contact.grid(column=5, row=1, padx=10, pady=10, sticky=tk.W)

        self.Entry_Placeofbirth = ttk.Entry(self.Grid_Frame, font=('Bell', 14))
        self.Entry_Placeofbirth.grid(
            column=1, row=2, padx=10, pady=10, sticky=tk.W)

        self.Entry_Date_of_Birth = ttk.Entry(
            self.Grid_Frame, font=('Bell', 14))
        self.Entry_Date_of_Birth.grid(
            column=3, row=2, padx=10, pady=10, sticky=tk.W)
        self.Entry_Arrival_Date = ttk.Entry(self.Grid_Frame, font=('Bell', 14))
        self.Entry_Arrival_Date.grid(
            column=5, row=2, padx=10, pady=10, sticky=tk.W)

        # Getting Tehsil and District Lists from db

        try:
            self.con = self.connectionstring
            if self.con.is_connected():
                db_Info = self.con.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                self.cur = self.con.cursor()
                self.cur.execute("Select Teh_name, ID from Tehsils;")
                self.data = self.cur.fetchall()
                self.Tehsil_data_dict = dict(self.data)
        except Error as e:
            print("Error while connecting to MySQL", e)

        Tehsil_List = list(self.Tehsil_data_dict.keys())
        # Tehsil_Keys = list(self.Tehsil_data_dict.keys())
        Province_List = ['Azad Jammu and Kashmir', 'Balochistan', 'Federal Govt',
                         'Gilgit-Baltistan', 'Khyber Pakhtunkhwa', 'Punjab', 'Sindh']
        Province_Keys = ['694', '491', '663', '666', '1', '167', '344']
        self.cur.execute("Select Dis_Name, ID from Districts")
        self.data = self.cur.fetchall()
        self.District_data_dict = dict(self.data)
        District_List = list(self.District_data_dict.keys())
        # District_Keys = list(self.District_data_dict.keys())
        # Function for autosearch listbox

        def search(event, widget_name):
            value = event.widget.get()

            if event.keysym == 'Return':
                self.widget_name = widget_name
                if widget_name == 'Pre_Tehsil' or widget_name == 'Prem_Tehsil':
                    val_List = Tehsil_List
                elif widget_name == 'Pre_District' or widget_name == 'Prem_District':
                    val_List = District_List

                if len(value.strip()) != 0:
                    r = event.widget.grid_info().get('row')
                    c = event.widget.grid_info().get('column')
                    r = r + 1

                    self.List_Tehsil.grid(column=c, row=r, sticky=tk.N)
                    self.List_Tehsil.delete(0, 'end')
                    data = []
                    for item in val_List:

                        if value.lower() in item.lower():
                            data.append(item)
                    indx = 0
                    for item in data:
                        self.List_Tehsil.insert(indx, item)
                        indx = indx + 1

        def focusout(event):
            event.widget.grid_forget()

        def selectval(event):
            if self.widget_name == 'Pre_Tehsil':
                self.Entry_Pre_Tehsil.delete(0, 'end')
                self.Entry_Pre_Tehsil.insert(0, self.List_Tehsil.get(
                    self.List_Tehsil.curselection()))
            elif self.widget_name == 'Pre_District':
                self.Entry_Pre_District.delete(0, 'end')
                self.Entry_Pre_District.insert(0, self.List_Tehsil.get(
                    self.List_Tehsil.curselection()))
            elif self.widget_name == 'Prem_Tehsil':
                self.Entry_Prem_Tehsil.delete(0, 'end')
                self.Entry_Prem_Tehsil.insert(0, self.List_Tehsil.get(
                    self.List_Tehsil.curselection()))
            elif self.widget_name == 'Prem_District':
                self.Entry_Prem_District.delete(0, 'end')
                self.Entry_Prem_District.insert(0, self.List_Tehsil.get(
                    self.List_Tehsil.curselection()))
            self.List_Tehsil.grid_forget()

        self.List_Tehsil = Listbox(self.Grid_Frame, exportselection=0, height=3, width=20, font=(
            'Bell', 14, 'bold'))
        self.List_Tehsil.bind('<FocusOut>', focusout)
        self.List_Tehsil.bind('<Double-Button-1>', selectval)

        self.Entry_Pre_Tehsil = ttk.Entry(self.Grid_Frame, font=(
            'Bell', 14, 'bold'))
        self.Entry_Pre_Tehsil.bind(
            '<KeyRelease>', lambda event: search(event, 'Pre_Tehsil'))
        self.Entry_Pre_Tehsil.grid(
            column=1, row=3, padx=10, pady=10, sticky=tk.W)

        self.Entry_Pre_District = tk.Entry(self.Grid_Frame, font=(
            'Bell', 14, 'bold'))
        self.Entry_Pre_District.bind(
            '<KeyRelease>', lambda event: search(event, 'Pre_District'))
        self.Entry_Pre_District.grid(
            column=3, row=3, padx=10, pady=10, sticky=tk.W)
        self.List_Pres_Province = tk.Listbox(self.Grid_Frame, exportselection=0, height=1, font=(
            'Bell', 14, 'bold'))

        self.List_Pres_Province.insert(1, "Azad Jammu and Kashmir")
        self.List_Pres_Province.insert(2, "Balochistan")
        self.List_Pres_Province.insert(3, "Federal Govt")
        self.List_Pres_Province.insert(4, "Gilgit-Baltistan")
        self.List_Pres_Province.insert(5, "Khyber Pakhtunkhwa")
        self.List_Pres_Province.insert(6, "Punjab")
        self.List_Pres_Province.insert(7, "Sindh")
        self.List_Pres_Province.grid(
            column=5, row=3, padx=10, pady=10, sticky=tk.W)
        self.Entry_Present_Address = ttk.Entry(
            self.Grid_Frame, width=60, font=('Bell', 14))
        self.Entry_Present_Address.grid(
            column=1, row=5, columnspan=4, padx=10, pady=10, sticky=tk.W)

        self.Entry_Prem_Tehsil = ttk.Entry(self.Grid_Frame, font=(
            'Bell', 14, 'bold'))
        self.Entry_Prem_Tehsil.bind(
            '<KeyRelease>', lambda event: search(event, 'Prem_Tehsil'))
        self.Entry_Prem_Tehsil.grid(
            column=1, row=6, padx=10, pady=10, sticky=tk.W)

        self.Entry_Prem_District = tk.Entry(self.Grid_Frame, font=(
            'Bell', 14, 'bold'))
        self.Entry_Prem_District.bind(
            '<KeyRelease>', lambda event: search(event, 'Prem_District'))
        self.Entry_Prem_District.grid(
            column=3, row=6, padx=10, pady=10, sticky=tk.W)
        self.List_Prem_Province = tk.Listbox(self.Grid_Frame, exportselection=0, height=1, font=(
            'Bell', 14, 'bold'))
        self.List_Prem_Province.insert(1, "Azad Jammu and Kashmir")
        self.List_Prem_Province.insert(2, "Balochistan")
        self.List_Prem_Province.insert(3, "Federal Govt")
        self.List_Prem_Province.insert(4, "Gilgit-Baltistan")
        self.List_Prem_Province.insert(5, "Khyber Pakhtunkhwa")
        self.List_Prem_Province.insert(6, "Punjab")
        self.List_Prem_Province.insert(7, "Sindh")
        self.List_Prem_Province.grid(
            column=5, row=6, padx=10, pady=10, sticky=tk.W)
        self.Entry_Permenent_Address = ttk.Entry(
            self.Grid_Frame, width=60, font=('Bell', 14))
        self.Entry_Permenent_Address.grid(
            column=1, row=8, columnspan=4, padx=10, pady=10, sticky=tk.W)

        self.List_Gender = tk.Listbox(self.Grid_Frame, exportselection=0, height=1, font=(
            'Bell', 14, 'bold'))
        self.List_Gender.insert(1, "Male")
        self.List_Gender.insert(2, "Female")
        self.List_Gender.insert(3, "Widow")
        self.List_Gender.grid(
            column=1, row=9, padx=10, pady=10, sticky=tk.W)

        self.List_Religion = tk.Listbox(self.Grid_Frame, exportselection=0, height=1, font=(
            'Bell', 14, 'bold'))
        self.List_Religion.insert(1, 'Islam')
        self.List_Religion.insert(2, 'Christanity')
        self.List_Religion.insert(3, 'Hindu')
        self.List_Religion.insert(4, 'Other')
        self.List_Religion.grid(
            column=3, row=9, padx=10, pady=10, sticky=tk.W)

        self.List_Marital_status = tk.Listbox(self.Grid_Frame, exportselection=0, height=1, font=(
            'Bell', 14, 'bold'))
        self.List_Marital_status.insert(1, 'Single')
        self.List_Marital_status.insert(2, 'Married')
        self.List_Marital_status.insert(3, 'Widow')
        self.List_Marital_status.insert(3, 'Divorced')
        self.List_Marital_status.grid(
            column=5, row=9, padx=10, pady=10, sticky=tk.W)

        self.Qualification = tk.Listbox(self.Grid_Frame,  exportselection=0, height=1, font=(
            'Bell', 14, 'bold'))
        # 1;Primary;2;Middle;3;SSC;4;HSSC;5;Bachelors;6;Masters;7;PhD;8;NotAvailable;9;Other
        self.Qualification.insert(1, 'Primary')
        self.Qualification.insert(2, 'Middle')
        self.Qualification.insert(3, 'SSC')
        self.Qualification.insert(4, 'HSSC')
        self.Qualification.insert(5, 'Bachelors')
        self.Qualification.insert(6, 'Masters')
        self.Qualification.insert(7, 'PhD')
        self.Qualification.insert(8, 'NotAvailable')
        self.Qualification.insert(9, 'Other')
        self.Qualification.grid(
            column=1, row=10, padx=10, pady=10, sticky=tk.W)
        # 1;Govt Employee;3;Own Business;4;Student;5;Other;6;House Wife;7;Private Job
        self.List_Occupation = tk.Listbox(self.Grid_Frame, exportselection=0, height=1, font=(
            'Bell', 14, 'bold'))
        self.List_Occupation.insert(1, 'Govt. Employee')
        self.List_Occupation.insert(2, 'Not Available')
        self.List_Occupation.insert(3, 'Own Business')
        self.List_Occupation.insert(4, 'Student')
        self.List_Occupation.insert(5, 'Other')
        self.List_Occupation.insert(6, 'House Wife')
        self.List_Occupation.insert(7, 'Private Job')
        self.List_Occupation.grid(
            column=3, row=10, padx=10, pady=10, sticky=tk.W)

        self.List_Process_Type = tk.Listbox(self.Grid_Frame, exportselection=0, height=1, font=(
            'Bell', 14, 'bold'))
        self.List_Process_Type.insert(1, 'Normal')
        self.List_Process_Type.insert(2, 'Urgent')
        self.List_Process_Type.grid(
            column=5, row=10, padx=10, pady=10, sticky=tk.W)

        self.List_Request_Type = tk.Listbox(self.Grid_Frame, exportselection=0, height=1, font=(
            'Bell', 14, 'bold'))
        self.List_Request_Type.insert(1, 'New')
        self.List_Request_Type.insert(2, 'Revised')
        self.List_Request_Type.insert(3, 'Duplicate')
        self.List_Request_Type.grid(
            column=1, row=11, padx=10, pady=10, sticky=tk.W)

        self.List_Application_Type = tk.Listbox(self.Grid_Frame, exportselection=0, height=1, font=(
            'Bell', 14, 'bold'))
        self.List_Application_Type.insert(1, 'Self')
        self.List_Application_Type.insert(2, 'Brother')
        self.List_Application_Type.grid(
            column=3, row=11, padx=10, pady=10, sticky=tk.W)

        self.List_Service_Type = tk.Listbox(self.Grid_Frame, exportselection=0, height=1, font=(
            'Bell', 14, 'bold'))
        self.List_Service_Type.insert(1, 'Offline')
        self.List_Service_Type.insert(2, 'Online')
        self.List_Service_Type.grid(
            column=5, row=11, padx=10, pady=10, sticky=tk.W)

        self.List_Pyament_Type = tk.Listbox(self.Grid_Frame, exportselection=0, height=1, font=(
            'Bell', 14, 'bold'))
        self.List_Pyament_Type.insert(1, 'Cash')
        self.List_Pyament_Type.insert(2, 'Manual - Through Challan')
        self.List_Pyament_Type.grid(
            column=1, row=12, padx=10, pady=10, sticky=tk.W)
        # AC (Saddar);AC (Industrial Area);AC (Shalimar)
        self.List_Approver = tk.Listbox(self.Grid_Frame, exportselection=0, height=1, font=(
            'Bell', 14, 'bold'))
        self.List_Approver.insert(0, 'AC (Saddar)')
        self.List_Approver.insert(1, 'AC (I/A)')
        self.List_Approver.insert(2, 'AC (Shalimar)')
        self.List_Approver.grid(
            column=3, row=12, padx=10, pady=10, sticky=tk.W)
        # Check Buttons

        cnic_front = IntVar()
        cnic_back = IntVar()
        cnic_guardian = IntVar()
        form_b = IntVar()
        domicile_of_guardian = IntVar()
        noc_from_concerned_district = IntVar()
        Residance_Prof = IntVar()
        utility_bill = IntVar()
        educational_certificate = IntVar()
        marriage_registration_certificate = IntVar()
        affidavit_voterlist = IntVar()
        affidavit_domicile = IntVar()
        voter_list = IntVar()
        domicile_challan = IntVar()

        chkfront = Checkbutton(self.Bottom_Frame, font=('Bell', 14), text="CNIC Front",
                               variable=cnic_front, onvalue=-1, offvalue=0, bd=5)
        chkfront.grid(column=0, row=1, padx=10, pady=5, sticky=tk.W)

        chkback = Checkbutton(self.Bottom_Frame, font=('Bell', 14), text="CNIC Back",
                              variable=cnic_back, onvalue=-1, offvalue=0, bd=5)
        chkback.grid(column=1, row=1, padx=10, pady=5, sticky=tk.W)

        chkguardian = Checkbutton(self.Bottom_Frame, font=('Bell', 14), text="CNIC Guardian",
                                  variable=cnic_guardian, onvalue=-1, offvalue=0, bd=5)
        chkguardian.grid(column=2, row=1, padx=10, pady=5, sticky=tk.W)

        chkformb = Checkbutton(self.Bottom_Frame, font=('Bell', 14), text="Form B",
                               variable=form_b, onvalue=-1, offvalue=0, bd=5)
        chkformb.grid(column=3, row=1, padx=10, pady=5, sticky=tk.W)
        chkdomguardian = Checkbutton(self.Bottom_Frame, font=('Bell', 14), text="Domicile of Guardian",
                                     variable=domicile_of_guardian, onvalue=-1, offvalue=0, bd=5)
        chkdomguardian.grid(column=4, row=1, padx=10, pady=5, sticky=tk.W)
        chknoc = Checkbutton(self.Bottom_Frame, font=('Bell', 14), text="NOC",
                             variable=noc_from_concerned_district, onvalue=-1, offvalue=0, bd=5)
        chknoc.grid(column=5, row=1, padx=10, pady=5, sticky=tk.W)

        chkResidance_Prof = Checkbutton(self.Bottom_Frame, font=('Bell', 14), text="Residance Prof",
                                        variable=Residance_Prof, onvalue=-1, offvalue=0, bd=5)
        chkResidance_Prof.grid(column=6, row=1, padx=10, pady=5, sticky=tk.W)
        chkutility_bill = Checkbutton(self.Bottom_Frame, font=('Bell', 14), text="Utility Bill",
                                      variable=utility_bill, onvalue=-1, offvalue=0, bd=5)
        chkutility_bill.grid(column=0, row=2, padx=10, pady=5, sticky=tk.W)
        chkeducer = Checkbutton(self.Bottom_Frame, font=('Bell', 14), text="Educational Certifiate",
                                variable=educational_certificate, onvalue=-1, offvalue=0, bd=5)
        chkeducer.grid(column=1, row=2, padx=10, pady=5, sticky=tk.W)

        chkmrc = Checkbutton(self.Bottom_Frame, font=('Bell', 14), text="Marriage Certifiate",
                             variable=marriage_registration_certificate, onvalue=-1, offvalue=0, bd=5)
        chkmrc.grid(column=2, row=2, padx=10, pady=5, sticky=tk.W)

        chkaffvotlst = Checkbutton(self.Bottom_Frame, font=('Bell', 14), text="Affidavit Voterlist",
                                   variable=affidavit_voterlist, onvalue=-1, offvalue=0, bd=5)
        chkaffvotlst.grid(column=3, row=2, padx=10, pady=5, sticky=tk.W)

        chkaffdom = Checkbutton(self.Bottom_Frame, font=('Bell', 14), text="Affidavit Domicile",
                                variable=affidavit_domicile, onvalue=-1, offvalue=0, bd=5)
        chkaffdom.grid(column=4, row=2, padx=10, pady=5, sticky=tk.W)

        chkvlist = Checkbutton(self.Bottom_Frame, font=('Bell', 14), text="Voter List",
                               variable=voter_list, onvalue=-1, offvalue=0, bd=5)
        chkvlist.grid(column=5, row=2, padx=10, pady=5, sticky=tk.W)

        chkdomch = Checkbutton(self.Bottom_Frame, font=('Bell', 14), text="Domicile Challan",
                               variable=domicile_challan, onvalue=-1, offvalue=0, bd=5)
        chkdomch.grid(column=6, row=2, padx=10, pady=5, sticky=tk.W)
        blank_label1 = Label(self.Status_Frame, width=20).grid(column=0, row=1)

        def save():
            today = date.today()
            if len(self.Entry_CNIC.get()) == 13:
                if self.Entry_CNIC.get().isnumeric() == FALSE:
                    return messagebox.showerror('showerror', 'CNIC is not numeric')

            else:
                print(len(self.Entry_CNIC.get()))
                return messagebox.showerror('showerror', 'CNIC is not 13 digit')

            if len(self.Entry_First_Name.get().strip()) == 0:
                return messagebox.showerror('showerror', 'Valid Name is Mandatory')
            if len(self.Entry_Father_Name.get().strip()) == 0:
                return messagebox.showerror('showerror', 'Valid Father Name is Mandatory')
            # finding present Tehsil in dictinery
            if len(self.Entry_Date_of_Birth.get().strip()) == 0:
                return messagebox.showerror('showerror', 'Valid (yyyy-) Father Name is Mandatory')

            if self.Entry_Pre_Tehsil.get() in Tehsil_List:
                # position = Tehsil_List.index(self.Entry_Pre_Tehsil.get())
                pre_Tehsil_id = self.Tehsil_data_dict.get(
                    self.Entry_Pre_Tehsil.get())  # Tehsil_Keys[position]
            else:
                return messagebox.showerror('showerror', 'Present Tehsil Not Found in List. Select One from List')

            if self.Entry_Pre_District.get() in District_List:
                # position = District_List.index(self.Entry_Pre_District.get())
                pre_District_id = self.District_data_dict.get(
                    self.Entry_Pre_District.get())  # District_Keys[position]
            else:
                return messagebox.showerror('showerror', 'Present District Not Found in List. Select One from List')

            if self.Entry_Prem_Tehsil.get() in Tehsil_List:
                # position = Tehsil_List.index(self.Entry_Prem_Tehsil.get())
                prem_Tehsil_id = self.Tehsil_data_dict.get(
                    self.Entry_Prem_Tehsil.get())  # Tehsil_Keys[position]
            else:
                return messagebox.showerror('showerror', 'Permenent Tehsil Not Found in List. Select One from List')

            if self.Entry_Prem_District.get() in District_List:
                # position = District_List.index(self.Entry_Prem_District.get())
                prem_District_id = self.District_data_dict.get(
                    self.Entry_Prem_District.get())  # District_Keys[position]
            else:
                return messagebox.showerror('showerror', 'Permenent District Not Found in List. Select One from List')

            # validating Lists
            pres_Province_id = 0
            if len(self.List_Pres_Province.curselection()) != 0:
                position = Province_List.index(self.List_Pres_Province.get(
                    self.List_Pres_Province.curselection()))
                pres_Province_id = Province_Keys[position]
            else:
                return messagebox.showerror('showerror', 'Select Province from List')

            prem_Province_id = 0
            if len(self.List_Prem_Province.curselection()) != 0:
                position = Province_List.index(self.List_Prem_Province.get(
                    self.List_Prem_Province.curselection()))
                prem_Province_id = Province_Keys[position]
            else:
                return messagebox.showerror('showerror', 'Select Province from List')

            if len(self.List_Gender.curselection()) != 0:
                Gender_Id = self.List_Gender.index(
                    self.List_Gender.curselection()) + 1
            else:
                return messagebox.showerror('showerror', 'Select Gender from List')
            if len(self.List_Religion.curselection()) != 0:
                Religion = self.List_Religion.get(
                    self.List_Religion.curselection())
            else:
                return messagebox.showerror('showerror', 'Select Religion from List')

            if len(self.List_Marital_status.curselection()) != 0:
                Marital_Status_Id = self.List_Marital_status.index(
                    self.List_Marital_status.curselection()) + 1
            else:
                return messagebox.showerror('showerror', 'Select Marital Status from List')
            if len(self.Qualification.curselection()) != 0:
                Qualification_Id = self.Qualification.index(
                    self.Qualification.curselection()) + 1
            else:
                return messagebox.showerror('showerror', 'Select Qualification from List')

            if len(self.List_Occupation.curselection()) != 0:
                Occupation_Id = self.List_Occupation.index(
                    self.List_Occupation.curselection()) + 1
            else:
                return messagebox.showerror('showerror', 'Select Occupation from List')
            if len(self.List_Application_Type.curselection()) != 0:
                Application_Type_Id = self.List_Application_Type.index(
                    self.List_Application_Type.curselection()) + 1
            else:
                return messagebox.showerror('showerror', 'Select Application Type from List')
            if len(self.List_Request_Type.curselection()) != 0:
                Request_Type_Id = self.List_Request_Type.index(
                    self.List_Request_Type.curselection()) + 1
            else:
                return messagebox.showerror('showerror', 'Select Request Type from List')
            if len(self.List_Service_Type.curselection()) != 0:
                Service_Type_Id = self.List_Service_Type.index(
                    self.List_Service_Type.curselection()) + 1
            else:
                return messagebox.showerror('showerror', 'Select Service Type from List')
            if len(self.List_Pyament_Type.curselection()) != 0:
                Payment_Type_Id = self.List_Pyament_Type.index(
                    self.List_Pyament_Type.curselection()) + 1
            else:
                return messagebox.showerror('showerror', 'Select Payment Type from List')

            # Dom_date, Status, CNIC, First_Name, Last_Name, Father_Name, Spouse_Name, Present_Address, Permenant_Address, Placeofbirth, Contact, Date_of_Birth, Arrival_Date, Gender, Religon, Marital_Status, Qualification, Occupation, Application_Type, Request_Type, Service_Type, Payment_Type, cnic_front, cnic_back, cnic_guardian, Residance_Prof, utility_bill, educational_certificate, marriage_registration_certificate, form_b, domicile_of_guardian, noc_from_concerned_district, affidavit_domicile, affidavit_voterlist, voter_listdomicile_challan

            Query = "Insert Into Domicile (Dom_date, Status, CNIC, First_Name, Last_Name, Father_Name, Spouse_Name, Pres_Tehsil, Pres_District, Pres_Province, Present_Address, Perm_Tehsil, Perm_District, Perm_Province, Permenant_Address, Placeofbirth, Contact, Date_of_Birth, Arrival_Date, Gender, Religon, Marital_Status, Qualification, Occupation, Application_Type, Request_Type, Service_Type, Payment_Type, cnic_front, cnic_back, cnic_guardian, Residance_Prof, utility_bill, educational_certificate, marriage_registration_certificate, form_b, domicile_of_guardian, noc_from_concerned_district, affidavit_domicile, affidavit_voterlist, voter_list, domicile_challan, Process_Type, Approver_Desig) values ('{}', 'Pending', '{}', '{}', '{}', '{}', '{}', {}, {}, {},'{}', {}, {}, {}, '{}', '{}', '{}', '{}', '{}', {}, '{}', {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, '{}', '{}')".format(today, self.Entry_CNIC.get(), self.Entry_First_Name.get(
            ), self.Entry_Last_Name.get(), self.Entry_Father_Name.get(), self.Entry_Spouse_Name.get(), pre_Tehsil_id, pre_District_id, pres_Province_id, self.Entry_Present_Address.get(), prem_Tehsil_id, prem_District_id, prem_Province_id, self.Entry_Prem_District.get(), self.Entry_Placeofbirth.get(), self.Entry_Contact.get(), self.Entry_Date_of_Birth.get(), self.Entry_Arrival_Date.get(), Gender_Id, Religion, Marital_Status_Id, Qualification_Id, Occupation_Id, Application_Type_Id, Request_Type_Id, Service_Type_Id, Payment_Type_Id, cnic_front.get(), cnic_back.get(), cnic_guardian.get(), Residance_Prof.get(), utility_bill.get(), educational_certificate.get(), marriage_registration_certificate.get(), form_b.get(), domicile_of_guardian.get(), noc_from_concerned_district.get(), affidavit_domicile.get(), affidavit_voterlist.get(), voter_list.get(), domicile_challan.get(), self.List_Process_Type.get(self.List_Process_Type.curselection()), self.List_Approver.get(self.List_Approver.curselection()))
            if len(self.child_data_list) != 0:
                try:
                    self.con = self.connectionstring
                    self.cur = self.con.cursor()
                    self.cur.execute(Query)
                    self.cur.execute('commit')
                    for items in self.child_data_list:
                        self.cur.execute("Insert into Childern (Father_CNIC, Child_Name, Child_dob) values ('{}', '{}', '{}')".fromat(
                            self.Entry_CNIC.get(), items[0], items[1]))
                        self.cur.execute('commit')
                    self.con.close()

                except Exception as e:
                    print('Opps!', e.__class__, ' Occured')

            messagebox.showinfo('showinfo', 'Record Saved')

        def add_Childerns():

            top_level = tk.Toplevel()
            top_level.geometry('500x400+100+100')
            top_frame = ttk.Frame(top_level)
            top_frame.pack(fill=X)
            middle_frame = ttk.Frame(top_level)
            middle_frame.pack(fill=BOTH, expand=TRUE)
            bottom_frame = ttk.Frame(top_level)
            bottom_frame.pack(fill=X)
            child_name_label = Label(top_frame, text='Child Name',
                                     font=('Bell', 12, 'bold'))
            child_name_label.grid(column=0, row=1, padx=20, pady=10)
            child_dob_label = Label(
                top_frame, text='Child Date of Birth', font=('Bell', 12, 'bold'))
            child_dob_label.grid(column=1, row=1, padx=20)
            child_name_entry = Entry(top_frame, font=('Bell', 12))
            child_name_entry.grid(column=0, row=2, padx=20)

            def add_Child(*arg):
                if validate_date(child_dob_entry.get()) != TRUE:
                    return messagebox.showerror('showerror', validate_date(child_dob_entry.get()))
                if len(child_name_entry.get()) == 0:
                    return messagebox.showerror('showerror', 'Please Provide Child Name')

                trv.insert("", 'end',
                           values=(child_name_entry.get(), child_dob_entry.get()))
                child_name_entry.delete('0', 'end')
                child_dob_entry.delete('0', 'end')
                child_name_entry.focus_set()

            child_dob_entry = Entry(top_frame, font=('Bell', 12))
            child_dob_entry.bind('<Return>', add_Child)
            child_dob_entry.grid(column=1, row=2, padx=20, pady=10)

            style = ttk.Style()
            style.configure('Treeview', font=('Helvetica', 12))
            style.configure("Treeview.Heading", font=('Helvetica', 12, 'bold'))
            trv = ttk.Treeview(middle_frame, selectmode='browse')
            trv.grid(row=3, column=0, columnspan=2, padx=20, pady=10)
            trv["columns"] = ("1", "2")
            trv['show'] = 'headings'
            trv.column("1", width=200, anchor='w')
            trv.column("2", width=200, anchor='w')
            trv.heading("1", text="Child Name", anchor='w')
            trv.heading("2", text="Date of Birth", anchor='w')

            def del_child():
                trv.delete(trv.selection())

            def validate_date(dob):
                if len(dob) > 10 or len(dob) < 10:
                    return 'Not a valid format'
                # to checkyou years is in 4 digit format
                if dob.find('-') == 4:
                    # to check you month in 02 digit format
                    if dob.find('-', 6) == 7:
                        if int(dob[:dob.find('-')]) > datetime.today().year:
                            return 'Invalid Year. Year is grater than today year'
                        elif int(datetime.today().year) - int(dob[:dob.find('-')]) > 80:
                            return 'Invalid Year. Year is grater than 80 years'
                        else:
                            if int(dob[5:7]) > 12 or int(dob[5:7]) < 0:
                                return 'Invalid Month'
                            else:
                                if int(dob[8:]) > 31 or int(dob[8:]) < 0:

                                    return 'Invalid Day'
                                else:
                                    return TRUE
                    else:
                        return 'Invalid Month'
                else:
                    return 'Invalid Year'

            def close_window():
                top_level.destroy()

            def Save_data():
                self.child_data_list = []

                for line in trv.get_children():
                    self.child_data_list.append(trv.item(line)['values'])
                top_level.destroy()

            Add_Btn = Button(bottom_frame, command=add_Child,
                             text='Add Child', width=15, font=('Bell', 12))
            Add_Btn.grid(column=1, row=1, padx=10, pady=10)
            Del_Btn = Button(bottom_frame, text='Del Child',
                             command=del_child, width=15, font=('Bell', 12))
            Del_Btn.grid(column=2, row=1, padx=10, pady=10)

            exit_Btn = Button(bottom_frame, text='Save + Exit Button',
                              command=Save_data, width=15, font=('Bell', 12))
            exit_Btn.grid(column=3, row=1, padx=10, pady=10)
            top_level.mainloop()

        def Receipt():
            pdf = FPDF()
            pdf.add_page()
            Req_type = {1: 'New', 2: 'Revised', 3: 'Duplicate'}
            Marital_Status = {1: 'Single', 2: 'Married',
                              3: 'Widow', 4: 'Divorced'}
            Gender = {1: 'Male', 2: 'Female',
                      3: 'Transgender'}
            # pdf.add_font('Bell MT', '', "c:\WINDOWS\Fonts\Bell.ttf", uni=True)
            pdf.set_font('Courier', 'B', size=18)
            pdf.set_fill_color(211, 211, 211)
            pdf.image('govt_logo.png', x=10, y=10, w=30, h=30)
            pdf.ln(7)
            pdf.cell(30, 6, txt='', align='C')
            pdf.cell(0, 6, txt='OFFICE OF THE DISTRICT MAGISTRATE',
                     ln=1, align='C')
            pdf.cell(30, 6, txt='', align='C')
            pdf.cell(0, 6, txt='CITIZEN FACILITATION CENTER',
                     ln=1, align='C')
            pdf.cell(30, 6, txt='', align='C')
            pdf.cell(0, 6, txt='ISLAMABAD CAPITAL TERRITORY',
                     ln=1, align='C')

            pdf.ln(8)
            try:
                con = self.connectionstring
                if con.is_connected():
                    cur = con.cursor(dictionary=True)
                    # Query = "Select * from Domicile Where CNIC = '9100301000850';"
                    Query = "Select * from Domicile Where CNIC = '{}';".format(
                        self.Entry_CNIC.get())

                    cur.execute(Query)
                    data = cur.fetchall()
            except Error as e:
                print("Error while connecting to MySQL", e)
                return

            pdf.set_font('Times', size=12)
            for row in data:

                pdf.cell(40, 8, 'Application No')
                pdf.cell(40, 8, str(row['Dom_id']))
                pdf.cell(20, 8, '')
                pdf.cell(40, 8, 'Appliccation Date')
                pdf.cell(50, 8, '{}'.format(row['Dom_date']))
                pdf.ln(8)
                pdf.cell(40, 8, 'Application Type')
                pdf.cell(40, 8, Req_type.get(row['Request_Type']))
                pdf.cell(20, 8, '')
                pdf.cell(40, 8, 'CNIC')
                pdf.cell(50, 8, row['CNIC'])
                pdf.ln(8)
                pdf.cell(40, 8, 'Name')
                pdf.cell(60, 8, row['First_Name'] + row['Last_Name'])
                pdf.cell(40, 8, 'Father Name')
                pdf.cell(50, 8, row['Father_Name'])
                pdf.ln(8)
                pdf.cell(40, 8, 'Spouse Name')
                pdf.cell(60, 8, row['Spouse_Name'])
                pdf.cell(40, 8, 'Date of Birth')
                pdf.cell(50, 8, '{}'.format(row['Date_of_Birth']))
                pdf.ln(8)
                pdf.cell(40, 8, 'Marital Status')
                pdf.cell(60, 8, Marital_Status.get(
                    row['Marital_Status']))
                pdf.cell(40, 8, 'Contact')
                pdf.cell(50, 8, row['Contact'])
                pdf.ln(8)
                pdf.cell(40, 8, 'Gender')
                pdf.cell(60, 8, Gender.get(
                    row['Gender']))
                pdf.cell(40, 8, 'Religion')
                pdf.cell(50, 8, row['Religon'])
                pdf.ln(8)
                pdf.cell(40, 8, 'Present Address')
                pdf.cell(150, 8, row['Present_Address'])
                pdf.ln(8)
                pdf.cell(40, 8, 'Permenant Address')
                pdf.cell(150, 8, row['Permenant_Address'])
                pdf.ln(24)
                pdf.multi_cell(0, 7, 'I hereby declare that the details furnished above are true and correct to the best of my knowledge and belief and iundertake to inform you of any changes therein, immediately. In case of any of the above information in found to be false or untrue or misleading or misrepresenting. I am aware that I may be held liable for it')
                pdf.ln(16)
                pdf.cell(100, 8, 'Domicile Clerk Signature_________________')

                pdf.cell(100, 8, 'Applicant Signature_________________')
                pdf.ln(8)

            pdf.output('Receipt.pdf')

            path = 'Receipt.pdf'
            os.system(path)

        def close_form():
            self.destroy()
        self.Add_Ch_button = tk.Button(
            self.Status_Frame, width=15, text='Add Childerns', command=add_Childerns, font=('Bell', 12))
        self.Add_Ch_button.grid(column=1, row=1, padx=10, pady=10)
        blank_label2 = Label(self.Status_Frame, width=20).grid(column=2, row=1)
        self.save_button = tk.Button(
            self.Status_Frame, width=15, text='Save', command=save, font=('Bell', 12))
        self.save_button.grid(column=3, row=1, padx=10, pady=10)
        blank_label4 = Label(self.Status_Frame, width=20).grid(column=4, row=1)

        self.Receipt_Button = Button(
            self.Status_Frame, text='Receipt', width=15, command=Receipt, font=('Bell', 12))
        self.Receipt_Button.grid(column=5, row=1)
        blank_label4 = Label(self.Status_Frame, width=20).grid(column=6, row=1)
        self.Exit_button = tk.Button(
            self.Status_Frame, width=15, text='Exit', command=close_form, font=('Bell', 12))
        self.Exit_button.grid(column=7, row=1, padx=10, pady=10)


class Sysentry(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('1000x800+50+50')
        self.Top_Frame = ttk.Frame(
            self, relief=RIDGE, border=1, height=10)
        self.Top_Frame.pack(fill=BOTH, expand=YES)
        self.Top_label = ttk.Label(
            self.Top_Frame, text='Javascript Generator', border=1, font=('Bell', 18, 'bold'))
        self.Top_label.pack(padx=10, pady=10, side=TOP)

        def check_event(event):
            if event.keysym == 'Return':
                generate()
                self.Js_Text.focus_set()
                self.Js_Text.tag_add(SEL, "1.0", END)
                self.Js_Text.mark_set(INSERT, "1.0")
                self.Js_Text.see(INSERT)
                return 'break'

        self.Label_CNIC = ttk.Label(
            self.Top_Frame, text='CNIC', border=1, font=('Bell', 12))
        self.Label_CNIC.place(x=50, y=55)
        self.Entry_CNIC = ttk.Entry(self.Top_Frame, font=('Bell', 12))

        self.Entry_CNIC.place(x=100, y=55)
        self.Js_Text = Text(self.Top_Frame, height=20, font=('Bell', 12))
        self.Js_Text.place(x=50, y=110)
        self.Js_child_Text = Text(self.Top_Frame, height=10, font=('Bell', 12))
        self.Js_child_Text.place(x=50, y=530)

        def Convert_Boolean(val):
            if val == 0:
                return 'false'
            elif val == -1:
                return 'true'

        def generate(*args):
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
            try:
                con = mysql.connector.connect(
                    host='25.20.12.230', database='domicile_reports', user='root', password='2891dimah')

                cur = con.cursor(dictionary=True)
                cur.execute(
                    "Select * from domicile Where CNIC='{}'".format(self.Entry_CNIC.get()))
                data = cur.fetchall()
            except Error as e:
                print("Error while connecting to MySQL", e)
                return
            if len(data) == 0:
                messagebox.showerror('showerror', 'Nothing Found')
                self.Entry_CNIC.focus_set()
                con.close()
                return
            con.close()
            for row in data:

                txt = "document.getElementById('first_name').value = '{}';".format(
                    row["First_Name"])
                self.Js_Text.insert(tk.END, txt + '\n')
                txt = "document.getElementById('last_name').value = '{}';".format(
                    row['Last_Name'])
                self.Js_Text.insert(tk.END, txt + '\n')
                txt = "document.getElementById('cnic').value = '{}';".format(
                    row['CNIC'])
                self.Js_Text.insert(tk.END, txt + '\n')
                txt = "document.getElementById('place_of_birth').value = '{}';".format(
                    row['Placeofbirth'])
                self.Js_Text.insert(tk.END, txt + '\n')
                txt = "document.getElementById('father_name').value = '{}';".format(
                    row['Father_Name'])
                self.Js_Text.insert(tk.END, txt + '\n')
                txt = "document.getElementById('spouse_name').value = '{}';".format(
                    row['Spouse_Name'])
                self.Js_Text.insert(tk.END, txt + '\n')
                txt = "document.getElementById('temp_address').value = '{}';".format(
                    row['Present_Address'])
                self.Js_Text.insert(tk.END, txt + '\n')
                txt = "document.getElementById('temp_province_id').value = '{}';".format(
                    row['Pres_Province'])
                self.Js_Text.insert(tk.END, txt + '\n')
                txt = "document.getElementById('temp_district_id').value = '{}';".format(
                    row['Pres_District'])
                self.Js_Text.insert(tk.END, txt + '\n')
                txt = "document.getElementById('temp_tehsil_id').value = '{}';".format(
                    row['Pres_Tehsil'])
                self.Js_Text.insert(tk.END, txt + '\n')
                txt = "document.getElementById('permanent_address').value = '{}';".format(
                    row['Permenant_Address'])
                self.Js_Text.insert(tk.END, txt + '\n')
                txt = "document.getElementById('permanent_province_id').value = '{}';".format(
                    row['Perm_Province'])
                self.Js_Text.insert(tk.END, txt + '\n')
                txt = "document.getElementById('permanent_district_id').value = '{}';".format(
                    row['Perm_District'])
                self.Js_Text.insert(tk.END, txt + '\n')
                txt = "document.getElementById('permanent_tehsil_id').value = '{}';".format(
                    row['Perm_Tehsil'])
                self.Js_Text.insert(tk.END, txt + '\n')
                txt = "document.getElementById('contact').value = '{}';".format(
                    row['Contact'])
                self.Js_Text.insert(tk.END, txt + '\n')
                txt = "document.getElementById('date_of_birth').value = '{}';".format(
                    row['Date_of_Birth'])
                self.Js_Text.insert(tk.END, txt + '\n')
                txt = "document.getElementById('arrival_date').value = '{}';".format(
                    row['Arrival_Date'])
                self.Js_Text.insert(tk.END, txt + '\n')
                txt = "document.getElementById('gender_id').value = '{}';".format(
                    row['Gender'])
                self.Js_Text.insert(tk.END, txt + '\n')
                txt = "document.getElementById('religion').value = '{}';".format(
                    row['Religon'])
                self.Js_Text.insert(tk.END, txt + '\n')
                txt = "document.getElementById('marital_status_id').value = '{}';".format(
                    row['Marital_Status'])
                self.Js_Text.insert(tk.END, txt + '\n')
                txt = "document.getElementById('qualification_id').value = '{}';".format(
                    row['Qualification'])
                self.Js_Text.insert(tk.END, txt + '\n')
                txt = "document.getElementById('occupation_id').value = '{}';".format(
                    row['Occupation'])
                self.Js_Text.insert(tk.END, txt + '\n')
                txt = "document.getElementById('applicant_type_id').value = '{}';".format(
                    row['Application_Type'])
                self.Js_Text.insert(tk.END, txt + '\n')
                txt = "document.getElementById('request_type_id').value = '{}';".format(
                    row['Request_Type'])
                self.Js_Text.insert(tk.END, txt + '\n')
                txt = "document.getElementById('service_type_id').value = '{}';".format(
                    row['Service_Type'])
                self.Js_Text.insert(tk.END, txt + '\n')
                txt = "document.getElementById('payment_type_id').value = '{}';".format(
                    row['Payment_Type'])
                self.Js_Text.insert(tk.END, txt + '\n')
                txt = "document.getElementById('docs-cnic-front').checked = {};".format(
                    Convert_Boolean(row['cnic_front']))
                self.Js_Text.insert(tk.END, txt + '\n')

                txt = "document.getElementById('docs[cnic_back]').checked = {};".format(
                    Convert_Boolean(row['cnic_back']))
                self.Js_Text.insert(tk.END, txt + '\n')
                txt = "document.getElementById('docs[cnic_guardian]').checked = {};".format(
                    Convert_Boolean(row['cnic_guardian']))
                self.Js_Text.insert(tk.END, txt + '\n')
                txt = "document.getElementById('docs[proof_of_residence]').checked = {};".format(
                    Convert_Boolean(row['Residance_Prof']))
                self.Js_Text.insert(tk.END, txt + '\n')
                txt = "document.getElementById('docs[utility_bill]').checked = {};".format(
                    Convert_Boolean(row['utility_bill']))
                self.Js_Text.insert(tk.END, txt + '\n')
                txt = "document.getElementById('docs[educational_certificate]').checked = {};".format(
                    Convert_Boolean(row['educational_certificate']))
                self.Js_Text.insert(tk.END, txt + '\n')
                txt = "document.getElementById('docs[marriage_registration_certificate]').checked = {};".format(
                    Convert_Boolean(row['marriage_registration_certificate']))
                self.Js_Text.insert(tk.END, txt + '\n')
                txt = "document.getElementById('docs[form_b]').checked = {};".format(
                    Convert_Boolean(row['form_b']))

                self.Js_Text.insert(tk.END, txt + '\n')
                txt = "document.getElementById('docs[domicile_of_guardian]').checked = {};".format(
                    Convert_Boolean(row['domicile_of_guardian']))

                self.Js_Text.insert(tk.END, txt + '\n')
                txt = "document.getElementById('docs[noc_from_concerned_district]').checked = {};".format(
                    Convert_Boolean(row['noc_from_concerned_district']))

                self.Js_Text.insert(tk.END, txt + '\n')
                txt = "document.getElementById('docs[affidavit_domicile]').checked = {};".format(
                    Convert_Boolean(row['affidavit_domicile']))

                self.Js_Text.insert(tk.END, txt + '\n')
                txt = "document.getElementById('docs[affidavit_voterlist]').checked = {};".format(
                    Convert_Boolean(row['affidavit_voterlist']))

                self.Js_Text.insert(tk.END, txt + '\n')
                txt = "document.getElementById('docs[voter_list]').checked = {};".format(
                    Convert_Boolean(row['voter_list']))

                self.Js_Text.insert(tk.END, txt + '\n')
                txt = "document.getElementById('docs[domicile_challan]').checked = {};".format(
                    Convert_Boolean(row['domicile_challan']))

                self.Js_Text.insert(tk.END, txt + '\n')
                try:
                    con = mysql.connector.connect(
                        host='25.20.12.230', database='domicile_reports', user='root', password='2891dimah')

                    cur = con.cursor(dictionary=True)
                    cur.execute(
                        "Select * from Childern Where Father_CNIC='{}'".format(self.Entry_CNIC.get()))
                    data = cur.fetchall()
                except Error as e:
                    print("Error while connecting to MySQL", e)
                    return
                if len(data) == 0:

                    con.close()
                    return
                con.close()
                vari = 97
                cnt = 0
                for row in data:
                    txt = "var {} = document.getElementsByName('children[{}][first_name]');".format(
                        chr(vari), cnt)
                    self.Js_child_Text.insert(tk.END, txt + '\n')
                    txt = chr(vari) + "[0].value = '" + \
                        row["Child_Name"] + "';"
                    self.Js_child_Text.insert(tk.END, txt + '\n')
                    var = vari + 1
                    txt = "var {} = document.getElementsByName('children[" + str(
                        cnt) + "][date_of_birth]');".format(chr(vari))
                    self.Js_child_Text.insert(tk.END, txt + '\n')
                    txt = chr(vari) + \
                        "[0].value = '{}';".format(row["Child_dob"])
                    self.Js_child_Text.insert(tk.END, txt + '\n')
                    cnt = cnt + 1
                    vari = vari + 1

        self.Entry_CNIC.bind('<Return>', check_event)

        def clear_text():
            self.Js_Text.delete('1.0', 'end')
            self.Js_child_Text.delete('1.0', 'end')
        self.Gen_JS_Button = Button(
            self.Top_Frame, text='Generate Js', command=generate, font=('Bell', 12))
        self.Gen_JS_Button.place(x=300, y=50)
        self.Clear_Button = Button(
            self.Top_Frame, text='Clear Text', command=clear_text, font=('Bell', 12))
        self.Clear_Button.place(x=430, y=50)


class Collection_Report(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('500x200')
        self.title('Report')

        self.Label_Main = tk.Label(
            self, text='Daily Domicile Collection Report', width=30, height=2, font=('Bell', 14, 'bold'))
        self.Label_Main.pack()
        self.Label_Date = tk.Label(
            self, text='Collection Date', font=('Bell', 12))
        self.Label_Date.place(x=50, y=50)

        def check_enter_press(event, collection_date):
            if event.keysym == 'Return':
                Report(collection_date)
        self.Entry_Date = tk.Entry(self, font=('Bell', 12))
        self.Entry_Date.bind(
            '<KeyRelease>', lambda event: check_enter_press(event, self.Entry_Date.get()))
        self.Entry_Date.insert(0, datetime.date(datetime.today()))
        self.Entry_Date.place(x=200, y=50)
        self.Label_Date = tk.Label(
            self, text='Calling Days', font=('Bell', 12))
        self.Label_Date.place(x=50, y=100)

        self.Entry_Days = tk.Entry(self, font=('Bell', 12))
        self.Entry_Days.insert(0, "3")
        self.Entry_Days.place(x=200, y=100)
        self.Rpt_btn = tk.Button(self, text='Report', width=15, font=(
            'Bell', 12), command=lambda: Report(self.Entry_Date.get()))

        self.Rpt_btn.place(x=150, y=150)

        def Report(collection_date):
            pdf = FPDF()
            pdf.add_page()

            # pdf.add_font('Bell MT', '', "c:\WINDOWS\Fonts\Bell.ttf", uni=True)
            pdf.set_font('Courier', 'B', size=18)
            pdf.set_fill_color(211, 211, 211)
            pdf.cell(0, 10, txt='Domicile Collection Report for {}'.format(collection_date),
                     ln=1, border=1, align='L', fill=True)
            yy, mm, dd = collection_date.split('-')
            called_date = datetime(int(yy), int(mm), int(dd))
            if len(self.Entry_Days.get()) == 0:
                days = 3
            else:
                if self.Entry_Days.get().isnumeric():
                    days = int(self.Entry_Days.get())
                else:
                    messagebox.showerror('showerror', 'Invalid Input')
                    self.focus_set()
                    return

            called_date = called_date + timedelta(days=days)
            pdf.cell(0, 10, txt='Applicants are called on {}'.format(called_date.date()),
                     ln=1, border=1, align='L', fill=True)
            pdf.ln(8)
            try:
                con = mysql.connector.connect(host='25.20.12.230',
                                              database='domicile_reports',
                                              user='root',
                                              password='2891dimah')

                cur = con.cursor()
                Query = "Select CNIC, First_Name from Domicile Where Dom_Date = '{}' And Process_Type = 'Normal';".format(
                    collection_date)

                cur.execute(Query)
                data = cur.fetchall()
            except Error as e:
                print("Error while connecting to MySQL", e)
                return
            sr = 0

            pdf.set_font('Courier', 'B', size=14)
            #     pdf.ln(12)
            pdf.cell(20, 8, 'S.No', border=1)
            pdf.cell(50, 8, 'CNIC', border=1)
            pdf.cell(120, 8, 'Name', border=1)
            pdf.ln(8)
            for dat in data:
                sr = sr + 1
                pdf.set_font('Courier', size=12)
                pdf.cell(20, 8, str(sr), border=1)
                pdf.cell(50, 8, dat[0], border=1)
                pdf.cell(120, 8, dat[1], border=1)
                pdf.ln(8)

            pdf.output('Daily_Report.pdf')

            path = 'Daily_Report.pdf'
            os.system(path)


# filepath = 'F:/Docs/OneDrive/Python Projects/CFC App/Office.db'
Obj = dataentry()
Obj.mainloop()
