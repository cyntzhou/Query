import string
import re

months28 = ["February","Feb","2","02"]
months30 = ["April","Apr","4","04","June","Jun","6","06","September","Sep","9","09","November","Nov","11","11"]
months31 = ["January","Jan","1","01","March","Mar","3","03","May","May","5","05","July","Jul","7","07","August","Aug","8","08","October","Oct","10","10","December","Dec","12","12"]

def validate(date, month, day, year, sortedDates, dictDates):
    valid = False
    i = 0
    monthName = ""
    if month in months28:
        if int(day) <= 29 and int(day) > 0:
            valid = True
            i = months28.index(month)/4*4
            monthName = months28[i]
    elif month in months30 and int(day) > 0:
        if int(day) <= 30:
            valid = True
            i = months30.index(month)/4*4
            monthName = months30[i]
    elif month in months31:
        if int(day) <= 31 and int(day) > 0:
            valid = True
            i = months31.index(month)/4*4
            monthName = months31[i]
    if valid:
        sortedDates.append(date)
        stringDate = monthName+" "+str(int(day))+", "+year #str(int(day)) because day might be 03, which is the same as 3
        if dictDates.has_key(stringDate):
            dictDates[stringDate] += 1
        else:
            dictDates[stringDate] = 1
        
def findMatches(text):

    dictDates = {} #each key is a dictionary with years as keys and dictionaries as values, with months as keys and dictionaries as values, with days as keys and frequencies as values; format: {Year:{Month:{Day:Frequency}}, Year:{Month:{Day:Frequency}}, etc.}

    #################FIND MATCHES BASED ON MONTH, DAY, YEAR FORMAT
    n = re.compile("[A-Z][a-z]+\s[0-3]?[0-9],?\s[0-9]{4}")
    dates = n.findall(text)
    
    #################SORT MATCHES
    sortedDates = []
    m = re.compile("([A-Z][a-z]+)\s([0-3]?[0-9]),?\s([0-9]{4})")
    for date in dates:
        month = m.match(date).group(1)
        day = m.match(date).group(2)
        year = m.match(date).group(3)
        validate(date, month, day, year, sortedDates, dictDates)

    #############FIND MATCHES BASED ON SLASH / OR DASH - FORMAT
    n = re.compile("[0-2]?[0-9][-/][0-3]?[0-9][-/][0-9]{4}")
    dates = n.findall(text)
    m = re.compile("([0-2]?[0-9])[-/]([0-3]?[0-9])[-/]([0-9]{4})")
    for date in dates:
        month = m.match(date).group(1)
        day = m.match(date).group(2)
        year = m.match(date).group(3)
        validate(date, month, day, year, sortedDates, dictDates)
    #return sortedDates <---LIST
    return sortDict(dictDates) #<---DICTIONARY

def sortDict(dictNames):
    from collections import OrderedDict
    sortedDict = OrderedDict(sorted(dictNames.items(), key=lambda t: t[1], reverse=True))
    return sortedDict

def mostCommon(text):
    dictNames = findMatches(text)
    return dictNames.keys()[0]

if __name__ == "__main__":
    print findMatches("")
    print mostCommon("")
