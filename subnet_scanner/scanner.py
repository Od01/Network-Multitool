import socket

net_addr =  raw_input("Please put in network address, without a node address. Example: 192.168.0 ")

for addr in range(2,255):
	str(net_addr)
	try:
		#str(addr)
		print socket.gethostbyaddr(net_addr + "." + str(addr))
	except socket.error:
		print(net_addr + "." + str(addr) + " Not found")
