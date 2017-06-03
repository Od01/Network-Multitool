from urllib2 import urlopen

url = raw_input("Please type in a valud URL. Do not include the leading 'http://'")

link = urlopen("http://" + url)

def checkUrl(link):
    statuses = [
        200, # success
        404, # Not found
        403, #Forbidden
        401, # Unauthorized
        500, # Internal server erro
        503, # Service Unavailable
        504 # Gateway Timeout

        ]

    status = link.getcode()

    if status == statuses[0]:
        global stat
        stat = 1
checkUrl(link)

if stat == 1:
    print "Good to move forward"