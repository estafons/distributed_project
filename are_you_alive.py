#are_you_alive.py

import socket
import time
import errno
from socket import error as socket_error

def are_you_alive(port):
   
# create a socket object
   

     

#!!!!! socket.gethostname() !!!! return a string containing the hostnameof the machine where the python interpreter is currently executing if you want to know the current machines s ip address you may want to use gethostbyname(gethostname()). 

     

# connection to hostname on the port.
     while True:
         time.sleep( 5 )
         for x in 
         try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            host = socket.gethostname()
            s.connect((host, 5005))
            s.send("ali")
    # Receive no more than 1024 bytes
            user_info = s.recv(1024)
            print(user_info)
         except socket_error as serr:
            if serr.errno != errno.ECONNREFUSED:
        # Not the error we are looking for, re-raise
                raise serr
            print("target is dead")
         s.close()

are_you_alive(5005)
