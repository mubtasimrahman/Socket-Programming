import sys
import socket
import os

if len(sys.argv) != 2:
    print("Error: You must provide exactly one argument.")
    sys.exit(1)

input_file = sys.argv[1]

# Specify the path to the input file
input_path = os.path.join(os.getcwd(), "input_file", input_file)

try:
    # Try to open the file in read mode
    f = open(input_path, "rb")
    f.close()
    print(f"File {input_file} exists.")
except FileNotFoundError:
    print(f"Error: File {input_file} not found. Exiting.")
    exit()

# Check if the input file meets the required format
with open(input_path, "rb") as f:
    total_chars = 0
    for line in f:
        total_chars += len(line)
        if total_chars + 1 > 80:
            print("Too many characters")
            sys.exit(1)

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the host and port
host = socket.gethostname()
port = 12345

# Bind the socket to the host and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(1)

while True:
    # Wait for a client to connect
    print("Waiting for client connection...")
    client_socket, client_address = server_socket.accept()
    print(f"Connected to client at {client_address}")

    # Send the input file to the client
    with open(input_path, "rb") as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            client_socket.sendall(data)

    # Close the client socket
    client_socket.close()
    print(f"Connection with client at {client_address} closed.")

