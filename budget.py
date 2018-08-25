#-*-coding: utf-8-*-
from Tkinter import *

class budget:
  def writeBudget(self): # Stores the budget in a text file
    with open('budjconfig.txt','w') as budgetfile:
      budgetfile.write(str(self.newbudj.get()))

  def __init__(self,master):
    master.title('Budget Plan')
    master.geometry()
    head = Label(master, justify = LEFT, padx = 10, text = 'Input new budget:').grid(row=0)

    self.newbudj = Entry(master)
    self.newbudj.grid(row=1,column=0)

    self.done = Button(master,text="Done",command=self.writeBudget).grid(row=2)

#Main
def mein():
  root = Tk()
  obj=budget(root) #object instantiated
  root.mainloop()
mein()
