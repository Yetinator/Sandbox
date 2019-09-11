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
from pagethree import PageThree



class View(tk.Tk):

    #initialize the View object which inherits from the tk.Tk class
    def __init__(self):

        #initialize the tk.Tk portion
        self.controllerObj = controller.Controller()
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
        # PageThree = pagethree.PageThree
        for F in (StartPage, PageTwo, PageThree):
            frame = F(self.containerRight, self)
            self.frames[F] = frame
            # frame.pack(fill=tk.BOTH, expand=1)
            frame.grid(row=0,column=0,sticky="nsew")

        #showFrame is a custom function I make
        self.showFrame(StartPage)

    #Show Screen function
    def showFrame(self, cont=False):
        #pass in a frame to pull forward
        #looking at the frames list at position cont
        if cont == False:
            cont = StartPage
        for gone in self.frames:
            gone.grid_forget(self)

            # frameForget = self.frames[gone]
            # frameForget.pack_forget()

        frame = self.frames[cont]
        frame.tkraise()

        # self.stupidPackSettings(frame)

    #depreciated
    def stupidPackSettings(self, frame):
        #basically pack the frame to spec for the right window
        frame = frame
        frame.config(bg='blue', width = 150)
        frame.pack(fill=tk.BOTH, expand=1)

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
        tk.label = tk.Label(self, bg = "green", text = "StartPage")
        tk.label.pack()
        butt = tk.Button(self, text="Change to Page 2", bg="teal", command=self.func1)
        butt2 = tk.Button(self, text="Change to Page 3", bg="cyan", command=self.func2)

        butt.pack()
        butt2.pack()

    def func1(self):
        self.controller.showFrame(PageTwo)

    def func2(self):
        self.controller.showFrame(PageThree)

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #LARGE_FONT defined above
        self.controller = controller
        self.parent = parent
        label = tk.Label(self, text = "PageTwo")
        label.pack()
        butt = tk.Button(self, text="Change to Start Page", bg="teal", command=self.func1)

        self.a = tk.StringVar()
        self.b = tk.StringVar()
        box1 = tk.Entry(self, text="Add value 1: ", textvariable=self.a)
        box2 = tk.Entry(self, text="Add value 2: ", textvariable=self.b)

        equalsButt = tk.Button(self, text="Equals", bg="yellow", command=self.getNums)



        butt.pack()
        box1.pack()
        box2.pack()
        equalsButt.pack()

    def func1(self):
        self.controller.showFrame(StartPage)

    def getNums(self):
        firstNum = int(self.a.get())
        secondNum = int(self.b.get())
        result = self.controller.controllerObj.dummyMath(firstNum, secondNum)
        print(result)



#start the app
app = View()
app.mainloop()
