import socket
import threading
port = 6967
sockets = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sockets.bind(('127.0.0.1',port))
sockets.listen(5)
while True:
    data, client = sockets.accept()
    print(f"client is connected {client}")

    def revice():
        while True:
            data.send(f"\n{data.recv(1024).decode()}".encode())
    thread = threading.Thread(target=revice).start()