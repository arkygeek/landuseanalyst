import os
import collections
from pathlib import Path
from uuid import uuid4
from la.lib.lautils import LaMessageBus

MESSAGE_BUS = LaMessageBus()

class Animal:
    def __init__(self,
                 theName = None,
                 theDescription = None,
                 theValue = None,
                 theUsableMeat = None,
                 theKillWeight = None,
                 theGuid = None
                ):
        self.name = theName
        self.description = theDescription
        self.meatFoodValue = theValue
        self.usableMeat = theUsableMeat
        self.killWeight = theKillWeight
        self.guid = uuid4()

    def __repr__(self):
        return "Animal()"

    def __str__(self):
        MESSAGE_BUS.debug(f"I am a {self.name}")
        return self


myAnimal = Animal()
myAnimal
myAnimal.name = "Bison"
Animal()

MESSAGE_BUS.debug(f"I am a {myAnimal.name} and my GUID is: {myAnimal.guid}")
MESSAGE_BUS.debug(str(Path.home()))