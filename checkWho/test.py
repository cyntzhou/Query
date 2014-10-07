import string
import re

#DIFFERENT TEXT FILES TO CHECK
berries = open("./texts/berry.txt",'r').read().replace("\n","")
saw = open("./texts/saw.txt",'r').read().replace("\n","")
giver = open("./texts/giver.txt",'r').read().replace("\n","")
twilight = open("./texts/twilight.txt",'r').read().replace("\n","")
moon = open("./texts/new_moon.txt",'r').read().replace("\n","")
breaking = open("./texts/breaking_dawn.txt",'r').read().replace("\n","")
hunger = open("./texts/hunger_games.txt",'r').read().replace("\n","")
wiki = open("./texts/wiki_history_of_science.txt",'r').read().replace("\n","")

common_words_1000 = open("common_words_1000.txt",'r').read().splitlines()

common_words_10000 = open("common_words_10000.txt",'r').read().splitlines()
#A LIST WITH THE 1000 MOST COMMON WORDS: FROM http://www.giwersworld.org/computers/linux/common-words.phtml
#common_words_10000.txt comes from https://github.com/first20hours/google-10000-english/blob/master/google-10000-english.txt

common_cities = open("common_cities.txt",'r').read().replace(" ","\n").splitlines()

common_names_text = open("common_names.txt",'r').read()
#common_names.txt from http://names.mongabay.com/female_names.htm
#the text has names as well as numbers, so only get the names with regex
r = re.compile("[A-Z]+")
common_names = r.findall(common_names_text)

names = []
sortedNames = []
new_names = []

def findMatches(text):

    #################FIND MATCHES
    n = re.compile("[A-Z][a-z]+\040[A-Z][a-z]+")
    #names = n.match(text)
    #print names.group()
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
            elif last.upper() not in common_words_1000 and first.lower() not in common_words_10000 and last not in common_cities:
                sortedNames.append(name)
        elif last.upper() in common_names:
            if first.upper() not in common_words_1000 and first.lower() not in common_words_10000 and first not in common_cities:
                sortedNames.append(name)
        #if first name and last name are NOT in common_names, check to see if they're regular words. if not, it's probably a name so add it to the sortedNames list
        elif first.upper() not in common_words_1000 and first.lower() not in common_words_10000 and first not in common_cities and last.upper() not in common_words_1000 and last.lower() not in common_words_10000 and last not in common_cities:
            sortedNames.append(name)
        else:
            print name
    print sortedNames
                
if __name__ == "__main__":
    findMatches(berries)
