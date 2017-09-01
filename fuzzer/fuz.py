import requests

url = raw_input("Please type in a URL to look through without the leading URL\n")
found_urls = []
numbers = '0123456789'
alnum = numbers + 'abcdefghijklmnopqrstuvwxyz'

for i in range(100):
	for x in range(100):
		for directory in alnum:
	 		r = requests.get("https://" + url + "/" + directory)
			status = r.status_code
			if status == "200":
				print "Found" + "https://" + url + "/" + directory
			else:
				print "Cannot find " + "https://" + url + "/" + directory
