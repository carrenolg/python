# String properties and methods
from audioop import mul


name = 'Sam'
# change firts letter
# we basically created a new variable
# Using slicing and concatenation
name = 'P' + name[1:]
print(name)
# string multiplication
multi = 'g' * 10
print(multi)
# methods
hello = 'hello world'
print(hello.upper())
# variable is not changed (not in place)
print(hello)
# split
split = 'hello world, this is a string'
print(split.split())