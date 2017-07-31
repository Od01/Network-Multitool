import socket

for addr in range(1,255):
	network_address = '192.168.0.'
	try:
		#str(addr)
		socket.getaddrinfo(network_address + str(addr), 0)
	except socket.error:
		print(network_address + " Not found")
