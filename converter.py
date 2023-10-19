#!/usr/bin/python3

from tkinter import *
from tkinter import ttk

def calculate(*args):
  try:
    value = float(inches.get())
    convertedValue = round(value * 25.4, 4)
    millimeters.set(convertedValue)
    print(convertedValue)
  except ValueError:
    pass


root = Tk()
root.title("Inches to Millimeters")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(row=0, column=0, sticky=(N, W, E, S))
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

inches = StringVar()
millimeters = StringVar()

inchesEntry = ttk.Entry(mainframe, width=7, textvariable=inches)
inchesEntry.grid(row=1, column=2, sticky=(W, E))

ttk.Label(mainframe, textvariable=millimeters).grid(row=2, column=2, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(row=3, column=3, sticky=W)

ttk.Label(mainframe, text="Inches").grid(row=1, column=3, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(row=2, column=1, sticky=E)
ttk.Label(mainframe, text="millimeters").grid(row=2, column=3, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

inchesEntry.focus()
root.bind('<Return>', calculate)

root.mainloop()
