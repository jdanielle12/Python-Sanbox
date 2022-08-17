import time # allows working with the functionality of time
import socket # performs connections between two nodes on the network
import sys # provides the valuable information about the Python interpreter
import os # interacts with the operating system


soc = socket.socket() # this creates the socket
host = socket.gethostname() # binds with the port and waits for connection
port = 8080 # binds with hostname and waits for connection with time
soc.bind(("",))

print("waiting for connections...")
soc.listen() # waits for TCP listener to accept the connection and stores in the variable conn, addr
conn, addr = soc.accept() # once connection happens it prints "is connected to server"

print(addr, "is connected to server")
command = input(str("Enter Command:")) # takes the imput and sends the TCP message to the client to encode
conn.send(command.encode())
print("Command has been sent successfully.")
data = conn.recv(1024) # stores the received message from the client

if data:
    print("command received and executed successfully.")

soc = socket.socket() #creating the soc variable
host = "75.145.114.90" # initializing the host variable
port = 8080
soc.connect((host, port)) # initiates the TCP connection and binds the socket to the host and port
print("Connected to Server.")
command = soc.recv(1024) # command we received from the server is stored here
command = command.decode() # function decodes the message
if command == "open":
    print("Command is:", command) # if the decoded message and command the user input is the same then print the command
    soc.send("Command received".encode()) # sends the TCP message by encoding it
    os.system('test.bat') # providing the file name in os.system to display the output

import time
import socket
import sys
import os

# Initialize soc to socket
soc = socket.socket()

# Initialize to host
host = socket.gethostname()

# Initialize the port
port = 8080

# Bind the socket with port and host
soc.bind(('', port))

print("waiting for connections...")

# listening for connections
soc.listen()

# accepting the incoming connections
conn, addr = soc.accept()

print(addr, "is connected to server")

# take command as input
command = input(str("Enter Command :"))

conn.send(command.encode())

# receive the confirmation
data = conn.recv(1024)

if data:
    print("command received and executed successfully.")

import time
import socket
import sys
import os

# Initialize soc to socket
soc = socket.socket()

# Initialize the host
host = "74.145.114.90"

# Initialize the port
port = 8080

# bind the socket with port and host
soc.connect((host, port))
print("Connected to Server.")

# receive the command from server program
command = soc.recv(1024)
command = command.decode()

# match the command and execute it on client system
if command == "open":
    print("Command is :", command)
    soc.send("Command received".encode())

    # give the file name as input
    os.system('test.bat')
