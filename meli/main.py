"""CSV with pet data
id,kind,name,sound
1,dog,fido,woof
2,cat,fluffy,meow
3,bird,tweety,tweet
4,turtle,manuelita,
"""
import csv
from hashlib import new
from typing import List

animals = '''id,kind,name,sound
1,dog,fido,woof
2,cat,fluffy,meow
3,bird,tweety,tweet
4,turtle,manuelita,'''

class Pet:
    """Pet class"""

    def __init__(self, name, kind, sound) -> None:
        self.name = name
        self.kind = kind
        self.sound = sound
    
    def greet(self) -> None:
        """Prints something like 'Hi!, I am a dog and my name is fido, woof!'."""
        print("Hi!, I'm a", self.kind, "and my name is", self.name, ",", self.sound)

def create_animals() -> List[Pet]:
    #with open("animals.csv", "w") as csvfile:
    #    with csv.reader(csvfile) as petfile:
    data:List[Pet] = list()
    items = animals.split('\n')
    for item in items:
        # get fields
        fields = item.split(',')
        animal = Pet(fields[1], fields[2], fields[3])
        data.append(animal)
    return data
