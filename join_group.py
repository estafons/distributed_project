#join_group.py

import socket

# get local machine name where we will connect afterwards to do what we got to do
def join_group(group,username):

# create a socket object


    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#!!!!! socket.gethostname() !!!! return a string containing the hostnameof the machine where the python interpreter is currently executing if you want to know the current machines s ip address you may want to use gethostbyname(gethostname()). 

    host = socket.gethostname() #returns name of the machine may cause problem with different ips. if so we need to specify somehow where to connect

# connection to hostname on the port.
    s.connect((host, 9999))

    s.send("jgr"+group+","+username)
# Receive no more than 1024 bytes
    user_info = s.recv(1024)
    print(user_info)
    s.close()
    return
