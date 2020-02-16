import socket
import subprocess
import sys
from datetime import datetime

subprocess.call('clear',shell=True)

remoteServer =raw_input("Enter a remote host to scan.")
remoteServerIP =socket.gethostbyname(remoteServer)

print "-" * 60
print "Please wait, Scanning remote host...", remoteServerIP
print "-" * 60

t1 = datetime.now()

try:
    for port in range(1,1025): #Specify Port Integers
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP,port))
        if result ==0:
            print "Port {}: Open".format(port)
        sock.close()
        
       #TO BE CONTINUED
