#!/usr/bin/python
# Python banner grabber
import socket
host = "192.168.1.68"
port = 80
request = "HEAD / HTTP/1.1\r\n\r\n"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("socket made")
s.connect((host, port))
print "connected to " + host
s.sendall(request)
print "request sent"
banner = s.recv(4096)
print(banner)
s.close()
