from tkinter import *

def rectangle(x1, y1, x2, y2):
    coord = [x1, y1, x2, y2]

    c_width = (x2-x1)
    c_height = (y2-y1)re


    root = Tk()
    root.title("My Rectangle")

    a = Canvas(root, width = c_width, height = c_height)
    a.pack()
    a.create_rectangle(coord, fill = "red")
    a.mainloop()

    
