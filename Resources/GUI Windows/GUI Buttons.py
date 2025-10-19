# button = you click it, then it does stuff

from tkinter import *

count = 0

def click():
    global count
    count += 1
    print(count)
    print("You clicked the button!")

window = Tk()

photo = PhotoImage(file="C:\\Users\\Mahendra's\\OneDrive\\Pictures\\Animek\\ちょこえい-chocoeiru.gif")
button = Button(window,text="Click Me!",
                command=click,
                font=("Comic Sans",30),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state=ACTIVE,
                image=photo,
                compound="bottom")
button.pack()

window.mainloop()