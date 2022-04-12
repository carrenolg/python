# class and attributes
class Dog():

    def __init__(self, name) -> None:
        self.myname = name

# run
mydog = Dog(name='Toby')
print(type(mydog)) # class '__main__.Dog'
print(mydog) # __main__.Dog object
print(mydog.myname)
