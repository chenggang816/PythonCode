# -*- coding:utf-8 -*-
# import Tkinter
# top = Tkinter.Tk()
# top.mainloop()
from Tkinter import *

root = Tk()
lang = ['C','C++','Python']
listb = Listbox(root)
for item in lang:
    listb.insert(0,item)
for item in lang:
    listb.insert(1,item)
listb.pack()
root.mainloop()