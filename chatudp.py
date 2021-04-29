import socket
import os
#import time
import threading
# udp protocal
protocal = socket.SOCK_DGRAM

# network address family
afn = socket.AF_INET

#this is our socket
s = socket.socket(afn,protocal)

ip = "192.168.1.13" # our ip 
port = 1234 

# binding our socket with ip and port
s.bind( (ip,port) )

recvip = input("enter reciever ip :")
print("\t\t\t\t\ chat app" )
print("you are connected to : ",recvip)


def recv():
    while True:
        xr = s.recvfrom(1024)
        clientip = xr[1][0]
        data = xr[0].decode() 
        
        print("\t\t message:  " + data +"\n")
#       os.system("tput setaf 0")
def send():
    while True :
        xs = input("enter message to send: ")
        s.sendto(xs.encode() , (recvip,port))
                
t1 = threading.Thread(target= recv)
t2 = threading.Thread(target= send)

t1.start()
t2.start()
