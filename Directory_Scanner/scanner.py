from urllib2 import urlopen

link = urlopen('http://georgeoffley.com')

statuses = [
    404, # Not found
    200, # success
    403 #Forbidden

    ]

status = link.getcode()

if status == statuses[1]:
    print "The site exists"