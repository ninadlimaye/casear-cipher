#!/usr/bin/python

import socket

import sys

print ("Port number is: %s" % str(sys.argv[1]))
print ("Shift number is: %s" % str(sys.argv[2]))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
print host
port = int(sys.argv[1])
shft = int(sys.argv[2])

def cipher(message, shift):
        new = ''
        
	for a in message:
            if a.isalpha():
             	num = ord(a)
             	num += shift

             	if a.isupper():
                	 if num > ord('Z'):
                     		num -= 26
                 	 elif num < ord('A'):
                     		num += 26
            	elif a.islower():
                	 if num > ord('z'):
                     		num -= 26
                 	 elif num < ord('a'):
                     		num += 26

             	new += chr(num)
            else:
           	new += a
        return new

s.bind((host, port))

s.listen(1)
c, addr = s.accept()
print 'Connected with:', addr

while True:
   msg = c.recv(1024)
   final = cipher(msg, shft)
   c.send(final)
c.close()
