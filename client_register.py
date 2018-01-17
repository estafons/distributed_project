#register client
import socket

# get local machine name where we will connect afterwards to do what we got to do
def register():

# create a socket object


    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#!!!!! socket.gethostname() !!!! return a string containing the hostnameof the machine where the python interpreter is currently executing if you want to know the current machines s ip address you may want to use gethostbyname(gethostname()). 

    host = socket.gethostname()
#input desired port
    port = raw_input("give me desired port to receive your messages")
#input name
    username = raw_input("what is your username? ")



# connection to hostname on the port.
    s.connect((host, 9999))

# Receive no more than 1024 bytes
    s.send("reg"+port+" "+username)
    port,username,ipaddr,my_id = (s.recv(1024)).split("#")
    s.close()
    return (my_id,username,ipaddr,port)
