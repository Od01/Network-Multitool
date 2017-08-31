import requests

site = raw_input("Please enter website url to check. Do not include 'http://'\n")


def webServerInfo(site):
	headers = {'content-type': 'Server'}
	try:
		r = requests.get('https://' + site, verify=True, headers=headers)
	except:
		print "There was a connection error"

	print r

webServerInfo(site)
