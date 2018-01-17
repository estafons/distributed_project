# tracker_server.py
import socket
import time
import thread
import errno
from socket import error as socket_error
#create a socket object sock stream is tcp
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name 
host = socket.gethostname()

port = 9999
global users



def are_you_alive(users,groups):
   
     while True:
         time.sleep( 5 )
         for x in users:
             curr_port=int(x[2])
             try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                host = socket.gethostname()
                s.connect((host, curr_port))
                s.send("ali")
    # Receive no more than 1024 bytes
                user_info = s.recv(1024)
             except socket_error as serr:
                if serr.errno != errno.ECONNREFUSED:
        # Not the error we are looking for, re-raise
                    raise serr
                print x[3], "is dead"
                users.remove(x)
                del_from_groups(x[3],groups)
                s.close()





def get_member_list(search,groups):
    for x in groups:
       if x[0]==search:
           return x[1:]
       
    return "problema"

def check_membership(group,user):
    flag=True
    for x in group:
       if x==user:
           flag=False
    return flag
 
def delete_member(group,groups,user):
     for x in groups:
       if x[0]==group:
           x.remove(user)

     return x[1:]
 
def get_ip(user,users):
    for x in users:
        if user==x[3]:
            print("kati ginetai")
            tup = (x[1],x[2])
            return '#'.join(tup)
    print("problem get ipsss")
    return "not found # 42"

def del_from_users_table(user,users):
    for x in users:
        if user==x[3]:
            users.remove(x)
            return "success"
    print("failure")
    return "failure"

def del_from_groups(user,groups):
    for x in groups:
        for y in x:
            if user==y:
                 x.remove(y)
    print "anihilated", user
    return

def get_ips(group,users):
    l = []
    for x in group:
        print(x)
        l.append(get_ip(x,users))
    return l

def add_user_to_group(user,group,groups):
    for x in groups:
       if x[0]==group:
           if check_membership(x,user): #check so that users are not added twice
                x.append(user)
                return x[1:]
           else:
                return "you are already a member!"
    groups.append([group,user]) #create new group
    return [user]
users = []
groups = [["dogs","dogg","doggie"], ["cats"]]
thread.start_new_thread( are_you_alive, (users,groups, ) )

# bind to the port
serversocket.bind((host,port))

#queue up to 5 requests
serversocket.listen(5)

unique_id = 0
while True:
    #establish a connection
    clientsocket,addr = serversocket.accept()
    ipaddr = str(addr[0])
    print("Got a connection from %s " % ipaddr)
    
    data = clientsocket.recv(1024)
    req_type = data[0:3]
    data = data[3:]
    if req_type=="reg": #register user
       currentTime = time.ctime(time.time()) + "\r\n"
       port, username = data.split()
       unique_id=unique_id+1
       unique= str(unique_id)
       print(unique)
       clientsocket.send(port+"#"+username+"#"+ipaddr+"#"+unique)
       clientsocket.close()
       print(currentTime)
       print(username)
       print(port)
       users +=[(unique_id,ipaddr,port,username)]#record user's info
    elif req_type=="lgr": #list groups
       currentTime = time.ctime(time.time()) + "\r\n"
       group_str =  ','.join(str(x[0]) for x in groups)
       clientsocket.send(group_str)
       clientsocket.close()
    elif req_type=="lmb": #list members
       currentTime = time.ctime(time.time()) + "\r\n"
       member_str = ','.join(str(x) for x in (get_member_list(data,groups)))
       clientsocket.send(member_str)
       clientsocket.close()
    elif req_type=="jgr": #join or create group if doesnt exist
       currentTime = time.ctime(time.time()) + "\r\n"
       data,username=data.split(",")
       users_in_group = add_user_to_group(username,data,groups)#maybe problem overwriting username after other user registers
       member_str = ','.join(str(x) for x in users_in_group)
       clientsocket.send(member_str)
       clientsocket.close()
    elif req_type=="egr": # user exits group
       currentTime = time.ctime(time.time()) + "\r\n"
       data,username=data.split(",")
       users_in_group = delete_member(data,groups,username)
       member_str = ','.join(str(x) for x in users_in_group)
       clientsocket.send("sucessefully exited, members now are "+member_str)
       clientsocket.close()
    elif req_type=="bye": # user exits app
       currentTime = time.ctime(time.time()) + "\r\n"
       del_from_groups(data,groups)
       print(del_from_users_table(data,users))
       clientsocket.close()
#now secondary cases tracker needs to handle where request is not made directly from user.
    elif req_type=="gip": #get ip adddresses and ports
       currentTime = time.ctime(time.time()) + "\r\n"
       got_the_ips = get_ips(get_member_list(data,groups),users)
       member_str = '!'.join(str(x) for x in got_the_ips) #instead of cats get group to send
       clientsocket.send(member_str)
       clientsocket.close()
    
       
     
