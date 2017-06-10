from time import gmtime, strftime
import random
import sys
import multiprocessing as mp

# Start Script

# Password trying to crack, will convert to password list
pwd = "123"

def cracker():
    # Prints time started
    print "Script Started at " + strftime("%a, %d %b %Y %H:%M:%S +0000")
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7",
                "8", "9"]

    length = "123"

    i = 0
    while i == 0:
        guess = ''.join(random.sample(letters, len(length)))

        print guess
        if guess == pwd:
            print "Password Cracked. Password is " + guess
            i = 1

pool = mp.Pool(processes=4)
results = [pool.apply_async(cracker)]
output = [p.get() for p in results]
# print output





# See https://gist.github.com/VenHayz/a0d88c248ddd7aceab545d2731240f80
# Also see https://www.reddit.com/r/learnpython/comments/267xg5/password_cracker/
# See also https://docs.python.org/3/library/multiprocessing.html for multiprocessing
# See this as well: http://sebastianraschka.com/Articles/2014_multiprocessing.html