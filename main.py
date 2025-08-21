from tkinter import *
from tkinter import ttk
from tkinter import filedialog

path = ""
def getDirectory():
    path = filedialog.askdirectory(initialdir="/", title="Select a folder") # add mustexist
    if not path:
        return
        # or if path: return path

root = Tk()#className="DupliCleave")
root.geometry("400x250")  # Set window size
root.title("DupliCleave")  # Set window title
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Select folders to scan:").grid(column=0, row=0)
ttk.Button(frm, text="Browse", command=getDirectory).grid(column=1, row=1)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=1)
# maybe display a tree?
root.mainloop()

files = list(path)
for f in files:
    print(f)