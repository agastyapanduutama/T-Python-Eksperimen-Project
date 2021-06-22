import socket
from time import sleep

# create and configure socket on local host
serverSocket = socket.socket()
host = "192.168.1.17"
port = 8080  # arbitrary port
serverSocket.bind((host, port))
serverSocket.listen(1)

con, addr = serverSocket.accept()

print("connected to client")

while True:
    # send wave to client
    con.send(bytes("Server wave", "UTF-8"))

    # receive wave from client
    message = con.recv(1024).decode("UTF-8")
    print(message)

    # wait 1 second
    sleep(1)

con.close()
