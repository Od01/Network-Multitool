import requests
from bs4 import BeautifulSoup

# Creating text file
found_link = []
found_link = open('found_links.txt', 'w')
# creating requests from user input
url = raw_input("Please enter a domain to crawl, without the 'http://www' part : ")
r = requests.get('http://' + url)
# Adding in BS4 for finding a tags in HTML
soup =  BeautifulSoup(r.content, 'html.parser')
link = soup.find_all('a')
# Writes a as the link found in the href
for a in link:
	a = a.get('href')
	a_string = str(a)

	# if statement to filter our links
	if a_string[0] == '#':
		# Same page anchor tags
		a_string = 'Not Valid Link'
	if a_string == 'javascript:;':
		# JS Links
		a_string = 'Not Valid Link'
	if a_string[0] == '/':
		# Realtive Links
		found_link.write(a_string + '\n')
	#else:	
	#	found_link.write(a_string + '\n')
found_link.close()

# Write out the rest of the if statements to filter out external links