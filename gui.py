#This is going to be a gui weather application that is able to acess the weather API.

from tkinter import *       
 
root = Tk() 
           
root.geometry('600x600')  
root.config(bg="black")   
 
label = Label(root, text="Weather App",fg="white",bg="black",font=("Helvetica", 16))
 
label.place(x = 225,y=0)
 
label.pack()

root.mainloop()