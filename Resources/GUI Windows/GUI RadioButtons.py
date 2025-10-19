# radio button = similar to checkbox, but you can only select one from a group.

from tkinter import *

food =["pizza","hamburger","hotdog"]

def order():
    if(x.get()==0):
        print("You ordered a pizza!")
    elif(x.get()==1):
        print("You ordered a hamburger!")
    elif(x.get()==2):
        print("You ordered a hotdog!")
    else:
        print("huh?")

window = Tk()

pizzaImage = PhotoImage(file="C:\\Users\\Mahendra's\\OneDrive\\Pictures\\Animek\\ちょこえい-chocoeiru.gif")
hamburgerImage = PhotoImage(file="C:\\Users\\Mahendra's\\OneDrive\\Pictures\\Animek\\ちょこえい-chocoeiru.gif")
hotdogImage = PhotoImage(file="C:\\Users\\Mahendra's\\OneDrive\\Pictures\\Animek\\ちょこえい-chocoeiru.gif")
foodImages= [pizzaImage,hamburgerImage,hotdogImage]
x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index], # adds text to radio buttons
                              variable=x, # groups radiobuttons together if they share the same variable
                              value=index, # assigns each radiobutton a different value
                              padx= 25, # adds padding on x-axis
                              font=("Arial",20),
                              image= foodImages[index], # adds an image to the radiobutton
                              compound = "left", # adds the image to the left of the text
                              indicatoron=0, # removes the default indicator
                              width = 375, # sets the width of the radiobutton
                              command=order # calls the order function when clicked
                              )
    radiobutton.pack(anchor=W)
window.mainloop()

#===================================================== Versi resized image ================================================================

from PIL import Image, ImageTk  # Importing Image and ImageTk from Pillow

food1 = ["pizza", "hamburger", "hotdog"]

def order1():
    if(x1.get()==0):
        print("You ordered a pizza!")
    elif(x1.get()==1):
        print("You ordered a hamburger!")
    elif(x1.get()==2):
        print("You ordered a hotdog!")
    else:
        print("huh?")

window = Tk()

# Load and resize images
pizzaImage1 = Image.open("C:\\Users\\Mahendra's\\OneDrive\\Pictures\\Animek\\ちょこえい-chocoeiru.gif").resize((100, 100))  # Resize to 100x100
hamburgerImage1 = Image.open("C:\\Users\\Mahendra's\\OneDrive\\Pictures\\Animek\\ちょこえい-chocoeiru.gif").resize((100, 100))
hotdogImage1 = Image.open("C:\\Users\\Mahendra's\\OneDrive\\Pictures\\Animek\\ちょこえい-chocoeiru.gif").resize((100, 100))
x1 = IntVar()
# Convert to PhotoImage
foodImages1 = [ImageTk.PhotoImage(pizzaImage1), ImageTk.PhotoImage(hamburgerImage1), ImageTk.PhotoImage(hotdogImage1)]

for index1 in range(len(food1)):
    radiobutton = Radiobutton(window,
                              text=food1[index1],
                              variable=x1,
                              value=index1,
                              padx=25,
                              font=("Arial", 20),
                              image=foodImages1[index1],
                              compound="left",
                              indicatoron=0,
                              width=375,
                              command=order1
                              )
    radiobutton.pack(anchor=W)

window.mainloop()