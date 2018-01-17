#do_the_talking.py

import socket


#UDP_IP = "127.0.0.1"
#UDP_PORT =5005

#request_ip_addresses and ports
def unfold_ip_port(data):
    list_of_lists = []
    final = []
    list_of_info_per_user = data.split("!")
    for x in list_of_info_per_user:
         list_of_lists+=[x.split("#")]
    for y in list_of_lists:
         final+=[[y[0],int(y[1])]]
    return final

def do_the_talking(data,group,username):


   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

   host = socket.gethostname()

# connection to hostname on the port.
   s.connect((host, 9999))

   s.send("gip"+group)
# Receive no more than 1024 bytes
   members =unfold_ip_port( s.recv(1024))
   #print(members)
   s.close()
   MESSAGE= data
   UDP_IP_UDP_PORT = members
   #print "message:", MESSAGE
   sock = socket.socket(socket.AF_INET, # internet
                     socket.SOCK_DGRAM) #UDP
   for [x,y] in UDP_IP_UDP_PORT:
       sock.sendto(MESSAGE+"#" +username, (x, y))
