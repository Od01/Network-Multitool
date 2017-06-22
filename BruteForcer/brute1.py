from time import gmtime, strftime
from datetime import datetime

# Start timer
startTime = datetime.now()

# Start Script

# Password trying to crack, will convert to password list
password = "abd1k"

def cracker():
    # Prints time started
    characters = 'abcdefghijklmnopqrstuvwxyz0123456789'
    a = []

    i = 0
    while i == 0:

        for b in xrange(len(password)): # Creates for loop for number of letters in the password

            a = [c for c in characters] # Creates our dataset
            for y in xrange(b): # For loop to populate b
                a = [x+c for c in characters for x in a]

        location = a.index(password)
        guess = a[location]
        if guess == password:
            print "Password Cracked. Password is " + guess
            i = 1

cracker()

print "Time to complete script:"
print datetime.now() - startTime