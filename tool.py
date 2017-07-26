import socket
import os
import sys
import time
from threading import Thread
import dns.resolver
from poker import portPoker
from hexToDec import hexToDec
from DNSCall import DNSCall
from subDomains import subDomains

sys.path.insert(0, '/home/fuck-you/Projects/Network-Multitool/crawler')
from run_first import userInput

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
4. Sub Domain Scanner
5. Website Link Crawler
"""

def toolCall(x):

	os.system('clear')
	x = x(x)

user_choice = raw_input("Please select your tool: ")

if user_choice == "1":
	os.system('clear')
	print "Welcome to the PortPoker"
	server = raw_input("Please enter a server ro scan: ")
	portPoker(server)
if user_choice == "2":
	os.system('clear')
	s = raw_input("please enter a hex number to convert: ")
	hexToDec(s)
if user_choice == "3":
	os.system('clear')
	record_type = raw_input("Select a Record Type A Records, NS Records, MX Records, TXT Records: ")
	record_type = record_type.upper()
	domain = raw_input("Enter a domain to scan, without the leading http://: ")
	DNSCall(record_type, domain)
if user_choice == "4":
	os.system('clear')
	domain = raw_input("Please enter a domain to scan, without the leading http:// ")
	subDomains(domain)
if user_choice ==  "5":
	os.system('clear')
	user_input = raw_input("Please enter URL. Please do not include http://: ")
	userInput(user_input)
else:
	print "Please make sure what you entered matches the choices."
