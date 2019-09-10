#raspTkinter

from abc import ABC, abstractmethod
from tkinter import *
from tkinter import Tk
import tkinter as tk
import tkinter.filedialog
from tkinter import ttk
import time
# import RPi.GPIO as GPIO

global rando
rando = 1

class AbstractWindow(ABC, tk.Tk):

    def NewFile(self):
        print ("New File called from super class")
    def OpenFile(self):
        print("OpenFile called from super class")
    def About(self):
        print ("About called from super class")

    def MakeFileMenu(self):
        self.menu = Menu()
        self.config(menu=self.menu)
        filemenu = Menu(self.menu)
        self.menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New", command=self.NewFile)
        filemenu.add_command(label="Open...", command=self.OpenFile)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit)

        helpmenu = Menu(self.menu)
        self.menu.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About...", command=self.About)

    def MakeScreen(self):
        self.label = tk.Label(text="Hello, world\nThis label was created in the super class")
        self.label.pack(padx=10, pady=10)


    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        ABC.__init__(self, *args, **kwargs)
        self.MakeFileMenu()
        self.MakeScreen()

class MyWindow(AbstractWindow, tk.Tk):
    #MakeScreen > MakeButtons, MakeGrid, MakeClock (LOOP MakeClock?)
    windowHeight = 240
    windowWidth = 320


    def ExitProgram(self):
        self.myButtons.buttonEnd()
        self.quit()

    def MakeScreen(self):
        #this is called in the constructer as part of the superclass
        #it basically calls other aspects of the screen that could probably be frames
        # self.label = tk.Label(text="Lap")
        # self.label.pack(padx=10, pady=10)
        width = 12
        height = 7
        label1 = Label(text = "woohoo", height=height, width=width).grid(row=0, column = 0)
        label2 = Label(text = "yowzaa", height=height, width=width).grid(row=0, column = 1)
        label3 = Label(text = "waaaaa", height=height, width=width).grid(row=1, column = 0)
        label4 = Label(text = "sup bro", height=height, width=width).grid(row=1, column = 1)

        style = ttk.Style()
        style.configure("label1",
                foreground="midnight blue",
                font="Times 20 bold italic",
                padding=20)

    def MakeButtons(self):

        item_index = 0
        Button(text='Quit', command=self.ExitProgram).grid(row=self.position_button_row, column=item_index, sticky=W, pady=4)
        item_index += 1
        Button(text='Log Inputs', command=self.GetInputs).grid(row=self.position_button_row, column=item_index, sticky=W, pady=4)
        item_index += 1
        Button(text='Test something', command=self.test_button).grid(row=self.position_button_row, column=item_index, sticky=W, pady=4)
        item_index += 1
        Button(text='Peloton Split', command=self.peloton_split_button).grid(row=self.position_button_row, column=item_index, sticky=W, pady=4)
        item_index += 1
        Button(text='Breakaway Split', command=self.breakaway_split_button).grid(row=self.position_button_row, column=item_index, sticky=W, pady=4)
        item_index += 1
        Button(text='Start Timer', command=self.start_button).grid(row=self.position_button_row, column=item_index, sticky=W, pady=4)

    # def HardButtons(self, aButton):
    #     if aButton == False:
    #         pass
    #
    #     if aButton ==  'a':
    #         self.peloton_split_button()
    #
    #     if aButton == 'b':
    #         self.breakaway_split_button()
    #
    #     if aButton == 'c':
    #         self.start_button()

    def looptie_loop(self):
        #any potential looping in this class should be limited to here, or mainloop
        # self.RefreshClock()
        out = False
        # out = self.myButtons.get()
        # self.HardButtons(out)
        #if out != False:
        #    print(str(out))
        #    time.sleep(0.2)

        self.after(1, self.looptie_loop)



    def __init__(self, *args, **kwargs):
        #makeConfigure is just my configuration file
        AbstractWindow.__init__(self, *args, **kwargs)
        # self.myButtons = piButtons()
        self.looptie_loop()

# class piButtons:
#     #This should interface with whatever hard buttons exist on the raspberry pi
#     def __init__(self, inButtons = ['a','b','c','d']):
#         GPIO.setmode(GPIO.BCM)
#         self.chan_list = [17,22,23,27]
#         self.buttons = inButtons
#         GPIO.setup(self.chan_list, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#
#     def get(self):
#         button = False
#         for i in range(len(self.chan_list)):
#             if GPIO.input(self.chan_list[i]) == False:
#                 #print(str(i) + ' Button Pressed')
#                 button = self.buttons[i]
#         return button
#
#     def buttonEnd(self):
#          self.run = False
#          GPIO.cleanup()

tempWindow = MyWindow()
tempWindow.geometry("320x240+100+100")
tempWindow.resizable(width=False, height=False)

mainloop()
