# canvas2 = widget that is used to draw graphs, plot, images in a window
# This is a example if the canvas is much, if only 1 canvas, ignore line 7-23
from tkinter import *
from tkinter import ttk
window = Tk()

notebook = ttk.Notebook(window) # widget that manages a collection of windows/displays

tab1 = Frame(notebook) # new frame for tab 1
tab2 = Frame(notebook) # new frame for tab 2\
tab3 = Frame(notebook)
tab4 = Frame(notebook)
tab5 = Frame(notebook)
tab6 = Frame(notebook)

notebook.add(tab1,text='Tab 1')
notebook.add(tab2,text='Tab 2')
notebook.add(tab3,text='Tab 3')
notebook.add(tab4,text='Tab 4')
notebook.add(tab5,text='Tab 5')
notebook.add(tab6,text='Tab 6')
notebook.pack(expand=True,fill='both') # expand = expand to fill any space not otherwise used
                                       # fill = fill space on x and y axis


# Tab 1 Canvas
canvas1 = Canvas(tab1,height=500,width=500,bg='white')
canvas1.pack()
blueLine = canvas1.create_line(0,0,500,500,fill='blue',width=50)
redLine = canvas1.create_line(0,500,500,0,fill='red',width=50)

# Tab 2 Canvas
canvas2 = Canvas(tab2,height=500,width=500,bg='white')
canvas2.pack()
rectangle = canvas2.create_rectangle(50,50,250,250,fill='black')

# Tab 3 Canvas
points = [250,0,500,500,0,500]
canvas3 = Canvas(tab3,height=500,width=500,bg='white')
canvas3.pack()
canvas3.create_polygon(points,fill='cyan',outline='blue',width=5)

# Tab 4 Canvas
canvas4 = Canvas(tab4,height=500,width=500,bg='white')
canvas4.pack()
canvas4.create_arc(0,0,500,500,fill='green')

# Tab 5 Canvas
canvas5 = Canvas(tab5,height=500,width=500,bg='white')
canvas5.pack()
canvas5.create_arc(0,0,500,500,style=PIESLICE,start=90,fill='yellow',extent=270) # style = ARC/CHORD/PIESLICE

# Poke ball (Tab 6)
canvas6 = Canvas(tab6,height=500,width=500,bg='white')
canvas6.pack()
canvas6.create_arc(0,0,500,500,fill='red',extent=180,width=10)
canvas6.create_arc(0,0,500,500,fill='white',extent=180,start=180,width=10)
canvas6.create_oval(190,190,310,310,fill='white',width=10)

window.mainloop()