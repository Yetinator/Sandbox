#Sandbox menuboiler
#Create a menu that does things and break it

import controller
from configurations import *

# Model class here
class Model:
    def __init__(self):
        pass

    def add(self, a, b):
        if type(a) == int:
            if type(b) == int:
                return a + b
            else:
                return "You're a dummy b is wrong"
        else:
            return "You're a dummy a is wrong"

        return "I'm a dummy"
