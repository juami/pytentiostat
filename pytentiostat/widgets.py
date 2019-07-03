from tkinter import *
from main import ProgramSetup as PS


def show_entry_fields():
   print("Max Voltage: %s\nMinimum Voltage: %s" % (e1.get(), e2.get()))
   print("scalar:",e3.get())
   max_v = float(e1.get())
   min_v = float(e2.get())
   s = float(e3.get())
   e1.delete(0,END)
   e2.delete(0,END)
   test.LSV(min_v, max_v, PlotCommand, WriteCommand)


test = PS()
test.setup_arduino()
PlotCommand = True
WriteCommand = False
master = Tk()
Label(master, text="Maximum Voltage").grid(row=0)
Label(master, text="Minimum Voltage").grid(row=1)
# Label(master, text="Scan Rate").grid(row=2)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)


e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Plot', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
# Button(master, text='Pause', command=pltClose).grid(row=3, column=2, sticky=W, pady=4)

mainloop()