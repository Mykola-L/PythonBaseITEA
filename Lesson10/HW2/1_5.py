import urllib2
from BeautifulSoup import BeautifulSoup

soup = BeautifulSoup(urllib2.urlopen("https://www.google.com"))
print
soup.title.string