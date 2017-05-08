from time import gmtime, strftime
import random
import sys

# Start Script

# Password trying to crack, will convert to password list
pwd = "pas"

def cracker():
    # Prints time started
    print "Script Started at " + strftime("%a, %d %b %Y %H:%M:%S +0000")
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                "w", "x", "y", "z"]

    length = "123"


    for i in xrange(sys.maxint):
        guess = ''.join(random.sample(letters, len(length)))
        print guess
        if guess == pwd:
            print "Password Cracked. Password is " + guess
            exit()

cracker()



# See https://gist.github.com/VenHayz/a0d88c248ddd7aceab545d2731240f80
# Also see https://www.reddit.com/r/learnpython/comments/267xg5/password_cracker/