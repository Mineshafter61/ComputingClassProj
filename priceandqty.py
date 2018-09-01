import thanks # Next item
from tkinter import *

class priceandqty:
  def __init__(self,master): # Constructor
    buttonCmd = 'Done'
    master.title('New Item')
    master.geometry()
    parent = Frame(master)

    # All widgets
    Label(parent, justify=LEFT, padx=10, text='Price').grid(row=0) # header (price)
    e=Entry(parent) # entry field for price
    e.grid(row=1)

    Label(parent, justify=LEFT, padx=10, text='Quantity').grid(row=2) # header (quantity)
    f=Entry(parent) # entry field for quantity
    f.grid(row=3)

    def inputitemname():
      with open('itemlist.txt','a') as itemlist:
        itemlist.write(str(e.get()+',')) # Write the price
        itemlist.write(str(f.get()+',')) # Write the quantity
        itemlist.write(str( str(float(e.get()) * float(f.get())) + '\n' )) # Write total and add new line
      thanks.mein() # Shows done tab
      global root
      root.destroy()

    self.done = Button(parent, text=buttonCmd, command=inputitemname).grid(row=4)

    parent.pack(expand=1)

def mein(): # Main
  root = Tk()
  obj=priceandqty(root)
  root.mainloop()
