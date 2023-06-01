# Socket-Programming
Client-server applications using the sockets API
This project aims to develop server and client software that enables the transfer of a text file using connection-based byte streams. The server, named server.py, receives a command-line argument specifying the file name and delivers this file to multiple clients concurrently. Each client, named client.py, accepts two mandatory command-line arguments: the server name and the output file name.

Server Usage:

To run the server, execute the following command:


python server.py [input file]

Ensure that the command is correctly formatted and that the input file exists. The server will create a connection-based socket and prepare it for incoming connections, using a chosen port number to avoid well-known port numbers.

Client Usage:

To run a client, execute the following command:



python client.py [server] [output file]

Make sure to provide the server name and the desired output file name as command-line arguments. The client will validate the syntax, parse the arguments, translate the server name into an IP address, and verify write access to the output file. Any errors encountered during this process will result in a brief error message and termination.

File Structure
Both the input file and the output file should be located in separate folders named input_file and output_file, respectively. The input file can contain any number of lines, terminated by a single linefeed. The total number of characters, including the linefeed at the end, should not exceed eighty.

After the last line of the file is transferred, the server closes the connection and waits for other client connections.

Feel free to explore and enhance this project according to your requirements.
