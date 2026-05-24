import socket
import threading


sockets = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ports = 6967
sockets.connect(('127.0.0.1',ports))

def revice():
    while True:
        print(sockets.recv(1024).decode())

threading.Thread(target=revice).start()
while True:
    
    entermsq = input("client: \n")
    sockets.send(f"client: {entermsq}\n".encode())