import socket

for addr in range(1,255):
	str(addr)
	network_address = '192.168.0.'
	try:
		socket.inet_aton(network_address)
	except socket.error:
		print(network_address + " Not found")		