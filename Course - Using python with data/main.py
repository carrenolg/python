# ASCII
'''
print('H')
print(ord('H'))
x = 'abc'
print(type(x))
x = u'abc'
print(type(x))
x = b'abc'
print(type(x))
'''

# HTTP request
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/2.0\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()
