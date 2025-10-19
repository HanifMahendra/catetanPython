# label = an area widget that holds text and/or an image within a window

from tkinter import *

window = Tk()

photo = PhotoImage(file="C:\\Users\\Mahendra's\\OneDrive\\Pictures\\Animek\\ちょこえい-chocoeiru.gif")

label = Label(window,text="Contoh ke-1",font=("Arial",40,"bold"),fg="black",bg="blue",
              relief=RAISED,bd=10,padx=20,pady=20,image=photo,compound="bottom") 
label.pack()                                                                                                                             
# NOTE: atau bisa menggunakan grid atau place
label2 = Label(window,text="Contoh ke-2",font=("Times New Roman",14,"bold"),fg="white",bg="blue") # fg nya bsa diganti ke hex color
label2.place(x=0,y=0)

window.mainloop()

# NOTE: Relief bisa diganti ke SUNKEN, compound bisa diganti ke TOP, BOTTOM, LEFT, RIGHT, CENTER, NONE
# fg nya bsa diganti ke hex color.
# Relief dan bd hanya bisa digunakan pada label, button, entry, frame, dan canvas saja