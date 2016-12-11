import urllib
from BeautifulSoup import *

position = 18
count = 7
step = 0

url = 'http://python-data.dr-chuck.net/known_by_Yahya.html'
while (step < count):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
    tags = soup('a')
    url = tags[position-1].get('href')
    step = step + 1
print url