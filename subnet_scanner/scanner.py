import socket
import sys
import os

net_addr =  raw_input("Please put in network address, without a node address. Example: 192.168.0 ")
last_string = net_addr[-1:]

# print socket.gethostbyaddr("10.0.2.15")

if last_string == ".":
	print "Please enter a network address with the format '192.168.0' please don't include the . at the end."
	sys.exit()

for addr in range(2,255):
	# Combine address entered and range number
	ip = net_addr + "." + str(addr)

	# Validate IP address format
	try:
		socket.inet_aton(ip)
	except socket.error:
		print "Not a valid IP address, closing scanner."
		sys.exit()

	# Check the address
	try:
		print socket.gethostbyaddr(ip)
		print ip + " is alive"
	except socket.error:
		print "Nothing is alive at " + ip
