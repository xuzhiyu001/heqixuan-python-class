import random
import tkinter


def run(a):
    a = tkinter.Tk()
    a.title("randing——")
    #读入文件
    content = open("__inpit__.txt", "r")
    file = content.readlines()
    #读入文件
    button = tkinter.Button(root,"look me!I'm ‘start’")
    button.pack()
    
    lable = tkinter.Label(a, file[0], "pink")
    lable.pack()
    a.mainloop()
