import socket

# take the server name and port name

host = input("Enter the host IP: ")
port = 65001	# port number

# create a socket at client side
# using TCP / IP protocol
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect it to server and port
# number on local computer.
c.connect(('127.0.0.1', port))
print("Connected to server......")

while(True):
	cmd = input("Enter command: ")

	if cmd == "speak":
		userTextToPrint = input("Enter text to speak: ")
		cmd = cmd + "@" + userTextToPrint
		print("Sending command to server...")
		c.send(cmd.encode())

	elif cmd != "speak":
		c.send(cmd.encode())

	elif cmd == "quit" or cmd == "exit" or cmd == "q" or cmd == "Q" or cmd == "quit()":
		print("Closing connection...")
		c.close()
		break

# disconnect the client
# s.close()
