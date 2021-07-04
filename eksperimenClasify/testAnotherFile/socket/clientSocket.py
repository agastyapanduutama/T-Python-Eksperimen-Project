import socket
from time import sleep

# configure socket and connect to server
clientSocket = socket.socket()
host = "192.168.1.17"
port = 9090
clientSocket.connect((host, port))

# keep track of connection status
connected = True
print("connected to server")

while True:
    # attempt to send and receive wave, otherwise reconnect
    try:
        message = clientSocket.recv(1024).decode("UTF-8")
        clientSocket.sendall(bytes("Sisi Klien", "UTF-8"))
        # clientSocket.sendall("GET / HTTP/1.1\r\nHost: www.cnn.com\r\n\r\n")
        # clientSocket.sendall("GET / HTTP/1.1\r\nHost: 192.168.1.17\r\n\r\n")
        print(message)
    except socket.error:
        # set connection status and recreate socket
        connected = False
        clientSocket = socket.socket()
        print("connection lost... reconnecting")
        while not connected:
            # attempt to reconnect, otherwise sleep for 2 seconds
            try:
                clientSocket.connect((host, port))
                connected = True
                print("re-connection successful")
            except socket.error:
                sleep(2)

clientSocket.close()
