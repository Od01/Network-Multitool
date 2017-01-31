import sys
import requests
from bs4 import BeautifulSoup

# creating requests from user input
url = raw_input("Bitch, put in your domain! Without the 'http://www' part : ")

def makeRequest(url):
	print("Trying...", url)
	r = requests.get('http://' + url)
	# Adding in BS4 for finding a tags in HTML
	soup =  BeautifulSoup(r.content, 'html.parser') 
	# Writes a as the link found in the href
	output = soup.find_all('a')
	return output

def makeFilter(link):
	# Creating array for our links
	found_link = []
	for a in link:
		a = a.get('href')
		a_string = str(a)

		if not a_string:
  			continue	
		# if statement to filter our links
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

	output = found_link
	# print a_string

	return output	

# Function for removing duplicates
def remove_duplicates(values):
	output = []
	seen = set()
	for value in values:
		if value not in seen:
			output.append(value)
			seen.add(value)
	return output

# Makes the request -> Filters the links -> Removes duplicates
def createURLList(values):
	global filtered_list
	try:
		requests = makeRequest(values)
	except:
		print "We can't find this shit! Try again idiot."
	try:
		new_list = makeFilter(requests)
	except:
		print "The fuck is this shit?. I can't make a list out of this."
	try:
		filtered_list = remove_duplicates(new_list)
	except:
		print "I can't do shit with this list. You fucked up"

	return filtered_list

result = createURLList(url)

# print result
crawled_urls = []
crawled_urls = open('crawled_urls.txt', 'w')

# for verifying and crawling resulting pages
for b in result:
	sub_directories = createURLList(url + b) # issue is right here, it's adding the url on the full URL in some instances

	# remove_duplicates(sub_directories)
	for z in sub_directories: # goes through the arrays crawled 
		crawler = []
		crawler.append(z)
		crawler = remove_duplicates(crawler) # remove duplicates from list
		crawler = str(crawler)
		crawled_urls.write(crawler + '\n')
crawled_urls.close()
