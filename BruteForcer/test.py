from datetime import datetime

startTime = datetime.now()
password = "tg4a3"
characters = 'abcdefghijklmnopqrstuvwxyz0123456789'
a = []

for b in xrange(len(password)):
    a = [i for i in characters]
    for y in xrange(b):
        a = [x+i for i in characters for x in a]

location = a.index(password)
guess = a[location]

print "Our password is " + guess