from tkinter import *
from tkinter import ttk, messagebox
from calendar import monthrange
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
            self, text='Report Month', font=self.label_font)
        self.Label_Date.place(x=50, y=50)

        self.List_Date = Listbox(
            self, font=self.label_font, exportselection=0, height=1, width=15)

        self.Month_dict = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06',
                           'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
        counter = 0
        for item in self.Month_dict:

            self.List_Date.insert(counter, item)
            counter += 1

        self.List_Date.place(x=220, y=50)
        self.Label_Date = ttk.Label(
            self, text='Report Year', font=self.label_font)
        self.Label_Date.place(x=50, y=100)

        self.List_Year = Listbox(
            self, font=self.label_font, exportselection=0, height=1, width=15)
        Year_list = ['2023', '2024', '2025',
                     '2026', '2027', '2028', '2029', '2030']
        for item in Year_list:

            self.List_Year.insert(Year_list.index(item), item)
        self.List_Year.place(x=220, y=100)
        self.List_Year.bind('<Return>', self.Report)
        self.Rpt_btn = ttk.Button(self, text='Report', width=15,
                                  command=self.Report)

        self.Rpt_btn.place(x=220, y=150)

    def Report(self, *args):
        # checking whether values from both list boxes are selected or not
        if len(self.List_Date.curselection()) == 0 or len(self.List_Year.curselection()) == 0:
            return messagebox.showerror('Error', 'Please select Month and Year from list')

        from_date = str(self.List_Year.get(self.List_Year.curselection(
        ))) + "-" + str(self.Month_dict[self.List_Date.get(self.List_Date.curselection())]) + "-" + "01"
        # getting max days in selected month using calander.monthrange
        month_obj = monthrange(int(self.List_Year.get(self.List_Year.curselection(
        ))), int(self.Month_dict[self.List_Date.get(self.List_Date.curselection())]))
        max_days = month_obj[1]
        to_date = str(self.List_Year.get(self.List_Year.curselection(
        ))) + "-" + str(self.Month_dict[self.List_Date.get(self.List_Date.curselection())]) + "-" + str(max_days)
        print("from {} to {}".format(from_date, to_date))

        pdf = FPDF()
        pdf.add_page()

        pdf.set_font('Courier', 'B', size=14)
        pdf.set_fill_color(211, 211, 211)
        pdf.cell(0, 7, txt='CITIZEN FACILITATION CENTER',
                 ln=1, align='C')
        pdf.cell(0, 7, txt="DEPUTY COMMISSIONER'S OFFICE",
                 ln=1, align='C')
        pdf.cell(0, 7, txt="ISLAMABAD CAPITAL TERRITORY",
                 ln=1, align='C')
        pdf.ln(8)
        pdf.cell(0, 10, txt='Domicile Receipt Report for {}, {}'.format(self.List_Date.get(self.List_Date.curselection(
        )), self.List_Year.get(self.List_Year.curselection())), ln=1, border=1, align='L', fill=True)

        pdf.ln(8)
        
        con, cur = open_con(True)
        if type(cur) is str:
            return messagebox.showerror("DB Connection Error", "Could Not connect to Database")
        Query = "Select Sum(Govt_Fee) as Total_Amount from Cash_Report Where Domicile_Date Between %s and %s And Duplicate_Entry = 'No' And Application_Type = 'offline' And Request_Type= 'New';"
        
        parm_list= [from_date, to_date]

        cur.execute(Query, parm_list)
        data = cur.fetchall()
        cur.execute("Select Count(Govt_Fee) as Total_Applications from cash_report Where Domicile_Date Between %s and %s And Duplicate_Entry = 'No' And Application_Type = 'offline' And Request_Type= 'New';", [from_date, to_date])
        count_data = cur.fetchall()
        cur.close()
        con.close()
        
        sr = 0

        pdf.set_font('Courier', 'B', size=14)
        # pdf.cell(10, 6, txt='')
        pdf.cell(120, 6, txt='Total No of Domiciles', align='C')
        pdf.cell(50, 6, txt='Total Amount Deposited', ln=1, align='C')
        pdf.set_font('Courier', size=14)
        # pdf.cell(10, 6, txt='')
        pdf.cell(120, 6, txt='{}'.format(
            str(count_data[0]['Total_Applications'])), align='C')
        pdf.cell(50, 6, txt='{}'.format(
            data[0]['Total_Amount']), ln=1, align='C')
        pdf.set_font('Courier', 'B', size=14)
        pdf.ln(8)
        pdf.ln(8)
        pdf.ln(8)
        pdf.cell(170, 6, txt='Domicile Clerk', align='R', ln=1)
        pdf.output('Daily_Report.pdf')

        path = 'Daily_Report.pdf'
        os.system(path)


if __name__ == '__main__':
    obj = Monthly_Report()
    # obj = Monthly_Report('25.33.21.56')
    obj.mainloop()
