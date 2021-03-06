'''Local machine server for Local client'''

import socket               

s = socket.socket()         
hostName = socket.gethostname() 
portNumber = 12345                

s.bind((hostName, portNumber))        
s.listen(5)                 

while True:
   clientSocket, address = s.accept()     
   print("Got connection from", address)
   result = bytes("Thank you for connecting", "utf-8")
   clientSocket.send(result)
   clientSocket.close()