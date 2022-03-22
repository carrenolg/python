# Formating to strings
# string interpolation
print('Most Soccer Club in the world is {}'.format('Real Madrid FC'))
colors = 'my favorite colors are {}, {}, and {}'
print(colors.format('green', 'yellow', 'blue'))
subjects = 'my favorite subjects are {}, {}, and {}'
print(subjects.format('math', 'physical', 'programming'))
# named
print('my name is {gio}'.format(gio="Giovanny"))
# working with numbers format
result = 100 / 777
# {value:with.precisionf}
print(result)
print('the result was {r:1.3f}'.format(r=result))
# f string literals
country = 'Brazil'
print(f"I'd like to visit {country}")
