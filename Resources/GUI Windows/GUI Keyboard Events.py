# Keyboard events
from tkinter import *

def function(event):
    print("You pressed: " + event.keysym)
    label.config(text=event.keysym)

window = Tk()

window.bind("<Return>",function) # event = w,a,s,d,etc (Return = Enter) If already use '<Key>' , This one no longer needed
window.bind("<Key>",function)

label = Label(window,font=("Helvetica",100))
label.pack()

window.mainloop()