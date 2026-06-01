import socket
import threading
import sys
import random


sockets = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ports = 6967
sockets.connect(('127.0.0.1',ports))
name = ["client1","client2","cliet3","client4","client5"]
n = random.shuffle(name)
def revice():
    while True:
        d = sockets.recv(1024).decode()
        print(d)

threading.Thread(target=revice).start()
while True:
    
    entermsq = input(f"\n{n}: ")
    sockets.send(f"\n{n}: {entermsq}".encode())
    print("\r\033[K", end="")