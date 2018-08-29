from tkinter import *
def mein():
  root = Tk()
  root.title('Please close all tabs')
  Label(root, justify=LEFT, padx=10, text='Item recorded. Please close all tabs.').place(relx=0.5,rely=0.5,anchor=CENTER)
  root.mainloop()
