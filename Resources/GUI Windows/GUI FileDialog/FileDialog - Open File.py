from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\Mahendra's\\OneDrive\\Documents\\Ngopi slur\\Python\\GUI Windows",
                                          title="Open file okay?",
                                          filetypes= (("text files","*.txt"),
                                         ("Python files","*.py")))
    file = open(filepath,'r')
    print(file.read())
    file.close()

window = Tk()
button = Button(text="Open",command=openFile)
button.pack()
window.mainloop()