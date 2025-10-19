
# widgets = GUI elements: button, textboxes, labels, image
# windows = serves as a container to hold or contain these widgets

from tkinter import *

window = Tk() # instantiate an instance of a window
window.geometry("780x780") # set the size of the window
window.title("Tkinter Tutorial")

icon = PhotoImage(file="C:\\Users\\Mahendra's\\OneDrive\\Pictures\\Animek\\ちょこえい-chocoeiru.gif") # ganti icon image sebelah title
window.iconphoto(True,icon) # set icon image

window.config(background="black") # set the background color of the window NOTE: bisa juga diganti dengan hex code
window.mainloop() # place window on computer screen. Listen to events