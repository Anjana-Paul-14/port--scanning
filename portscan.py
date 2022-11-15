import socket, subprocess,sys
from datetime import datetime

rmip = input("\t Enter the remote host IP to scan: ")
r1 = int(input("\t Enter the start port number: \t"))
r2 = int(input("\t Enter the last port number: \t"))

print("*"*40)
print("Scanner is working on ",rmip)
print("*"*40)

t1= datetime.now()

try:
    for port in range(r1,r2):
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result =sock.connect_ex((rmip,port))
        if result==0:
            print("Port Open:-->\t", port)
            sock.close()

except KeyboardInterrupt:
    print("You stopped this")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved")
    sys.exit()
    
except socket.error:
    print("could not connect to server")
    sys.exit()
    
t2= datetime.now()
total =t2-t1
print("Scanning complete in ", total)