#inputs for other stuff
#Part of Sandbox project
from tkinter import *
from tkinter import Tk

class defaultsMy:
        #This class should become a goto for all defaults in other software
        def testMe():
            print("Hey, is defaultsMy working?")

        def __init__(self):
            self.numberOne = 1
            self.userData = ("First Name", "Last Name", "Phone Number", "Address")
            self.colorScheme = ("Blue", "Turqouise", "Green")

class menuBar(Menu):
        def __init__(self,root):
            Menu.__init__(self,root)
            self.thingy = 1
            fileMenu = Menu(menuBar, tearoff=0)
            secondMenu = Menu(menuBar, tearoff=0)

            fileMenu.add_command(label = "anotherbike", command=anotherBike)
            fileMenu.add_command(label = "exit", command=root.quit)

            secondMenu.add_command(label = "all the bikes")

            menuBar.add_cascade(label="File", menu=fileMenu)
            menuBar.add_cascade(label="second", menu=secondMenu)
