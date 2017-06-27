from urllib2 import urlopen
import os.path

url = raw_input("Please type in a valud URL. Do not include the leading 'http://'")

link = urlopen("http://" + url)

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

    status = link.getcode()
    if status == statuses[0]:
        i = True
        return i
    else:
        i = None
        print "There is an issue, check your URL."

def lookForRobots(link):
    robot_path = "http://" + str(link) + "/robots.txt"
    robot_present = os.path.exists(robot_path)
    if robot_present == True:
        d = True
    else:
        d = None
        print "There is no robot file"

    return d

# Run function to check the URL
x = checkUrl(link)
if x == True:
    lookForRobots(link)
if d == True:
    print "Here be robots"