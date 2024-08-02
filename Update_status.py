from tkinter import Tk, ttk, Listbox, Toplevel, messagebox
from tools import open_con
from datetime import datetime
class Update_Status():
    def __init__(self):
        self.root = Tk()
        self.root.geometry("500x200+100+100")
        self.root.title("Update Approved Documetns Status")
        self.widget_style = ttk.Style(self.root)
        self.widget_style.configure("Treeview.Heading", font=('Courier', 14, 'bold'))
        self.widget_style.configure('TButton', font=('Courier', 14), width=20)
        self.widget_style.configure('TLabel', font=('Courier', 14))
        self.widget_style.configure('TEntry', font=('Courier', 14), width=40)
        self.top_label = ttk.Label(
            self.root, text='Update Approved Documetns Status', anchor='center', font=('Courier', 18, 'bold'))
        self.top_label.pack(fill='x', padx=10, pady=10)
        self.widget_frame = ttk.Frame(self.root)
        self.widget_frame.pack(fill='both', expand=True)
        self.date_label = ttk.Label(self.widget_frame, text='Receiving Date')
        self.date_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        self.date_entry = ttk.Entry(self.widget_frame, font=('Courier', 14))
        self.date_entry.grid(row=0, column=1, padx=10, pady=10, sticky='w')

        self.officer_label = ttk.Label(self.widget_frame, text='Approving officer')
        self.officer_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.officer_list = Listbox(self.widget_frame, height=1, exportselection=False, font=('Courier', 14))
        self.officer_list.grid(row=1, column=1, padx=10, pady=10, sticky='w')

        self.add_btn = ttk.Button(self.widget_frame, text='Add Approver', command=self.add_approver)
        self.add_btn.grid(row=2, column=0, padx=10, pady=10)

        self.submit_btn = ttk.Button(self.widget_frame, text='Update', command=self.update_status)
        self.submit_btn.grid(row=2, column=1, padx=10, pady=10)
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
    def update_status(self):
        if len(self.officer_list.curselection()) ==0:
            return messagebox.showerror('Selection Error', 'Please Select Approver Name from list')
        try:
            doc_date = datetime.strptime(self.date_entry.get().strip(), "%Y-%m-%d").date()
        except ValueError:
            return messagebox.showerror('Date format Error', 'Invalid Date. Try "yyyy-mm-dd"')
        con, cur = open_con(False)
        if type(cur) is str:
            return messagebox.showerror('Db Connection Error', 'Unable to connect to Db')
        cur.execute("Update domicile set Status = 'Approval Received', approver_id = (select approver_id from approvers where approver_name = %s) Where dom_date = %s and Process_Type = 'Normal'",[self.officer_list.get(self.officer_list.curselection()), doc_date])
        con.commit()
        cur.close()
        con.close()
        messagebox.showinfo('Success', 'Records updated')
        self.date_entry.delete(0, 'end')
    def add_approver(self):
        add_window = Toplevel()
        add_window.geometry("430x150")
        add_window.title('Add New Approver')
        ttk.Label(add_window, text='Approver Name').grid(row=0, column=0, padx=10, pady=10)
        app_name = ttk.Entry(add_window, font=('Courier', 14))
        app_name.grid(row=0, column=1, padx=10, pady=10)
        ttk.Label(add_window, text='Designation').grid(row=1, column=0, padx=10, pady=10)
        designation = Listbox(add_window, height=1, exportselection=False, font=('Courier', 14))
        designation.grid(row=1, column=1, padx=10, pady=10)
        designation.insert(0, "AC (Saddar)")
        designation.insert(1, "AC (Shalimar)")
        designation.insert(2, "AC (Sectt.)")
        designation.insert(3, "AC (Nelior)")
        designation.insert(4, "AC (Rular)")
        designation.insert(5, "AC (I/A)")
        designation.insert(6, "AC (Potohar)")
        designation.insert(7, "AC (City)")
        def save():
            
            if len(app_name.get()) ==0:
                messagebox.showerror('Approver Name Error', 'Please Provide Approver Name')
                return
            if len(designation.curselection()) != 1:
                messagebox.showerror('Designation Selecction Error', 'Please Select designation from list')
            con, cur = open_con(False)
            if type(cur) is str:
                return messagebox.showerror('Db Connection Error', 'Unable to connect to Db')
            cur.execute("Select approver_name from approvers where approver_name = %s;",[app_name.get().strip()])
            existing_data = cur.fetchall()
            if existing_data:
                messagebox.showerror('Existed', 'Approver Name already Existed')
                cur.close()
                con.close()
                return
            else:
                cur.execute("Insert Into approvers (approver_name, designation) values (%s, %s);",[app_name.get().strip(), designation.get(designation.curselection())])
                con.commit()
            cur.close()
            con.close()
            messagebox.showinfo('Success', 'Approver Saved')
            self.get_approers()
            add_window.destroy()
        ttk.Button(add_window, text='Save', command=save).grid(row=2, column=1, padx=10, pady=10)
if __name__ == '__main__':
    obj = Update_Status()
    obj.root.mainloop()