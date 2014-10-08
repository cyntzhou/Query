import string
import re

#DIFFERENT TEXT FILES TO CHECK
text = open("important_dates.txt",'r').read()

dates = []
sortedDates = []
dictDates = {}

months = ["January","February","March","April","May","June","July","August","September","October","November","December","Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

def addDict(n):
    if dictNames.has_key(n):
        dictNames[n] = dictNames[n] + 1
    else:
        dictNames[n] = 1

def findMatches1(text):

    #################FIND MATCHES BASED ON MONTH, DAY, YEAR FORMAT
    n = re.compile("[A-Z][a-z]+\s[0-3]?[0-9],?\s[0-9]{1,4}")
    #names = n.match(text)
    #print names.group()
    dates = n.findall(text)
    print dates
    
    #################SORT MATCHES
    print "\nFILTERED DATES:"
    m = re.compile("[A-Z][a-z]+")
    for date in dates:
        month = m.match(date).group()
        if month in months:
            sortedDates.append(date)
    dates = []
    d = re.compile("\s([0-3]?[0-9]),?")
    for date in sortedDates:
        day = d.findall(date)[0]
        if int(day) < 32:
            dates.append(date)
    return dates

def findMatches2(text):

    #############FIND MATCHES BASED ON SLASH / OR DASH - FORMAT
    n = re.compile("[0-2]?[0-9].[0-3]?[0-9].[0-9]{1,4}")
    dates = n.findall(text)
    print dates
    
                
if __name__ == "__main__":
    print findMatches1(text)
    findMatches2(text)
    """
    print sortedDates
    print dates
    print dictDates.items()
    """
