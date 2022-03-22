# list [] = square brackets
my_list = ['string', 2, 3.14]
print(my_list)
# len, indexing/slicing, concatenate
first_list = ['one', 'two', 'three']
second_list = ['four', 'five', 'six']
# len
print(len(first_list), len(second_list))
# concatenate
new_list = first_list + second_list
# slicing
print(new_list[0:3])
print(new_list[-3:])
# append, pop
new_list.append('seven') #in-place
print(new_list)
# indexing (changing item)
new_list[0] = 'ONE'
print(new_list)
# pop
new_list.pop(0)
print(new_list)
# remove any item by index
poped_item = new_list.pop(-2)
print(new_list)
# sorted list
alpha_list = ['a', 'e', 'x', 'b', 'c']
num_list = [4, 1, 8, 3]
alpha_list.sort() # in-place
num_list.sort()
print(alpha_list)
print(num_list)
# reverse
num_list.reverse()
print(num_list)
