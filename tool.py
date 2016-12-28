import socket
import os
import sys
import time
from threading import Thread
import dns.resolver

os.system('clear')
print """
 __        __   _                            _                               
 \ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___                         
  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \                        
   \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) |                       
  __\_/\_/ \___|_|\___\___/|_| |_| |_|\___|_ \__\___/_   _ _____           _ 
 |  _ \ ___ _ __ ___   ___ | |_ ___  |  \/  |_   _| | |_(_)_   _|__   ___ | |
 | |_) / _ \ '_ ` _ \ / _ \| __/ _ \ | |\/| | | | | | __| | | |/ _ \ / _ \| |
 |  _ <  __/ | | | | | (_) | ||  __/ | |  | | |_| | | |_| | | | (_) | (_) | |
 |_| \_\___|_| |_| |_|\___/ \__\___| |_|  |_|\__,_|_|\__|_| |_|\___/ \___/|_|


Please Choose from these Tool:
1. Port Poker(Port Scanner) 
2. Hex to Dec Converter
3. DNS Lookup
4. DNS Brute Force
"""

# Port Poker(Port Scanner) | Line 58
# Hex to Dec Converter | Line 127
# DNS Lookup | Line 147
# DNS Brute Force | Line 206

user_choice = raw_input("Please select your tool!")

if user_choice == 1:
	return portPoker()
if user_choice == 2:
	hexToDec()
if user_choice == 3:
	DNSCall()
if user_choice == 4:
	subDomains()

# ^^^ This isn't working	


"""
////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////
Network MultiTool

See labels below

"""

#Port Poker - Remote Port Scanner

def portPoker():

	#clears terminal window and sets up program in terminal
	os.system('clear')
	print """
//    _____           _     _____      _             
//   |  __ \         | |   |  __ \    | |            
//   | |__) |__  _ __| |_  | |__) |__ | | _____ _ __ 
//   |  ___/ _ \| '__| __| |  ___/ _ \| |/ / _ \ '__|
//   | |  | (_) | |  | |_  | |  | (_) |   <  __/ |   
//   |_|   \___/|_|   \__| |_|   \___/|_|\_\___|_|   
//                                                   
//                                                                                                     
	"""
	server = raw_input("Please enter a server name ")
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

"""
Hex to Dec converter
////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////
"""

def hexToDec():
	#clears termianl screen
	os.system('clear')
	# asks for input 
	s = raw_input("Please put in the hex number you wish to convert: ")
	# converts to base 16
	try: 
		convert = int(s, 16)
	except:
		print "This was not a hex value"

	print("Here is your decimal " + str(convert))

"""
DNS Lookup
////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////
"""	


def DNSCall():
    # clears the screen
    os.system('clear')
 
    # ask for the records
    # record types:
    # A
    # NS
    # MX
    # TXT
    welcome_message = """
Welcome to DNS Lookup
 
What kinds of records are you looking for?
 
A Records
NS Records
MX Records
TXT Records
 
Input: """
 
    record_type = raw_input(welcome_message)
    record_type = record_type.upper()
 
    # raise error if the record is wrong
    while record_type == "A" or record_type == "NS" or record_type == "MX" or record_type == "TXT":
        record_type = record_type
       
        # define your functions for record lookups
        def dns_rec(record_type):
            domain = raw_input("Please put in a domain ")
            answers = dns.resolver.query(domain, record_type)
 
            for server in answers:
                print server   
 
        # if statement for input
        if record_type == "A":
            return dns_rec(record_type == "A")
        if record_type == "NS":
            return dns_rec(record_type == "NS")
        if record_type == "MX":
            return dns_rec(record_type == "MX")
        if record_type == "TXT":
            return dns_rec(record_type == "TXT")   
        else:
            "Please check your answer and make sure it matches one of the options above"
 
    else:
        print "Oops you typed in something incorrectly, try again."
        sys.exit()	

"""
DNS Brute Forcer
////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////
"""	        

def subDomains():
	file1 = open('wordlist.txt', 'r')
	checklist = file1.read().splitlines()
	file1.close()

	checkedlist = []
	checkedfile = open('checked.txt', 'w')
	site = raw_input('Please enter domain name, do not include http://: ')

	for check in checklist:
		try:
			addthis = socket.gethostbyname(check + '.' + site) + '=' + check + '.' + site
			print addthis
			checkedlist.insert(0, addthis)
		except socket.gaierror:
			print 'nothing found'
		time.sleep(0.3)

	print 'done checking'			

	for results in checkedlist:
		checkedfile.write(results + '\n')
	checkedfile.close()	