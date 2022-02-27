import socket
import threading

PORT = 5050
# get the ip address of this computer
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

# specify the address family: ipV4
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to the specified address
server.bind(ADDR)


def handle_client(connection, address):
    """
    A function that handles newly connected clients
    """
    pass


def start():
    """
    A function that listen to new connections
    """
    server.listen()
    while True:
        # accept an incoming connection and return the socket of the
        # connection and the client's address
        connection, address = server.accept()

        # start a thread for the new connection
        thread = threading.Thread(
            target=handle_client, args=(connection, address))
        thread.start()

        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


print("[STARTING] server is starting...")
start()
