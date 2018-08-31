import priceandqty # next item
from tkinter import *

class itemname:
  def __init__(self,master):
    '''constructor and variables'''
    displayHeader='Item name'
    buttonCmd = 'Next'
    master.title('New Item')
    master.geometry()
    parent = Frame(master)

    # All widgets
    Label(parent, justify=LEFT, padx=10, text=displayHeader).grid(row=0) # header
    e=Entry(parent) # Text box
    e.grid(row=1)

    def inputitemname(): # Add the product name to the itemlist
      with open('itemlist.txt','a') as itemlist:
        itemlist.write(str(e.get()+','))
      priceandqty.mein()
      root.destroy()

    self.done = Button(parent, text=buttonCmd, command=inputitemname).grid(row=2) # the 'next' button

    parent.pack(expand=1)

def mein(): # Main script
  root = Tk()
  obj=itemname(root)
  root.mainloop()
