#-*-coding: utf-8-*-
import thanks # Next tab
from tkinter import *

class item:
  def __init__(self,master):
    '''variables and constructor'''
    displayHeaderCategory='Category\n\n'
    displayHeaderItemName='Item name'
    buttonCmd='Next'
    master.title('New Item')
    master.geometry()
    parent = Frame(master)

    # All widgets
    Label(parent, justify=LEFT, padx=10, text=displayHeaderCategory).grid(row=0) # header
    cat = StringVar(master); cat.set("Select..."); catoptions = OptionMenu(master, cat, "Antiques", "Art", "Baby","Books","Business & Industrial","Cameras & Photo","Cell Phones & Accessories","Clothing, Shoes & Accessories","Coins & Paper Money","Collectibles","Computers/Tablets & Networking","Consumer Electronics","Crafts","Dolls & Bears","DVDs & Movies","Entertainment Memorabilia","Food","Gift Cards & Coupons","Health & Beauty","Home & Garden","Jewelry & Watches","Music","Musical Instruments & Gear","Pet Supplies","Pottery & Glass","Real Estate","Specialty Services","Sporting Goods","Sports Mem, Cards & Fan Shop","Stamps","Tickets & Experiences","Toys & Hobbies","Travel","Video Games & Consoles","Everything Else"); catoptions.place(relx=0.5,rely=0.35,anchor=CENTER) # Categories and Selection



    Label(parent, justify=LEFT, padx=10, text=displayHeaderItemName).grid(row=2) # header
    e=Entry(parent) # Text box
    e.grid(row=3)



    Label(parent, justify=LEFT, padx=10, text='Price').grid(row=4) # header (price)
    g=Entry(parent) # entry field for price
    g.grid(row=5)

    Label(parent, justify=LEFT, padx=10, text='Quantity').grid(row=6) # header (quantity)
    f=Entry(parent) # entry field for quantity
    f.grid(row=7)



    def inputnext():
      with open('itemlist.txt','a') as itemlist: # Write category to itemlist
        itemlist.write(str(cat.get()+','))
        itemlist.write(str(e.get()+','))
        itemlist.write(str(g.get()+',')) # Write the price
        itemlist.write(str(f.get()+',')) # Write the quantity
        itemlist.write(str( str(float(g.get()) * float(f.get())) + '\n' )) # Write total and add new line

      thanks.mein()
      self.root.destroy()

    self.done = Button(parent,text = buttonCmd,command=inputnext).grid(row=9) # Next

    parent.pack(expand=1)

def mein(): # Main script
  root = Tk()
  obj=item(root)
  root.mainloop()
