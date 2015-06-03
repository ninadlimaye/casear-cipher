#!/usr/bin/python

import socket

import sys

print ("Address is: %s" % str(sys.argv[1]))
print ("Port number is: %s" % str(sys.argv[2]))
print ("Message is: %s" % str(sys.argv[3:]))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = str(sys.argv[1])
port = int(sys.argv[2])

s.connect((host, port))
# print s.recv(1024)
message = str(sys.argv[3:])
print "Sending message to server"
s.send(message)

final = s.recv(1024)

s.close()

print "The translated message is", final
