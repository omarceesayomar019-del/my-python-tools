import socket
s=input("Site: ")
try:
 socket.gethostbyname(s)
 print(s,"ONLINE")
except:
 print(s,"OFFLINE")
