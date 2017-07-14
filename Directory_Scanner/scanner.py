from urllib2 import urlopen
import urllib2
import requests
import os.path

# Functions
def checkUrl(link):
    statuses = [
        200, # success
        404, # Not found
        403, #Forbidden
        401, # Unauthorized
        500, # Internal server error
        503, # Service Unavailable
        504 # Gateway Timeout

        ]

    a = requests.get("https://" + url)
    status = a.status_code
    if status == statuses[0]:
        i = True
        return i
    else:
        i = None

    return i

def lookForRobots(link):
    robot_path = link + "/robots.txt"
    robot_present = urllib2.urlopen(robot_path)

    a = robot_present.read()

    return a

def lookForSiteMaps(link):
    sitemap_path = link + "/sitemap.xml"
    sitemap_present = urllib2.urlopen(sitemap_path)

    a = sitemap_present.read()

    return a

# Run function to check the URL
url = raw_input("Please type in a valud URL. Do not include the leading 'http://' ")
link = "http://" + url

if checkUrl(link) == True:
    print "That link exists! Let's look for a robot file"

if lookForRobots(link) == None:
    print "No Robot"
else:
    print lookForRobots(link)

if lookForSiteMaps(link) == None:
    print "There's no sitemap"
else:
    print "Displaying sitemap"
    print lookForSiteMaps(link)
