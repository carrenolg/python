# lambda expressions (anonymous functions)
def square(num):
    return num ** 2
# define a lambda
lambda_square = lambda num: num ** 2
# lambda with map
mynums = [1, 2, 3, 4, 5]
list_nums = map(lambda_square, mynums)
# lambda two parameters
lambda_xy = lambda x, y: x * y
#run
print(square(5))
print(lambda_square(5))
for num in list_nums:
    print(num)
print(lambda_xy(5, 5))
