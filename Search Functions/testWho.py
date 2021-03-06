import string
import re
from bs4 import BeautifulSoup

common_words_1000 = open("./texts/common_words_1000.txt",'r').read().splitlines()

common_words_10000 = open("./texts/common_words_10000.txt",'r').read().splitlines()
#A LIST WITH THE 1000 MOST COMMON WORDS: FROM http://www.giwersworld.org/computers/linux/common-words.phtml
#common_words_10000.txt comes from https://github.com/first20hours/google-10000-english/blob/master/google-10000-english.txt

common_cities = open("./texts/common_cities.txt",'r').read().replace(" ","\n").splitlines()

common_names_text = open("./texts/common_names.txt",'r').read()
#common_names.txt from http://names.mongabay.com/female_names.htm
#the text has names as well as numbers, so only get the names with regex
r = re.compile("[A-Z]+")
common_names = r.findall(common_names_text)


def addDict(n, dictNames):
    if dictNames.has_key(n):
        dictNames[n] = dictNames[n] + 1
    else:
        dictNames[n] = 1

def findMatches(text):
    
    names = []
    sortedNames = []
    dictNames = {}

    #################FIND MATCHES
    n = re.compile("[A-Z][a-z]+\040[A-Z][a-z]+") #\040 is space char
    names = n.findall(text)

    #################SORT MATCHES
    n = re.compile("[A-Z][a-z]+")
    for name in names:
        first_last = n.findall(name)
        first = first_last[0]
        last = first_last[1]
        #first check if first name or last name is in the list common_names
        if first.upper() in common_names:
            #if first name is in common_names, check to see if the last name is a name,
            #then check if the last name is a common word or city. if not, add to sortedNames list
            if last.upper() in common_names:
                sortedNames.append(name)
                addDict(name, dictNames)
            elif last.upper() not in common_words_1000 and last.lower() not in common_words_10000 and last not in common_cities:
                sortedNames.append(name)
                addDict(name, dictNames)
        elif last.upper() in common_names:
            if first.upper() not in common_words_1000 and first.lower() not in common_words_10000 and first not in common_cities:
                sortedNames.append(name)
                addDict(name, dictNames)
        #if first name and last name are NOT in common_names, check to see if they're regular words. if not, it's probably a name so add it to the sortedNames list
        elif first.upper() not in common_words_1000 and first.lower() not in common_words_10000 and first not in common_cities and last.upper() not in common_words_1000 and last.lower() not in common_words_10000 and last not in common_cities:
            sortedNames.append(name)
            addDict(name, dictNames)
    #return sortedNames <--LIST
    return sortDict(dictNames) #<--DICTIONARY

def sortDict(dictNames):
    #from operator import itemgetter
    #return sorted(dictNames.items(), key=itemgetter(1))
    from collections import OrderedDict
    sortedDict = OrderedDict(sorted(dictNames.items(), key=lambda t: t[1], reverse=True))
    return sortedDict

#returns the most frequent result
def mostCommon(text):
    dictNames = findMatches(text)
    return dictNames.keys()[0]
                
if __name__ == "__main__":
    print findMatches("")
    print mostCommon("")
