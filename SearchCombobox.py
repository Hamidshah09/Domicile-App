
from tkinter import ttk, messagebox


class SCombobox(ttk.Combobox):
    def __init__(self, *args):
        super().__init__()
        self.set('Search')
