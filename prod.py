from tkinter import ttk
from tkinter import filedialog

import tkinter as tk
import os

class App:
    def __init__(self, window):
        self.window = window
        self.window.title("DupliCleave")
        self.window.geometry("500x340")
        window.minsize(291,62)

        self.treeView = ttk.Treeview() # create columns

        frm = ttk.Frame(window, padding=10)
        frm.grid()
        window.columnconfigure(0, weight=1)
        window.columnconfigure(1, weight=3)
        ttk.Label(frm, text="Select folders to scan:").grid(column=0, row=0)
        self.selected_dir = ttk.Label(frm, text="No folder selected")
        self.selected_dir.grid(column=0,row=1)
        ttk.Button(frm, text="Browse", command=self.getDirectory).grid(column=1, row=1)
        ttk.Button(frm, text="Quit", command=frm.quit).grid(column=2, row=1)

    def getDirectory(self):
        self.path = filedialog.askdirectory(initialdir="~", title="Select a folder") # ~add mustexist~
        path = self.path
        if path:
            self.selected_dir.config(text=path)
            self.files=next(os.walk(path, topdown=True, followlinks=True))
            #for root, dirnames, filenames in os.walk(path):
            #    print(root)
            #    print(dirnames)
            #    print(filenames)
            #    print('---')
            #print(self.files)
            self.checkDupes()
            #self.treeView.insert(tk.END, path)
            #return self.path
    #@staticmethod
    def checkDupes(self):
        path = self.path
        files = self.files
        for i in range(len(self.files[1])-1):
            if files[i] in files[i+1:]:
                print("directory name match found!")
                print(files[i])
        for i in range(len(self.files[2])-1):
            if files[i] in files[i+1:]:
                print("filename match found!")
                print(files[i])

if __name__ == "__main__":
    window = tk.Tk()
    app = App(window)
    window.mainloop()