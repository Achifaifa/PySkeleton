#! /usr/bin/env python

import serial, time, tkFont, Tkinter
from PIL import Image, ImageTk

# Windows is created when importing this module
root=Tkinter.Tk()
root.wm_title("PySkeleton")
bigfont=tkFont.Font(root=root, font=None, name=None, family='Mono', size=50, weight='bold')
bigishfont=tkFont.Font(root=root, font=None, name=None, family='Mono', size=26, weight='bold')
smallfont=tkFont.Font(root=root, font=None, name=None, family='Mono', size=25)
Tkinter.mainloop(1) 

# Set up serial port
a=serial.Serial()
a.setBaudrate=(9600)
a.setPort("/dev/ttyACM0")
a.open()
a.write("255,255,255\n")

def sendblinks():

  try: 
    a.write("0,255,0\n")
    time.sleep(1)
    a.write("255,255,255\n")
    time.sleep(1)
  except Exception as e: print e

sendblinks()

def update_window():

  # defaultimg=ImageTk.PhotoImage(Image.open("./init.jpg"))
  # photo=Tkinter.Label(image=defaultimg, width=100, height=100)
  # photo.image=defaultimg
  handle=Tkinter.Label(text="", font=bigfont)
  handlename=Tkinter.Label(text="", font=bigishfont)
  date=Tkinter.Label(text="", font=bigishfont)
  tweet=Tkinter.Label(text="", font=smallfont, wraplength=800, justify="left")
  # photo.pack()
  handle.pack(side="top", padx=10, fill="x")
  handlename.pack(side="top", padx=10, fill="x")
  date.pack(side="top", padx=10, fill="x")
  tweet.pack(side="top", padx=10, fill="x")
  root.update()

  while 1:

    try: 
      timestamp,user,username,text = yield #, avatar
      timestamp=" ".join(timestamp.split()[1:4])
      handle.config(text="\n"+user)
      handlename.config(text="@"+username)
      date.config(text=timestamp+"\n")
      tweet.config(text=text)

    # try:
    #   photo.config(image=Image.open(avatar))
    # except: 
    #   photo.config(image=defaultimg)
      root.update()
      sendblinks()
    except: pass
    
 