import json
from tkinter import ttk, messagebox, Tk


class settings():
    def __init__(self):
        f = open("config.json", "r")
        self.j_obj = json.load(f)
        f.close()
        window = Tk()

    def font_name(self):
        return self.j_obj['font_name']

    def set_font(self, font_name):
        self.j_obj['font_name'] = font_name
        return

    def server_1_address(self):
        return self.j_obj['server_1']

    def set_server_1_address(self, server_address):
        self.j_obj['server_1'] = server_address
        return

    def server_2_address(self):
        return self.j_obj['server_2']

    def set_server_2_address(self, server_address):
        self.j_obj['server_2'] = server_address
        return

    def set_theme(self):
        if self.theme_name == 'light':
            self.tk.call("set_theme", "dark")
            self.theme_name = 'dark'
        else:
            self.tk.call("set_theme", "light")
            self.theme_name = 'light'

    def save_settings(self):
        with open("config.json", "w") as outfile:
            json.dump(self.j_obj, outfile)


if __name__ == '__main__':
    obj = settings()
    print(obj.font_name())
