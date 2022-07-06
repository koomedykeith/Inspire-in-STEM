#!/usr/bin/python
###################################
#   
#   GUI examples using tkinter 
#   date:07/06/22
###################################

from tkinter import *

#Create an instance of window
window = Tk()
window.title("Welcome to my app")
window.configure(bg ='teal')

#Set the geometry of the window
#window.geometry("400*400")

f_name = Label(window, text = "First Name ",font = ("Monaco",30))
s_name = Label(window, text = "Second Name",font = ("Perpetua",30))

f_name.grid(column = 60 , row = 100)
s_name.grid(column = 60 , row = 120)

btn = Button(window,text ="Click me",bg = 'green',fg = 'brown',command= open)
btn.grid(column = 400 , row = 400)

f_name_box = Entry (window ,width = 70)
f_name_box.grid(column = 100,row = 100)


s_name_box = Entry (window ,width = 50)
s_name_box.grid(column = 100,row = 120)

def open_popup():
    top = Toplevel(window)
    top.geometry("300*300")
    top.title("Pop Up Window")
    top.configure(bg = "Archid")
    msg = Label(top,text = "Welcome to pop up",font = ('mistral 18')).place(x=150,y= 150) 
window.mainloop()