#bye_bye.py

import socket

# get local machine name where we will connect afterwards to do what we got to do
def bye_bye(user):

# create a socket object


    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#!!!!! socket.gethostname() !!!! return a string containing the hostnameof the machine where the python interpreter is currently executing if you want to know the current machines s ip address you may want to use gethostbyname(gethostname()). 

    host = socket.gethostname()

# connection to hostname on the port.
    s.connect((host, 9999))

    s.send("bye"+user)
# Receive no more than 1024 bytes
    print("you will be missed")
    s.close()
    return
