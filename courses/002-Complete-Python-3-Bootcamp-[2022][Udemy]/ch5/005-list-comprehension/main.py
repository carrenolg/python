# list comprehension
mylist = list(range(0,10))
print(mylist)
pows = [num**2 for num in mylist]
print(pows)
# get each letter
word = 'python'
letters = [item for item in word]
print(letters)
# using if
numbers = range(0, 10)
odds = [num for num in numbers if num % 2 != 0]
print(odds)
# loop nested
elements = [(x * y) for x in [2, 4, 6] for y in [1, 10, 100]]
print(elements)
