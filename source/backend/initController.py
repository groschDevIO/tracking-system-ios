import socket
import getpass
import json

username = raw_input("Special username: ")
password = getpass.getpass("Special password: ")

HOST = 'daring.cwi.nl'
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(username, " ", password)
data = s.recv(1024)
s.close()
print 'Received', repr(data)