import string
import re
from bs4 import BeautifulSoup

#DIFFERENT TEXT FILES TO CHECK
text = open("important_dates.txt",'r').read()

dates = []
sortedDates = []
dictDates = {}

def addDict(n):
    if dictNames.has_key(n):
        dictNames[n] = dictNames[n] + 1
    else:
        dictNames[n] = 1

def findMatches(text):

    #################FIND MATCHES
    n = re.compile("[A-Z][a-z]+\s[0-3]?[0-9],?\s[0-9]{1,4}")
    #names = n.match(text)
    #print names.group()
    dates = n.findall(text)
    print dates

    #################SORT MATCHES
    print "\nFILTERED DATES:"
    for date in dates:
        print date
                
if __name__ == "__main__":
    findMatches(text)
    print sortedDates
    print dictDates.items()
