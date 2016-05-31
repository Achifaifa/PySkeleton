#! /usr/bin/env python

import tkFont, Tkinter
from PIL import Image, ImageTk

# Windows is created when importing this module
root=Tkinter.Tk()
root.wm_title("PySkeleton")
bigfont=tkFont.Font(root=root, font=None, name=None, family='Mono', size=50, weight='bold')
bigishfont=tkFont.Font(root=root, font=None, name=None, family='Mono', size=26, weight='bold')
smallfont=tkFont.Font(root=root, font=None, name=None, family='Mono', size=25)
Tkinter.mainloop(1) 

def update_window():

  # defaultimg=ImageTk.PhotoImage(Image.open("./init.jpg"))
  # photo=Tkinter.Label(image=defaultimg, width=100, height=100)
  # photo.image=defaultimg
  name=Tkinter.Label(text="", font=bigfont)
  username=Tkinter.Label(text="", font=bigishfont)
  date=Tkinter.Label(text="", font=bigishfont)
  tweet=Tkinter.Label(text="", font=smallfont, wraplength=800, justify="left")
  # photo.pack()
  name.pack(side="top", padx=10, fill="x")
  username.pack(side="top", padx=10, fill="x")
  date.pack(side="top", padx=10, fill="x")
  tweet.pack(side="top", padx=10, fill="x")
  root.update()

  while 1:

    timestamp,user,username,text = yield #, avatar
    name.config(text="\n",user)
    username.config(text=username)
    date.config(text=timestamp+"\n")
    tweet.config(text=text)
    # try:
    #   photo.config(image=Image.open(avatar))
    # except: 
    #   photo.config(image=defaultimg)
    root.update()
    
 