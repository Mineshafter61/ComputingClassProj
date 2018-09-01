from tkinter import *
def mein(): # script to tell user that the product has been recorded
  root = Tk()
  root.title('Please close all tabs')

  itemlist = open('itemlist.txt','r')
  budjconfig = open('budjconfig.txt','r+')
  lastitem = float(((list(itemlist)[-1]).split(','))[-1])
  budj = float(list(budjconfig)[-1])
  rem = budj - lastitem
  budjconfig.write(str(rem)+'\n')
  itemlist.close()
  budjconfig.close()

  if rem > 0:
    Label(root, justify=CENTER, padx=10, text='Item recorded. Please close all tabs.\nYour remaining budget is: '+str(rem)).place(relx=0.5,rely=0.5,anchor=CENTER)
  else:
    Label(root, justify=CENTER, padx=10, text='Item recorded. Please close all tabs.\nOH NO!!! YOU SPENT ALL YOUR MONEY!!! You owe: '+str(abs(rem))).place(relx=0.5,rely=0.5,anchor=CENTER)
  root.mainloop()
mein()
