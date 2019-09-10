#Sandbox menuboiler
#Create a menu that does things and break it

#frame forward implementation and MVC implentation

#MVC
#init(parent, controller) - the parent is a tk.Tk root object created in main

#frame forward - really obscure varibles imported - can I be less obscure and have it work?
#class name(tk.Tk)
#   init(self, args, kwargs)
#       tk.Tk.init(self, args, kwargs)
import tkinter as tk

import controller
from configurations import *



class View(tk.Tk):

    #initialize the View object which inherits from the tk.Tk class
    def __init__(self):

        #initialize the tk.Tk portion
        tk.Tk.__init__(self)

        #back to View Code
        self.geometry(SCREEN_GEOMETRY)
        self.createInterfaceBase()
        self.createSubFramesRight()

    #Initialzer function
    def createInterfaceBase(self):
        #create the main window layout for the menu and software
        self.containerLeft = tk.Frame(self, width = 150, bg="green")
        self.containerRight = tk.Frame(self, width = 150, bg="red")


        self.containerLeft.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        self.containerRight.pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)

    #Initialzer function
    def createSubFramesRight(self):
        #This is the code for the frame forward implementation
        self.frames = {}
        for F in (StartPage, PageTwo):
            frame = F(self.containerRight, self)
            self.frames[F] = frame
            frame.pack(fill=tk.BOTH, expand=1)

        #showFrame is a custom function I make
        self.showFrame(StartPage)

    #Show Screen function
    def showFrame(self, cont):
        #pass in a frame to pull forward
        #looking at the frames list at position cont
        for gone in self.frames:
            gone.pack_forget(self)
        frame = self.frames[cont]
        frame.tkraise()

    #ToDo
    # Should I remove each frame class to a different file?
    # there may be circular imports if I do.
    # Some pages may need info from the controller
    # Some pages will feed info to the controller
    # Should that info pass through the view model?
    # Will the class object existing in the view model be enough to not need to import controller to the class itself?
    # build two pages here, and a third in it's own file and see how it works.

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        #the parent for the above frame was an object that inherited from tk.Tk root window
        #but in this case...
        tk.Frame.__init__(self, parent)
        #LARGE_FONT defined above
        self.controller = controller
        self.parent = parent
        label = tk.Label(self, text = "StartPage")
        label.pack()

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #LARGE_FONT defined above
        self.controller = controller
        label = tk.Label(self, text = "PageTwo")
        label.pack()



#start the app
app = View()
app.mainloop()
