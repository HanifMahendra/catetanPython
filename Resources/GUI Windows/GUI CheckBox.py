from tkinter import *

def display():
    if(x.get()==1):
        print("You agree!")
    else:
        print("You don't agree :(")

window = Tk()

x = IntVar() # Bisa diganti ke StringVar/BolleanVar (Kalo mau diganti, bagian function display ganti juga)

python_photo = PhotoImage(file="C:\\Users\\Mahendra's\\OneDrive\\Pictures\\Animek\\ちょこえい-chocoeiru.gif")

check_button = Checkbutton(window,
                           text="I agree to something",
                           variable=x,
                           onvalue=1,  # Kalo StringVar = "YES", BolleanVar = True
                           offvalue=0, # Kalo StringVar = "NO", BolleanVar = False
                           command=display,
                           font=("Times New Roman",20),
                           fg="#00FF00",
                           bg="black",
                           activeforeground="#00FF00",
                           activebackground="black",
                           padx=25,
                           pady=10,
                           image=python_photo,
                           compound="left")
check_button.pack()
window.mainloop()