# tuple
t = (0, 1, 2)
print(t)
# inmutability
print(t[0])
# t[0] = 5, not support
# like to list
t = ('one', 1/2, [1, 2, 3])
print(t)
# methods - index, count
t = ('a', 'b', 'c', 'd', 'e', 'a', 'a')
index = t.index('a')
print('index:', index)
count = t.count('a')
print('count:', count)
# Support for slicing
print(t[0:3])
