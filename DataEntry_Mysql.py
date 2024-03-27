import os
from datetime import timedelta
import Validation
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.filedialog import askopenfile
from datetime import datetime
from Monthly_Report import Monthly_Report
from fpdf import FPDF
import json
from PIL import Image, ImageTk
from tools import open_con

class dataentry(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('1400x750+50+50')
        # self.attributes('-fullscreen', True)
        # self.attributes('-alpha', 0.8)
        path = os.getcwd()
        path = path+r"\theme"
        self.title('CFC APP 1.7')
        self.state('zoomed')
        # self.tk.call('lappend', 'auto_path',
        #              path)
        # self.tk.call('package', 'require', 'awblack')
        f = open("config.json", "r")
        self.j_obj = json.load(f)
        f.close()
        self.tk.call("source", "{}".format(self.j_obj['theme_source']))
        self.tk.call("set_theme", "{}".format(self.j_obj['theme_mode']))

        self.theme_style = ttk.Style(self)
        font_name = 'Courier New'
        self.label_font = (font_name, 14, 'bold')
        self.entry_font = (font_name, 14)
        self.list_font = (font_name, 14)
        self.check_font = (font_name, 12)
        self.button_font = (font_name, 14, 'bold')
        self.treeview_font = (font_name, 12)
        self.treeview_heading_font = (font_name, 12, 'bold')
        self.rec_id = 0
        self.cnic_dup_check = False
        # self.theme_style.theme_use('awblack')
        self.theme_style.configure('TButton', font=self.label_font)
        # self.theme_style.configure('TLabel', font=('Bell', 'B', 12))
        # self.theme_style.configure('TEntry', font=('Bell', 14))
        # self.configure(bg='#24304a')
        self.binaryfile = None
        self.widget_name = ''
        self.child_data_list = []
        self.child_insert_chk = tk.IntVar(self)
        self.on_img = PhotoImage('on.png')
        self.off_img = PhotoImage('off.png')
        self.Top_Frame = Frame(
            self, relief=RIDGE, border=1, height=10)  # bg='#24304a'
        self.Top_Frame.pack(padx=10, pady=10, fill=X)
        self.Top_label = ttk.Label(
            self.Top_Frame, text='New Domicile Application', border=1, font=('Courier New', 18, 'bold'))  # background='#24304a'
        self.Top_label.pack()
        self.edit_mode = FALSE
        self.Grid_Frame = Frame(self, relief=RIDGE, border=1)  # bg='#24304a'
        self.Grid_Frame.pack(padx=10, pady=5, fill=BOTH, expand=TRUE)
        self.Bottom_Frame = Frame(
            self, relief=RIDGE, border=1)  # , bg='#24304a'
        self.Bottom_Frame.pack(padx=10, pady=5, fill=BOTH, expand=TRUE)
        self.Status_Frame = Frame(
            self, relief=RIDGE, border=1)  # , bg='#24304a'
        self.Status_Frame.pack(padx=10, pady=5, fill=BOTH, expand=TRUE)

        # self.List_Teh_Dist = tk.Listbox(
        #     self.Grid_Frame, selectmode='single', exportselection=0, height=3, font=self.list_font)
        # Creating Labels
        self.Record_Date_Label = ttk.Label(
            self.Grid_Frame, text='Record Date', font=self.label_font)
        self.Record_Date_Label.grid(
            column=0, row=0, padx=10, pady=10, sticky=tk.W)
        self.Lbl_CNIC = ttk.Label(self.Grid_Frame, text='CNIC', font=self.label_font).grid(
            column=2, row=0, padx=10, pady=10, sticky=tk.W)
        self.Lbl_First_Name = ttk.Label(self.Grid_Frame, text='First Name', font=self.label_font).grid(
            column=4, row=0, padx=10, pady=10, sticky=tk.W)
        # self.Lbl_Last_Name = ttk.Label(self.Grid_Frame, text='Last Name', font=self.label_font).grid(
        #     column=4, row=0, padx=10, pady=10, sticky=tk.W)
        self.Lbl_Father_Name = ttk.Label(self.Grid_Frame, text='Father Name', font=self.label_font).grid(
            column=0, row=1, padx=10, pady=10, sticky=tk.W)
        self.Lbl_Spouse_Name = ttk.Label(self.Grid_Frame, text='Spouse Name', font=self.label_font).grid(
            column=2, row=1, padx=10, pady=10, sticky=tk.W)
        self.Lbl_Contact = ttk.Label(self.Grid_Frame, text='Contact', font=self.label_font).grid(
            column=4, row=1, padx=10, pady=10, sticky=tk.W)
        self.Lbl_Placeofbirth = ttk.Label(self.Grid_Frame, text='Place of birth', font=self.label_font).grid(
            column=0, row=2, padx=10, pady=10, sticky=tk.W)
        self.Lbl_Date_of_Birth = ttk.Label(self.Grid_Frame, text='Date of Birth', font=self.label_font).grid(
            column=2, row=2, padx=10, pady=10, sticky=tk.W)
        self.Lbl_Arrival_Date = ttk.Label(self.Grid_Frame, text='Arrival Date', font=self.label_font).grid(
            column=4, row=2, padx=10, pady=10, sticky=tk.W)

        self.Lbl_Pre_Tehsil = ttk.Label(self.Grid_Frame, text='Present Tehsil', font=self.label_font).grid(
            column=0, row=3, padx=10, pady=10, sticky=tk.W)
        self.Label_Pre_District = ttk.Label(self.Grid_Frame, text='Present District', font=self.label_font).grid(
            column=2, row=3, padx=10, pady=10, sticky=tk.W)
        self.Lbl_Present_Province = ttk.Label(self.Grid_Frame, text='Present Province', font=self.label_font).grid(
            column=4, row=3, padx=10, pady=10, sticky=tk.W)
        self.Lbl_Present_Address = ttk.Label(self.Grid_Frame, text='Present Address', font=self.label_font).grid(
            column=0, row=5, padx=10, pady=10, sticky=tk.W)

        self.Lbl_Prme_Tehsil = ttk.Label(self.Grid_Frame, text='Permenent Tehsil', font=self.label_font).grid(
            column=0, row=6, padx=10, pady=10, sticky=tk.W)
        self.Label_Prme_District = ttk.Label(self.Grid_Frame, text='Permenent District', font=self.label_font).grid(
            column=2, row=6, padx=10, pady=10, sticky=tk.W)
        self.Lbl_Perm_Province = ttk.Label(self.Grid_Frame, text='Permenent Province', font=self.label_font).grid(
            column=4, row=6, padx=10, pady=10, sticky=tk.W)
        self.Lbl_Permenent_Address = ttk.Label(self.Grid_Frame, text='Permenent Address', font=self.label_font).grid(
            column=0, row=8, padx=10, pady=10, sticky=tk.W)
        self.Lbl_Gender = ttk.Label(self.Grid_Frame, text='Gender', font=self.label_font).grid(
            column=0, row=9, padx=10, pady=10, sticky=tk.W)
        self.Lbl_Religion = ttk.Label(self.Grid_Frame, text='Religion', font=self.label_font).grid(
            column=2, row=9, padx=10, pady=10, sticky=tk.W)
        self.Lbl_Marital_Status = ttk.Label(self.Grid_Frame, text='Marital Status', font=self.label_font).grid(
            column=4, row=9, padx=10, pady=10, sticky=tk.W)
        self.Lbl_Qulification = ttk.Label(self.Grid_Frame, text='Qulification', font=self.label_font).grid(
            column=0, row=10, padx=10, pady=10, sticky=tk.W)
        self.Lbl_Occupation = ttk.Label(self.Grid_Frame, text='Occupation', font=self.label_font).grid(
            column=2, row=10, padx=10, pady=10, sticky=tk.W)
        self.Lbl_Process_type = ttk.Label(self.Grid_Frame, text='Proccess Type', font=self.label_font).grid(
            column=4, row=10, padx=10, pady=10, sticky=tk.W)
        self.Lbl_Request_Type = ttk.Label(self.Grid_Frame, text='Request Type', font=self.label_font).grid(
            column=0, row=11, padx=10, pady=10, sticky=tk.W)
        self.Lbl_Application_Type = ttk.Label(self.Grid_Frame, text='Application Type', font=self.label_font).grid(
            column=2, row=11, padx=10, pady=10, sticky=tk.W)
        self.Lbl_Service_Type = ttk.Label(self.Grid_Frame, text='Service Type', font=self.label_font).grid(
            column=4, row=11, padx=10, pady=10, sticky=tk.W)
        self.Lbl_Payment_Type = ttk.Label(self.Grid_Frame, text='Payment Type', font=self.label_font).grid(
            column=0, row=12, padx=10, pady=10, sticky=tk.W)
        self.Lbl_Approver = ttk.Label(self.Grid_Frame, text='Approver', font=self.label_font).grid(
            column=2, row=12, padx=10, pady=10, sticky=tk.W)

        self.Record_Date = ttk.Entry(
            self.Grid_Frame, font=self.entry_font)
        self.Record_Date.grid(
            column=1, row=0, padx=10, pady=10, sticky=tk.W)
        self.Record_Date.insert(0, datetime.today().date())

        self.Entry_CNIC = ttk.Entry(
            self.Grid_Frame, font=self.entry_font)
        self.Entry_CNIC.grid(column=3, row=0, padx=10, pady=10, sticky=tk.W)
        self.bind('<Tab>', lambda cnic: self.check_dup_cnic(
            cnic=self.Entry_CNIC.get()))
        self.Entry_First_Name = ttk.Entry(
            self.Grid_Frame, font=self.entry_font)
        self.Entry_First_Name.grid(
            column=5, row=0, padx=10, pady=10, sticky=tk.W)

        # self.Entry_Last_Name = ttk.Entry(self.Grid_Frame, font=self.entry_font)
        # self.Entry_Last_Name.grid(column=5, row=0, padx=10,
        #                           pady=10, sticky=tk.W)

        self.Entry_Father_Name = ttk.Entry(
            self.Grid_Frame, font=self.entry_font)
        self.Entry_Father_Name.grid(
            column=1, row=1, padx=10, pady=10, sticky=tk.W)

        self.Entry_Spouse_Name = ttk.Entry(
            self.Grid_Frame, font=self.entry_font)
        self.Entry_Spouse_Name.grid(
            column=3, row=1, padx=10, pady=10, sticky=tk.W)

        self.Entry_Contact = ttk.Entry(self.Grid_Frame, font=self.entry_font)
        self.Entry_Contact.grid(column=5, row=1, padx=10, pady=10, sticky=tk.W)
        self.Entry_Contact.insert(0, '00000000000')
        self.Entry_Placeofbirth = ttk.Entry(
            self.Grid_Frame, font=self.entry_font)
        self.Entry_Placeofbirth.grid(
            column=1, row=2, padx=10, pady=10, sticky=tk.W)
        self.Entry_Placeofbirth.insert(0, 'ISLAMABAD')

        self.Entry_Date_of_Birth = ttk.Entry(
            self.Grid_Frame, font=self.entry_font)
        self.Entry_Date_of_Birth.grid(
            column=3, row=2, padx=10, pady=10, sticky=tk.W)
        self.Entry_Date_of_Birth.bind(
            '<FocusOut>', self.update_arrival)
        self.Entry_Arrival_Date = ttk.Entry(
            self.Grid_Frame, font=self.entry_font)
        self.Entry_Arrival_Date.grid(
            column=5, row=2, padx=10, pady=10, sticky=tk.W)
        self.widget_focus = False
        self.widget_name = ''
        self.data_list = tk.Listbox(
            self.Grid_Frame, selectmode='single', exportselection=0, height=5, font=self.list_font)
        self.data_list.bind('<Return>', self.export_selection)
        self.data_list.bind('<Double-Button-1>', self.export_selection)

        self.Entry_Pre_Tehsil = ttk.Entry(
            self.Grid_Frame, font=self.entry_font)
        self.Entry_Pre_Tehsil.bind(
            '<KeyRelease>', lambda event: self.list_search(event, self.Tehsils_data_list, 'Pre_Tehsil'))
        self.Entry_Pre_Tehsil.bind('<FocusOut>', self.widget_lost_focus)
        self.Entry_Pre_Tehsil.bind(
            '<FocusIn>', lambda event: self.data_list.place_forget())
        self.Entry_Pre_Tehsil.bind('<Down>', self.list_get_focus)
        self.Entry_Pre_Tehsil.grid(
            column=1, row=3, padx=10, pady=10, sticky=tk.W)
        self.Entry_Pre_District = ttk.Entry(
            self.Grid_Frame, font=self.entry_font)
        self.Entry_Pre_District.bind(
            '<KeyRelease>', lambda event: self.list_search(event, self.Districts_data_list, 'Pre_District'))
        self.Entry_Pre_District.bind('<FocusOut>', self.widget_lost_focus)
        self.Entry_Pre_District.bind(
            '<FocusIn>', lambda event: self.data_list.place_forget())
        self.Entry_Pre_District.bind('<Down>', self.list_get_focus)
        self.Entry_Pre_District.grid(
            column=3, row=3, padx=10, pady=10, sticky=tk.W)
        # Getting Tehsil and District Lists from db
        self.List_Pres_Province = tk.Listbox(
            self.Grid_Frame, selectmode='single', exportselection=0, height=1, font=self.list_font)

        self.List_Pres_Province.insert(1, "Azad Jammu and Kashmir")
        self.List_Pres_Province.insert(2, "Balochistan")
        self.List_Pres_Province.insert(3, "Federal Govt")
        self.List_Pres_Province.insert(4, "Gilgit-Baltistan")
        self.List_Pres_Province.insert(5, "Khyber Pakhtunkhwa")
        self.List_Pres_Province.insert(6, "Punjab")
        self.List_Pres_Province.insert(7, "Sindh")
        self.List_Pres_Province.bind('<KeyPress>', self.select_keysym_value)
        self.List_Pres_Province.bind(
            '<FocusIn>', lambda event: self.data_list.place_forget())
        self.List_Pres_Province.grid(
            column=5, row=3, padx=10, pady=10, sticky=tk.W)
        self.Entry_Present_Address = ttk.Entry(
            self.Grid_Frame, width=60, font=self.entry_font)
        self.Entry_Present_Address.grid(
            column=1, row=5, columnspan=4, padx=10, pady=10, sticky=tk.W)

        self.Btn_Same_Address = ttk.Button(
            self.Grid_Frame, text='Copy Address', command=self.copy_address)
        self.Btn_Same_Address.grid(
            column=4, row=5, padx=10, pady=10, sticky=tk.W)
        self.Btn_Same_Address.bind('<Alt-c>', self.copy_address)
        self.Entry_Prem_Tehsil = ttk.Entry(
            self.Grid_Frame, font=self.entry_font)
        self.Entry_Prem_Tehsil.bind(
            '<KeyRelease>', lambda event: self.list_search(event, self.Tehsils_data_list, 'Prem_Tehsil'))
        self.Entry_Prem_Tehsil.bind('<FocusOut>', self.widget_lost_focus)
        self.Entry_Prem_Tehsil.bind(
            '<FocusIn>', lambda event: self.data_list.place_forget())
        self.Entry_Prem_Tehsil.bind('<Down>', self.list_get_focus)
        self.Entry_Prem_Tehsil.grid(
            column=1, row=6, padx=10, pady=10, sticky=tk.W)

        self.Entry_Prem_District = ttk.Entry(
            self.Grid_Frame, font=self.entry_font)
        self.Entry_Prem_District.bind(
            '<KeyRelease>', lambda event: self.list_search(event, self.Districts_data_list, 'Prem_District'))
        self.Entry_Prem_District.bind('<FocusOut>', self.widget_lost_focus)
        self.Entry_Prem_District.bind(
            '<FocusIn>', lambda event: self.data_list.place_forget())
        self.Entry_Prem_District.bind('<Down>', self.list_get_focus)
        self.Entry_Prem_District.grid(
            column=3, row=6, padx=10, pady=10, sticky=tk.W)
        self.List_Prem_Province = tk.Listbox(
            self.Grid_Frame, selectmode='single', exportselection=0, height=1, font=self.list_font)
        self.List_Prem_Province.insert(1, "Azad Jammu and Kashmir")
        self.List_Prem_Province.insert(2, "Balochistan")
        self.List_Prem_Province.insert(3, "Federal Govt")
        self.List_Prem_Province.insert(4, "Gilgit-Baltistan")
        self.List_Prem_Province.insert(5, "Khyber Pakhtunkhwa")
        self.List_Prem_Province.insert(6, "Punjab")
        self.List_Prem_Province.insert(7, "Sindh")
        self.List_Prem_Province.bind('<KeyPress>', self.select_keysym_value)
        self.List_Prem_Province.bind(
            '<FocusIn>', lambda event: self.data_list.place_forget())
        self.List_Prem_Province.grid(
            column=5, row=6, padx=10, pady=10, sticky=tk.W)

        self.Entry_Permenant_Address = ttk.Entry(
            self.Grid_Frame, width=60, font=self.entry_font)
        self.Entry_Permenant_Address.bind(
            '<FocusIn>', lambda event: self.data_list.place_forget())
        self.Entry_Permenant_Address.grid(
            column=1, row=8, columnspan=4, padx=10, pady=10, sticky=tk.W)
        self.Btn_Add_Dis = ttk.Button(
            self.Grid_Frame, text='Set District', command=self.set_district)
        self.Btn_Add_Dis.grid(
            column=4, row=8, padx=10, pady=10, sticky=tk.W)
        self.Entry_Pre_Tehsil.insert(0, 'Islamabad')
        self.Entry_Pre_District.insert(0, 'Islamabad ICT')

        self.List_Gender = tk.Listbox(
            self.Grid_Frame, exportselection=0, height=1, font=self.list_font)
        self.List_Gender.insert(1, "Male")
        self.List_Gender.insert(2, "Female")
        self.List_Gender.insert(3, "Widow")
        self.List_Gender.grid(
            column=1, row=9, padx=10, pady=10, sticky=tk.W)
        self.List_Gender.bind('<KeyPress>', self.select_keysym_value)
        self.List_Religion = tk.Listbox(
            self.Grid_Frame, exportselection=0, height=1, font=self.list_font)
        self.List_Religion.insert(1, 'Islam')
        self.List_Religion.insert(2, 'Christanity')
        self.List_Religion.insert(3, 'Hindu')
        self.List_Religion.insert(4, 'Other')
        self.List_Religion.grid(
            column=3, row=9, padx=10, pady=10, sticky=tk.W)
        self.List_Religion.select_set(0)
        self.List_Religion.bind('<KeyPress>', self.select_keysym_value)
        self.Religion_list = ['Islam', 'Christanity', 'Hindu', 'Other']
        self.List_Marital_status = tk.Listbox(
            self.Grid_Frame, exportselection=0, height=1, font=self.list_font)
        self.List_Marital_status.insert(1, 'Single')
        self.List_Marital_status.insert(2, 'Married')
        self.List_Marital_status.insert(3, 'Widow')
        self.List_Marital_status.insert(4, 'Divorced')
        self.List_Marital_status.grid(
            column=5, row=9, padx=10, pady=10, sticky=tk.W)
        self.List_Marital_status.bind('<KeyPress>', self.select_keysym_value)
        self.Qualification = tk.Listbox(
            self.Grid_Frame,  exportselection=0, height=1, font=self.list_font)
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
        self.Qualification.select_set(7)
        self.Qualification.see(7)
        self.Qualification.bind('<KeyPress>', self.select_keysym_value)
        # 1;Govt Employee;3;Own Business;4;Student;5;Other;6;House Wife;7;Private Job
        self.List_Occupation = tk.Listbox(
            self.Grid_Frame, exportselection=0, height=1, font=self.list_font)
        self.List_Occupation.insert(1, 'Govt. Employee')
        self.List_Occupation.insert(2, 'Not Available')
        self.List_Occupation.insert(3, 'Own Business')
        self.List_Occupation.insert(4, 'Student')
        self.List_Occupation.insert(5, 'Other')
        self.List_Occupation.insert(6, 'House Wife')
        self.List_Occupation.insert(7, 'Private Job')
        self.List_Occupation.grid(
            column=3, row=10, padx=10, pady=10, sticky=tk.W)
        self.List_Occupation.select_set(6)
        self.List_Occupation.see(6)
        self.List_Occupation.bind('<KeyPress>', self.select_keysym_value)

        self.List_Process_Type = tk.Listbox(
            self.Grid_Frame, exportselection=0, height=1, font=self.list_font)
        self.List_Process_Type.insert(1, 'Normal')
        self.List_Process_Type.insert(2, 'Urgent')
        self.List_Process_Type.grid(
            column=5, row=10, padx=10, pady=10, sticky=tk.W)
        self.List_Process_Type.bind('<KeyPress>', self.select_keysym_value)

        self.Process_List = ['Normal', 'Urgent']
        self.List_Request_Type = tk.Listbox(
            self.Grid_Frame, exportselection=0, height=1, font=self.list_font)
        self.List_Request_Type.insert(1, 'New')
        self.List_Request_Type.insert(2, 'Revised')
        self.List_Request_Type.insert(3, 'Duplicate')
        self.List_Request_Type.grid(
            column=1, row=11, padx=10, pady=10, sticky=tk.W)
        self.List_Request_Type.bind('<KeyPress>', self.select_keysym_value)

        self.List_Application_Type = tk.Listbox(
            self.Grid_Frame, exportselection=0, height=1, font=self.list_font)
        self.List_Application_Type.insert(1, 'Self')
        self.List_Application_Type.insert(2, 'Brother')
        self.List_Application_Type.grid(
            column=3, row=11, padx=10, pady=10, sticky=tk.W)
        self.List_Application_Type.bind('<KeyPress>', self.select_keysym_value)

        self.List_Service_Type = tk.Listbox(
            self.Grid_Frame, exportselection=0, height=1, font=self.list_font)
        self.List_Service_Type.insert(1, 'Offline')
        self.List_Service_Type.insert(2, 'Online')
        self.List_Service_Type.grid(
            column=5, row=11, padx=10, pady=10, sticky=tk.W)
        self.List_Service_Type.bind('<KeyPress>', self.select_keysym_value)

        self.List_Pyament_Type = tk.Listbox(
            self.Grid_Frame, exportselection=0, height=1, font=self.list_font)
        self.List_Pyament_Type.insert(1, 'Cash')
        self.List_Pyament_Type.insert(2, 'Challan')
        self.List_Pyament_Type.grid(
            column=1, row=12, padx=10, pady=10, sticky=tk.W)
        self.List_Pyament_Type.bind('<KeyPress>', self.select_keysym_value)
        # AC (Saddar);AC (Industrial Area);AC (Shalimar)
        self.List_Approver = tk.Listbox(
            self.Grid_Frame, exportselection=0, height=1, font=self.list_font)
        self.List_Approver.insert(0, 'AC (Saddar)')
        self.List_Approver.insert(1, 'AC (I/A)')
        self.List_Approver.insert(2, 'AC (Shalimar)')
        self.List_Approver.insert(3, 'AC (Rural)')
        self.List_Approver.grid(
            column=3, row=12, padx=10, pady=10, sticky=tk.W)
        self.List_Approver.bind('<KeyPress>', self.select_keysym_value)
        # Check Buttons
        self.Approver_List = ['AC (Saddar)', 'AC (I/A)',
                              'AC (Shalimar)', 'AC (Rural)']
        self.Lbl_purpose = ttk.Label(self.Grid_Frame, text='Purpuse', font=self.label_font).grid(
            column=4, row=12, padx=10, pady=10, sticky=tk.W)
        self.Entry_purpuse = ttk.Entry(self.Grid_Frame, font=self.entry_font)
        self.Entry_purpuse.grid(column=5, row=12, padx=10, pady=10, sticky=tk.W)

        self.cnic_front = IntVar(self)
        self.cnic_back = IntVar(self)
        self.cnic_guardian = IntVar(self)
        self.form_b = IntVar(self)
        self.domicile_of_guardian = IntVar(self)
        self.noc_from_concerned_district = IntVar(self)
        self.Residance_Prof = IntVar(self)
        self.utility_bill = IntVar(self)
        self.educational_certificate = IntVar(self)
        self.marriage_registration_certificate = IntVar(self)
        self.affidavit_voterlist = IntVar(self)
        self.affidavit_domicile = IntVar(self)
        self.voter_list = IntVar(self)
        self.domicile_challan = IntVar(self)
        self.theme_style.configure('TCheckbutton', font=self.check_font)
        self.chkfront = ttk.Checkbutton(self.Bottom_Frame, text="CNIC Front",
                                        variable=self.cnic_front, onvalue=-1, offvalue=0)
        self.chkfront.grid(column=0, row=1, padx=10, pady=5, sticky=tk.W)

        self.chkback = ttk.Checkbutton(self.Bottom_Frame, text="CNIC Back",
                                       variable=self.cnic_back, onvalue=-1, offvalue=0)
        self.chkback.grid(column=1, row=1, padx=10, pady=5, sticky=tk.W)

        self.chkguardian = ttk.Checkbutton(self.Bottom_Frame, text="CNIC Guardian",
                                           variable=self.cnic_guardian, onvalue=-1, offvalue=0)
        self.chkguardian.grid(column=2, row=1, padx=10, pady=5, sticky=tk.W)

        self.chkformb = ttk.Checkbutton(self.Bottom_Frame, text="Form B",
                                        variable=self.form_b, onvalue=-1, offvalue=0)
        self.chkformb.grid(column=3, row=1, padx=10, pady=5, sticky=tk.W)
        self.chkdomguardian = ttk.Checkbutton(self.Bottom_Frame, text="Domicile of Guardian",
                                              variable=self.domicile_of_guardian, onvalue=-1, offvalue=0)
        self.chkdomguardian.grid(column=4, row=1, padx=10, pady=5, sticky=tk.W)
        self.chknoc = ttk.Checkbutton(self.Bottom_Frame, text="NOC",
                                      variable=self.noc_from_concerned_district, onvalue=-1, offvalue=0)
        self.chknoc.grid(column=5, row=1, padx=10, pady=5, sticky=tk.W)

        self.chkResidance_Prof = ttk.Checkbutton(self.Bottom_Frame, text="Residance Prof",
                                                 variable=self.Residance_Prof, onvalue=-1, offvalue=0)
        self.chkResidance_Prof.grid(
            column=6, row=1, padx=10, pady=5, sticky=tk.W)
        self.chkutility_bill = ttk.Checkbutton(self.Bottom_Frame, text="Utility Bill",
                                               variable=self.utility_bill, onvalue=-1, offvalue=0)
        self.chkutility_bill.grid(
            column=0, row=2, padx=10, pady=5, sticky=tk.W)
        self.chkeducer = ttk.Checkbutton(self.Bottom_Frame, text="Educational Certifiate",
                                         variable=self.educational_certificate, onvalue=-1, offvalue=0)
        self.chkeducer.grid(column=1, row=2, padx=10, pady=5, sticky=tk.W)

        self.chkmrc = ttk.Checkbutton(self.Bottom_Frame, text="Marriage Certifiate",
                                      variable=self.marriage_registration_certificate, onvalue=-1, offvalue=0)
        self.chkmrc.grid(column=2, row=2, padx=10, pady=5, sticky=tk.W)

        self.chkaffvotlst = ttk.Checkbutton(self.Bottom_Frame, text="Affidavit Voterlist",
                                            variable=self.affidavit_voterlist, onvalue=-1, offvalue=0)
        self.chkaffvotlst.grid(column=3, row=2, padx=10, pady=5, sticky=tk.W)

        self.chkaffdom = ttk.Checkbutton(self.Bottom_Frame, text="Affidavit Domicile",
                                         variable=self.affidavit_domicile, onvalue=-1, offvalue=0)
        self.chkaffdom.grid(column=4, row=2, padx=10, pady=5, sticky=tk.W)

        self.chkvlist = ttk.Checkbutton(self.Bottom_Frame, text="Voter List",
                                        variable=self.voter_list, onvalue=-1, offvalue=0)
        self.chkvlist.grid(column=5, row=2, padx=10, pady=5, sticky=tk.W)

        self.chkdomch = ttk.Checkbutton(self.Bottom_Frame, text="Domicile Challan",
                                        variable=self.domicile_challan, onvalue=-1, offvalue=0)
        self.chkdomch.grid(column=6, row=2, padx=10, pady=5, sticky=tk.W)
        self.Add_Ch_button = ttk.Button(
            self.Status_Frame, width=15, text='Add Childerns', command=self.add_Childerns)
        self.Add_Ch_button.grid(column=1, row=1, padx=10, pady=10)

        self.save_button = ttk.Button(
            self.Status_Frame, width=15, text='Save', command=self.save)
        self.save_button.grid(column=2, row=1, padx=10, pady=10)
        # blank_label4 = Label(self.Status_Frame, width=20).grid(column=4, row=1)
        self.edit_Button = ttk.Button(
            self.Status_Frame, text='Edit', width=15, command=self.edit)
        self.edit_Button.grid(column=3, row=1, padx=10, pady=10)
        self.Collection_Report_Button = ttk.Button(
            self.Status_Frame, text='Collection Report', width=18, command=self.collection_report)
        self.Collection_Report_Button.grid(column=4, row=1, padx=10, pady=10)
        # blank_label4 = Label(self.Status_Frame, width=20).grid(column=6, row=1)
        self.Monthly_Report_Button = ttk.Button(
            self.Status_Frame, width=18, text='Monthly Report', command=self.monthly_report)
        self.Monthly_Report_Button.grid(column=5, row=1, padx=10, pady=10)
        # self.Temp_save_button = ttk.Button(
        #     self.Status_Frame, width=15, text='Temp Save', command=temp_save)
        # self.Temp_save_button.grid(column=6, row=1, padx=10, pady=10)
        # self.Temp_load_button = ttk.Button(
        #     self.Status_Frame, width=15, text='Temp Load', command=temp_load)
        # self.Temp_load_button.grid(column=7, row=1, padx=10, pady=10)
        self.Pic_button = ttk.Button(
            self.Status_Frame, width=15, text='Show History', command=self.show_history)
        self.Pic_button.grid(column=8, row=1, padx=10, pady=10)
        self.Exit_button = ttk.Button(
            self.Status_Frame, width=15, text='Exit', command=self.destroy)
        self.Exit_button.grid(column=9, row=1, padx=10, pady=10)
        self.List_Process_Type.select_set(0)
        self.List_Request_Type.select_set(0)
        self.List_Application_Type.select_set(0)
        self.List_Service_Type.select_set(0)
        self.List_Pyament_Type.select_set(0)
        self.List_Approver.select_set(0)
        self.List_Pres_Province.select_set(2)
        self.List_Prem_Province.select_set(2)

        con, cur = open_con(True)
        
        if type(cur) is str:
            messagebox.showerror('Db Connection Error', con)            
        con1, cur1 = open_con(False)
        cur.execute(
            "Select * from Tehsils;")
        self.Tehsils_data_dict = cur.fetchall()
        cur1.execute(
            "Select Teh_name from Tehsils;")
        # self.Tehsil_data_dict = dict(self.Tehsils_data)
        self.Tehsils_data_list = cur1.fetchall()
        cur.execute(
            "Select * from Districts;")
        self.Districts_data_dict = cur.fetchall()
        cur1.execute(
            "Select Dis_Name from Districts;")
        self.Districts_data_list = cur1.fetchall()
        # self.District_data_dict = dict(self.Districts_data)
        cur1.close()
        con1.close()
        cur.close()
        con.close()

        # self.Tehsil_List = list(self.Tehsil_data_dict.keys())
        # self.Tehsil_values = list(self.Tehsil_data_dict.values())
        # Tehsil_Keys = list(self.Tehsil_data_dict.keys())
        self.Province_List = ['Azad Jammu and Kashmir', 'Balochistan', 'Federal Govt',
                              'Gilgit-Baltistan', 'Khyber Pakhtunkhwa', 'Punjab', 'Sindh']
        self.Province_Keys = [694, 491, 663, 666, 1, 167, 344]

        # self.District_List = list(self.District_data_dict.keys())
        # self.District_values = list(self.District_data_dict.values())
        self.List_Pres_Province.select_set(2)
        self.List_Pres_Province.see(2)
        self.List_Prem_Province.select_set(2)
        self.List_Prem_Province.see(2)
        self.Entry_CNIC.focus()
        # self.Entry_First_Name.insert(0, 'Hamid shah')
        # self.Entry_Father_Name.insert(0, 'Jahangir shah')
        # self.Entry_Date_of_Birth.insert(0, '1982-06-05')
        # self.Entry_Arrival_Date.insert(0, '1982-06-05')
        # self.Entry_Pre_Tehsil.insert(0, 'Islamabad')
        # self.Entry_Pre_District.insert(0, 'Islamabad ICT')
        # self.Entry_Prem_Tehsil.insert(0, 'Islamabad')
        # self.Entry_Prem_District.insert(0, 'Islamabad ICT')
        # self.Entry_Pre_Tehsil.insert(0, Tehsil_txt)
        self.List_Prem_Province.bind('<FocusOut>', self.check_selection)
        self.List_Pres_Province.bind('<FocusOut>', self.check_selection)
        self.List_Gender.bind('<FocusOut>', self.check_selection)
        self.List_Religion.bind('<FocusOut>', self.check_selection)
        self.List_Marital_status.bind('<FocusOut>', self.check_selection)
        self.Qualification.bind('<FocusOut>', self.check_selection)
        self.List_Occupation.bind('<FocusOut>', self.check_selection)
        self.List_Process_Type.bind('<FocusOut>', self.check_selection)
        self.List_Request_Type.bind('<FocusOut>', self.check_selection)
        self.List_Application_Type.bind('<FocusOut>', self.check_selection)
        self.List_Service_Type.bind('<FocusOut>', self.check_selection)
        self.List_Pyament_Type.bind('<FocusOut>', self.check_selection)
        self.List_Approver.bind('<FocusOut>', self.check_selection)
        self.data_list.bind('<FocusOut>', self.check_selection)

    def collection_report(self):
        obj = Collection_Report()
        obj.mainloop()

    def monthly_report(self):
        obj1 = Monthly_Report()
        obj1.mainloop()

    def copy_address(self, *args):
        self.Entry_Prem_Tehsil.delete(0, 'end')
        self.Entry_Prem_District.delete(0, 'end')
        self.Entry_Prem_Tehsil.insert(0, self.Entry_Pre_Tehsil.get())
        self.Entry_Prem_District.insert(0, self.Entry_Pre_District.get())
        self.Entry_Permenant_Address.delete(0, 'end')
        self.Entry_Permenant_Address.insert(
            0, self.Entry_Present_Address.get())
        self.List_Prem_Province.select_set(2)
        self.List_Prem_Province.see(2)

    def search_dict(self, dict_data_set, key_for_search, value, return_key):
        result = None
        for i in range(len(dict_data_set)):
            if dict_data_set[i][key_for_search] == value:
                result = dict_data_set[i][return_key]
                break

        return result

    def set_district(self):
        if len(self.Entry_Prem_Tehsil.get()) == 0 or len(self.Entry_Prem_District.get()) == 0:
            return messagebox.showerror('Error', 'No Data to Set')
        self.prem_District_id = self.search_dict(
            self.Districts_data_dict, 'Dis_Name', self.Entry_Prem_District.get().strip(), 'ID')
        if self.prem_District_id == 'None':
            messagebox.showerror(
                'showerror', 'Incorrect Spellings for Permanent District')
            return 'invalid'
        con, cur = open_con(False)
        Query = "Update tehsils set Dis_Id = %s Where Teh_name = %s;"
        parm_list = [self.prem_District_id, self.Entry_Prem_Tehsil.get()]
        cur.execute(Query, parm_list)
        con.commit()

        position = self.Province_List.index(self.List_Prem_Province.get(
            self.List_Prem_Province.curselection()))
        pro_id = self.Province_Keys[position]

        Query = "Update districts set Pro_Id = %s Where Dis_Name = %s;"
        parm_list = [pro_id, self.Entry_Prem_District.get()]
        cur.execute(Query, parm_list)
        con.commit()
        cur.close()
        con.close()

    def check_selection(self, event):
        if len(event.widget.curselection()) > 1:
            messagebox.showerror('Error', 'Please recheck selection')



    def check_dup_cnic(self, **kwargs):
        if self.edit_mode == TRUE:
            return
        cnic = kwargs['cnic']
        cnic = cnic.strip()
        if len(cnic.strip()) == 0:
            return 'Zero Lenth'
        elif len(cnic) == 13:
            if cnic.isnumeric() == FALSE:
                messagebox.showerror('showerror', 'CNIC is not numeric')
                return 'CNIC is not numeric'
        else:
            messagebox.showerror('showerror', 'CNIC is not 13 digit')
            return

        Query = "Select CNIC from domicile where CNIC = %s;"
        con, cur = open_con(False)
        cur.execute(Query, [cnic])
        data = cur.fetchall()
        if len(data) != 0:

            messagebox.showerror('showerror', 'CNIC already exist')
            cur.close()
            con.close()
            return 'CNIC already exist'
        
        Query = "Select CNIC from cancellation where CNIC = %s;"
        con, cur = open_con(False)
        cur.execute(Query, [cnic])
        data = cur.fetchall()
        if len(data) != 0:
            messagebox.showerror('Domicile Cancelled', 'Applicant Domicil has been cancelled')
            cur.close()
            con.close()
            
        return 'CNIC donot exist'


    def update_arrival(self, event):
        self.Entry_Arrival_Date.delete(0, 'end')
        self.Entry_Arrival_Date.insert(0, self.Entry_Date_of_Birth.get())

    def upload_pic(self):
        file = askopenfile(mode='rb', filetypes=[
                           ('Picture Files', '*.png, *.jpeg, *.jpg')])
        if file is not None:
            self.binaryfile = file.read()
            file.close
        else:
            self.binaryfile is None

    def export_selection(self, event):
        if len(self.data_list.curselection()) > 1:
            return
        self.data_list.place_forget()
        if self.widget_name == 'Pre_Tehsil':
            self.Entry_Pre_Tehsil.delete(0, 'end')
            self.Entry_Pre_Tehsil.insert(0, self.data_list.get(
                self.data_list.curselection()))

            self.Entry_Pre_District.focus()
        elif self.widget_name == 'Pre_District':
            self.Entry_Pre_District.delete(0, 'end')
            self.Entry_Pre_District.insert(
                0, self.data_list.get(self.data_list.curselection()))
            self.List_Pres_Province.focus()
        elif self.widget_name == 'Prem_Tehsil':
            self.Entry_Prem_Tehsil.delete(0, 'end')
            self.Entry_Prem_Tehsil.insert(0, self.data_list.get(
                self.data_list.curselection()))
            if self.get_district_province(self.data_list.get(self.data_list.curselection())) is None:
                self.Entry_Prem_District.focus()
            else:
                self.Entry_Permenant_Address.focus()
        elif self.widget_name == 'Prem_District':
            self.Entry_Prem_District.delete(0, 'end')
            self.Entry_Prem_District.insert(
                0, self.data_list.get(self.data_list.curselection()))
            self.List_Prem_Province.focus()
        self.data_list.delete(0, 'end')

    def widget_lost_focus(self, event):
        self.widget_focus = False

    def list_get_focus(self, event):
        self.data_list.focus()
        self.data_list.select_set(0)
        self.data_list.see(0)

    def get_district_province(self, teh_name):
        dis_id = self.search_dict(
            self.Tehsils_data_dict, 'Teh_name', teh_name, 'Dis_Id')
        print(dis_id)
        if dis_id is None:
            return None
        dis_text = self.search_dict(
            self.Districts_data_dict, 'ID', dis_id, 'Dis_Name')
        pro_id = self.search_dict(
            self.Districts_data_dict, 'ID', dis_id, 'Pro_Id')
        if pro_id is not None:
            Prov_indx = self.Province_Keys.index(pro_id)
        self.Entry_Prem_District.delete(0, 'end')
        self.Entry_Prem_District.insert(0, dis_text)
        self.List_Prem_Province.selection_clear(0, 'end')
        self.List_Prem_Province.select_set(Prov_indx)
        self.List_Prem_Province.see(Prov_indx)
        return 'ok'

    def list_search(self, event, data, w_name):
        self.widget_name = w_name
        # Exempted keys upon which no action would be taken

        if event.keysym == "BackSpace" or event.keysym == "Tab" or event.keysym == "Enter":
            return
        elif event.keysym == "Space":
            return
        elif event.keysym[0:5] == "Shift":
            return

        # checking, atleast one character to serach list
        if self.widget_focus == False:
            self.data_list.place(x=event.widget.winfo_x(),
                                 y=event.widget.winfo_y()+event.widget.winfo_height())
            self.data_list.lift()
            self.widget_focus = True
        if event.widget.get():
            txt_lenth = len(event.widget.get())
            filtered = filter(lambda dat: dat[0][:txt_lenth].upper(
            ) == event.widget.get().upper(), data)
            filtered_list = list(filtered)
            self.data_list.delete(0, 'end')
            i = 0
            for item in filtered_list:
                self.data_list.insert(i, item[0])
                i += 1
                # if len(filtered_list) != 0:
            #     event.widget.delete(0, END)
            #     event.widget.insert(0, filtered_list[0][0])
            #     event.widget.selection_range(txt_lenth, 'end')

            #     self.List_Teh_Dist.delete(0, 'end')
            #     lp = 0
            #     for item in filtered_list:
            #         if lp > 5:
            #             break
            #         self.List_Teh_Dist.insert(lp, item[0])
            #         lp += 1
            #     self.List_Teh_Dist.grid(row=4, column=1, rowspan=4)
            # else:
            #     self.List_Teh_Dist.forget()
            # for dat in data:
            #     txt_lenth = len(event.widget.get())
            #     if dat[0][:txt_lenth].upper() == event.widget.get().upper():
            #         event.widget.delete(0, END)
            #         event.widget.insert(0, dat[0])
            #         event.widget.selection_range(txt_lenth, 'end')
            #         break

    def select_keysym_value(self, event):

        for itm in range(event.widget.size()):
            if event.keysym.upper() == event.widget.get(itm)[:1]:
                event.widget.selection_clear(0, END)
                event.widget.select_set(itm)
                event.widget.see(itm)
                event.widget.activate(itm)
                break

                # if event.keysym in self.List_Prem_Province.:
            #     messagebox.showinfo('showinfo', 'a found')

                # blank_label1 = Label(self.Status_Frame, width=20).grid(column=0, row=1)
    def Columns_dict(self):

        con, cur = open_con(True)
        cur.execute("SHOW COLUMNS FROM domicile;")
        data = cur.fetchall()
        cur.close()
        cur.close()
        con.close()
        my_dict = {}
        for row in data:
            my_dict[row['Field']] = ''

        return my_dict

    def edit(self):
        self.Record_Selector()
        if self.rec_id is None:
            return messagebox.showerror('Error', 'Nothing Selected')
        if self.rec_id == 0:
            return messagebox.showerror('Error', 'Nothing Selected')
        self.edit_mode = TRUE
        self.save_button.configure(text='Update')
        self.Add_Ch_button.configure(text='Edit Childerns')
        self.old_CNIC = self.Entry_CNIC.get()

        con, cur = open_con(True)
        Query = "Select * from Domicile Where Dom_id = %s;"
        cur.execute(Query, [self.rec_id])
        data = cur.fetchall()
        Query = "Select * from childern where father_cnic = %s order by child_dob asc;"
        cur.execute(Query, [data[0]['CNIC']])
        self.child_old_data = cur.fetchall()
        cur.close()
        con.close()

        if len(data) != 0:
            self.edit_mode = TRUE
            self.save_button.config(text='Update')
            self.Add_Ch_button.config(text='Edit Childerns')
            for row in data:
                self.Entry_CNIC.delete(0, 'end')
                self.Entry_CNIC.insert(0, row['CNIC'])
                self.Entry_First_Name.delete(0, 'end')
                self.Entry_First_Name.insert(0, str(row['First_Name']))
                # self.Entry_Last_Name.delete(0, 'end')
                # self.Entry_Last_Name.insert(0, str(row['Last_Name']))
                self.Entry_Father_Name.delete(0, 'end')
                self.Entry_Father_Name.insert(0, row['Father_Name'])

                self.Entry_Spouse_Name.delete(0, 'end')
                self.Entry_Spouse_Name.insert(
                    0, str(row['Spouse_Name']))

                self.Entry_Contact.delete(0, 'end')
                self.Entry_Contact.insert(0, row['Contact'])

                self.Entry_Placeofbirth.delete(0, 'end')
                self.Entry_Placeofbirth.insert(
                    0, row['Placeofbirth'])

                self.Entry_Date_of_Birth.delete(0, 'end')
                self.Entry_Date_of_Birth.insert(
                    0, row['Date_of_Birth'])
                self.Entry_Arrival_Date.delete(0, 'end')
                self.Entry_Arrival_Date.insert(
                    0, row['Arrival_Date'])

                # Getting Tehsil and District Lists from db
                # self.Tehsil_values = list(
                #     self.Tehsil_data_dict.values())
                # self.District_values = list(
                #     self.District_data_dict.values())
                
                Tehsil_txt = self.search_dict(
                    self.Tehsils_data_dict, 'ID', row['Pres_Tehsil'], 'Teh_name')
                District_txt = self.search_dict(
                    self.Districts_data_dict, 'ID', row['Pres_District'], 'Dis_Name')
                self.Entry_Pre_Tehsil.delete(0, 'end')
                self.Entry_Pre_Tehsil.insert(0, Tehsil_txt)

                self.Entry_Pre_District.delete(0, 'end')
                self.Entry_Pre_District.insert(0, District_txt)

                # self.List_Pres_Province.delete(0, 'end')
                self.List_Pres_Province.selection_clear(0, 'end')
                self.List_Pres_Province.select_set(
                    self.Province_Keys.index(int(row['Pres_Province'])))
                self.List_Pres_Province.see(
                    self.Province_Keys.index(int(row['Pres_Province'])))

                self.Entry_Present_Address.delete(0, 'end')
                self.Entry_Present_Address.insert(
                    0, row['Present_Address'])

                Tehsil_txt = self.search_dict(
                    self.Tehsils_data_dict, 'ID', row['Perm_Tehsil'], 'Teh_name')
                District_txt = self.search_dict(
                    self.Districts_data_dict, 'ID', row['Perm_District'], 'Dis_Name')
                self.Entry_Prem_Tehsil.delete(0, 'end')
                self.Entry_Prem_Tehsil.insert(0, Tehsil_txt)
                self.Entry_Prem_District.delete(0, 'end')
                self.Entry_Prem_District.insert(0, District_txt)

                self.List_Prem_Province.selection_clear(0, 'end')
                self.List_Prem_Province.select_set(
                    self.Province_Keys.index(int(row['Perm_Province'])))
                self.List_Prem_Province.see(
                    self.Province_Keys.index(int(row['Perm_Province'])))
                self.Entry_Permenant_Address.delete(0, 'end')
                self.Entry_Permenant_Address.insert(
                    0, row['Permenant_Address'])

                self.List_Gender.selection_clear(0, 'end')
                self.List_Gender.select_set(int(row['Gender'])-1)
                self.List_Gender.see(int(row['Gender'])-1)

                self.List_Religion.selection_clear(0, 'end')
                self.List_Religion.select_set(
                    int(self.Religion_list.index(row['Religon'])))
                self.List_Religion.see(
                    int(self.Religion_list.index(row['Religon'])))

                self.List_Marital_status.selection_clear(0, 'end')
                self.List_Marital_status.select_set(
                    int(row['Marital_Status'])-1)
                self.List_Marital_status.see(
                    int(row['Marital_Status']-1))

                self.Qualification.selection_clear(0, 'end')
                self.Qualification.select_set(
                    int(row['Qualification'])-1)
                self.Qualification.see(
                    int(row['Qualification'])-1)

                self.List_Occupation.selection_clear(0, 'end')
                self.List_Occupation.select_set(
                    int(row['Occupation'])-1)
                self.List_Occupation.see(
                    int(row['Occupation'])-1)

                self.List_Process_Type.selection_clear(0, 'end')
                self.List_Process_Type.select_set(
                    self.Process_List.index(row['Process_Type']))
                self.List_Process_Type.see(
                    self.Process_List.index(row['Process_Type']))

                self.List_Request_Type.selection_clear(0, 'end')
                self.List_Request_Type.select_set(
                    self.List_Request_Type.index(int(row['Request_Type']-1)))
                self.List_Request_Type.see(
                    self.List_Request_Type.index(int(row['Request_Type']-1)))

                self.List_Application_Type.selection_clear(0, 'end')
                self.List_Application_Type.select_set(
                    int(row['Application_Type'])-1)
                self.List_Application_Type.see(
                    int(row['Application_Type'])-1)

                self.List_Service_Type.selection_clear(0, 'end')
                self.List_Service_Type.select_set(
                    int(row['Service_Type'])-1)
                self.List_Service_Type.see(
                    int(row['Service_Type'])-1)

                self.List_Pyament_Type.selection_clear(0, 'end')
                self.List_Pyament_Type.select_set(
                    int(row['Payment_Type'])-1)
                self.List_Pyament_Type.see(
                    int(row['Payment_Type'])-1)

                self.List_Approver.selection_clear(0, 'end')
                self.List_Approver.select_set(self.Approver_List.index(
                    row['Approver_Desig']))
                self.List_Approver.see(self.Approver_List.index(
                    row['Approver_Desig']))
                # Check Buttons
                self.Entry_purpuse.delete(0, 'end')
                self.Entry_purpuse.insert(0, str(row['Purpuse']))

                self.cnic_front.set(row['cnic_front'])
                self.cnic_back.set(row['cnic_back'])
                self.cnic_guardian.set(row['cnic_guardian'])
                self.form_b.set(row['form_b'])
                self.domicile_of_guardian.set(
                    row['domicile_of_guardian'])
                self.noc_from_concerned_district.set(
                    row['noc_from_concerned_district'])
                self.Residance_Prof.set(row['Residance_Prof'])
                self.utility_bill.set(row['utility_bill'])
                self.educational_certificate.set(
                    row['educational_certificate'])
                self.marriage_registration_certificate.set(
                    row['marriage_registration_certificate'])
                self.affidavit_voterlist.set(row['affidavit_voterlist'])
                self.affidavit_domicile.set(row['affidavit_domicile'])
                self.voter_list.set(row['voter_list'])
                self.domicile_challan.set(row['domicile_challan'])
        else:
            messagebox.showerror('showerror', 'Record Not Found')

    def clear_widgets(self):
        self.Entry_CNIC.delete(0, 'end')
        self.Entry_First_Name.delete(0, 'end')
        # self.Entry_Last_Name.delete(0, 'end')
        self.Entry_Father_Name.delete(0, 'end')
        self.Entry_Spouse_Name.delete(0, 'end')
        self.Entry_Contact.delete(0, 'end')
        self.Entry_Contact.insert(0, '00000000000')
        self.Entry_Placeofbirth.delete(0, 'end')
        self.Entry_Placeofbirth.insert(0, 'ISLAMABAD')
        self.Entry_Date_of_Birth.delete(0, 'end')
        self.Entry_Arrival_Date.delete(0, 'end')
        self.Entry_Pre_Tehsil.delete(0, 'end')
        self.Entry_Pre_Tehsil.insert(0, 'Islamabad')
        self.Entry_Pre_District.delete(0, 'end')
        self.Entry_Pre_District.insert(0, 'Islamabad ICT')
        # self.List_Pres_Province.selection_clear(0, END)
        self.Entry_Present_Address.delete(0, 'end')
        self.Entry_Prem_Tehsil.delete(0, 'end')
        self.Entry_Prem_District.delete(0, 'end')
        # self.List_Prem_Province.selection_clear(0, END)
        self.Entry_Permenant_Address.delete(0, 'end')
        self.List_Gender.selection_clear(0, END)
        self.List_Religion.selection_clear(0, END)
        self.List_Marital_status.selection_clear(0, END)
        self.Qualification.selection_clear(0, END)
        self.List_Occupation.selection_clear(0, END)
        # self.List_Process_Type.selection_clear(0, END)
        # self.List_Request_Type.selection_clear(0, END)
        # self.List_Application_Type.selection_clear(0, END)
        # self.List_Service_Type.selection_clear(0, END)
        # self.List_Pyament_Type.selection_clear(0, END)
        # self.List_Approver.selection_clear(0, END)
        self.cnic_front.set(0)
        self.cnic_back.set(0)
        self.cnic_guardian.set(0)
        self.form_b.set(0)
        self.domicile_of_guardian.set(0)
        self.noc_from_concerned_district.set(0)
        self.Residance_Prof.set(0)
        self.utility_bill.set(0)
        self.educational_certificate.set(0)
        self.marriage_registration_certificate.set(0)
        self.affidavit_voterlist.set(0)
        self.affidavit_domicile.set(0)
        self.voter_list.set(0)
        self.domicile_challan.set(0)

    def temp_load(self):
        pass

    def check_validations(self):

        if len(self.Entry_CNIC.get()) == 13:
            if self.Entry_CNIC.get().isnumeric() == FALSE:
                messagebox.showerror('showerror', 'CNIC is not numeric')
                return 'invalid'

        else:

            messagebox.showerror('showerror', 'CNIC is not 13 digit')
            return 'invalid'
        if len(self.Entry_Contact.get()) != 11:
            messagebox.showerror('showerror', 'Contact is not 11 digit')
            return 'invalid'
        else:
            if self.Entry_Contact.get().isnumeric() == False:
                messagebox.showerror('showerror', 'Contact is not number')
                return 'invalid'
        input_widgets_list = [self.Entry_First_Name.get(), self.Entry_Father_Name.get(), self.Entry_Date_of_Birth.get(), self.Entry_Pre_Tehsil.get(), self.Entry_Pre_Tehsil.get(
        ), self.Entry_Pre_District.get(), self.Entry_Prem_Tehsil.get(), self.Entry_Prem_District.get(), self.Entry_Placeofbirth.get(), self.Entry_Contact.get(), self.Entry_Arrival_Date.get()]
        for item in input_widgets_list:
            if item.lower().find('update') != -1 or item.lower().find('delete') != -1 or item.lower().find('char(') != -1:
                messagebox.showerror(
                    'showerror', 'Milicouse word found in input widget')
                return 'invalid'
        if len(self.Entry_First_Name.get().strip()) == 0:
            messagebox.showerror('showerror', 'Valid Name is Mandatory')
            return 'invalid'
        if len(self.Entry_Father_Name.get().strip()) == 0:
            messagebox.showerror('showerror', 'Valid Father Name is Mandatory')
            return 'invalid'

        validation_result = Validation.validate_date(
            self.Entry_Date_of_Birth.get().strip())
        if validation_result != 'valid':
            messagebox.showerror('Error', validation_result)
            return 'invalid'
        validation_result = Validation.validate_date(
            self.Record_Date.get().strip())
        if validation_result != 'valid':
            messagebox.showerror('Error', validation_result)
            return 'invalid'

        # finding present Tehsil in dictinery
        self.pre_Tehsil_id = self.search_dict(
            self.Tehsils_data_dict, 'Teh_name', self.Entry_Pre_Tehsil.get().strip(), 'ID')
        if self.pre_Tehsil_id == 'None':
            messagebox.showerror(
                'showerror', 'Incorrect Spellings for Present Tehsil')
            return 'invalid'

        self.pre_District_id = self.search_dict(
            self.Districts_data_dict, 'Dis_Name', self.Entry_Pre_District.get().strip(), 'ID')
        if self.pre_District_id == 'None':
            messagebox.showerror(
                'showerror', 'Incorrect Spellings for Present District')
            return 'invalid'

        self.prem_Tehsil_id = self.search_dict(
            self.Tehsils_data_dict, 'Teh_name', self.Entry_Prem_Tehsil.get().strip(), 'ID')
        if self.prem_Tehsil_id == 'None':
            messagebox.showerror(
                'showerror', 'Incorrect Spellings for Permanent Tehsil')
            return 'invalid'

        self.prem_District_id = self.search_dict(
            self.Districts_data_dict, 'Dis_Name', self.Entry_Prem_District.get().strip(), 'ID')
        if self.prem_District_id == 'None':
            messagebox.showerror(
                'showerror', 'Incorrect Spellings for Permanent District')
            return 'invalid'

        # validating Lists
        self.pres_Province_id = 0

        if len(self.List_Pres_Province.curselection()) != 0:

            position = self.Province_List.index(self.List_Pres_Province.get(
                self.List_Pres_Province.curselection()))
            self.pres_Province_id = self.Province_Keys[position]
        else:
            messagebox.showerror('showerror', 'Select Temp Province from List')
            return 'invalid'

        self.prem_Province_id = 0
        if len(self.List_Prem_Province.curselection()) != 0:
            position = self.Province_List.index(self.List_Prem_Province.get(
                self.List_Prem_Province.curselection()))
            self.prem_Province_id = self.Province_Keys[position]
        else:
            messagebox.showerror(
                'showerror', 'Select Permenant Province from List')
            return 'invalid'

        if len(self.List_Gender.curselection()) != 0:
            self.Gender_Id = self.List_Gender.index(
                self.List_Gender.curselection()) + 1
        else:
            messagebox.showerror('showerror', 'Select Gender from List')
            return 'invalid'
        if len(self.List_Religion.curselection()) != 0:
            self.Religion = self.List_Religion.get(
                self.List_Religion.curselection())
        else:
            messagebox.showerror('showerror', 'Select Religion from List')
            return 'invalid'

        if len(self.List_Marital_status.curselection()) != 0:
            self.Marital_Status_Id = self.List_Marital_status.index(
                self.List_Marital_status.curselection()) + 1
        else:
            messagebox.showerror(
                'showerror', 'Select Marital Status from List')
            return 'invalid'
        if len(self.Qualification.curselection()) != 0:
            self.Qualification_Id = self.Qualification.index(
                self.Qualification.curselection()) + 1
        else:
            messagebox.showerror('showerror', 'Select Qualification from List')
            return 'invalid'

        if len(self.List_Occupation.curselection()) != 0:
            self.Occupation_Id = self.List_Occupation.index(
                self.List_Occupation.curselection()) + 1
        else:
            messagebox.showerror('showerror', 'Select Occupation from List')
            return 'invalid'
        if len(self.List_Application_Type.curselection()) != 0:
            self.Application_Type_Id = self.List_Application_Type.index(
                self.List_Application_Type.curselection()) + 1
        else:
            messagebox.showerror(
                'showerror', 'Select Application Type from List')
            return 'invalid'
        if len(self.List_Request_Type.curselection()) != 0:
            self.Request_Type_Id = self.List_Request_Type.index(
                self.List_Request_Type.curselection()) + 1
        else:
            messagebox.showerror('showerror', 'Select Request Type from List')
            return 'invalid'
        if len(self.List_Service_Type.curselection()) != 0:
            self.Service_Type_Id = self.List_Service_Type.index(
                self.List_Service_Type.curselection()) + 1
        else:
            messagebox.showerror('showerror', 'Select Service Type from List')
            return 'invalid'
        if len(self.List_Pyament_Type.curselection()) != 0:
            self.Payment_Type_Id = self.List_Pyament_Type.index(
                self.List_Pyament_Type.curselection()) + 1
        else:
            messagebox.showerror('showerror', 'Select Payment Type from List')
            return 'invalid'
        # Dom_date, Status, CNIC, First_Name, Last_Name, Father_Name, Spouse_Name, Present_Address, Permenant_Address, Placeofbirth, Contact, Date_of_Birth, Arrival_Date, Gender, Religon, Marital_Status, Qualification, Occupation, Application_Type, Request_Type, Service_Type, Payment_Type, cnic_front, cnic_back, cnic_guardian, Residance_Prof, utility_bill, educational_certificate, marriage_registration_certificate, form_b, domicile_of_guardian, noc_from_concerned_district, affidavit_domicile, affidavit_voterlist, voter_listdomicile_challan

    def save(self):
        if self.check_validations() == 'invalid':
            return
        if self.edit_mode == TRUE:
            Query = """Update Domicile Set CNIC=%s,
                                        Dom_date=%s,
                                        First_Name=%s,
                                        Father_Name=%s,
                                        Spouse_Name=%s,
                                        Pres_Tehsil=%s,
                                        Pres_District=%s,
                                        Pres_Province=%s,
                                        Present_Address=%s,
                                        Perm_Tehsil=%s,
                                        Perm_District=%s,
                                        Perm_Province=%s,
                                        Permenant_Address=%s,
                                        Placeofbirth=%s,
                                        Contact=%s,
                                        Date_of_Birth=%s,
                                        Arrival_Date=%s,
                                        Gender=%s,
                                        Religon=%s,
                                        Marital_Status=%s,
                                        Qualification=%s,
                                        Occupation=%s,
                                        Application_Type=%s,
                                        Request_Type=%s,
                                        Service_Type=%s,
                                        Payment_Type=%s,
                                        cnic_front=%s,
                                        cnic_back=%s,
                                        cnic_guardian=%s,
                                        Residance_Prof=%s,
                                        utility_bill=%s,
                                        educational_certificate=%s,
                                        marriage_registration_certificate=%s,
                                        form_b=%s,
                                        domicile_of_guardian=%s,
                                        noc_from_concerned_district=%s,
                                        affidavit_domicile=%s,
                                        affidavit_voterlist=%s,
                                        voter_list=%s,
                                        domicile_challan=%s,
                                        Process_Type=%s,
                                        Approver_Desig=%s,
                                        Purpuse=%s Where Dom_id = %s;"""

            parm_inputs = [self.Entry_CNIC.get(), f'{datetime.today()}', self.Entry_First_Name.get(), self.Entry_Father_Name.get(), self.Entry_Spouse_Name.get(), self.pre_Tehsil_id, self.pre_District_id, self.pres_Province_id, self.Entry_Present_Address.get(), self.prem_Tehsil_id, self.prem_District_id, self.prem_Province_id, self.Entry_Permenant_Address.get(), self.Entry_Placeofbirth.get(), self.Entry_Contact.get(), self.Entry_Date_of_Birth.get(), self.Entry_Arrival_Date.get(), self.Gender_Id, self.Religion, self.Marital_Status_Id, self.Qualification_Id, self.Occupation_Id, self.Application_Type_Id, self.Request_Type_Id, self.Service_Type_Id, self.Payment_Type_Id, self.cnic_front.get(), self.cnic_back.get(), self.cnic_guardian.get(), self.Residance_Prof.get(), self.utility_bill.get(), self.educational_certificate.get(), self.marriage_registration_certificate.get(), self.form_b.get(), self.domicile_of_guardian.get(), self.noc_from_concerned_district.get(), self.affidavit_domicile.get(), self.affidavit_voterlist.get(), self.voter_list.get(), self.domicile_challan.get(), self.List_Process_Type.get(self.List_Process_Type.curselection()), self.List_Approver.get(self.List_Approver.curselection()), self.Entry_purpuse.get(), self.rec_id]
            self.child_addition_list = []
            self.child_deletion_list = []
            self.child_old_data_list = []
            for row in self.child_old_data:
                self.child_old_data_list.append(
                    list(("{}".format(row['Child_Name']), "{}".format(row['Child_dob']))))
            # Looking for deleted childerns
            for row in self.child_old_data_list:
                if row not in self.child_data_list:
                    self.child_deletion_list.append(row)
            # Lookin for added childerns
            for item in self.child_data_list:
                if item not in self.child_old_data_list:
                    self.child_addition_list.append(item)
            process = 'Update'
        else:
            dup_check_status = self.check_dup_cnic(
                cnic=self.Entry_CNIC.get().strip())

            if dup_check_status != 'CNIC donot exist':
                return messagebox.showerror('Error', dup_check_status)
             
            process = 'Save'
            Query = "Insert Into Domicile (Dom_date, Status, CNIC, First_Name, Father_Name, Spouse_Name, Pres_Tehsil, Pres_District, Pres_Province, Present_Address, Perm_Tehsil, Perm_District, Perm_Province, Permenant_Address, Placeofbirth, Contact, Date_of_Birth, Arrival_Date, Gender, Religon, Marital_Status, Qualification, Occupation, Application_Type, Request_Type, Service_Type, Payment_Type, cnic_front, cnic_back, cnic_guardian, Residance_Prof, utility_bill, educational_certificate, marriage_registration_certificate, form_b, domicile_of_guardian, noc_from_concerned_district, affidavit_domicile, affidavit_voterlist, voter_list, domicile_challan, Process_Type, Approver_Desig, Purpuse) values (%s, 'Pending', %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            parm_inputs = [self.Record_Date.get(), self.Entry_CNIC.get(), self.Entry_First_Name.get(
            ), self.Entry_Father_Name.get(), self.Entry_Spouse_Name.get(), self.pre_Tehsil_id, self.pre_District_id, self.pres_Province_id, self.Entry_Present_Address.get(), self.prem_Tehsil_id, self.prem_District_id, self.prem_Province_id, self.Entry_Permenant_Address.get(), self.Entry_Placeofbirth.get(), self.Entry_Contact.get(), self.Entry_Date_of_Birth.get(), self.Entry_Arrival_Date.get(), self.Gender_Id, self.Religion, self.Marital_Status_Id, self.Qualification_Id, self.Occupation_Id, self.Application_Type_Id, self.Request_Type_Id, self.Service_Type_Id, self.Payment_Type_Id, self.cnic_front.get(), self.cnic_back.get(), self.cnic_guardian.get(), self.Residance_Prof.get(), self.utility_bill.get(), self.educational_certificate.get(), self.marriage_registration_certificate.get(), self.form_b.get(), self.domicile_of_guardian.get(), self.noc_from_concerned_district.get(), self.affidavit_domicile.get(), self.affidavit_voterlist.get(), self.voter_list.get(), self.domicile_challan.get(), self.List_Process_Type.get(self.List_Process_Type.curselection()), self.List_Approver.get(self.List_Approver.curselection()), self.Entry_purpuse.get()]
            self.binaryfile = None
        print(f'Procceding {process}')
        con, cur = open_con(True)
        cur.execute(Query, parm_inputs)
        con.commit()
        if self.edit_mode == TRUE:
            Query = "Insert into dataentry_history (rec_id, his_status, timestamp) values (%s, 'Updated', CURRENT_TIMESTAMP);"
            cur.execute(Query, [self.rec_id])
            con.commit()
        else:
            cur.execute('Select LAST_INSERT_ID();')
            last_id = cur.fetchone()['LAST_INSERT_ID()']
            Query = "Insert into dataentry_history (rec_id, his_status, timestamp) values (%s, 'Created', CURRENT_TIMESTAMP);"
            cur.execute(Query, [last_id])
            con.commit()
        if self.edit_mode == TRUE:
            if len(self.child_addition_list) != 0:
                child_count = 0
                for items in self.child_addition_list:
                    child_count=+1
                    if len(items[1].strip()) == 0:
                        Query = "Insert into Childern (Father_CNIC, Child_Name, Child_dob) values ('{}', '{}', Null)".format(
                            self.Entry_CNIC.get(), items[0])
                    else:
                        Query = "Insert into Childern (Father_CNIC, Child_Name, Child_dob) values ('{}', '{}', '{}')".format(
                            self.Entry_CNIC.get(), items[0], items[1])
                    try:
                        cur.execute(Query)
                        con.commit()
                        print(f'Saving Childern {child_count}')
                    except Exception:
                        print(f'Error While Saving Child {child_count}')
                self.child_addition_list = []

            if len(self.child_deletion_list) != 0:
                for items in self.child_deletion_list:
                    Query = "Delete From Childern Where Father_CNIC='{}' And Child_Name='{}' And Child_dob='{}';".format(
                        self.Entry_CNIC.get(), items[0], items[1])
                    cur.execute(Query)
                    con.commit()
                self.child_deletion_list = []
        else:
            if len(self.child_data_list) != 0:
                for items in self.child_data_list:
                    
                    print('Proceeding to save childerns')
                    if len(items[1].strip()) == 0:
                        Query = "Insert into Childern (Father_CNIC, Child_Name, Child_dob) values ('{}', '{}', Null)".format(
                            self.Entry_CNIC.get(), items[0])
                    else:
                        Query = "Insert into Childern (Father_CNIC, Child_Name, Child_dob) values ('{}', '{}', '{}')".format(
                            self.Entry_CNIC.get(), items[0], items[1])

                    cur.execute(Query)
                    con.commit()
                count = 0
                for Query in self.Insert_query_list:
                    count = count +1
                    print(f"executing childern Query No. {count}")
                    # print(Query)
                    cur.execute(Query)
                    con.commit()
                self.Insert_query_list = []
            self.child_data_list = []
        cur.execute('Select dom_id from domicile order by dom_id desc limit 1;')
        last_rec = cur.fetchall()
        if self.binaryfile is not None and self.edit_mode == FALSE:
            
            cur.execute(
                "Insert Into pictures (Dom_Id, Pic) values(%s, %s)", (last_rec[0][0], self.binaryfile))
            con.commit()
            
        elif self.binaryfile is not None and self.edit_mode == TRUE:
            cur.execute(
                "Select Pic_id from pictures Where Dom_id = %s", [self.rec_id])
            data = cur.fetchall()
            if len(data) == 0:
                cur.execute(
                    "Insert Into pictures (Dom_Id, Pic) values(%s, %s)", (self.rec_id, self.binaryfile))
            else:
                cur.execute(
                    "Update pictures set Pic= %s where Dom_id = %s;", (self.binaryfile, self.rec_id))
            con.commit()

        if self.edit_mode == TRUE:
            messagebox.showinfo(
                'showinfo', 'Record No {} Updated'.format(self.rec_id))
        else:
            messagebox.showinfo(
                'showinfo', 'Record Saved with id {}'.format(last_rec[0]['dom_id']))
        self.rec_id = 0
        cur.close()
        con.close()
        self.binaryfile = None
        self.clear_widgets()
        self.edit_mode = FALSE
        self.save_button.config(text='Save')
        self.Add_Ch_button.config(text='Add Childerns')
        self.cnic_dup_check = False
    def show_history(self):
        window = Toplevel()
        window.geometry("350x400")
        label_frame = Frame(window)
        label_frame.pack(fill='x')
        main_frame = Frame(window)
        main_frame.pack(fill='both', expand=True)
        top_label = Label(label_frame, text='History', anchor='center', font=('Courier', 14))
        top_label.pack(fill='x')
        his_list = Listbox(main_frame, height=20, width=80, exportselection=0, font=('Courier', 14))
        his_list.grid(row=0, column=0)
        if self.rec_id is None: 
            pass
        elif self.rec_id ==0:
            pass
        else:
            con, cur = open_con(True)
            if type(cur) is str:
                return messagebox.showerror('Connection Error', 'Unable to Connect to Db')
            
            Query = "Select h.his_status, h.timestamp from dataentry_history as h Join domicile as d on h.rec_id = d.dom_id where h.rec_id = %s;"
            cur.execute(Query, [self.rec_id])
            data = cur.fetchall()
            a = 0
            for row in data:
                his_list.insert(a, f"{row['status']} on {row['timestamp']}")
                a += 1
            con.close()
            cur.close()
        window.mainloop()
    def switch_control(self):
        if self.child_insert_chk == 0:
            self.child_insert_chk = 1

        else:
            self.child_insert_chk = 0

        print(self.child_insert_chk)
    
    def check_childern_duplicate(self):
        
        dup_check_status = self.check_dup_cnic(
                    cnic=self.child_cnic_entry.get().strip())
        if dup_check_status != 'CNIC donot exist':
            messagebox.showerror('Error', 'Duplicate CNIC')
            return 'Duplicate CNIC'
        
    

    def add_Childerns(self):

        top_level = tk.Toplevel(self)
        top_level.geometry('550x580+100+100')
        child_theme_style = ttk.Style(top_level)
        child_theme_style.configure('TButton', font=self.button_font)
        # child_theme_style.configure('TEntry', font=self.entry_font)
        # child_theme_style.configure('TLabel', font=self.label_font)
        self.Insert_query_list = []
        child_theme_style.configure(
            'Treeview', font=self.treeview_font, width=60)
        child_theme_style.configure(
            "Treeview.Heading", font=self.treeview_heading_font)
        top_frame = ttk.Frame(top_level)
        top_frame.pack(fill=X)
        middle_frame = ttk.Frame(top_level)
        middle_frame.pack(fill=BOTH, expand=TRUE)
        bottom_frame = ttk.Frame(top_level)
        bottom_frame.pack(fill=X)
        child_cnic_label = ttk.Label(
            top_frame, text='Child CNIC', font=self.label_font)
        child_cnic_label.grid(column=0, row=0, padx=10, pady=10, sticky=W)
        self.child_cnic_entry = ttk.Entry(top_frame, font=self.entry_font)
        self.child_cnic_entry.grid(column=1, row=0, padx=10)
        # self.child_cnic_entry.bind('<Tab>', self.)
        child_name_label = ttk.Label(
            top_frame, text='Child Name', font=self.label_font)
        child_name_label.grid(column=0, row=1, padx=10, pady=10, sticky=W)
        child_name_entry = ttk.Entry(top_frame, font=self.entry_font)
        child_name_entry.grid(column=1, row=1, padx=10)

        child_gender_label = ttk.Label(
            top_frame, text='Child Gender', font=self.label_font)
        child_gender_label.grid(column=0, row=2, padx=10, pady=5, sticky=W)
        child_gender_list = tk.Listbox(
            top_frame, exportselection=0, height=1, font=self.list_font)
        child_gender_list.grid(column=1, row=2, padx=10)
        child_gender_list.insert(1, "Male")
        child_gender_list.insert(2, "Female")
        child_gender_list.insert(3, "Widow")
        child_gender_list.select_set(0)
        child_gender_list.bind('<KeyPress>', self.select_keysym_value)
        child_dob_label = ttk.Label(
            top_frame, text='Date of Birth', font=self.label_font)
        child_dob_label.grid(column=0, row=3, padx=10, sticky=W)

        def add_Child(*arg):

            widget_list = [self.child_cnic_entry.get(
            ), child_name_entry.get(), child_dob_entry.get()]
            for item in widget_list:
                if item.lower().find('update') != -1 or item.lower().find('delete') != -1 or item.lower().find('char(') != -1:
                    return messagebox.showerror('showerror', 'Milicouse word found in child input widgets')
            if len(child_gender_list.curselection()) > 1:
                return messagebox.showerror('showerror', 'Please Check Gender Selection')
            if len(child_dob_entry.get()) != 0:
                validation_result = Validation.validate_date(
                    child_dob_entry.get())
                if validation_result != 'valid':
                    return messagebox.showerror('Error', validation_result)
            if len(child_name_entry.get()) == 0:
                return messagebox.showerror('showerror', 'Please Provide Child Name')
            # checking for duplicate child in grid
            for line in trv.get_children():
                if trv.item(line)['values'][0].upper() == child_name_entry.get().upper() and trv.item(line)['values'][1] == child_dob_entry.get():
                    return messagebox.showerror('Error', 'Child Already exist')

            if self.child_insert_chk.get() == 1:

                dup_check_status = self.check_dup_cnic(
                    cnic=self.child_cnic_entry.get().strip())
                if dup_check_status != 'CNIC donot exist':
                    return messagebox.showerror('Error', dup_check_status)
                if self.check_validations() != 'invalid':
                    # Creating Insert Query String for domicile tabel
                    col_dict = {}

                    col_dict['Dom_date'] = "'{}'".format(
                        self.Record_Date.get())
                    col_dict['Status'] = "'Pending'"
                    col_dict['CNIC'] = "'{}'".format(self.child_cnic_entry.get())
                    col_dict['First_Name'] = "'{}'".format(
                        child_name_entry.get())
                    col_dict['Father_Name'] = "'{}'".format(
                        self.Entry_First_Name.get())
                    col_dict['Spouse_Name'] = 'Null'
                    col_dict['Pres_Tehsil'] = self.pre_Tehsil_id
                    col_dict['Pres_District'] = self.pre_District_id
                    col_dict['Pres_Province'] = self.pres_Province_id
                    col_dict['Present_Address'] = "'{}'".format(
                        self.Entry_Present_Address.get())
                    col_dict['Perm_Tehsil'] = self.prem_Tehsil_id
                    col_dict['Perm_District'] = self.prem_District_id
                    col_dict['Perm_Province'] = self.prem_Province_id
                    col_dict['Permenant_Address'] = "'{}'".format(
                        self.Entry_Permenant_Address.get())
                    col_dict['Placeofbirth'] = "'{}'".format(
                        self.Entry_Placeofbirth.get())
                    col_dict['Contact'] = "'{}'".format(
                        self.Entry_Contact.get())
                    col_dict['Date_of_Birth'] = "'{}'".format(
                        child_dob_entry.get())
                    col_dict['Arrival_Date'] = "'{}'".format(
                        child_dob_entry.get())
                    col_dict['Gender'] = child_gender_list.curselection()[0]+1
                    col_dict['Religon'] = "'{}'".format(self.List_Religion.get(
                        self.List_Religion.curselection()))
                    col_dict['Marital_Status'] = 1
                    col_dict['Qualification'] = 2
                    col_dict['Occupation'] = 4
                    col_dict['Application_Type'] = 1
                    col_dict['Request_Type'] = 1
                    col_dict['Service_Type'] = 1
                    col_dict['Payment_Type'] = 1
                    col_dict['Have_Childern'] = 'Null'
                    col_dict['cnic_front'] = -1
                    col_dict['cnic_back'] = -1
                    col_dict['cnic_guardian'] = -1
                    col_dict['Residance_Prof'] = -1
                    col_dict['utility_bill'] = -1
                    col_dict['educational_certificate'] = -1
                    col_dict['marriage_registration_certificate'] = 0
                    col_dict['form_b'] = -1
                    col_dict['domicile_of_guardian'] = -1
                    col_dict['noc_from_concerned_district'] = 0
                    col_dict['affidavit_domicile'] = -1
                    col_dict['affidavit_voterlist'] = -1
                    col_dict['voter_list'] = -1
                    col_dict['domicile_challan'] = 0
                    col_dict['Process_Type'] = f"'{self.List_Process_Type.get(self.List_Process_Type.curselection())}'"
                    col_dict['Approver_Desig'] = "'AC (Saddar)'"
                    col_dict['user_id'] = 'Null'
                    Query_part1 = ''
                    Query_part2 = ''
                    lop_count = 0
                    for item in col_dict:
                        lop_count += 1

                        if lop_count == 1:
                            Query_part1 = item
                            Query_part2 = str(col_dict[item])
                        else:
                            Query_part1 = Query_part1 + ", " + item
                            Query_part2 = Query_part2 + \
                                ", " + str(col_dict[item])
                    Query = "Insert Into Domicile (" + Query_part1 + \
                        ") values (" + Query_part2 + ");"
                    print(Query)
                    self.Insert_query_list.append(Query)

                else:
                    return messagebox.showerror('showerror', 'validation failed')

            trv.insert("", 'end',
                       values=(child_name_entry.get(), child_dob_entry.get()))
            self.child_cnic_entry.delete('0', 'end')
            child_name_entry.delete('0', 'end')
            child_dob_entry.delete('0', 'end')
            self.child_cnic_entry.focus_set()

        child_dob_entry = ttk.Entry(top_frame, font=self.entry_font)
        child_dob_entry.bind('<Return>', add_Child)
        child_dob_entry.grid(column=1, row=3, padx=10, pady=10)
        child_dob_entry.insert(0, 'yyyy-mm-dd')

        trv = ttk.Treeview(
            middle_frame, selectmode='browse')
        trv.grid(row=3, column=0, columnspan=2, padx=20, pady=10)
        trv["columns"] = ("1", "2")
        trv['show'] = 'headings'
        trv.column("1", width=250, anchor='w')
        trv.column("2", width=200, anchor='w')
        trv.heading("1", text="Child Name", anchor='w')
        trv.heading("2", text="Date of Birth", anchor='w')

        if self.edit_mode == TRUE:
            for row in self.child_old_data:
                trv.insert("", 'end',
                           values=(row['Child_Name'], row['Child_dob']))

        def del_child():
            trv.delete(trv.selection())
            selectedItem = self.trv.selection()[0]
            child_selected_name = self.trv.item(selectedItem)['values'][0]
            for item in self.Insert_query_list:
                if child_selected_name.upper() == item[3].upper():
                    target_list_item = self.Insert_query_list.index(item)
                    self.Insert_query_list.remove(target_list_item)
                    break

        def close_window():
            top_level.destroy()

        def Save_data():
            self.child_data_list = []
            for line in trv.get_children():
                self.child_data_list.append(trv.item(line)['values'])
            top_level.destroy()

        self.insert_switch = ttk.Checkbutton(bottom_frame, text="Childerns are also domicile applicants", variable=self.child_insert_chk, onvalue=1, offvalue=0)
        self.insert_switch.grid(
            column=1, row=0, columnspan=3, padx=10, pady=5)
        if self.edit_mode == TRUE:
            self.insert_switch.config(state='disable')

        Add_Btn = ttk.Button(bottom_frame, command=add_Child,
                             text='Add Child')
        Add_Btn.grid(column=1, row=1, padx=10, pady=10)
        Del_Btn = ttk.Button(bottom_frame, text='Del Child',
                             command=del_child)
        Del_Btn.grid(column=2, row=1, padx=10, pady=10)

        exit_Btn = ttk.Button(bottom_frame, text='Save & Exit',
                              command=Save_data, width=15)
        exit_Btn.grid(column=3, row=1, padx=10, pady=10)
        top_level.mainloop()

    def import_data(self):
        file = askopenfile(mode='r', filetypes=[('Text Data Files', '*.txt')])
        if file is not None:
            lines = file.readlines()
        file.close
        print("Data Lenth:-{}".format(len(lines)))
        
        con, cur = open_con(False)
        for line in lines:
            cur.execute(line)
        con.commit()
        cur.close()
        con.close()
        messagebox.showinfo('Success', '{} rows inserted'.format(len(lines)))

    def Receipt(self):

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
        con, cur = open_con(True)
        cur.execute(
            "Select * from domicile Where CNIC=%s", [self.Entry_CNIC.get()])
        data = cur.fetchall()

        cur.close()
        con.close()    
    

        pdf.set_font('Times', size=12)
        for row in data:

            pdf.cell(40, 8, 'Application No')
            pdf.cell(40, 8, str(row['Dom_id']))
            pdf.cell(20, 8, '')
            pdf.cell(40, 8, 'Application Date')
            pdf.cell(50, 8, '{}'.format(row['Dom_date']))
            pdf.ln(8)
            pdf.cell(40, 8, 'Application Type')
            pdf.cell(40, 8, Req_type.get(row['Request_Type']))
            pdf.cell(20, 8, '')
            pdf.cell(40, 8, 'CNIC')
            pdf.cell(50, 8, row['CNIC'])
            pdf.ln(8)
            pdf.cell(40, 8, 'Name')
            pdf.cell(60, 8, row['First_Name'])
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

    def export_form(self):
        self.import_data()
        return

        def export(self):
            return messagebox.showerror('Error', 'Not Completed yet')
            con = sqlite3.connect(filepath)
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            # Query = "Select * from Domicile Where CNIC = '9100301000850';"
            Query = "Select * from Domicile Where Dom_date = '{}';".format(
                date_entry.get())

            cur.execute(Query)
            data = cur.fetchall()
            if len(data) != 0:
                f = open('Export_data.txt', 'w')
                for row in data:
                    txt_line = "Insert Into Domicile (Dom_date, Status, CNIC, First_Name, Father_Name, Spouse_Name, Pres_Tehsil, Pres_District, Pres_Province, Present_Address, Perm_Tehsil, Perm_District, Perm_Province, Permenant_Address, Placeofbirth, Contact, Date_of_Birth, Arrival_Date, Gender, Religon, Marital_Status, Qualification, Occupation, Application_Type, Request_Type, Service_Type, Payment_Type, cnic_front, cnic_back, cnic_guardian, Residance_Prof, utility_bill, educational_certificate, marriage_registration_certificate, form_b, domicile_of_guardian, noc_from_concerned_district, affidavit_domicile, affidavit_voterlist, voter_list, domicile_challan, Process_Type, Approver_Desig) values ('{}', 'Pending', '{}', '{}', '{}', '{}', '{}', {}, {}, {},'{}', {}, {}, {}, '{}', '{}', '{}', '{}', '{}', {}, '{}', {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, '{}', '{}');".format(
                        row['dom_date'], row['CNIC'], row['First_name'], row['Father_Name'], row['Spouse_Name'], row['Pres_Tehsil'], row['Pres_District'], row['Pres_Province'], row['Present_Address'], row['Perm_Tehsil'], row['Perm_District'], row['Perm_Province'], row['Permenant_Address'], row['Placeofbirth'], row['Contact'], row['Date_of_Birth'], row['Arrival_Date'], row['Gender'], row['Religon'], row['Marital_Status'], row['Qualification'], row['Occupation'], row['Application_Type'], row['Request_Type'], row['Service_Type'], row['Payment_Type'], row['cnic_front'], row['cnic_back'], row['cnic_guardian'], row['Residance_Prof'], row['utility_bill'], row['educational_certificate'], row['marriage_registration_certificate'], row['form_b'], row['domicile_of_guardian'], row['noc_from_concerned_district'], row['affidavit_domicile'], row['affidavit_voterlist'], row['voter_list'], row['domicile_challan'], row['Process_Type'], row['Approver_Desig'])
                    f.write(txt_line+'\n')
                    Query = "Select * from Childern Where Father_CNIC = '{}';".format(
                        row['CNIC'])
                    cur.execute(Query)
                    Childern_data = cur.fetchall()
                    for row1 in Childern_data:

                        txt_line = "Insert Into Childern (Father_CNIC, Child_Name, Child_dob) values ('{}', '{}', '{}');".format(
                            row1[1], row1[2], row1[3])
                        f.write(txt_line + '\n')
                f.close()

                messagebox.showinfo('showinfo', 'Data Exported')
            else:
                messagebox.showinfo('showinfo', 'No Records Found')
                export_window.focus_set()
        export_window = tk.Toplevel()
        export_window.geometry('400x220+100+100')
        # export_window.configure(bg='#24304a')
        date_label = ttk.Label(
            export_window, text='Date', font=self.label_font)
        date_label.grid(row=0, column=0, padx=10, pady=10)
        date_entry = ttk.Entry(export_window, font=self.entry_font)
        date_entry.grid(row=0, column=1, padx=10, pady=10)
        date_button = ttk.Button(
            export_window, text='Import Data', command=export)
        date_button.grid(row=1, column=1, padx=10, pady=10)

    def Record_Selector(self):
        def Search(*args):
            if len(search_input.get()) == 0:
                return messagebox.showerror(
                    'Error', 'Please Provide Search Input')
            Query = "SELECT Dom_id, Dom_date, Status, CNIC, First_Name, Father_Name, Contact, Date_of_Birth FROM domicile "
            if search_type.get(search_type.curselection()) == 'Date':
                validation_result = Validation.validate_date(
                    search_input.get())
                if validation_result != 'valid':
                    return messagebox.showerror('Error', validation_result)
                else:
                    Query_part = "Where Dom_Date = '{}'".format(
                        search_input.get())
            elif search_type.get(search_type.curselection()) == 'ID':
                if search_input.get().isnumeric():
                    Query_part = 'Where Dom_id = {}'.format(search_input.get())
                else:
                    return messagebox.showerror('Error', "ID shall be a number")
            elif search_type.get(search_type.curselection()) == 'CNIC':
                if len(search_input.get()) != 13:
                    return messagebox.showerror('Error', "CNIC Number lenth shall be 13 digit without dashes")
                if search_input.get().isnumeric():
                    Query_part = "Where CNIC Like '%{}%'".format(
                        search_input.get())
                else:
                    return messagebox.showerror('Error', "Input for CNIC search shall be a number")
            elif search_type.get(search_type.curselection()) == 'Status':
                if search_input.get().upper() == 'PENDING' or search_input.get().upper() == 'APPROVED':
                    Query_part = "Where Status = '{}'".format(
                        search_input.get())
                else:
                    return messagebox.showerror('Error', "Status shall be Pending or Approved")
            elif search_type.get(search_type.curselection()) == 'Name':
                Query_part = "Where First_Name Like '%{}%'".format(
                    search_input.get())
            elif search_type.get(search_type.curselection()) == 'Father Name':
                Query_part = "Where Father_Name Like '%{}%'".format(
                    search_input.get())
            elif search_type.get(search_type.curselection()) == 'Contact':
                if search_input.get().isnumeric():
                    Query_part = "Where Contact Like '%{}%'".format(
                        search_input.get())
                else:
                    return messagebox.showerror('Error', "Input for Contact Number search shall be a number")
            elif search_type.get(search_type.curselection()) == 'Date of Birth':
                validation_result = Validation.validate_date(
                    search_input.get())
                if validation_result != 'valid':
                    return messagebox.showerror('Error', validation_result)
                else:
                    Query_part = "Where Date_of_Birth = '{}'".format(
                        search_input.get())
            else:
                return messagebox.showerror(
                    'Error', "Please Select Search Type from List")
            Query = Query + Query_part + " order by Dom_id desc;"

            con, cur = open_con(True)
            cur.execute(Query)
            data = cur.fetchall()
            cur.close()
            con.close()
            trv.delete(*trv.get_children())

            for row in data:
                trv.insert("", 'end',
                           values=(row['Dom_id'], row['Dom_date'], row['Status'], row['CNIC'], row['First_Name'], row['Father_Name'], row['Contact'], row['Date_of_Birth']))

        def start_up():
            Query = "SELECT Dom_id, Dom_date, Status, CNIC, First_Name, Father_Name, Contact, Date_of_Birth FROM domicile order by Dom_id desc Limit 200;"
            con, cur = open_con(True)
            cur.execute(Query)
            data = cur.fetchall()
            cur.close()
            con.close()
            trv.delete(*trv.get_children())

            for row in data:

                trv.insert("", 'end',
                           values=(row['Dom_id'], row['Dom_date'], row['Status'], row['CNIC'], row['First_Name'], row['Father_Name'], row['Contact'], row['Date_of_Birth']))

        def cancel():
            self.rec_id = 0
            self.edit_window.quit()
            self.edit_window.destroy()

        def trv_click(*args):
            if len(trv.selection()) == 0:
                return print('Nothing Selected')
            selectedItem = trv.selection()[0]

            self.rec_id = trv.item(selectedItem)['values'][0]
            self.edit_window.quit()
            self.edit_window.destroy()

        self.rec_id = 0
        self.edit_window = Toplevel()
        self.edit_window.geometry("1200x400")
        self.edit_window.title('Record Selection')
        # self.edit_window.configure(bg='#24304a')
        Top_Frame = Frame(self.edit_window)  # bg='#24304a'
        Top_Frame.pack(fill=X)
        query_dict = {'ID': 'Dom_id', 'Date': 'Dom_Date', 'Status': 'Status', 'CNIC': 'CNIC', 'Name': 'First_Name',
                      'Father Name': 'Father_Name', 'Contact': 'Contact', 'Date of Birth': 'Date_of_Birth'}
        list_values = []
        for item in query_dict.keys():
            list_values.append(item)
        list_items = Variable(value=list_values)
        search_type = Listbox(
            Top_Frame, width=15, height=1, listvariable=list_items, exportselection=0, font=('Bell', 12))
        search_type.grid(row=1, column=0, padx=10, pady=10)
        search_type.select_set(0)
        search_type.see(0)
        search_input = ttk.Entry(Top_Frame, width=15, font=self.entry_font)
        search_input.grid(row=1, column=1, padx=10, pady=10)
        search_input.bind('<Return>', Search)
        Bottom_Frame = Frame(self.edit_window)  # bg='#24304a'
        Bottom_Frame.pack(fill=X, expand=1)
        trv_font = ttk.Style(self.edit_window)
        trv_font.configure('TButton', font=self.button_font)
        trv_font.configure('Treeview', font=('Courier', 12))
        trv_font.configure('Treeview.Heading', font=('Courier', 12, 'bold'))
        trv = ttk.Treeview(Bottom_Frame, selectmode='browse', height=15)
        trv.pack(fill=BOTH, expand=TRUE, padx=10, pady=10)
        trv["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8")
        trv['show'] = 'headings'
        trv.column("1", width=50, anchor='w')
        trv.column("2", width=80, anchor='w')
        trv.column("3", width=100, anchor='w')
        trv.column("4", width=120, anchor='w')
        trv.column("5", width=120, anchor='w')
        trv.column("6", width=150, anchor='w')
        trv.column("7", width=120, anchor='w')
        trv.column("8", width=150, anchor='w')

        trv.heading("1", text="ID", anchor='w')
        trv.heading("2", text="Date", anchor='w')
        trv.heading("3", text="Status", anchor='w')
        trv.heading("4", text="CNIC", anchor='w')
        trv.heading("5", text="Name", anchor='w')
        trv.heading("6", text="Father Name", anchor='w')
        trv.heading("7", text="Contact", anchor='w')
        trv.heading("8", text="Date of Birth", anchor='w')

        trv.bind("<Double-1>", trv_click)

        search_btn = ttk.Button(Top_Frame, width=15,
                                text='Search', command=Search)
        search_btn.grid(row=1, column=3)
        cancel_btn = ttk.Button(Top_Frame, width=15, text='Cancel',
                                command=cancel)
        cancel_btn.grid(row=1, column=4, padx=10, pady=10)

        start_up()
        self.edit_window.mainloop()


class Sysentry(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('1100x800+50+50')
        self.tk.call('source', 'azure.tcl')
        self.tk.call('set_theme', 'light')
        self.Top_Frame = ttk.Frame(
            self, relief=RIDGE)
        self.Top_Frame.pack(fill=X)
        self.Middle_Frame = ttk.Frame(
            self, relief=RIDGE)
        self.Middle_Frame.pack(fill=X)
        self.Bottom_Frame = ttk.Frame(
            self, relief=RIDGE, border=1, height=10)
        self.Bottom_Frame.pack(fill=BOTH, expand=YES)
        self.Top_label = ttk.Label(
            self.Top_Frame, text='Javascript Generator', border=1, font=('Courier', 18, 'bold'))
        self.Top_label.pack(padx=10, pady=10, side=TOP)
        sys_style = ttk.Style()
        # sys_style.theme_use('classic')
        sys_style.configure('TButton', font=('Courier', 12, 'bold'))
        sys_style.configure('TCheckButton', font=('Courier', 12))
        self.Label_CNIC = ttk.Label(
            self.Middle_Frame, text='CNIC', border=1, font=('Courier', 12))
        self.Label_CNIC.grid(row=0, column=0, padx=10, pady=10)
        self.Entry_CNIC = ttk.Entry(self.Middle_Frame, font=('Courier', 12))
        self.Entry_CNIC.grid(row=0, column=1)
        self.Entry_CNIC.bind('<Return>', self.check_event)
        self.Label_ID = ttk.Label(
            self.Middle_Frame, text='ID', border=1, font=('Courier', 12))
        self.Label_ID.grid(row=0, column=2, padx=10, pady=10)
        self.Entry_ID = ttk.Entry(self.Middle_Frame, font=('Courier', 12))
        self.Entry_ID.grid(row=0, column=3, padx=10, pady=10)
        self.Entry_ID.bind('<Return>', self.check_event)
        self.Gen_JS_Button = ttk.Button(
            self.Middle_Frame, text='Generate Js', command=self.generate)
        self.Gen_JS_Button.grid(row=0, column=4, padx=10, pady=10)
        self.Clear_Button = ttk.Button(
            self.Middle_Frame, text='Clear Text', command=self.clear_text)
        self.Clear_Button.grid(row=0, column=5, padx=10, pady=10)
        self.Js_Text = Text(self.Bottom_Frame, height=30, font=('Courier', 12))
        self.Js_Text.grid(row=0, column=0, padx=10, pady=10)
        self.Js_Text.bind('<Control-c>', self.update_main)

        # raw_img = Image.open(
        #     r'F:\Docs\OneDrive\Python Projects\CFC App\pic_26875.jpg')
        # resized_image = raw_img.resize((300, 300))
        # resized_image.show()
        # img1 = ImageTk.PhotoImage(resized_image)
        # img = PhotoImage(r'F:\Docs\OneDrive\Pictures\Camera Roll\pic_2.jpg')
        self.image_label = ttk.Label(self.Bottom_Frame)
        self.image_label.grid(row=0, column=1, padx=10, pady=10)
        self.Pic_path_lbl = ttk.Label(
            self.Middle_Frame, text='Pic Path', border=1, font=('Courier', 12))
        self.Pic_path_lbl.grid(row=1, column=0, padx=10, pady=10)
        self.Pic_path = ttk.Entry(
            self.Middle_Frame, width=60, font=('Courier', 12))
        self.Pic_path.grid(row=1, column=1, columnspan=3, padx=10, pady=10)
        self.check_val = IntVar()
        self.show_checkbutton = ttk.Checkbutton(
            self.Middle_Frame, text='Show Images', variable=self.check_val, onvalue=1, offvalue=0)
        self.show_checkbutton.grid(row=1, column=4, padx=10, pady=10)

    def update_main(self, *args):
       
        con, cur = open_con(False)
        if con.is_connected():
            
            if len(self.Entry_CNIC.get()) != 0:
                cur.execute("Update domicile Set Status = 'Exported' Where CNIC=%s;", [self.Entry_CNIC.get()])
            else:
                cur.execute("Update domicile Set Status = 'Exported' Where Dom_Id=%s;", [self.Entry_ID.get()])
            con.commit()
            cur.close()
            con.close()
        

    def check_event(self, event):
        if event.keysym == 'Return':
            self.generate()
            self.Js_Text.focus_set()
            self.Js_Text.tag_add(SEL, "1.0", END)
            self.Js_Text.mark_set(INSERT, "1.0")
            self.Js_Text.see(INSERT)
            return 'break'

        # self.Js_child_Text = Text(self.Top_Frame, height=10, font=('Courier', 12))
        # self.Js_child_Text.place(x=50, y=530)

    def Converit_Boolean(self, val):
        if val == 0:
            return 'false'
        elif val == -1:
            return 'true'

    def save_pic(self, pic_data, filename):
        filename = "Pictures\pic_" + str(filename) + ".jpg"
        with open(filename, 'wb') as pic_file:
            pic_file.write(pic_data)
        cur_path = os.getcwd()
        if self.check_val.get() == 1:
            raw_img = Image.open(filename)
            resized_image = raw_img.resize((200, 200))
            resized_image.show()
            img1 = ImageTk.PhotoImage(resized_image)
            self.image_label.config(image=img1)
        img_path = cur_path + "\\" + filename
        self.Pic_path.insert(0, img_path)
        # os.system(filename)

    def generate(self, *args):
        con, cur = open_con(True)
        if len(self.Entry_CNIC.get()) != 0:
            if len(self.Entry_CNIC.get()) != 13:
                messagebox.showerror('showerror', 'Incorrect CNIC')
                self.Entry_CNIC.focus_set()
                return
            if self.Entry_CNIC.get().isnumeric():
                Query = "Select * from domicile Where CNIC='{}';".format(
                    self.Entry_CNIC.get())
                Query2 = """select Child_Name, Child_dob
                        from childern
                        inner Join domicile
                        on domicile.CNIC = childern.Father_CNIC
                        where domicile.CNIC = '{}';""".format(self.Entry_CNIC.get())
            else:
                messagebox.showerror('showerror', 'Invalid CNIC')
                self.Entry_CNIC.focus_set()
                return
        else:

            if self.Entry_ID.get().isnumeric():
                Query = "Select * from domicile Where Dom_ID={};".format(
                    self.Entry_ID.get())
                Query2 = """select Child_Name, Child_dob
                            from childern
                            inner Join domicile
                            on domicile.CNIC = childern.Father_CNIC
                            where domicile.Dom_id = {};""".format(self.Entry_ID.get())
            else:
                messagebox.showerror(
                    'showerror', 'Either ID is not numeric or no input provided')
                self.Entry_ID.focus_set()
                return
        # try:

        if con.is_connected():
            if self.Entry_CNIC.get().upper().find('UPDATE') != -1 or self.Entry_CNIC.get().upper().find('DELETE') != -1:
                return messagebox.showerror('Error', 'Miliciouse Word Found in CNIC Widget')
            

            cur.execute(Query)
            data = cur.fetchall()
            if len(data) != 0:
                Query = "Select Pic from pictures where Dom_ID = {}".format(
                    data[0]['Dom_id'])
                cur.execute(Query)
                pic_data = cur.fetchall()
                if len(pic_data) != 0:
                    self.save_pic(pic_data[0]['Pic'], data[0]['Dom_id'])
            cur.execute(Query2)
            child_data = cur.fetchall()
            if len(data) != 0:
                Query = "Update domicile Set Status = 'Exported' Where CNIC='{}';".format(
                    data[0]['CNIC'])
                cur.execute(Query)
            cur.close()
            con.close()
        # except Exception as e:
        #     print("Error while connecting to Mysqldb", e)
        #     return
        if len(data) == 0:
            messagebox.showerror('showerror', 'Nothing Found')
            self.Entry_CNIC.focus_set()
            return

        for row in data:
            txt = "document.getElementById('first_name').value = '{}';".format(
                row["First_Name"])
            self.Js_Text.insert(tk.END, txt + '\n')
            # txt = "document.getElementById('last_name').value = '{}';".format(
            #     row['Last_Name'])
            # self.Js_Text.insert(tk.END, txt + '\n')
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
                self.Converit_Boolean(row['cnic_front']))
            self.Js_Text.insert(tk.END, txt + '\n')

            txt = "document.getElementById('docs[cnic_back]').checked = {};".format(
                self.Converit_Boolean(row['cnic_back']))
            self.Js_Text.insert(tk.END, txt + '\n')
            txt = "document.getElementById('docs[cnic_guardian]').checked = {};".format(
                self.Converit_Boolean(row['cnic_guardian']))
            self.Js_Text.insert(tk.END, txt + '\n')
            txt = "document.getElementById('docs[proof_of_residence]').checked = {};".format(
                self.Converit_Boolean(row['Residance_Prof']))
            self.Js_Text.insert(tk.END, txt + '\n')
            txt = "document.getElementById('docs[utility_bill]').checked = {};".format(
                self.Converit_Boolean(row['utility_bill']))
            self.Js_Text.insert(tk.END, txt + '\n')
            txt = "document.getElementById('docs[educational_certificate]').checked = {};".format(
                self.Converit_Boolean(row['educational_certificate']))
            self.Js_Text.insert(tk.END, txt + '\n')
            txt = "document.getElementById('docs[marriage_registration_certificate]').checked = {};".format(
                self.Converit_Boolean(row['marriage_registration_certificate']))
            self.Js_Text.insert(tk.END, txt + '\n')
            txt = "document.getElementById('docs[form_b]').checked = {};".format(
                self.Converit_Boolean(row['form_b']))

            self.Js_Text.insert(tk.END, txt + '\n')
            txt = "document.getElementById('docs[domicile_of_guardian]').checked = {};".format(
                self.Converit_Boolean(row['domicile_of_guardian']))

            self.Js_Text.insert(tk.END, txt + '\n')
            txt = "document.getElementById('docs[noc_from_concerned_district]').checked = {};".format(
                self.Converit_Boolean(row['noc_from_concerned_district']))

            self.Js_Text.insert(tk.END, txt + '\n')
            txt = "document.getElementById('docs[affidavit_domicile]').checked = {};".format(
                self.Converit_Boolean(row['affidavit_domicile']))

            self.Js_Text.insert(tk.END, txt + '\n')
            txt = "document.getElementById('docs[affidavit_voterlist]').checked = {};".format(
                self.Converit_Boolean(row['affidavit_voterlist']))

            self.Js_Text.insert(tk.END, txt + '\n')
            txt = "document.getElementById('docs[voter_list]').checked = {};".format(
                self.Converit_Boolean(row['voter_list']))

            self.Js_Text.insert(tk.END, txt + '\n')
            txt = "document.getElementById('docs[domicile_challan]').checked = {};".format(
                self.Converit_Boolean(row['domicile_challan']))

            self.Js_Text.insert(tk.END, txt + '\n')

            vari = 97
            cnt = 0
            if len(data) != 0:
                self.Js_Text.insert(tk.END, txt + '\n')
                txt = "var check_click = document.getElementsByClassName('input-span');"
                self.Js_Text.insert(tk.END, txt + '\n')
                txt = "check_click[0].click();"
                self.Js_Text.insert(tk.END, txt + '\n')
            for row in child_data:
                txt = "var {} = document.getElementsByName('children[{}][first_name]');".format(
                    chr(vari), cnt)
                self.Js_Text.insert(tk.END, txt + '\n')
                txt = chr(vari) + "[0].value = '" + \
                    row["Child_Name"] + "';"
                self.Js_Text.insert(tk.END, txt + '\n')
                var = vari + 1
                txt = "var {} = document.getElementsByName('children[".format(chr(vari)) + str(
                    "{}".format(cnt)) + "][date_of_birth]');"
                self.Js_Text.insert(tk.END, txt + '\n')
                txt = chr(vari) + \
                    "[0].value = '{}';".format(row["Child_dob"])
                self.Js_Text.insert(tk.END, txt + '\n')
                txt = "document.getElementById('addRowButton').click();"
                self.Js_Text.insert(tk.END, txt + '\n')
                cnt = cnt + 1
                vari = vari + 1

    def clear_text(self):
        self.Js_Text.delete('1.0', 'end')


class Collection_Report(tk.Tk):
    def __init__(self):
        super().__init__()
        path = os.getcwd()
        path = path+r"\theme"
        self.tk.call('source', 'azure.tcl')
        self.tk.call('set_theme', 'light')
        self.geometry('500x200')
        col_style = ttk.Style(self)
        self.title('Report')
        self.label_font = ('Courier New', 12, 'bold')
        self.Label_Main = tk.Label(
            self, text='Daily Domicile Collection Report', width=40, height=2, font=self.label_font)
        self.Label_Main.pack()
        self.Label_Date = tk.Label(
            self, text='Collection Date', font=self.label_font)
        self.Label_Date.place(x=50, y=50)

        self.Entry_Date = tk.Entry(self, font=self.label_font)
        self.Entry_Date.bind(
            '<Return>', lambda event: Report(self.Entry_Date.get()))
        self.Entry_Date.insert(0, datetime.date(datetime.today()))
        self.Entry_Date.place(x=220, y=50)
        self.Label_Date = tk.Label(
            self, text='Calling Days', font=self.label_font)
        self.Label_Date.place(x=50, y=100)

        self.Entry_Days = tk.Entry(self, font=self.label_font)
        self.Entry_Days.insert(0, "3")
        self.Entry_Days.place(x=220, y=100)
        self.Rpt_btn = ttk.Button(self, text='Report', width=15,
                                  command=lambda: Report(self.Entry_Date.get()))

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
            con, cur = open_con(True)
            
            Query = "Select CNIC, First_Name from Domicile Where Dom_Date = '{}' And Process_Type = 'Normal';".format(
                collection_date)

            cur.execute(Query)
            data = cur.fetchall()
            cur.close()
            con.close()
            
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
                pdf.cell(50, 8, dat['CNIC'], border=1)
                pdf.cell(120, 8, dat['First_Name'], border=1)
                pdf.ln(8)

            pdf.output('Daily_Report.pdf')

            path = 'Daily_Report.pdf'
            os.system(path)


if __name__ == '__main__':
    # obj = dataentry('25.33.21.56')
    # obj.mainloop()
    obj = dataentry()
    obj.mainloop()
    # obj = Collection_Report('25.48.184.239')
    # obj.mainloop()
    # obj = Sysentry()
    # obj.mainloop()
