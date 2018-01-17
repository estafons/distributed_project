#im_alive.py

import socket

def im_alive(port):

   # create a socket object
   #create a socket object sock stream is tcp
   serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

   # get local machine name 
   host = socket.gethostname()

   serversocket.bind((host,port))

   #queue up to 5 requests
   serversocket.listen(5)

   while True:
     #establish a connection
      clientsocket,addr = serversocket.accept()
      ipaddr = str(addr[0])
      #print("hey " + ipaddr)
      #print(port)
      data = clientsocket.recv(1024)
      clientsocket.send("yeah"+str(port))
      clientsocket.close()
   return
