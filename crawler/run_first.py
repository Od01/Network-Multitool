import os

def userInput():
    user_input = raw_input("Please enter URL. Please do not include http://: ")
    #print user_input

userInput()

os.system("scrapy runspider crawler_prod.py")
