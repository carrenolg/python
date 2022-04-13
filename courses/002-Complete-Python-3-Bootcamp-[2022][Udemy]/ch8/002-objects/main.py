# class and attributes
class Dog():
    # class object attributes
    species = 'mammal'

    # attributes
    def __init__(self, breed, name, spots) -> None:
        self.mybreed = breed
        self.myname = name
        self.myspots = spots
    
    # Methods
    def bark(self):
        print("Woof! My name is {}".format(self.myname))

# new class
class Circle:

    # Class object attribute
    PI = 3.14

    # init
    def __init__(self, radius) -> None:
        self.radius = radius

    # Method
    def get_circumference(self):
        return self.radius * Circle.PI * 2
# run
mydog = Dog(breed='Lab', name='Toby', spots=False)
print(type(mydog)) # class '__main__.Dog'
print(mydog) # __main__.Dog object
print(mydog.myname)
print(mydog.species)
mydog.bark()
mycircule = Circle(radius=5)
print('Circumference:', mycircule.get_circumference())