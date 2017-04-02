#-*-coding:utf-8 -*-
import Tkinter
import tkMessageBox
top = Tkinter.Tk()
def hello():
    tkMessageBox.showinfo('test','Hello World!')
B1 = Tkinter.Button(top,text = 'Say Hello',command = hello)
B1.pack()
top.mainloop()