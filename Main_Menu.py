import customtkinter as ct
from splash_screen_gui import splashscreen
import DataEntry_
import NOC_Letter
obj = splashscreen()
ct.set_appearance_mode('Dark')
ct.set_default_color_theme("sweetkind")
root = ct.CTk()
root.title('CFC APP')
width_of_window = 600
height_of_window = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
root.geometry("%dx%d+%d+%d" %
              (width_of_window, height_of_window, x_coordinate, y_coordinate))
main_frame = ct.CTkFrame(master=root)
main_frame.pack(pady=10, padx=10, fill="both", expand=True)
# frame1 = ct.CTkFrame(master=main_frame)
# frame1.pack(fill=ct.X, side=ct.TOP)
frame2 = ct.CTkFrame(master=main_frame)
frame2.pack(fill="both", expand=True)
lbl_font = ("Candara", 18)
label1 = ct.CTkLabel(
    master=frame2, text="CFC APP", text_font=("Game Of Squids", 24))
label1.pack(padx=10, pady=10)


def dataentry():
    data_obj = DataEntry_.dataentry()
    data_obj.mainloop()


def noc_to_other_district():
    noc_obj = NOC('25.48.184.239')
    noc_obj.mainloop()


btn_title = '            Data Entry             '
btn1 = ct.CTkButton(
    master=frame2, height=3, text=btn_title, width=30, text_font=lbl_font, command=dataentry)
btn1.pack(padx=10, pady=10)
btn_title = '  Noc to Other Districts  '
btn2 = ct.CTkButton(master=frame2, text=btn_title, width=15,
                    text_font=lbl_font, command=noc_to_other_district)
btn2.pack(padx=10, pady=10)
btn3 = ct.CTkButton(
    master=frame2, text='Cancellation of Domicile', width=15, text_font=lbl_font)
btn3.pack(padx=10, pady=10)
btn4 = ct.CTkButton(
    master=frame2, text=' Verification of Domicile ', width=15, text_font=lbl_font)
btn4.pack(padx=10, pady=10)
btn5 = ct.CTkButton(
    master=frame2, text='    NOC for ICT Domicile    ', width=15, text_font=lbl_font)
btn5.pack(padx=10, pady=10)
btn6 = ct.CTkButton(
    master=frame2, text='                    Exit                      ', width=15, text_font=lbl_font, command=root.destroy)
btn6.pack(padx=10, pady=10)

root.mainloop()
