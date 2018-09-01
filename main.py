# main script
import calc
import budget
import newcategory
from tkinter import *

root = Tk()
root.title('Budget Planner')
root.geometry('500x500')

# Functions for buttons
def calcmein():
  calc.mein()
def budgetmein():
  budget.mein()
def itemmein():
  newcategory.mein()

# What should I buy less?
def buymein():
  count=[]
  categories=("Antiques", "Art", "Baby","Books","Business & Industrial","Cameras & Photo","Cell Phones & Accessories","Clothing, Shoes & Accessories","Coins & Paper Money","Collectibles","Computers/Tablets & Networking","Consumer Electronics","Crafts","Dolls & Bears","DVDs & Movies","Entertainment Memorabilia","Gift Cards & Coupons","Health & Beauty","Home & Garden","Jewelry & Watches","Music","Musical Instruments & Gear","Pet Supplies","Pottery & Glass","Real Estate","Specialty Services","Sporting Goods","Sports Mem, Cards & Fan Shop","Stamps","Tickets & Experiences","Toys & Hobbies","Travel","Video Games & Consoles","Everything Else")
  prices = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  itemlist = open('itemlist.txt','r').read() # The entire item list
  itemlist = itemlist.split('\n')
  for i in itemlist: # Change this such that each line is an element in a list.
    icat, inam, ipri, iqty, ipqt = itemlist[itemlist.index(i)].split(',')
    prices[categories.index(icat)] += ipqt
  nobuy = categories[prices.index(max(prices))] # largest number becomes nobuy
  buy = Label(root, justify=CENTER, padx=10, text=str("You should cut down on buying items from this category:\n" + nobuy)).place(relx=0.5, rely=0.3, anchor=CENTER) # reload label
  with open('dontbuy.txt','w') as dontbuy: # Save
    dontbuy.write(nobuy)

try:
  dontbuy = open('dontbuy.txt','r') # Load the file
except:
  nobuy='Something failed! Try clicking "What should I stop buying?" or add an item!' # fail
else:
  nobuy=str(dontbuy.readline()) # Load nobuy
  dontbuy.close()

buy = Label(root, justify=CENTER, padx=10, text=str("You should cut down on buying items from this category:\n" + nobuy)).place(relx=0.5, rely=0.3, anchor=CENTER) # Show which item to buy less

budgetb = Button(root,text="Change budget",command=budgetmein).place(relx=0.5, rely=0.4, anchor=CENTER) # Change Budget button
calcb = Button(root,text="Calculator",command=calcmein).place(relx=0.5, rely=0.5, anchor=CENTER) # Calculator button
newitemb = Button(root,text="New Item...",command=itemmein).place(relx=0.5,rely=0.6,anchor=CENTER) # New Item button
buyless = Button(root,text="What should I stop buying?",command=buymein).place(relx=0.5,rely=0.7,anchor=CENTER) # Calculate buy less item

root.mainloop()
