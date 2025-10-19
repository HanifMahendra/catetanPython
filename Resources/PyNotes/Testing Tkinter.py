from tkinter import *

class Counter:
    def __init__(self):
        window = Tk()
        self.label = Label(master = window, text = 0)
        btInc = Button(window, text = "Increment", bg ="blue",\
                       command = self.increment )
        btDec = Button(window, text = "Decrement", bg ="yellow",\
                       command = self.decrement )
        self.label.pack()
        btInc.pack()
        btDec.pack()

        window.mainloop()

    def increment(self):
        self.label['text'] += 1

    def decrement(self):
        self.label['text'] -= 1

Counter()