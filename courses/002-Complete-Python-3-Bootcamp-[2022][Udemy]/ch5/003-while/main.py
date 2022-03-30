# while loop
x = 0
while x < 5:
    print(f'The current value of x is {x}')
    x = x + 1
else:
    print(f'The current value of x is greater or equal that {x}')
# keywsord pass
x = [1, 2, 3]
for item in x:
    # comment
    pass
# continue
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        print('go to the top')
        continue
    print(num)
# break
elements = [0, 1, 2, 3, 'a', 5, 6, 7, 8, 9, 10]
for item in elements:
    if item == 'a':
        print('break out the loop')
        break
    print(item)
