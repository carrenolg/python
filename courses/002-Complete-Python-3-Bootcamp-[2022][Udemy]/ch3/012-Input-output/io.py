# i/o
myfile = open('myfile.txt')
print(myfile.read())
print('file:', myfile.read())
# reset cursor to zero
myfile.seek(0)
print('file', myfile.read())
# get all content
myfile.seek(0)
content = myfile.read()
print(content)
# get lines into a list
myfile.seek(0)
lines = myfile.readlines()
print(lines)
# with
with open('myfile.txt') as new_file:
    content = new_file.read()
    print('printing using "with"')
    print(content)
# add new line
with open('newfile.txt', mode='a') as f:
    f.write('\nLAST LINE')
# read
with open('newfile.txt', mode='r') as f:
    content = f.read()
    print(content)
# overiding
with open('another_file.txt', mode='w') as f:
    f.write('\nI created this file.')
with open('another_file.txt', mode='r') as f:
    print(f.read())
