from tkinter import *
from tkinter import messagebox

def click():
    # messagebox.showinfo(title="This is an info message box",message = "You are a person!")
    # messagebox.showwarning(title = "WARNING",message = "You have a VIRUS!")
    # messagebox.showerror(title = "ERROR!",message = "Something went wrong :(")
    # if messagebox.askokcancel(title = "Ask ok Cancel", message = "Do you want to do the thing?"):
    #     print("You did a thing!")
    # else:
    #     print("You canceled a thing :(")
    # if messagebox.askretrycancel(title = " Ask Retry Cancel", message = "Do you want to retry a thing?"):
    #     print("You retried a thing!")
    # else:
    #     print("You canceled a thing :(")
    # if messagebox.askyesno(title = "Ask yes or no", message = "Do you like python?"):
    #     print("I like python too :)")
    # else:
    #     print("Why not?")
    # answer = messagebox.askquestion(title = "ask question",message = "Do you like pie?")
    # if answer == 'yes':
    #     print("I like pie too :)")
    # else:
    #     print("Why not?")
    answer = messagebox.askyesnocancel(title = "Yes no cancel", message = "Do you like to code?", icon="warning")
    if answer == True:
        print("You like to code")
    elif answer == False:
        print("You don't like to code")
    else:
        print("You have dodged the question")

window = Tk()

button = Button(window,
                command = click,
                text = "click me")
button.pack()

window.mainloop()