# main script
import calc
import budget
from Tkinter import *

root = Tk()
root.title('Budget Planner')
root.geometry("500x500")

def calcmein():
  calc.mein()
def budgetmein():
  budget.mein()

budgetb = Button(root,text="Change budget",command=budgetmein).place(relx=0.5, rely=0.4, anchor=CENTER)
calcb = Button(root,text="Calculator",command=calcmein).place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()
