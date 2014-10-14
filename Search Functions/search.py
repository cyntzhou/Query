import google
import  urllib
from bs4 import UnicodeDammit
import testWho
import testWhen
from collections import Counter 

from bs4 import BeautifulSoup
def searchx(text):
    g = google.search(text,start =0,stop =10)
    urls= [x for x in g]
    count = 0;
    soup = Counter({})
    if( "Who" in text or "who" in text):
         while count <= 9 and count < len(urls):
            u = urllib.urlopen(urls[count])
            soup = soup + Counter(testWho.findMatches(u.read()))
            count += 1

            results =[]
            check = 0;
            
    elif ("When" in text or "when" in text):
         while count <= 9and count < len(urls):
            u = urllib.urlopen(urls[count])
            soup = soup + Counter(testWhen.findMatches(u.read()))
            
            count += 1

            results =[]
            check = 0;
           
    else:
        return ["Please include Who or When as part of the search!"]

    if(len(soup)==0):
        return ["No results","No results"]
    elif(len(soup)==1):
        results[0]= " *Most common result is given below*"
    high= max(soup, key=soup.get)   
    while (check <= 5 and len(results)<= 1):
        if(high not in text ):

                
            results.append(high)
            soup.pop(high,None)
            high= max(soup, key=soup.get) 
            check += 1
            
        elif (check <= 3):
            soup.pop(high,None)
            high= max(soup, key=soup.get) 
            check += 1
        else:
            results.append(high)
    return  results

if __name__ == "__main__":
    print searchx("When was Albert Einstein born?")[0]


