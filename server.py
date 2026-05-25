import socket
import threading
port = 6967
sockets = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sockets.bind(('127.0.0.1',port))
sockets.listen(5)

data, client = sockets.accept()
print(f"client is connected {client}")
def revice():
    while True:
        print(data.recv(1024).decode())

threading.Thread(target=revice).start()
while True:
    entermsq = input("\nserver: ")
    data.send(f"\nserver: {entermsq}".encode())