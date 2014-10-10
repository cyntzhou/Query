import google
import  urllib

from bs4 import BeautifulSoup
g = google.search("michael huang",start =0,stop =10)
urls= [x for x in g]
u = urllib.urlopen(urls[4])
#print u.read()

soup = BeautifulSoup(u.read())
soup = soup.get_text()
print soup
