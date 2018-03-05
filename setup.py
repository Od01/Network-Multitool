import sys
import os
import subprocess as sub


# Check for Python Version, will import to python 3 at some point
if sys.version_info[0] > 2:
    print "Project requiresd Python 2.7+"
    print "Closing Project"
    sys.exit()
else:
    print "Running Correct Python Version grabbing dependancies..."

# Check for platform and change the pip install commands
if platform == "linux" or platform == "linux2":
    # linux
    try:
        os.system("sudo pip install dnspython")
        os.system("sudo pip install scrapy")
        os.system("sudo pip install multiprocessing")
    except ValueError:
        print "Could not install all required packages"
elif platform == "win32":
    # Windows...
        os.system("pip install dnspython")
        os.system("pip install scrapy")
        os.system("pip install multiprocessing")
