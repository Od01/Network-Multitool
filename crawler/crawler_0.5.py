import requests
from bs4 import BeautifulSoup

# Creating array for our links
found_link = []

# creating requests from user input
url = raw_input("Please enter a domain to crawl, without the 'http://www' part : ")

def makeRequest(url):
	r = requests.get('http://' + url)
	# Adding in BS4 for finding a tags in HTML
	soup =  BeautifulSoup(r.content, 'html.parser')
	# Writes a as the link found in the href
	global link
	link = soup.find_all('a')

makeRequest(url)	

def makeFilter(link):
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
			found_link.append(a_string)

		if 'http://' + url in a_string:
			# Links from the same site
			found_link.append(a_string)

		if 'https://' + url in a_string:
			# Links from the same site with SSL
			found_link.append(a_string)

		if 'http://www.' + url in a_string:
			# Links from the same site
			found_link.append(a_string)

		if 'https://www.' + url in a_string:
			# Links from the same site with SSL
			found_link.append(a_string)
		#else:	
		#	found_link.write(a_string + '\n') # testing only
makeFilter(link)		

# Function for removing duplicates
def remove_duplicates(values):
	output = []
	seen = set()
	for value in values:
		if value not in seen:
			output.append(value)
			seen.add(value)
	return output

# Run the function with our list	
result = remove_duplicates(found_link)

print result

#for verifying and crawling resulting pages
for b in result:
	directories = requests.get('http://' + url + b)
	status = directories.status_code
	# print status
	if status == 200:
		makeRequest(b)
		makeFilter(link)
		remove_duplicates()

# print result



# Need to figure out how to use my three functions to cralw the sites that were found in the original page
# Also need to figure out how to take the original set of urls and add in the urls from all the other pages while also
# filtering out duplicates