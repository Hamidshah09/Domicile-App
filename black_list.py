from datetime import datetime
from tkinter import Tk, Toplevel, ttk, messagebox, Listbox, Text

from tools import open_con
class Black_List():
    def __init__(self, login_data):
        self.window = Tk()
        self.rec_id = 0
        self.login_data = login_data
        self.pre_login = ''
        self.__font = ('Century Gothic', 12, 'bold')
        self.window.geometry('1400x700+50+50')
        self.window.title("Black Listed CNICs")
        self.btn_font = ('Century Gothic', 12)
        user_style = ttk.Style(self.window)
        user_style.configure('TButton', font=self.btn_font)
        user_style.configure('TLabel', font=self.btn_font)
        user_style.configure('TEntry', font=self.btn_font)
        user_style.configure('TCheckbutton', font=self.btn_font)
        user_style.configure('Treeview',
                             rowheight=36, font=self.btn_font)
        user_style.configure("Treeview.Heading",
                             font=self.__font, background="blue")
        self.top_frame = ttk.Frame(self.window, relief='ridge',
                                   borderwidth=2)
        self.top_frame.pack(side='top', fill='x')
        self.top_frame1 = ttk.Frame(self.window, relief='ridge',
                                    borderwidth=2)
        self.top_frame1.pack(side='top', fill='x')

        self.filter_type = Listbox(self.top_frame1, height=1, bg='#272727',
                                   font=self.btn_font, exportselection=0)
        self.filter_type.grid(row=1, column=1, padx=10, pady=10)
        self.filter_type.insert(0, 'ID')
        self.filter_type.insert(1, 'CNIC')
        self.filter_type.insert(2, 'Status')
        self.filter_type.insert(3, 'Created on')
        self.filter_type.select_set(0)

        self.filter_input = ttk.Entry(self.top_frame1, font=self.btn_font)
        self.filter_input.grid(row=1, column=2, padx=10, pady=10)
        self.filter_input.bind(
            '<Return>', lambda event: self.search(self.filter_type.get(self.filter_type.curselection()), self.filter_input.get(), 'None'))
        self.middle_frame = ttk.Frame(
            self.window, relief='ridge', borderwidth=2)
        self.middle_frame.pack(fill='both', expand=True)
        # self.left_frame = ttk.Frame(
        #     self.window, relief='ridge', borderwidth=2)
        # self.left_frame.pack(side='left', fill='y')
        # self.right_frame = ttk.Frame(
        #     self.window, relief='ridge', borderwidth=2)
        # self.right_frame.pack(side='left', fill='both', expand=True)
        self.title_label = ttk.Label(
            self.top_frame, text='Block Listed CNICs', font=self.__font)
        self.title_label.pack(ipady=10)
        self.trv = ttk.Treeview(
            self.middle_frame, selectmode='browse')
        self.trv.pack(fill='both', expand=True)
        
        self.trv["columns"] = ("1", "2", "3", "4", "5", "6", "7")
        self.trv['show'] = 'headings'
        self.trv.column("1", width=70, anchor='center')
        self.trv.column("2", width=150, anchor='center')
        self.trv.column("3", width=350)
        self.trv.column("4", width=350)
        self.trv.column("5", width=150, anchor='center')
        self.trv.column("6", width=150, anchor='center')
        self.trv.column("7", width=150, anchor='center')

        self.trv.heading("1", text="ID", anchor='center')
        self.trv.heading("2", text="CNIC", anchor='center')
        self.trv.heading("3", text="Blocked Reason", anchor='center')
        self.trv.heading("4", text="Unblocked Reason", anchor='center')
        self.trv.heading("5", text="Status", anchor='center')
        self.trv.heading("6", text="Blocked By", anchor='center')
        self.trv.heading("7", text="Blocked on", anchor='center')

        self.Search_btn = ttk.Button(self.top_frame1, text='Search', command=lambda: self.search(self.filter_type.get(self.filter_type.curselection()), self.filter_input.get(), 'None'),
                                width=15)
        self.Search_btn.grid(row=1, column=3, padx=10, pady=10)
        self.add_btn = ttk.Button(self.top_frame1, text='Add CNIC', command=self.add_cnic,width=15)
        self.add_btn.grid(row=1, column=4, padx=10, pady=10)
        self.rem_btn = ttk.Button(self.top_frame1, text='Remove CNIC', command=self.remove_cnic,width=15)
        self.rem_btn.grid(row=1, column=5, padx=10, pady=10)
        self.his_btn = ttk.Button(self.top_frame1, text='Show History', command=self.show_history, width=15)
        self.his_btn.grid(row=1, column=6, padx=10, pady=10)
    
    def add_cnic(self):
        add_window = Toplevel()
        add_window.geometry("500x400")
        toplabel_frame = ttk.Frame(add_window)
        toplabel_frame.pack(fill='x')
        widget_frame = ttk.Frame(add_window)
        widget_frame.pack(fill='both', expand=True)
        main_label = ttk.Label(
            toplabel_frame, text='Add CNIC to Black List', anchor='center', font=self.btn_font)
        main_label.pack(fill='x')
        
        cnic_label = ttk.Label(
            widget_frame, text='CNIC', font=self.btn_font)
        cnic_label.grid(
            column=0, row=0, padx=10, pady=10, sticky='w')
        cnic_input = ttk.Entry(
            widget_frame, font=self.btn_font)
        cnic_input.grid(column=1, row=0, padx=10, pady=10, sticky='w')

        reason_label = ttk.Label(
            widget_frame, text='Reason', font=self.btn_font)
        reason_label.grid(
            column=0, row=1, padx=10, pady=10, sticky='w')
        reason_input = Text(
            widget_frame, width=40,  height=10,font=self.btn_font)
        reason_input.grid(column=1, row=1, padx=10, pady=10, sticky='w')
        def save_data():
            if len(cnic_input.get().strip()) !=13:
                messagebox.showerror('CNIC Length Error', 'CNIC must be 13 digits without dashes')
                return add_window.focus()
            elif cnic_input.get().strip().isnumeric() == False:
                messagebox.showerror('CNIC Data Error', 'CNIC shall only be digits')
                return add_window.focus()
            if len(reason_input.get('1.0', 'end')) < 10:
                messagebox.showerror('Reason Length Error', 'Reason shall atleast be 10 chararcters')
                return add_window.focus()
            con, cur  = open_con(False)
            if type(cur) is str:
                messagebox.showerror('Database Error', con)
            cur.execute("Select cnic, reason from black_list where cnic = %s;",[cnic_input.get().strip()])
            data = cur.fetchall()
            if not data:
                try:
                    cur.execute("Insert Into black_list (cnic, reason, user_id) values (%s, %s, %s);",[cnic_input.get().strip(),reason_input.get('1.0', 'end'), self.login_data['user_id']])
                    con.commit()
                    cur.execute("select Last_insert_id();")
                    last_id = cur.fetchone()
                    cur.execute("Insert Into black_list_history (black_list_id, remarks, user_id) values (%s, %s, %s);",[last_id[0], f"CNIC Blocked. {reason_input.get('1.0', 'end')}", self.login_data['user_id']])
                    con.commit()
                    cur.close()
                    con.close()
                except Exception as e:
                    cur.close()
                    con.close()
                    return messagebox.showerror('Db Error', e)
            else:
                try:
                    cur.execute("Update black_list set reason=%s, status='Blocked' where cnic=%s;",[reason_input.get('1.0', 'end'), cnic_input.get().strip()])
                    con.commit()
                    cur.execute("Insert Into black_list_history (remarks, user_id) values (%s, %s);",[f"CNIC Blocked. {reason_input.get('1.0', 'end')}", self.login_data['user_id']])
                    con.commit()
                    cur.close()
                    con.close()
                except Exception as e:
                    cur.close()
                    con.close()
                    return messagebox.showerror('Db Error', e)
            messagebox.showinfo('Black Listed', 'CNIC has been Black Listed')
            add_window.destroy()
        add_cnic_btn = ttk.Button(widget_frame, text='Save', command=save_data,width=15)
        add_cnic_btn.grid(row=2, column=1, padx=10, pady=10)
    def search(self, keyword, value, query_type, *args):
        parm_list = []
        if len(value) == 0 or value == 'None':
            query_type = 'All'
        else:
            query_type = 'None'
        if keyword == "ID":
            query_part = "black_list_id = %s"
            parm_list.append(value)
        elif keyword == "CNIC":
            query_part = "cnic like %s"
            value = f"%{value}%"
            parm_list.append(value)
        elif keyword == "Status":
            query_part = "status = %s"
            value = value
            parm_list.append(value)
        elif keyword == "Created on":
            if value.strip().find(' ') != -1:
                val1, val2 = value.split(' ')
                try:
                    frm_date = datetime.strptime(val1, "%Y-%m-%d").date()
                    to_date = datetime.strptime(val2, "%Y-%m-%d").date()
                except Exception:
                    messagebox.showerror('Wrong Date', 'Wrong Date Format please follow yyyy-mm-dd')
                    return
                query_part = "date(created_at) Between '%s' and '%s'"
                parm_list.append(frm_date)
                parm_list.append(to_date)
            else:
                try:
                    serch_date = datetime.strptime(val1, "%Y-%m-%d").date()
                except Exception:
                    messagebox.showerror('Wrong Date', 'Wrong Date Format please follow yyyy-mm-dd')
                    return
                query_part = "date(created_at) = '%s'"
                parm_list.append(serch_date)
        self.trv.delete(*self.trv.get_children())
        con, cur = open_con(True)
        if query_type == 'All':
            Query = """Select b.black_list_id,
                              b.cnic,
                              b.status,
                              b.reason,
                              b.clearance_reason,
                              u.user_name,
                              b.created_at 
                    from black_list as b 
                    Join users as u
                        on b.user_id = u.user_id
                    order by black_list_id Desc Limit 200;"""
            cur.execute(Query)

        else:
            Query = """Select b.black_list_id,
                              b.cnic,
                              b.status,
                              b.reason,
                              b.clearance_reason,
                              u.user_name,
                              b.created_at 
                    from black_list as b 
                    Join users as u
                        on b.user_id = u.user_id Where """ + \
                query_part + " order by black_list_id Desc;"
            cur.execute(Query, parm_list)

        self.agr_data = cur.fetchall()
        if self.agr_data:    
            for row in self.agr_data:
                self.trv.insert("", 'end', values=(
                    row['black_list_id'], row['cnic'], row['reason'], row['clearance_reason'], row['status'], row['user_name'], row['created_at']))
        con.close()
    def show_history(self):
        if len(self.trv.selection()) == 0:
            return
        window = Toplevel()
        window.geometry("900x400+100+100")
        label_frame = ttk.Frame(window)
        label_frame.pack(fill='x')
        top_label = ttk.Label(label_frame, text='History', anchor='center', font=('Courier', 14, 'bold'))
        top_label.pack(fill='x')
        self.title_label.pack(ipady=10)
        his_list = ttk.Treeview(
            window, selectmode='browse')
        his_list.pack(fill='both', expand=True)
        
        his_list["columns"] = ("1", "2", "3")
        his_list['show'] = 'headings'
        his_list.column("1", width=400)
        his_list.column("2", width=150, anchor='center')
        his_list.column("3", width=200, anchor='center')
        

        his_list.heading("1", text="Remarks", anchor='center')
        his_list.heading("2", text="User Name", anchor='center')
        his_list.heading("3", text="Time Stamp", anchor='center')
    
        for item in self.trv.selection():
            selected = self.trv.item(item, 'values')
            con, cur = open_con(True)
            if type(cur) is str:
                return messagebox.showerror('Connection Error', 'Unable to Connect to Db')
            
            Query = "Select h.remarks, h.created_at, u.user_name from black_list_history as h Join users as u on u.user_id = h.user_id where h.black_list_id = %s;"
            cur.execute(Query, [selected[0]])
            data = cur.fetchall()
            for row in data:
                his_list.insert("", 'end', values=(row['remarks'], row['user_name'], row['created_at']))
            
            con.close()
            cur.close()
        window.mainloop()
    def remove_cnic(self):
        if len(self.trv.selection()) ==0:
            return
        add_window = Toplevel()
        add_window.geometry("500x400")
        toplabel_frame = ttk.Frame(add_window)
        toplabel_frame.pack(fill='x')
        widget_frame = ttk.Frame(add_window)
        widget_frame.pack(fill='both', expand=True)
        main_label = ttk.Label(
            toplabel_frame, text='Remove CNIC from Black List', anchor='center', font=self.btn_font)
        main_label.pack(fill='x')

        reason_label = ttk.Label(
            widget_frame, text='Reason', font=self.btn_font)
        reason_label.grid(
            column=0, row=1, padx=10, pady=10, sticky='w')
        reason_input = Text(
            widget_frame, width=40,  height=10,font=self.btn_font)
        reason_input.grid(column=1, row=1, padx=10, pady=10, sticky='w')
        def save_data():
            for item in self.trv.selection():
                selected = self.trv.item(item, 'values')
            if len(reason_input.get('1.0', 'end')) < 10:
                messagebox.showerror('Reason Length Error', 'Reason shall atleast be 10 chararcters')
                return add_window.focus()
            con, cur  = open_con(False)
            if type(cur) is str:
                messagebox.showerror('Database Error', con)
            try:
                cur.execute("Update black_list set clearance_reason=%s, status='Unblocked' where black_list_id=%s;",[reason_input.get('1.0', 'end'), selected[0]])
                con.commit()
                cur.execute("Insert Into black_list_history (black_list_id, remarks, user_id) values (%s, %s, %s);",[selected[0], f"CNIC Unblocked. {reason_input.get('1.0', 'end')}", self.login_data['user_id']])
                con.commit()
                cur.close()
                con.close()
            except Exception as e:
                cur.close()
                con.close()
            messagebox.showinfo('Clear Black Listed', 'CNIC has been Removed from Black List')
            add_window.destroy()
        add_cnic_btn = ttk.Button(widget_frame, text='Save', command=save_data,width=15)
        add_cnic_btn.grid(row=2, column=1, padx=10, pady=10)
        
            
    
if __name__ == '__main__':
    obj = Black_List({'user_id':1})
    obj.window.mainloop()