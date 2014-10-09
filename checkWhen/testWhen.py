import string
import re

text = open("important_dates.txt",'r').read()

dates = []
sortedDates1 = []
sortedDates2 = []
dictDates = {} #each key is a dictionary with years as keys and dictionaries as values, with months as keys and dictionaries as values, with days as keys and frequencies as values; format: {Year:{Month:{Day:Frequency}}, Year:{Month:{Day:Frequency}}, etc.}

months28 = ["February","Feb","2","02"]
months30 = ["April","Apr","4","04","June","Jun","6","06","September","Sep","9","09","November","Nov","11","11"]
months31 = ["January","Jan","1","01","March","Mar","3","03","May","May","5","05","July","Jul","7","07","August","Aug","8","08","October","Oct","10","10","December","Dec","12","12"]

def addDict(n):
    if dictNames.has_key(n):
        dictNames[n] = dictNames[n] + 1
    else:
        dictNames[n] = 1

def validate(date, month, day, year, sortedDates):
    valid = False
    i = 0
    monthName = ""
    if month in months28:
        if int(day) <= 29:
            valid = True
            i = months28.index(month)/4
            monthName = months28[i]
    elif month in months30:
        if int(day) <= 30:
            valid = True
            i = months30.index(month)/4
            monthName = months30[i]
    elif month in months31:
        if int(day) <= 31:
            valid = True
            i = months31.index(month)/4
            monthName = months31[i]
    if valid:
        sortedDates.append(date)
        if dictDates.has_key(year):
            if dictDates.get(year).has_key(monthName):
                if dictDates.get(year).get(monthName).has_key(day):
                    dictDates.get(year).get(monthName)[day] += 1
                else:
                    dictDates.get(year).get(monthName)[day] = 1
            else:
                dictDates.get(year)[monthName] = {day:1}
        else:
            dictDates[year] = {monthName:{day:1}}
        

def findMatches1(text):

    #################FIND MATCHES BASED ON MONTH, DAY, YEAR FORMAT
    n = re.compile("[A-Z][a-z]+\s[0-3]?[0-9],?\s[0-9]{4}")
    #names = n.match(text)
    #print names.group()
    dates = n.findall(text)
    
    #################SORT MATCHES
    m = re.compile("([A-Z][a-z]+)\s([0-3]?[0-9]),?\s([0-9]{4})")
    for date in dates:
        month = m.match(date).group(1)
        day = m.match(date).group(2)
        year = m.match(date).group(3)
        validate(date, month, day, year, sortedDates1)
    return sortedDates1

def findMatches2(text):

    #############FIND MATCHES BASED ON SLASH / OR DASH - FORMAT
    n = re.compile("[0-2]?[0-9][-/][0-3]?[0-9][-/][0-9]{4}")
    dates = n.findall(text)
    print dates
    m = re.compile("([0-2]?[0-9])[-/]([0-3]?[0-9])[-/]([0-9]{4})")
    for date in dates:
        month = m.match(date).group(1)
        day = m.match(date).group(2)
        year = m.match(date).group(3)
        validate(date, month, day, year, sortedDates2)
    return sortedDates2
                
if __name__ == "__main__":
    print findMatches1(text)
    print findMatches2(text)
    print dictDates.items()
