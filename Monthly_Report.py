from tkinter import *
from tkinter import ttk, messagebox
from calendar import monthrange
from Validation import validate_date
from datetime import datetime
from tools import open_con
from fpdf import FPDF
import os


class Monthly_Report(Tk):
    def __init__(self):
        super().__init__()
        self.tk.call('source', 'azure.tcl')
        self.tk.call('set_theme', 'light')
        self.geometry('500x200')
        self.label_font = ('Courier New', 12, 'bold')
        col_style = ttk.Style(self)
        col_style.configure('TButton', font=self.label_font)
        self.title('Monthly Report')

        self.Label_Main = ttk.Label(
            self, text='Monthly Receipt Report', font=('Courier New', 14, 'bold'))
        self.Label_Main.pack()
        self.Label_Date = ttk.Label(
            self, text='From', font=self.label_font)
        self.Label_Date.place(x=50, y=50)

        self.from_date = ttk.Entry(self, font=self.label_font, width=15)

        self.from_date.place(x=220, y=50)
        self.to_date_lbl = ttk.Label(
            self, text='To', font=self.label_font)
        self.to_date_lbl.place(x=50, y=100)

        self.to_date = ttk.Entry(self, font=self.label_font,width=15)
        self.to_date.place(x=220, y=100)
        self.Rpt_btn = ttk.Button(self, text='Report', width=15,
                                  command=self.Report)

        self.Rpt_btn.place(x=220, y=150)

    def Report(self, *args):
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
        pdf.cell(0, 10, text='Domicile Receipt Report form {} to {}'.format(self.from_date.get(), self.to_date.get()), new_x="LMARGIN", new_y="NEXT", border=1, align='L', fill=True)

        pdf.ln(8)
        
        con, cur = open_con(True)
        if type(cur) is str:
            return messagebox.showerror("DB Connection Error", "Could Not connect to Database")
        Query = "Select Sum(Govt_Fee) as Total_Amount from Cash_Report Where Domicile_Date Between %s and %s And Duplicate_Entry = 'No' And Application_Type = 'offline' And Request_Type= 'New';"
        
        parm_list= [self.from_date.get(), self.to_date.get()]

        cur.execute(Query, parm_list)
        data = cur.fetchall()
        cur.execute("Select Count(Govt_Fee) as Total_Applications from cash_report Where Domicile_Date Between %s and %s And Duplicate_Entry = 'No' And Application_Type = 'offline' And Request_Type= 'New';", [self.from_date.get(), self.to_date.get()])
        count_data = cur.fetchall()
        cur.close()
        con.close()
        
        sr = 0

        pdf.set_font('Courier', 'B', size=14)
        # pdf.cell(10, 6, text='')
        pdf.cell(120, 6, text='Total No of Domiciles', align='C')
        pdf.cell(50, 6, text='Total Amount Deposited', new_x="LMARGIN", new_y="NEXT", align='C')
        pdf.set_font('Courier', size=14)
        # pdf.cell(10, 6, text='')
        pdf.cell(120, 6, text='{}'.format(
            str(count_data[0]['Total_Applications'])), align='C')
        pdf.cell(50, 6, text='{}'.format(
            data[0]['Total_Amount']), new_x="LMARGIN", new_y="NEXT", align='C')
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
