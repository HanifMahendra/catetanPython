from tkinter import *

def submit():
    print("The temperature is: " + str(scale.get()) + " degrees C")

window = Tk()

hotImage = PhotoImage(file="C:\\Users\\Mahendra's\\OneDrive\\Documents\\Ngopi slur\\Python\\GUI Windows\\fire.png")
hotLabel = Label(image=hotImage)
hotLabel.pack()

scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              orient=HORIZONTAL, # horizontal slider
              font=("Consolas", 20),
              tickinterval=10, # major tick every 10 units
              # showvalue = 0, # hide the current value
              resolution=5, # minor tick every 5 units
              troughcolor="#69EAFF",
              fg="#FF1C00",
              bg="#111111",
              )
scale.set(((scale["from"] - scale["to"]) / 2) + scale["to"])  # set current value to 50

scale.pack()

coldImage = PhotoImage(file="C:\\Users\\Mahendra's\\OneDrive\\Documents\\Ngopi slur\\Python\\GUI Windows\\ice.png")
coldLabel = Label(image=coldImage)
coldLabel.pack()

button = Button(window, text="submit", command=submit)
button.pack()

window.mainloop()