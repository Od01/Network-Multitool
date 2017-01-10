import requests
from bs4 import BeautifulSoup
import sys

# creating requests from user input
url = raw_input("Please enter a domain to crawl, without the 'http://www' part : ")

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

		#else:	
		#	found_link.write(a_string + '\n') # testing only
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

# Run the function with our list in this order -> Makes the request -> Filters the links -> Removes duplicates
def createURLList(values):
	requests = makeRequest(values)
	new_list = makeFilter(requests)
	filtered_list = remove_duplicates(new_list)

	return filtered_list

result = createURLList(url)

# print result
crawled_urls =[]
crawled_urls = open('crawled_urls.txt', 'w')

# for verifying and crawling resulting pages
for b in result:
	sub_directories = createURLList(url + b)
	crawler = []
	crawler.append(sub_directories)
	crawler = str(crawler)
	crawled_urls.write(crawler + '\n')

crawled_urls.close()

	# print crawler

# print remove_duplicates(crawler)	

# Has the crawled links going into a txt file. Still need to figure out why this is failing.
# Also need to run this through the duplicates function, need to filter out the duplicates
# See http://stackoverflow.com/questions/41454811/issue-with-web-crawler-indexerror-string-index-out-of-range for reference.