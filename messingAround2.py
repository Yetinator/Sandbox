from tkinter import ttk
from tkinter import *
from inputFile import *

#colorsMain = ("Item Name", "Item Brand", "Item Weight (MG)", "Item Purpose", "Item Group", "color")
localDefaults = defaultsMy()
colorsMain = localDefaults.userData
inputUserMain = list()
inputUserString = {}

def exit():
    print("quit")

def anotherBike():
    print("bikes are great")

def screenReturn(inputs):
    #collects inputs from screen
    for item in inputs:
        #create a dictionary
        iterate = inputs.index(item)
        inputUserString[colorsMain[iterate]] = item.get()
        #inputUserString.append(item.get())
        # print(item.get())

def testFunction():
    #prints strings
    for item in inputUserString:
        print(item + " " + inputUserString[item])
    defaultsMy.testMe()

def windowGrid1():
    for r in range(3):
       for c in range(4):
          Label(root, text='R%s/C%s'%(r,c),
             borderwidth=1 ).grid(row=r,column=c)

def windowGrid2(colors, inputUser):

    for color in colors:
        indexLocation = colors.index(color)
        Label(root, text = color, borderwidth=1).grid(row = indexLocation, column = 0)
        #e1 = Entry(root, textvariable=color).grid(row = indexLocation, column = 1)
        entry_id = StringVar() # create an id for your entry, this helps getting the text
        entry = Entry(root, textvariable=entry_id)
        entry.grid(row=indexLocation, column=1)
        inputUser.append(entry)
        #inputUser[index.get()]

    Button(root, text = "Return", command= lambda: screenReturn(inputUser)).grid(row = 10, column = 0)
    Button(root, text = "Quit", command=root.quit).grid(row = 10, column = 1)
    Button(root, text = "Test", command=testFunction).grid(row = 10, column = 2)

root = Tk()
root.minsize(width="500", height="500")
# bar = Menu(root)
bar=menuBar(root)
# menuBar = Menu(root)
#
# fileMenu = Menu(menuBar, tearoff=0)
#
#
# secondMenu = Menu(menuBar, tearoff=0)
#
#
#
# fileMenu.add_command(label = "anotherbike", command=anotherBike)
# fileMenu.add_command(label = "exit", command=root.quit)
#
# secondMenu.add_command(label = "all the bikes")
#
# menuBar.add_cascade(label="File", menu=fileMenu)
# menuBar.add_cascade(label="second", menu=secondMenu)

# menuBar.add_cascade(label="File", menu=fileMenu)

windowGrid2(colorsMain, inputUserMain)

root.config(menu=menuBar)
root.mainloop()
