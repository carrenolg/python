# *args - *kwargs
def myfunc(args):
    print(tuple(args))
# star arguments
def star_args(*args):
    print(args)
# doble star arguments
def doble_star_argms(**kwargs):
    print('dict', kwargs)
    if 'fruit' in kwargs:
        print("My fruit of chose is {}".format(kwargs['fruit']))
# run
mylist = [0, 1, 2, 3]
myfunc(mylist)
star_args(0, 1, 2, 3)
doble_star_argms(fruit='banana', veggie ='lettuce')
# exercise
def get_string(data):
    result = ""
    for index, char in enumerate(data):
        if index % 2 != 0:
            result = result + char.capitalize()
        else:
            result = result + char.lower()
    return result
result = get_string('abcdefg')
print(result)