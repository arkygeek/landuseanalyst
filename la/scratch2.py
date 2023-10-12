import os
import collections

from pathlib import Path
from uuid import uuid4


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
        print(f"I am a {self.name}")
        return self


myAnimal = Animal()
myAnimal
myAnimal.name = "Bison"
Animal()

print(f"I am a {myAnimal.name} and my GUID is: {myAnimal.guid}")

print(str(Path.home()))
print