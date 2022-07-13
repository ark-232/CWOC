import socket
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
	print("Received data from client: " + decodedData)

	# Decoded data split on the "@" = command @ phrase
	if decodedData and "speak" in decodedData:
		cmd = decodedData.split("@")[0]
		phrase = decodedData.split("@")[1]
		print("Text to speak is: " + phrase)
		functions.speak(phrase)

	elif decodedData == "play":
		print("Playing...")
		functions.play()

	elif decodedData == "quit" or decodedData == "exit" or decodedData == "q" or decodedData == "Q" or decodedData == "quit()":
		c.close()
		functions.quit()

	elif decodedData == "light":
		functions.light()

