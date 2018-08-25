#-*-coding: utf-8-*-
from Tkinter import *

class budget:
  def writeBudget(self): # Stores the budget in a txt file
    with open('budjconfig.txt','w') as budgetfile:
      budgetfile.write(str(self.newbudj.get()))

  def __init__(self,master):
    master.title('Change Budget')
    master.geometry()
    head = Label(master, justify = LEFT, padx = 10, text = 'Input new budget:').place(relx=0.5,rely=0.4,anchor=CENTER) # header text

    # input field for budget
    self.newbudj = Entry(master)
    self.newbudj.place(relx=0.5,rely=0.5,anchor=CENTER)

    self.done = Button(master,text="Done",command=self.writeBudget).place(relx=0.5,rely=0.6,anchor=CENTER) # activation

#Main
def mein():
  root = Tk()
  obj=budget(root) #object instantiated
  root.mainloop()
