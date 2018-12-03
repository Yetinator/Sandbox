#From Sandbox
import readline
import string
from pathlib import Path
import copy

class ReadFile:
    #This class is mainly meant to read variables stored in a text file, and
    #store those variables as a dictionary using the .dictionaryData function
    #These variables can then be used for program configuration or other inputs
    #correct usage would be to have each line in the .txt file represent a
    # different value in the dictionary.  Seperate the values by a colon :
    # ie- First_Name:Brian will create a dictionary entry of First_Name = Brian

    def readFile(self):
        self.thisData = self.file_object.read()
        return self.thisData

    def openFile(self, fileName):
        self.file_object = open(fileName, 'r')

    def closeFile(self):
        pass

    def getValuesAsDictionary(self):
        print('making Dictionary')
        #loop through items either in file or in string variable
        for i in range(10):
            #TODO improve for loop

            #Read a line and split
            x = self.file_object.readline().split(':')

            #add line to dictionaryData
            if(len(x)>1):
                #get rid of endline charactor
                if x[1].endswith('\n'):
                    x[1] = x[1][0:-1]
                self.dictionaryData[x[0]] = x[1]
        return self.dictionaryData
        #self.thisData = self.file_object.read()
        # for line in self.file_object.read():
        #     a = line.split(':')
        #     print(a)

    def __init__(self, fileName):
        self.fileName = fileName
        self.openFile(fileName)
        self.dictionaryData = dict()

class WriteFile:
    #This class is mainly meant to write variables to be stored in a text file, and
    # those variables can be accessed as a dictionary using the ReadFile Class
    #This is meant to be a permanent storage for dictionaryData so that it can
    #be refered to later.  This is a really low grade database
    #correct usage would be to have each line in the .txt file represent a
    # different value in the dictionary.  Seperate the values by a colon :
    # ie- First_Name:Brian will create a dictionary entry of First_Name = Brian
    def readFile(self):
        print('reading file')
        self.thisData = self.file_object.read()
        print('read file complete')
        return self.thisData

    def openFile(self, fileName):
        print('opening file')
        filePath = Path(fileName)
        if filePath.is_file():
            print('warning! Filename already exists.  Will be written over')
        self.file_object = open(fileName, 'w')
        print('opened file')

    def closeFile(self):
        pass

    def saveValuesAsDictionary(self):
        combineText = list()
        for i in self.dictionaryData:
            # print(type(i))
            # print(i)
            # print(self.dictionaryData[i])
            # thisLine = i + self.dictionaryData[i] + "\n"
            thisLine = ":".join((i,self.dictionaryData[i]))
            combineText.append(thisLine)
            # self.localText.join(thisLine)
        # print("the list is")
        # print(combineText)
        newText = "\n".join(combineText)
        # print("newText is")
        # print(newText)
        with open(self.fileName, 'w') as f:
            print(newText, file=f)

    def __init__(self, fileName, inputDictionary):
        self.fileName = fileName
        self.dictionaryData = copy.deepcopy(inputDictionary)
        self.openFile(fileName)
        self.localText = string
        # print(inputDictionary)
        # print("inputDictionary type = ")
        # print(type(inputDictionary))
        # print("dictionaryData type = ")
        # print(type(self.dictionaryData))
