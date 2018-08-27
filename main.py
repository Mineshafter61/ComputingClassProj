# main script
import calc
import budget
import newitem
from tkinter import *

root = Tk()
root.title('Budget Planner')
root.geometry("500x500")

# Functions for buttons
def calcmein():
  calc.mein()
def budgetmein():
  budget.mein()
def itemmein():
  newitem.mein()

budgetb = Button(root,text="Change budget",command=budgetmein).place(relx=0.5, rely=0.4, anchor=CENTER) # Change Budget button
calcb = Button(root,text="Calculator",command=calcmein).place(relx=0.5, rely=0.5, anchor=CENTER) # Calculator button
newitemb = Button(root,text="New Item...",command=itemmein).place(relx=0.5,rely=0.6,anchor=CENTER) # New Item button

root.mainloop()
