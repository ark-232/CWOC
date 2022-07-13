import socket
import playsound
import os
import functions
import variables

cwd = os.getcwd()

# take the server name and port name
host = 'local host'
port = 65001

# create a socket at server side
# using TCP / IP protocol
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket with server
# and port number
s.bind(('', port))

# allow maximum 1 connection to
# the socket
s.listen(1)
print("Waiting for connection......")

# wait till a client accept
# connection
while(True):
	print("Connected to client......")
	c, addr = s.accept()
	dataFromClient = c.recv(1024)
	cmd = dataFromClient.decode()

	if cmd == "play":
		print("Playing...")
		functions.play()
		break

	elif cmd == "speak":
		functions.speak(variables.userTextToPrint)
		break

	elif cmd == "quit" or cmd == "exit" or cmd == "q" or cmd == "Q" or cmd == "quit()":
		functions.quit()

	elif cmd == "light":
		functions.light()
		break

# disconnect the server
c.close()
