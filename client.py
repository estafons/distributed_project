# client.py
import socket
import thread
from client_register import register
from list_groups import list_groups
from list_members import list_members
from join_group import join_group
from exit_group import exit_group
from do_the_talking import do_the_talking
from client_listener import client_listener
from bye_bye import bye_bye
from im_alive import im_alive
#port = 9999
#username = raw_input("what is your username? ")
# connection to hostname on the port.
#s.connect((host, port))
(my_id,username,ip,port) = register()

#!!! client_listener(ip,port)

# Receive no more than 1024 bytes
#s.send(username)
thread.start_new_thread( client_listener, (ip, int(port), ) )
thread.start_new_thread( im_alive, (int(port), ) )
#s.close()

# possible problem because of thread. interupts the communication and when unpacking with split problem occurs and tracker crashes

#are you okay message from tracker to client every few seconds
print("successfully registered waiting for your commands")
while True:
    comm = raw_input("")
    if comm[0]!="!":
        try:
             do_the_talking(comm,current_group,username)#broadcast message
        except NameError:
             print("you have to specify where to talk silly!")
    else:
        comm = comm.replace(" ","") #remove white spaces from commands
        if comm[1] =="l":
            if comm[2]=="g":
               list_groups()
            elif comm[2]=="m":
               list_members(comm[3:])
        elif comm[1] =="j":
           join_group(comm[2:],username)
        elif comm[1]=="w":
           current_group = comm[2:]
        elif comm[1]=="e":
           exit_group(comm[2:],username)
        elif comm[1]=="q":
           bye_bye(username)
           break
        else:
           print("there is no such command try again")

