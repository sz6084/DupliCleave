from tkinter import ttk
from tkinter import filedialog

import tkfilebrowser
import tkinter as tk
import os
import pathlib
from pathlib import Path
from filecmp import cmp

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
        ttk.Button(frm, text="Browse", command=self.get_directories).grid(column=1, row=1)
        ttk.Button(frm, text="Quit", command=frm.quit).grid(column=2, row=1)

    def get_directories(self):
        self.dirs = list(tkfilebrowser.askopendirnames())
        if not self.dirs:
            self.dirs = []
            return "N/A"
        self.checkDupes()
        #print(list(self.dirs))

    def checkDupes(self):
        path = self.path
        files = self.files
        print(sorted(os.listdir(path)))
        for i in range(len(files[1])-1):
            if Path(path).rglob(files[1][i]):
                print("directory name match found!")
                print(i)
                #print(files[1][i])
        for i in range(len(files[2])-1):
            if Path(path).rglob(files[1][i]):
                print("filename match found!")
                #print(files[2][i])

if __name__ == "__main__":
    window = tk.Tk()
    app = App(window)
    window.mainloop()