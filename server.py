import socket
import threading

HEADER = 64  # message length
PORT = 5050
# get the ip address of this computer
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'  # message encryption format
DISCONNECT_MESSAGE = "!DISCONNECT"

# SETUP THE SOCKET: specify the address family: ipV4
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to the specified address
server.bind(ADDR)


def handle_client(connection, address):
    """
    A function that handles newly connected clients
    """
    print(f"[NEW CONNECTION] {address} connected")

    connected = True
    while connected:
        msg_length = connection.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = connection.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{address}] {msg}")
            # send receipt to the client
            connection.send("Message received".encode(FORMAT))

    connection.close()


def start():
    """
    A function that listen to new connections
    """
    server.listen()     # accept unlimited connections
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        # accept an incoming connection and return the socket of the
        # connection and the client's address
        connection, address = server.accept()    # blocking operation

        # start a thread for the new connection
        thread = threading.Thread(
            target=handle_client, args=(connection, address))
        thread.start()

        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


print("[STARTING] server is starting...")
start()
