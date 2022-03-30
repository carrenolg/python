# for
# simple loop
mylist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in mylist:
    print(num)
# loop + control flow
for num in mylist:
    # check for even
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd Number {num}')
# omited variable in loop
for _ in mylist:
    print('Python!')
# unpacking tuples
mylist = [(1, 2), (3, 4), (5,6)]
for (a, b) in mylist:
    print(a, b)
# loop over dict
d = {'k1': 1, 'k2': 3, 'k3': 3,}
for item in d:
    print(item) # print out keys
# print items
for key, value in d.items():
    print(key, value)
