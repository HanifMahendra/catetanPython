from tkinter import *
from tkinter import colorchooser # submodule

def click():
    color = colorchooser.askcolor() # assign color to a variable
    colorHex = color[1]             # assigns element at index 1 to a variable 
                                    # (normally used when u want the Hex value of the color)
    window.config(bg=colorHex)      # Bisa diubah menjadi window.config(bg=color[1])

window = Tk()
window.geometry("420x420")
button = Button(text="click me",command=click)
button.pack()
window.mainloop()