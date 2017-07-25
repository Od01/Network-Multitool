import os

def hexToDec(s):
	#clears termianl screen
	os.system('clear')
	# converts to base 16
	try:
		convert = int(s, 16)
	except:
		print "This was not a hex value"

	print("Here is your decimal " + str(convert))
