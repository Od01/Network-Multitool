import socket
import sys
import os
from threading import Thread
import thread

net_addr =  raw_input("Please put in network address, without a node address. Example: 192.168.000 or 010.001.056\n")
last_string = net_addr[-1:]
length_string = len(net_addr)

if last_string == ".":
	print "Please enter a network address with the format '192.168.000' or 010.001.056 please don't include the . at the end."
	sys.exit()
if length_string != 11:
	print "Please enter a network address with the format '192.168.000' or 010.001.056 please don't include the . at the end."
	sys.exit()

def addr_checker(net_addr):
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

#		size = 20
#		for i in range(1, 1000, size):
#			t = Thread(target=addr_checker, args=(i, i+size))
#			t.start
	for i in range(1,100):
		i = thread.start_new_thread(addr_checker, (net_addr,))

addr_checker(net_addr)
