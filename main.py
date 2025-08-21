from tkinter import *
from tkinter import ttk
from tkinter import filedialog

def getDirectory():
    return filedialog.askdirectory(initialdir="/", title="Select file")

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Select folders to scan:").grid(column=0, row=0)
ttk.Button(frm, text="Browse", command=getDirectory).grid(column=1, row=1)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=1)
root.mainloop()