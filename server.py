import socket
import playsound
import os

cwd = os.getcwd()

# take the server name and port name
host = 'local host'
port = 65001

# create a socket at server side
# using TCP / IP protocol
s = socket.socket(socket.AF_INET,
				socket.SOCK_STREAM)

# bind the socket with server
# and port number
s.bind(('', port))

# allow maximum 1 connection to
# the socket
s.listen(1)

# wait till a client accept
# connection
while(True):
	c, addr = s.accept()
	dataFromClient = c.recv(1024)

	if dataFromClient.decode() == "play":
		print("Playing...")
		break
		#playsound(cwd+'\Audio\Reville.wav')

# disconnect the server
c.close()
