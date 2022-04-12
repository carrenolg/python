# LEGB Rule
# L:Local = Names assiggned in any way within a function (def or lambda)
# and not declared global in that function.
# E:Enclosing function locals = Names in the local scope of any and all
# enclosing function, from inner to outer
# G:Global (module) = Names assigned at the top-level of a module file,
# or declared global in a def within the file.
# B:Built-in (Python) = Names preassigned in the built-in names module:
# open, range, SyntaxError...
name = "I'm Sammy from Global"

def greet():
    name = "I'm Sammy from Enclosing function"
    def hello():
        name = "I'm Sammy from Local"
        print('Hello, '+name)
    # call
    hello()
# keyword 'global'
x = 25

def func(x):
    # LOCAL
    print(f'x is = {x}')

def func_global():
    # GLOBAL
    print(f'x is = {x}')
# using keyword
def func_keyword():
    global x
    x = 50
    print(f'x is = {x}')
#run
greet()
func(20)
func_global()
print('global:', x)
func_keyword()
print('global:', x)
