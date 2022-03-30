# range (generator)
for x in range(10):
    print(x)
# with step
for x in range(0, 20, 2):
    print(x)
# generator
gen = range(0, 5)
print(gen)
numbers = list(gen)
print(numbers)
# enumerate
word = 'python'
for item in enumerate(word):
    print(item)
# unpacking
for index, value in enumerate(word):
    print(index, value)
# zip
mylist1 = [1, 2, 3, 4]
mylist2 = ['a', 'b', 'c', 'd']
for item in zip(mylist1, mylist2):
    print(item)
# in
result = 'x' in [0, 1, 2]
print(result)
result = 'python' in "we love python"
print(result)
result = 'k1' in {'k0': 0, 'k1': 1}
print(result)
# min - max
letters = "abcdefghijk"
print(min(letters)) # 'a'
print(max(letters)) # 'k'
# random
from random import shuffle
characters = ['a', 'b', 'c']
shuffle(characters)
print(characters)
from random import randint
print(randint(0, 10))
