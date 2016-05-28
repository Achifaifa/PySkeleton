#! /usr/bin/env python

import tkFont, Tkinter


# Windows is created when importing this module
root=Tkinter.Tk()
root.wm_title("PySkeleton")
smallfont=tkFont.Font(root=root, font=None, name=None, family='Mono', size=100, weight='bold')
Tkinter.mainloop(1) 

def update_window():

  while 1:

    date,user,text,avatar=yield
    
    date=Tkinter.Label(root, text=date)
    date.pack()
    name=Tkinter.Label(root, text=user)
    name.pack(side="top", padx=10, fill="x")
    tweet=Tkinter.Label(text=text, font=smallfont)
    tweet.pack()
    root.update()

    




