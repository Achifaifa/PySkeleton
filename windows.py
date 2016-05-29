#! /usr/bin/env python

import tkFont, Tkinter


# Windows is created when importing this module
root=Tkinter.Tk()
root.wm_title("PySkeleton")
bigfont=tkFont.Font(root=root, font=None, name=None, family='Mono', size=50, weight='bold')
bigishfont=tkFont.Font(root=root, font=None, name=None, family='Mono', size=30, weight='bold')
smallfont=tkFont.Font(root=root, font=None, name=None, family='Mono', size=25, weight='bold')
Tkinter.mainloop(1) 

def update_window():

  name=Tkinter.Label(text="", font=bigfont)
  date=Tkinter.Label(text="", font=bigishfont)
  tweet=Tkinter.Label(text="", font=smallfont, wraplength=800, justify="left")
  name.pack(side="top", padx=10, fill="x")
  date.pack(side="top", padx=10, fill="x")
  tweet.pack(side="top", padx=10, fill="x")
  root.update()

  while 1:

    timestamp,user,text,avatar = yield
    name.config(text=user+"\n")
    date.config(text=timestamp+"\n")
    tweet.config(text=text)
    root.update()
    
 