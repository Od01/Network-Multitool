import socket
import time

def subDomains(domain):
	file1 = open('wordlist.txt', 'r')
	checklist = file1.read().splitlines()
	file1.close()

	checkedlist = []
	checkedfile = open('checked.txt', 'w')
	# site = raw_input('Please enter domain name, do not include http://: ')

	for check in checklist:
		try:
			addthis = socket.gethostbyname(check + '.' + domain) + '=' + check + '.' + domain
			print addthis
			checkedlist.insert(0, addthis)
		except socket.gaierror:
			print 'nothing found'
		time.sleep(0.3)

	print "Done checking, please see the 'checked.txt' file for the found sub domains"

	for results in checkedlist:
		checkedfile.write(results + '\n')
	checkedfile.close()
