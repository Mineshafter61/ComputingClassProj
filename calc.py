#-*-coding: utf-8-*-
from tkinter import *
import math

class calc:
 def getandreplace(self):
  """replace x with * and ÷ with /"""

  self.expression = self.e.get()
  self.newtext=self.expression.replace('÷','/')
  self.newtext=self.expression.replace('mod','%')
  self.newtext=self.newtext.replace('^','**')
  self.newtext=self.newtext.replace('x','*')

 def equals(self):
  """when the equal button is pressed"""

  self.getandreplace()
  try:
   self.value = eval(self.newtext) #evaluate the expression using the eval function
  except SyntaxError or NameErrror:
   self.e.delete(0,END)
   #self.e.insert(0,'Invalid Input!')
   self.e.set(0,'Invalid Input!')
  else:
   self.e.delete(0,END)
   self.e.insert(0,self.value)
   #self.e.set(0,self.value)

 def squareroot(self):
  """squareroot method"""

  self.getandreplace()
  try:
   self.value= eval(self.newtext) #evaluate the expression using the eval function
  except SyntaxError or NameErrror:
   self.e.delete(0,END)
   self.e.insert(0,'Invalid Input!')
  else:
   self.sqrtval=math.sqrt(self.value)
   self.e.delete(0,END)
   self.e.insert(0,self.sqrtval)

 def square(self):
  """square method"""

  self.getandreplace()
  try:
   self.value= eval(self.newtext) #evaluate the expression using the eval function
  except SyntaxError or NameErrror:
   self.e.delete(0,END)
   self.e.insert(0,'Invalid Input!')
  else:
   self.sqval=math.pow(self.value,2)
   self.e.delete(0,END)
   self.e.insert(0,self.sqval)

 def clearall(self):
  """when clear button is pressed,clears the text input area"""
  self.e.delete(0,END)

 def clear1(self): # backspace
  self.txt=self.e.get()[:-1]
  self.e.delete(0,END)
  self.e.insert(0,self.txt)

 def action(self,argi):
  """pressed button's value is inserted into the end of the text area"""
  self.e.insert(END,argi)

 def __init__(self,master):
  """Constructor method"""
  master.title('Calculator')
  master.geometry()
  self.e = Entry(master)
  self.e.place(relx=0.5,rely=0.3,anchor=CENTER)
  self.e.focus_set() #Sets focus on the input text area

  self.div='÷'
  #self.newdiv=self.div.decode('utf-8')

  #Generating Buttons
  parent = Frame(master)
  Button(parent,text="=",width=3,command=lambda:self.equals()).grid(row=4, column=4)
  Button(parent,text="aⁿ",width=3,command=lambda:self.action('^')).grid(row=4, column=5)
  Button(parent,text='AC',width=3,command=lambda:self.clearall()).grid(row=1, column=4)
  Button(parent,text='←',width=3,command=lambda:self.clear1()).grid(row=1, column=5)
  Button(parent,text="+",width=3,command=lambda:self.action('+')).grid(row=4, column=3)
  Button(parent,text="x",width=3,command=lambda:self.action('x')).grid(row=2, column=3)
  Button(parent,text="-",width=3,command=lambda:self.action('-')).grid(row=3, column=3)
  Button(parent,text="÷",width=3,command=lambda:self.action('÷')).grid(row=1, column=3)
  Button(parent,text="mod",width=3,command=lambda:self.action('mod')).grid(row=4, column=2)
  Button(parent,text="7",width=3,command=lambda:self.action(7)).grid(row=1, column=0)
  Button(parent,text="8",width=3,command=lambda:self.action(8)).grid(row=1, column=1)
  Button(parent,text="9",width=3,command=lambda:self.action(9)).grid(row=1, column=2)
  Button(parent,text="4",width=3,command=lambda:self.action(4)).grid(row=2, column=0)
  Button(parent,text="5",width=3,command=lambda:self.action(5)).grid(row=2, column=1)
  Button(parent,text="6",width=3,command=lambda:self.action(6)).grid(row=2, column=2)
  Button(parent,text="1",width=3,command=lambda:self.action(1)).grid(row=3, column=0)
  Button(parent,text="2",width=3,command=lambda:self.action(2)).grid(row=3, column=1)
  Button(parent,text="3",width=3,command=lambda:self.action(3)).grid(row=3, column=2)
  Button(parent,text="0",width=3,command=lambda:self.action(0)).grid(row=4, column=0)
  Button(parent,text=".",width=3,command=lambda:self.action('.')).grid(row=4, column=1)
  Button(parent,text="(",width=3,command=lambda:self.action('(')).grid(row=2, column=4)
  Button(parent,text=")",width=3,command=lambda:self.action(')')).grid(row=2, column=5)
  Button(parent,text="√",width=3,command=lambda:self.squareroot()).grid(row=3, column=4)
  Button(parent,text="x²",width=3,command=lambda:self.square()).grid(row=3, column=5)
  parent.pack(expand=1)
#Main
def mein():
 root = Tk()
 obj=calc(root) #object instantiated
 root.mainloop()
