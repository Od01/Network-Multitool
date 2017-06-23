from urllib2 import urlopen

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
        i = Null
        print "There is an issue, check your URL."

# Run function to check the URL
x = checkUrl(link)
if x == True:
    print "Good to move forward"