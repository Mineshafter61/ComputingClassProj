#-*-coding: utf-8-*-
import thanks # Next tab
from tkinter import *

class item:
  def __init__(self,master):
    '''variables and constructor'''
    displayHeaderItemName='Item name'
    buttonCmd='Delete!'
    master.title('Delete Item')
    master.geometry()
    parent = Frame(master)

    # All widgets
    with open("itemlist.txt",'r') as itemlist:

      # Options Parser
      itemlistlist=[]
      line = itemlist.readline()
      while line:
        itemlistlist.append(line.split(",")[1])
        line = itemlist.readline()
      itemlistlist=tuple(itemlistlist)

      # Select item to delete
      cat = StringVar(master); cat.set("Select item to delete..."); catoptions = OptionMenu(master, cat, *itemlistlist); catoptions.place(relx=0.5,rely=0.35,anchor=CENTER);

      # Does nothing

    # Function for Next button
      def inputnext():
        with open("itemlist.txt",'r') as itemlist:
          f = itemlist.readlines()
        with open("itemlist.txt",'w') as itemlist:
          for line in f:
            if cat.get() not in line:
              itemlist.write(line)


    self.done = Button(parent,text = buttonCmd,command=inputnext).grid(row=9) # Next

    parent.pack(expand=1)

def mein(): # Main script
  root = Tk()
  obj=item(root)
  root.mainloop()
