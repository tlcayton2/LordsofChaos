# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 10:11:47 2015

@author: Ayme
"""

#from Tkinter import *
# if you are working under Python 3, comment the previous line and comment out the following line
from tkinter import *
class App:
  def __init__(self, master):
    frame = Frame(master)
    frame.pack()
    self.button = Button(frame, 
                         text="QUIT", fg="red",
                         command=frame.quit)
    self.button.pack(side=LEFT)
    self.slogan = Button(frame,
                         text="Hello",
                         command=self.write_slogan)
    self.slogan.pack(side=LEFT)
  def write_slogan(self):
    print("Tkinter is easy to use!")

root = Tk()
app = App(root)
root.mainloop()