import os
import sys
import socket

if len(sys.argv) != 3:
    print("Error: You must provide exactly two arguments.")
    sys.exit(1)

server_name = sys.argv[1]
input_file = sys.argv[2]

# Translate server name into an IP address
try:
    server_ip = socket.gethostbyname(server_name)
except socket.gaierror:
    print(f"Error: Could not resolve hostname {server_name}. Exiting.")
    sys.exit(1)

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the port
port = 12345
host = socket.gethostname()

print(f"Connecting to {host}:{port}...")

# Connect to the server
try:
    client_socket.connect((server_ip, port))
    print("Connected to server.")
except ConnectionRefusedError:
    print(f"Error: Could not connect to {server_name}. Exiting.")
    sys.exit(1)

output_path = os.path.join(os.getcwd(), "output_file", input_file)

if os.path.exists(output_path) and input_file == os.path.basename(output_path):
    print(f"Error: {input_file} already exists. Exiting.")
    sys.exit(1)

with open(output_path, "wb") as f:
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        f.write(data)

# Close the socket
client_socket.close()