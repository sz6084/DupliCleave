from tkinter import *
from tkinter import ttk
from tkinter import filedialog

import tkinter as tk

class App:
    def __init__(self, window):
        self.window = window
        self.window.title("DupliCleave")
        self.window.geometry("500x340")
        window.minsize(291,62)

        frm = ttk.Frame(window, padding=10)
        frm.grid()
        window.columnconfigure(0, weight=1)
        window.columnconfigure(1, weight=3)
        ttk.Label(frm, text="Select folders to scan:").grid(column=0, row=0)
        ttk.Button(frm, text="Browse", command=self.getDirectory).grid(column=1, row=1)
        ttk.Button(frm, text="Quit", command=frm.quit).grid(column=2, row=1)

    def getDirectory(self):
        path = filedialog.askdirectory(initialdir="~", title="Select a folder")
        if path:
            return path

if __name__ == "__main__":
    window = tk.Tk()
    app = App(window)
    window.mainloop()