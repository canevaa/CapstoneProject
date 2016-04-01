#!/usr/bin/python
import socket
import subprocess
from Crypto import Random
from Crypto.PublicKey import RSA

#Gets the local IP address of server and returns it
def encrypt_data(data, user):
	
def decrypt_data(data):
	
def get_local_ip():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("gmail.com",80))
	Address = (s.getsockname()[0])
	s.close()
	return Address
	
#Creates the Server Socket for messaging returns server socket
def create_server_connection():
	ServerS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	Port = 5000
	ServerS.bind((Address, Port))
	ServerS.listen(5)
	return ServerS

#Takes connections from the clients then connects them to each other
def connect_with_clients():
	clientport = "5005"
	a = 0
	while (a < 2):
		Client, ClientAddr = ServerS.accept()
		print "Got Connection from", ClientAddr
		x = "Connected to Server"
		Client.send(x)
		ClientIP = Client.recv(1024)
		print "ClientIP recv"
		ClientUN = Client.recv(1024)
		print "ClientUN recv"
#		ClientCT = Client.recv(1024) #Code is freezing here? why?? removing to test
#		print "ClientCT recv"
		if (a == 0):
			print "Entered if a = 0"
			outgoing = "true"
			Client.send(outgoing)
			print Client.recv(1024)
			Client.send(clientport)
			ClientAIP = ClientIP
			a = 1
		if (a == 1):
			print "Entered if a = 1"
			outgoing = "false"
			Client.send(outgoing)
			print Client.recv(1024)#
			print "Server Version of Client-Server Address" + ClientAIP
			Client.send(ClientAIP) #
			print Client.recv(1024) #
			Client.send(clientport) #
			print "Server Version of Port: " + clientport
		#offer a break for the server
			b = raw_input("Enter c to continue, q to quit")
			if b == "c":
				a = 0	
			if b == "q":
				a = 2
			else 
				a = 2
		Client.close()
		
	ServerS.close()
	return

	
#-------------------------------------------------------------------
#        	Start Calling Functions for use!
#-------------------------------------------------------------------

Address = get_local_ip()
ServerS = create_server_connection()
connect_with_clients()

#Creates a connection to get public address of itself
#Address = subprocess.check_output("wget http://people.sunyit.edu/~greenli/ip.php -qO -", shell=True)
