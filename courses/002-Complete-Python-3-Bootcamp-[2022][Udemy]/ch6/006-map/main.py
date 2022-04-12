# map
def square(num):
    return num**2
my_nums = [1, 2, 3, 4, 5]
for item in map(square, my_nums):
    print(item)
# iterable
nums_iter = map(square, my_nums)
print(type(nums_iter))
list_num = list(map(square, my_nums))
print(list_num)
# map with strings
