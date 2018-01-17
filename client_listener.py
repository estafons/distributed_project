#client_listener.py

import socket
def client_listener(ip,port):
    UDP_IP = ip
    UDP_PORT =port
    sock = socket.socket(socket.AF_INET, # Internet
    socket.SOCK_DGRAM) #UDP
    sock.bind((UDP_IP, UDP_PORT))
    while True:
       data, addr = sock.recvfrom(1024)
       message,user =  data.split("#")# buffer size is 1024 bytes
       print user, "says:", message
