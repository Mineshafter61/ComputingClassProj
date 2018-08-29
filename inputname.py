import priceandqty
from tkinter import *

class itemname:
  def __init__(self,master):
    displayHeader='Item name'
    buttonCmd = 'Next'
    master.title('New Item')
    master.geometry()
    parent = Frame(master)

    # All widgets
    Label(parent, justify=LEFT, padx=10, text=displayHeader).grid(row=0)
    e=Entry(parent)
    e.grid(row=1)

    def inputitemname():
      with open('itemlist.txt','a') as itemlist:
        itemlist.write(str(e.get()+','))
      priceandqty.mein()
      root.destroy()

    self.done = Button(parent, text=buttonCmd, command=inputitemname).grid(row=2)

    parent.pack(expand=1)

def mein():
  root = Tk()
  obj=itemname(root)
  root.mainloop()
