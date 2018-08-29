#-*-coding: utf-8-*-
import inputname
from tkinter import *

class priceandquantity:
  def __init__(self,master):
    pass

class item:
  def __init__(self,master):
    displayHeader='Category\n\n'
    buttonCmd='Next'
    master.title('New Item')
    master.geometry()
    parent = Frame(master)

    # All widgets
    Label(parent, justify=LEFT, padx=10, text=displayHeader).grid(row=0)
    cat = StringVar(master); cat.set("Select..."); catoptions = OptionMenu(master, cat, "Food", "Fashion", "Groceries","Electronics","Furniture","Travel","Others"); catoptions.place(relx=0.5,rely=0.5,anchor=CENTER) # Selection

    def inputnext():
      global itemarr
      with open('itemlist.txt','a') as itemlist:
        itemlist.write(str(cat.get()+'---'))
      inputname.mein()
      self.root.destroy()

    self.done = Button(parent,text = buttonCmd,command=inputnext).grid(row=2) # Next

    parent.pack(expand=1)

def mein():
  root = Tk()
  obj=item(root)
  root.mainloop()
