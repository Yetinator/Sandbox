import tkinter as tk

import controller
from configurations import *


class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        #the parent for the above frame was an object that inherited from tk.Tk root window
        #but in this case...
        tk.Frame.__init__(self, parent)
        #LARGE_FONT defined above
        self.controller = controller
        self.parent = parent
        tk.label = tk.Label(self, bg = "purple", text = "Page Three")
        tk.label.pack()
        butt = tk.Button(self, text="Change to Start Page", bg="teal", command=self.func1)
        butt.pack()

    def func1(self):
        self.controller.showFrame()
