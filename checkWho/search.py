import google
import  urllib
from bs4 import UnicodeDammit
import testWho
from collections import Counter 

from bs4 import BeautifulSoup
g = google.search("Who played The Dark knight?",start =0,stop =10)
urls= [x for x in g]
count = 0;
soup = Counter({})
while count <= 9:
    u = urllib.urlopen(urls[count])
    soup = soup + Counter(testWho.findMatches(u.read()))
    count += 1



high= max(soup, key=soup.get)
print high
soup.pop(high,None)
print max(soup, key=soup.get)
