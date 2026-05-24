import socket
import argparse

paser  = argparse.ArgumentParser()
paser.add_argument("-ip",required=True)
args = paser.parse_args()
print("scan start")
print("")
print("port service status")
count = 0
for i in range(1,1024):
    try:
        
        sockets = socket.socket()
        socket.timeout(1)
        sockets.connect((args.ip,i))
    except socket.error:
        pass
    else:
        count += 1
        print(f"{i}     {socket.getservbyport(i)}   open")
print("")
print(f"{count} open port found scan close")