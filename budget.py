from Tkinter import *

def writeBudget(budg):
  with open('budget.txt','w') as budgetfile:
    budgetfile.write(str(budg))
