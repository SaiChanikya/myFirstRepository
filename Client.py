'''Local client for a Local machine server.'''

import socket              

s = socket.socket()        
hostName = socket.gethostname() 
portNumber = 12345                

s.connect((hostName, portNumber))
print(s.recv(1024))
s.close()    