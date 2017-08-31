import requests

site = raw_input("Please enter website url to check. Do not include 'http://'\n")


def webServerInfo(site):
	headers = {'key': 'value'}
	try:
		r = requests.get('https://' + site, verify=True)
	except:
		print "There was a connection error"

	print r.headers('Servers')

webServerInfo(site)
