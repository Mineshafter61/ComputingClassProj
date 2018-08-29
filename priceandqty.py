from tkinter import *

class priceandqty:
  def __init__(self,master):
    buttonCmd = 'Done'
    master.title('New Item')
    master.geometry()
    parent = Frame(master)

    # All widgets
    Label(parent, justify=LEFT, padx=10, text='Price').grid(row=0)
    e=Entry(parent)
    e.grid(row=1)

    Label(parent, justify=LEFT, padx=10, text='Quantity').grid(row=2)
    f=Entry(parent)
    f.grid(row=3)

    def inputitemname():
      with open('itemlist.txt','a') as itemlist:
        itemlist.write(str(e.get()+'---'))
        itemlist.write(str(f.get()+'---'))
        itemlist.write(str( float(e.get()) * float(f.get()) + '\n' )

    self.done = Button(parent, text=buttonCmd, command=inputitemname).grid(row=4)

    parent.pack(expand=1)

def mein():
  root = Tk()
  obj=priceandqty(root)
  root.mainloop()
