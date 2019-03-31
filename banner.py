#!/usr/bin/python
# Python banner grabber
import socket
import sys

# Command line arguments are host (1) and port (2)
host = sys.argv[1]
port = int(sys.argv[2])
http_request = "GET / HTTP/1.1\r\n\r\n" #The request for HTTP port 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "socket made"
s.connect((host, port))
print "connected to " + host
s.sendall(http_request)
print "request sent"
banner = s.recv(4096)
print(banner)
s.close()
print "All done boss"
