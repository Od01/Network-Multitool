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
	try:
		print socket.gethostbyaddr(net_addr + "." + str(addr))
		print net_addr + "." + str(addr) + " is alive"
		#host_up = True if os.system("ping -c 1 " + net_addr + "." + str(addr)) is 0 else False
		#if host_up == True:
			#print net_addr + "." + addr + " is alive"
	except socket.error:
		#print(net_addr + "." + str(addr) + " Not found")
		print "no"
