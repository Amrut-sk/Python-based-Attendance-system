import sys
import os
import tkinter as tk
from PIL import Image, ImageTk

def attendance():
    os.system('python Take_attendance.py')
    
  
root = tk.Tk()
root.title("Automatic Attendance System")

canvas = tk.Canvas(root, width=600, height=400)
canvas.grid(columnspan=3)

#our logo
logo = Image.open('logo1.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1,row=0)


#button
#take attendance button
take_attendance = tk.StringVar()
take_att_btn = tk.Button(root,textvariable=take_attendance,font="Raleway",fg="white",height=2,width=15,bg="#6953FE",command = attendance )
take_attendance.set("Take Attendance")
take_att_btn.grid(column=1,row=1)

#save attendance buttonS
save_attendance = tk.StringVar()
save_att_btn = tk.Button(root,textvariable=save_attendance,font="Raleway",fg="white",height=2,width=15,bg="#6953FE")
save_attendance.set("Save Attendance")
save_att_btn.grid(column=1,row=2)


root.mainloop()