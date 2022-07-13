import socket
import playsound
import os
import functions

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
	c, addr = s.accept()
	print("Connected to client......")
	dataFromClient = c.recv(1024)
	decodedData = dataFromClient.decode()

	# Decoded data split on the "@" = command @ phrase
	cmd = decodedData.split("@")[0]
	phrase = decodedData.split("@")[1]

	if cmd == "play":
		print("Playing...")
		functions.play()
		break

	elif cmd == "speak":
		functions.speak(phrase)
		break

	elif cmd == "quit" or cmd == "exit" or cmd == "q" or cmd == "Q" or cmd == "quit()":
		functions.quit()

	elif cmd == "light":
		functions.light()
		break

# disconnect the server
c.close()
