#-*-coding: utf-8-*-
from tkinter import *

class item:
  def nxt():
    pass
  def __init__(self,master):
    displayHeader='Category'
    buttonCmd='Next'
    master.title('New Item')
    master.geometry()
    parent = Frame(master)

    # All widgets
    Label(parent, justify = LEFT, padx = 10, text = displayHeader).grid(row=0)
    self.newbudj = Entry(parent)
    self.newbudj.grid(row=1)
    self.done = Button(parent,text=buttonCmd,command=self.next).grid(row=2) # activation
    parent.pack(expand=1)

def mein():
  root = Tk()
  obj=item(root) #object instantiated
  root.mainloop()
