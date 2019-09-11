#Sandbox menuboiler
#Create a menu that does things and break it

from configurations import *
import model

class Controller():

    def __init__(self):
        #Create a model defined by MenConstruct in the model.py file
        self.init_model()

    def init_model(self):
        self.model = model.Model()

    def dummyMath(self, a, b):
        return self.model.add(a, b)
