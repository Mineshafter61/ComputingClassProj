#-*-coding: utf-8-*-
import inputname # Next tab
from tkinter import *

class item:
  def __init__(self,master):
    '''variables and constructor'''
    displayHeader='Category\n\n'
    buttonCmd='Next'
    master.title('New Item')
    master.geometry()
    parent = Frame(master)

    # All widgets
    Label(parent, justify=LEFT, padx=10, text=displayHeader).grid(row=0) # header
    cat = StringVar(master); cat.set("Select..."); catoptions = OptionMenu(master, cat, "Antiques", "Art", "Baby","Books","Business & Industrial","Cameras & Photo","Cell Phones & Accessories","Clothing, Shoes & Accessories","Coins & Paper Money","Collectibles","Computers/Tablets & Networking","Consumer Electronics","Crafts","Dolls & Bears","DVDs & Movies","Entertainment Memorabilia","Food","Gift Cards & Coupons","Health & Beauty","Home & Garden","Jewelry & Watches","Music","Musical Instruments & Gear","Pet Supplies","Pottery & Glass","Real Estate","Specialty Services","Sporting Goods","Sports Mem, Cards & Fan Shop","Stamps","Tickets & Experiences","Toys & Hobbies","Travel","Video Games & Consoles","Everything Else"); catoptions.place(relx=0.5,rely=0.5,anchor=CENTER) # Categories and Selection

    def inputnext():
      with open('itemlist.txt','a') as itemlist: # Write category to itemlist
        itemlist.write(str(cat.get()+','))
      inputname.mein()
      root.destroy()

    self.done = Button(parent,text = buttonCmd,command=inputnext).grid(row=2) # Next

    parent.pack(expand=1)

def mein(): # Main script
  root = Tk()
  obj=item(root)
  root.mainloop()
