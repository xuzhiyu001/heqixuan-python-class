import random
import tkinter.messagebox


def helloCallBack():
    b = random.randint(1, 100)
    tkinter.messagebox.askokcancel('结局', b)
