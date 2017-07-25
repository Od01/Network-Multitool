import os
import socket
from threading import Thread

def portPoker(server):

	# server = raw_input("Please enter a server name ")
	serv_ip = socket.gethostbyname(server) # connects to server through try
	print "Please wait, scanning remote host", serv_ip

	def portConnect(from_, to_):

		try:

			for port in range(from_, to_):
				sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				connect =  sock.connect_ex((serv_ip, port))
				if connect == 0:
					print "Port {}: Open".format(port)
			sock.close()

		except socket.gaierror:
			print """
			________________$$$$
			______________$$____$$
			______________$$____$$
			______________$$____$$
			______________$$____$$
			______________$$____$$
			__________$$$$$$____$$$$$$
			________$$____$$____$$____$$$$
			________$$____$$____$$____$$__$$
			$$$$$$__$$____$$____$$____$$____$$
			$$____$$$$________________$$____$$
			$$______$$______________________$$
			__$$____$$______________________$$
			___$$$__$$______________________$$
			____$$__________________________$$
			_____$$$________________________$$
			______$$______________________$$$
			_______$$$____________________$$
			________$$____________________$$
			_________$$$________________$$$
			__________$$________________$$
			__________$$$$$$$$$$$$$$$$$$$$

			I can't find that server, idiot! Try again
			"""
			sys.exit()

	size = 20
	for i in range(1, 1000, size):
		t = Thread(target=portConnect, args=(i, i+size))
		t.start()
