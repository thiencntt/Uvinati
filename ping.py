# import modules
from tkinter import *
from pythonping import ping
 
def get_ping():
    result = ping(e.get(), verbose=True)
    res.set(result)
 
# object of tkinter
# and background set for light grey
master = Tk()
master.configure(bg='light grey')
 
# Variable Classes in tkinter
res = StringVar()
 
# Creating label for each information
# name using widget Label
Label(master, text="Enter URL or IP :",
      bg="light grey").grid(row=0, sticky=W)
Label(master, text="Result :", bg="light grey").grid(row=1, sticky=W)
 
# Creating label for class variable
# name using widget Entry
Label(master, text="", textvariable=res, bg="light grey").grid(
    row=1, column=1, sticky=W)
 
e = Entry(master)
e.grid(row=0, column=1)
 
# creating a button using the widget
# Button that will call the submit function
b = Button(master, text="Show", command=get_ping)
b.grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5)
 
mainloop()