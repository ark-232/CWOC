import socket
import variables

# take the server name and port name

host = input("Enter the host IP: ")
port = 65001	# port number

# create a socket at client side
# using TCP / IP protocol
s = socket.socket(socket.AF_INET,
				socket.SOCK_STREAM)

# connect it to server and port
# number on local computer.
s.connect(('127.0.0.1', port))
print("Connected to server......")

cmd = input("Enter command: ")
if cmd == "speak":
	variables.userTextToPrint = input("Enter text to speak: ")
	s.send(cmd.encode())

# disconnect the client
s.close()
