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

    if robot_present == 200:
        d = True
    else:
        d = "This is bullshit"

    robot_present

def lookForSiteMaps(link):
    sitemap_path = link + "/sitemap.xml"
    sitemap_present = urllib2.urlopen(sitemap_path)

    for line in sitemap_present:
        a = line.rstrip()

    return a

# Run function to check the URL
url = raw_input("Please type in a valud URL. Do not include the leading 'http://' ")
link = "http://" + url

if checkUrl(link) == True:
    print "That link exists! Let's look for a robot file"
    print lookForRobots(link)
    print lookForSiteMaps(link)
