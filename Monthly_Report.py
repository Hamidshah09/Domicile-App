from tkinter import *
from tkinter import ttk, messagebox
from calendar import monthrange
from Validation import validate_date
from datetime import datetime
from tools import open_con
from fpdf import FPDF
from fpdf.fonts import FontFace
import os


class Monthly_Report(Tk):
    def __init__(self):
        super().__init__()
        self.tk.call('source', 'azure.tcl')
        self.tk.call('set_theme', 'light')
        self.geometry('400x300')
        self.label_font = ('Courier New', 12, 'bold')
        col_style = ttk.Style(self)
        col_style.configure('TButton', font=self.label_font)
        col_style.configure('TLabel', font=self.label_font)
        self.title('Monthly Report')

        self.Label_Main = ttk.Label(
            self, text='Monthly Receipt Report', font=('Courier New', 14, 'bold'))
        self.Label_Main.pack()
        
        self.widget_frame = ttk.Frame(self)
        self.widget_frame.pack(fill='both', expand=True)
        self.Label_Date = ttk.Label(
            self.widget_frame, text='From', font=self.label_font)
        self.Label_Date.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        self.from_date = ttk.Entry(self.widget_frame, font=self.label_font, width=15)

        self.from_date.grid(row=0, column=1, padx=10, pady=10, sticky='w')
        self.to_date_lbl = ttk.Label(
            self.widget_frame, text='To', font=self.label_font)
        self.to_date_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        self.to_date = ttk.Entry(self.widget_frame, font=self.label_font,width=15)
        self.to_date.grid(row=1, column=1, padx=10, pady=10, sticky='w')
        
        self.from_date.insert(0, datetime.now().date())
        self.to_date.insert(0, datetime.now().date())

        self.doc_type_lbl = ttk.Label(
            self.widget_frame, text='Document Type', font=self.label_font)
        self.doc_type_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.doc_type = Listbox(self.widget_frame, height=1, exportselection=0, font=('Courier New', 14), width=15)
        self.doc_type.grid(row=2, column=1, padx=10, pady=10, sticky='w')
        self.doc_type.insert(0, "Issued Domicile")
        self.doc_type.insert(1, "Accepted Files")
        self.doc_type.insert(2, "Verification Letters")
        self.doc_type.insert(3, "Approved Files")
        self.doc_type.select_set(0)
        self.doc_type.see(0)

        self.officer_lbl = ttk.Label(
            self.widget_frame, text='Officer Name', font=self.label_font)
        self.officer_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        self.officer_list = Listbox(self.widget_frame, height=1, exportselection=0, font=('Courier New', 14), width=15)
        self.officer_list.grid(row=3, column=1, padx=10, pady=10, sticky='w')
        

        self.Rpt_btn = ttk.Button(self.widget_frame, text='Monthly Report', width=15,
                                  command=lambda: self.Report(self.doc_type.get(self.doc_type.curselection())))

        self.Rpt_btn.grid(row=4, column=0, padx=10, pady=10, sticky='w')

        self.Rpt_btn1 = ttk.Button(self.widget_frame, text='Report by Day', width=15,
                                  command=lambda: self.No_of_Domiciles_by_date(self.doc_type.get(self.doc_type.curselection())))
        self.Rpt_btn1.grid(row=4, column=1, padx=10, pady=10, sticky='w')
        self.get_approers()
    def get_approers(self):
            con, cur = open_con(False)
            if type(cur) is str:
                return messagebox.showerror('Db Connection Error', 'Unable to connect to Db')
            cur.execute("select * from approvers;")
            data = cur.fetchall()
            if data:
                self.officer_list.delete(0, 'end')
                a = 0
                for row in data:
                    self.officer_list.insert(a, row[1])
                    a += 1
            cur.close()
            con.close()
    def Report(self, typ):
        # checking whether values from both list boxes are selected or no')
        validation_result = validate_date(self.from_date.get())
        if validation_result != 'valid':
            return messagebox.showerror('From Date Error', validation_result)
        validation_result = validate_date(self.to_date.get())
        if validation_result != 'valid':
            return messagebox.showerror('From Date Error', validation_result)
        from_date_obj = datetime.strptime(self.from_date.get(), '%Y-%m-%d').date()
        to_date_obj = datetime.strptime(self.to_date.get(), '%Y-%m-%d').date()
        if from_date_obj > to_date_obj  :
            return messagebox.showerror('From to Date Error', 'From Date shall be greater than to date')

        if typ == 'Issued Domicile':
            Query = "Select Count(Govt_Fee) as Total_Applications from cash_report Where Duplicate_Entry = 'No' And Application_Type = 'offline' And Request_Type= 'New' And Domicile_Date Between %s and %s;"
            type_of_domicile = "Total No of Domiciles"
            title = 'Domicile Receipt Report form from {} to {}'.format(self.from_date.get(), self.to_date.get())
            parm_list= [self.from_date.get(), self.to_date.get()]
        elif typ =='Accepted Files':
            Query = """SELECT count(dom_id) as no_of_domiciles 
                    FROM domicile_reports.domicile 
                    Where Dom_Date Between %s and %s;"""
            type_of_domicile = "Total No of Processed Domicile Files"
            title = 'Processed Files Report from {} to {}'.format(self.from_date.get(), self.to_date.get())
            parm_list= [self.from_date.get(), self.to_date.get()]
        elif typ=='Verification Letters':
            Query = "select count(letter_id) as issued_letters from verification_letters where timestamp between %s and %s;"
            type_of_domicile = "Total No of Verification Letters Issued"
            title = 'Verification Letters Report from {} to {}'.format(self.from_date.get(), self.to_date.get())
            parm_list= [self.from_date.get(), self.to_date.get()]
        elif typ=='Approved Files':
            Query = "select count(dom_id) as approved_files from domicile where approver_id = (select approver_id from approvers where approver_name = %s) and Dom_Date Between %s and %s;"
            type_of_domicile = "Total No of Approved Files"
            title = 'Approved Files Report from {} to {}'.format(self.from_date.get(), self.to_date.get())
            parm_list= [self.officer_list.get(self.officer_list.curselection()), self.from_date.get(), self.to_date.get()]        
        pdf = FPDF()
        pdf.add_page()

        pdf.set_font('Courier', 'B', size=14)
        pdf.set_fill_color(211, 211, 211)
        pdf.cell(0, 7, text='CITIZEN FACILITATION CENTER',
                 new_x="LMARGIN", new_y="NEXT", align='C')
        pdf.cell(0, 7, text="DEPUTY COMMISSIONER'S OFFICE",
                 new_x="LMARGIN", new_y="NEXT", align='C')
        pdf.cell(0, 7, text="ISLAMABAD CAPITAL TERRITORY",
                 new_x="LMARGIN", new_y="NEXT", align='C')
        pdf.ln(8)
        pdf.cell(0, 10, text=title, new_x="LMARGIN", new_y="NEXT", border=1, align='L', fill=True)

        pdf.ln(8)
        
        con, cur = open_con(True)
        if type(cur) is str:
            return messagebox.showerror("DB Connection Error", "Could Not connect to Database")
        
        cur.execute(Query, parm_list)
        count_data = cur.fetchall()
        cur.close()
        con.close()
        
        sr = 0

        pdf.set_font('Courier', 'B', size=14)
        # pdf.cell(10, 6, text='')
        pdf.cell(120, 6, text=type_of_domicile, align='C')
        
        if typ == 'Issued Domicile':
            pdf.cell(50, 6, text='Total Amount Deposited', new_x="LMARGIN", new_y="NEXT", align='C')
            pdf.set_font('Courier', size=14)
            # pdf.cell(10, 6, text='')
            pdf.cell(120, 6, text='{}'.format(
                str(count_data[0]['Total_Applications'])), align='C')
            pdf.cell(50, 6, text='{}'.format(
                int(count_data[0]['Total_Applications'])*200), new_x="LMARGIN", new_y="NEXT", align='C')
        elif typ == "Accepted Files":
            pdf.cell(50, 6, text='{}'.format(
                str(count_data[0]['no_of_domiciles'])), align='C')
        elif typ == "Approved Files":
            pdf.cell(50, 6, text='{}'.format(
                str(count_data[0]['approved_files'])), align='C')
        else:
            pdf.cell(50, 6, text='{}'.format(
                str(count_data[0]['issued_letters'])), align='C')
        pdf.set_font('Courier', 'B', size=14)
        pdf.ln(8)
        pdf.ln(8)
        pdf.ln(8)
        pdf.ln(8)
        pdf.cell(170, 6, text='Domicile Clerk', align='R', new_x="LMARGIN", new_y="NEXT")
        pdf.output('Daily_Report.pdf')

        path = 'Daily_Report.pdf'
        os.system(path)
    def No_of_Domiciles_by_date(self, typ):
        # checking whether values from both list boxes are selected or no')
        
        if len(self.doc_type.curselection()) == 0:
            return messagebox.showerror('Selection Error', "Please select type of Report from list")
        elif len(self.doc_type.curselection()) > 1:
            return messagebox.showerror('Selection Error', "Please select apropriate item from list")
        validation_result = validate_date(self.from_date.get())
        if validation_result != 'valid':
            return messagebox.showerror('From Date Error', validation_result)
        validation_result = validate_date(self.to_date.get())
        if validation_result != 'valid':
            return messagebox.showerror('From Date Error', validation_result)
        from_date_obj = datetime.strptime(self.from_date.get(), '%Y-%m-%d').date()
        to_date_obj = datetime.strptime(self.to_date.get(), '%Y-%m-%d').date()
        if from_date_obj > to_date_obj  :
            return messagebox.showerror('From to Date Error', 'From Date shall be greater than to date')
        con, cur = open_con(True)
        if type(cur) is str:
            return messagebox.showerror("DB Connection Error", "Could Not connect to Database")
        if typ == 'Issued Domicile':
            Query = """SELECT Domicile_Date, count(Domicile_ID) as no_of_domiciles 
                    FROM domicile_reports.cash_report 
                    Where Duplicate_Entry = 'No'
                    and Application_Type = 'offline'
                    and Domicile_Date Between %s and %s group by domicile_date;"""
            type_of_domicile = "No of Issued Domicile"
            title = 'Issued Domiciles for each day from {} to {}'.format(self.from_date.get(), self.to_date.get())
            parm_list= [self.from_date.get(), self.to_date.get()]
        elif typ == "Accepted Files":
            Query = """SELECT Dom_Date, count(dom_id) as no_of_domiciles 
                    FROM domicile_reports.domicile 
                    Where Process_Type <> 'Urgent'
                    and Dom_Date Between %s and %s group by Dom_Date order by Dom_Date;"""
            type_of_domicile = "No of Accepted Domicile Files"
            title = 'Accepted Files Report for each day from {} to {}'.format(self.from_date.get(), self.to_date.get())
            parm_list= [self.from_date.get(), self.to_date.get()]
        elif typ == "Verification Letters":
            Query = "select count(letter_id) as Total_Letters, date(timestamp) from verification_letters where timestamp between %s and %s group by Date(timestamp);"
            type_of_domicile = "Verification Letters issued"
            title = 'Verification Letters Report for each day from {} to {}'.format(self.from_date.get(), self.to_date.get())
            parm_list= [self.from_date.get(), self.to_date.get()]
        elif typ == "Approved Files":
            if len(self.officer_list.curselection()) !=1:
                return messagebox.showerror('Selection Error', "Please select type of Report from list")
            Query = "select count(dom_id) as Approved_Files, dom_date from domicile where approver_id = (select approver_id from approvers where approver_name = %s) and dom_date between %s and %s group by dom_date;"
            type_of_domicile = "Approved Files"
            title = 'Approved Files Report for each day from {} to {}'.format(self.from_date.get(), self.to_date.get())
            parm_list= [self.officer_list.get(self.officer_list.curselection()) ,self.from_date.get(), self.to_date.get()]
        
        
        cur.execute(Query, parm_list)
        data = cur.fetchall()
        cur.execute("Select * from approvers where approver_name = %s;",[self.officer_list.get(self.officer_list.curselection())])
        approver_data =  cur.fetchall()
        cur.close()
        con.close()

        pdf = FPDF()
        pdf.add_page(format='A4')
        pdf.set_left_margin(7)
        pdf.set_right_margin(7)
        pdf.set_font('Courier', 'B', size=14)
        pdf.set_fill_color(211, 211, 211)
        pdf.cell(0, 7, text='CITIZEN FACILITATION CENTER',
                 new_x="LMARGIN", new_y="NEXT", align='C')
        pdf.cell(0, 7, text="DEPUTY COMMISSIONER'S OFFICE",
                 new_x="LMARGIN", new_y="NEXT", align='C')
        pdf.cell(0, 7, text="ISLAMABAD CAPITAL TERRITORY",
                 new_x="LMARGIN", new_y="NEXT", align='C')
        pdf.ln(8)
        
        
        
        pdf.multi_cell(0, 10, text=title, new_x="LMARGIN", new_y="NEXT", border=1, align='C', fill=True)
        if typ=='Approved Files':
            name_desig = self.officer_list.get(self.officer_list.curselection()) + ", " + str(approver_data[0]['designation'])
            pdf.ln(8)
            pdf.cell(96, text='Approver Name   : Mr./Mrs./Miss.')
            pdf.cell(100, text=f'{name_desig}', new_x="LMARGIN", new_y="NEXT")
        pdf.ln(8)
        
        sl = 0

        pdf.set_font('Courier', 'B', size=14)
        # pdf.cell(10, 6, text='')
        grey = (128, 128, 128)
        white = (255, 255, 255)
        headings_style = FontFace(emphasis="BOLD", fill_color=grey)
        table_style = FontFace(fill_color=white)
        with pdf.table(headings_style=headings_style, first_row_as_headings=False, line_height=7, padding=2, text_align=("CENTER", "LEFT", "CENTER"), col_widths=(10, 41, 40)) as table:
            row = table.row()
            row.cell("S.No")
            row.cell("Date")
            row.cell(type_of_domicile)
            for data_row in data:
                row = table.row(style=table_style)
                sl += 1
                row.cell(str(sl))
                if typ == "Issued Domicile":
                    row.cell(str(data_row["Domicile_Date"]))
                    row.cell(str(data_row["no_of_domiciles"]))
                elif typ == "Accepted Files":
                    row.cell(str(data_row["Dom_Date"]))
                    row.cell(str(data_row["no_of_domiciles"]))
                elif typ == "Approved Files":
                    row.cell(str(data_row["dom_date"]))
                    row.cell(str(data_row["Approved_Files"]))
                else:
                    row.cell(str(data_row["date(timestamp)"]))
                    row.cell(str(data_row["Total_Letters"]))
        pdf.set_font('Courier', size=14)
        # pdf.cell(10, 6, text='')
        pdf.set_font('Courier', 'B', size=14)
        pdf.ln(8)
        pdf.ln(8)
        pdf.ln(8)
        pdf.cell(170, 6, text='Domicile Clerk', align='R', new_x="LMARGIN", new_y="NEXT")
        pdf.output('Daily_Report.pdf')

        path = 'Daily_Report.pdf'
        os.system(path)
    


if __name__ == '__main__':
    obj = Monthly_Report()
    # obj = Monthly_Report('25.33.21.56')
    obj.mainloop()
