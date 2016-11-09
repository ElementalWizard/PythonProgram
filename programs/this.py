from Tkinter import *
from math import *



def areacirculo(r):
    a = pi*pow(r, 2)
    print a


def make_gui(name, title, w, h, cordx, cordy):
    w = w
    name = name
    h = h
    name = Tk()
    name.title(title)
    name.minsize(width=w, height=h)
    name.geometry(str(w)+"x"+str(h)+"+"+str(cordx)+"+"+str(cordy))

    txt = Label(name, text="Hi jolly")

    txt.pack()

    name.mainloop()


def create_canvas(name, master, w, h):
    name = Canvas(master, height=h, width=w)


