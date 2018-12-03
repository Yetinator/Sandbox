#this is part of Sandbox
from tkinter import *
from tkinter import Tk
from writeClass import WriteFile
from writeClass import ReadFile

thisFile = ReadFile('sampleData.txt')
# thisTextNasty = thisFile.readFile()
# print(thisTextNasty)
thisText = thisFile.getValuesAsDictionary()
print(thisText)
print(thisText['First_Name '])

print("moving to write file")
thisWriteFile = WriteFile('savedSampleData.txt', thisText)
thisWriteFile.saveValuesAsDictionary()
