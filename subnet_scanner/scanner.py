import socket
import sys

net_addr =  raw_input("Please put in network address, without a node address. Example: 192.168.0 ")
last_string = net_addr[-1:]

if last_string == ".":
	print "Please enter a network address with the format '192.168.0' please don't include the . at the end."
	sys.exit()

for addr in range(2,255):
	str(net_addr)

	try:
		#str(addr)
		print socket.gethostbyaddr(net_addr + "." + str(addr))
	except socket.error:
		print(net_addr + "." + str(addr) + " Not found")
