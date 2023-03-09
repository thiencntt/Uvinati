from tkinter import *
from tkinter import messagebox
from pathlib import Path

import tkinter as tk
import webbrowser
import psutil
import os

import platform

# Lấy thông tin tên máy tính
my_system = platform.uname()
computerName = "Tên máy tính: " + my_system.node
# Create window object
root = Tk()

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen


path = Path(__file__).parent.absolute()
# root.iconphoto(False, tk.PhotoImage(file='C:\\Users\\SPC\\TienIchVina\\icon.png'))
root.iconphoto(False, tk.PhotoImage(file=path.__str__()+'\\icon.png'))


# Lấy thông tin kết nối mạng của máy tính
Dic = psutil.net_if_addrs()
if Dic.get('Ethernet') is not None:
    macAddr = "Mac Address: " + (Dic['Ethernet'])[0].address
    ipAddr = "IP Address: " + (Dic['Ethernet'])[1].address
    netMask = "Subnet Mask: " + (Dic['Ethernet'])[1].netmask
elif Dic.get('Ethernet 2') is not None:
    macAddr = "Mac Address: " + (Dic['Ethernet 2'])[0].address
    ipAddr = "IP Address: " + (Dic['Ethernet 2'])[1].address
    netMask = "Subnet Mask: " + (Dic['Ethernet 2'])[1].netmask
else:
    macAddr = "Mac Address: Unknown"
    ipAddr = "Mac Address: Unknown"
    netMask = "Mac Address: Unknown"

def openHelp():
    newWindow = Toplevel(root)
    newWindow.iconphoto(False, tk.PhotoImage(file=path.__str__()+'\\icon.png'))
    newWindow.title("Thông tin chương trình")
    w = 500
    h = 200
    # calculate x and y coordinates for the Tk root window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    newWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))
    Label(newWindow, text ="Chương trình được viết những dòng code đầu tiên vào ngày 07/03/2023 tại phòng lab 2").pack()

def openSysInfo():
    SysInfoWindow = Toplevel(root)
    SysInfoWindow.iconphoto(False, tk.PhotoImage(file=path.__str__()+'\\icon.png'))
    SysInfoWindow.title("Thông tin hệ thống")
    w = 500
    h = 200
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    SysInfoWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))
    Label(SysInfoWindow, text = computerName, font=('bold', 14)).pack()
    Label(SysInfoWindow, text = macAddr, font=('bold', 14)).pack()
    Label(SysInfoWindow, text = ipAddr, font=('bold', 14)).pack()
    Label(SysInfoWindow, text = netMask, font=('bold', 14)).pack()
        
def goHomepage():
    webbrowser.open('https://thiencntt.com')

# Menu
menubar = Menu(root)

file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Hệ thống', menu = file)
file.add_command(label ='Thông tin hệ thống', command = openSysInfo)
file.add_command(label ='Open...', command = None)
file.add_command(label ='Save', command = None)
file.add_separator()
file.add_command(label ='Thoát', command = root.destroy, accelerator="Ctrl+Q")

edit = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Quản lý', menu = edit)
edit.add_command(label ='Cut', command = None)
edit.add_command(label ='Copy', command = None)
edit.add_command(label ='Paste', command = None)
edit.add_command(label ='Select All', command = None)
edit.add_separator()
edit.add_command(label ='Find...', command = None)
edit.add_command(label ='Find again', command = None)

help_ = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Trợ giúp', menu = help_)
help_.add_command(label ='Trang chủ', command = goHomepage)
help_.add_command(label ='Cập nhật chương trình', command = None)
help_.add_separator()
help_.add_command(label ='Thông tin phần mềm', command = openHelp)

root.config(menu = menubar)
root.bind_all("<Control-q>", root.destroy)




# máy tính cá nhân
def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

# 'bt_clear' function :This is used to clear 
# the input field

def bt_clear(): 
    global expression 
    expression = "" 
    input_text.set("")
 
# 'bt_equal':This method calculates the expression 
# present in input field
 
def bt_equal():
    global expression
    result = str(eval(expression)) 
    input_text.set(result)
    expression = ""
 
expression = ""

def pingGooogle():
    os.system("start /B start cmd.exe @cmd /k ping google.com -t")


chucnang_frame = Frame(root, width=312, height=30, bd=0, highlightbackground="green",
 highlightcolor="yellow", highlightthickness=2)

pingGoogleBtn = Button(chucnang_frame, text = "Ping Google.com", fg = "black", 
width = 22, height = 3, bd = 0, bg = "#eee", cursor = "hand2", 
command = lambda: pingGooogle()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)

chucnang_frame.grid(row=0, column=0) 
chucnang_frame.pack(ipady=0)

# 'StringVar()' :It is used to get the instance of input field
 
input_text = StringVar()
 
# Let us creating a frame for the input field
 
input_frame = Frame(root, width=312, height=50, bd=0, highlightbackground="black",
 highlightcolor="black", highlightthickness=2)
 
input_frame.pack(side=TOP)
 
#Let us create a input field inside the 'Frame'
 
input_field = Entry(input_frame, font=('arial', 18, 'bold'), 
textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)
 
input_field.grid(row=0, column=0)
 
input_field.pack(ipady=10)

 
btns_frame = Frame(root, width=312, height=272.5, bg="grey")
 
btns_frame.pack()
 
# first row
 
clear = Button(btns_frame, text = "C", fg = "black", 
width = 32, height = 3, bd = 0, bg = "#eee", cursor = "hand2", 
command = lambda: bt_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
 
divide = Button(btns_frame, text = "/", fg = "black",
 width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", 
 command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
 
# second row
 
seven = Button(btns_frame, text = "7", fg = "black", 
width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2",
 command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
 
eight = Button(btns_frame, text = "8", fg = "black", 
width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2",
 command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
 
nine = Button(btns_frame, text = "9", fg = "black", 
width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2",
 command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
 
multiply = Button(btns_frame, text = "*", fg = "black",
 width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",
  command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
 
# third row
 
four = Button(btns_frame, text = "4", fg = "black",
 width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2",
  command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
 
five = Button(btns_frame, text = "5", fg = "black", 
width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", 
command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
 
six = Button(btns_frame, text = "6", fg = "black",
 width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", 
 command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
 
minus = Button(btns_frame, text = "-", fg = "black",
 width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",
  command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
 
# fourth row
 
one = Button(btns_frame, text = "1", fg = "black",
 width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2",
  command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
 
two = Button(btns_frame, text = "2", fg = "black",
 width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2",
  command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
 
three = Button(btns_frame, text = "3", fg = "black",
 width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2",
  command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
 
plus = Button(btns_frame, text = "+", fg = "black",
 width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",
  command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
 
# fourth row
 
zero = Button(btns_frame, text = "0", fg = "black",
 width = 21, height = 3, bd = 0, bg = "#fff", cursor = "hand2",
  command = lambda: btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
 
point = Button(btns_frame, text = ".", fg = "black",
 width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",
  command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
 
equals = Button(btns_frame, text = "=", fg = "black",
 width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",
  command = lambda: bt_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)
# end máy tính cá nhân






# Part
# part_text = StringVar()
# part_label = Label(root, text='Part Name', font=('bold', 14), pady=20)
# part_label.grid(row=0, column=0, sticky=W)
# part_entry = Entry(root, textvariable=part_text)
# part_entry.grid(row=0, column=1)
# # Customer
# customer_text = StringVar()
# customer_label = Label(root, text='Customer', font=('bold', 14))
# customer_label.grid(row=0, column=2, sticky=W)
# customer_entry = Entry(root, textvariable=customer_text)
# customer_entry.grid(row=0, column=3)
# Retailer
# retailer_text = StringVar()
# retailer_label = Label(root, text='Retailer', font=('bold', 14))
# retailer_label.grid(row=1, column=0, sticky=W)
# retailer_entry = Entry(root, textvariable=retailer_text)
# retailer_entry.grid(row=1, column=1)
# Price
# price_text = StringVar()
# price_label = Label(root, text='Price', font=('bold', 14))
# price_label.grid(row=1, column=2, sticky=W)
# price_entry = Entry(root, textvariable=price_text)
# price_entry.grid(row=1, column=3)
# Parts List (Listbox)
# parts_list = Listbox(root, height=8, width=50, border=0)
# parts_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)
# Create scrollbar
# scrollbar = Scrollbar(root)
# scrollbar.grid(row=3, column=3)
# Set scroll to listbox
# parts_list.configure(yscrollcommand=scrollbar.set)
# scrollbar.configure(command=parts_list.yview)


root.title('Tiện ích dành cho Admin hệ thống')

w = 700 # width for the Tk root
h = 350 # height for the Tk root

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))


# Start program
root.mainloop()


# To create an executable, install pyinstaller and run
# '''
# pyinstaller --onefile --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' part_manager.py
# '''