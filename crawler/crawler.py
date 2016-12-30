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
	if 'http://' + url in a_string:

		# Links from the same site
		found_link.write(a_string + '\n')
	if 'https://' + url in a_string:

		# Links from the same site with SSL
		found_link.write(a_string + '\n')
	if 'http://www.' + url in a_string:

		# Links from the same site
		found_link.write(a_string + '\n')
	if 'https://www.' + url in a_string:

		# Links from the same site with SSL
		found_link.write(a_string + '\n')
	#else:	
	#	found_link.write(a_string + '\n') # testing only

found_link.close()

# Open newly created file full of links
crawled_links = open('found_links.txt', 'r')
stored_urls = crawled_links.read().splitlines()

def remove_duplicates(values):
	output = []
	seen = set()
	for value in values:
		if value not in seen:
			output.append(value)
			seen.add(value)
	return output
	
result = remove_duplicates(stored_urls)

no_dups = []
no_dups = open('nodups_links.txt', 'w')

# For readability
for a in result:
	no_dups.write(a + '\n')

crawled_links.close()

# Need to figure out how to add the non duplicates to the original file