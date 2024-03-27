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
