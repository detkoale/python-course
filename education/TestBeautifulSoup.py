import urllib
from BeautifulSoup import*


html = urllib.urlopen('http://python-data.dr-chuck.net/comments_233209.html')
soup = BeautifulSoup(html)
tags = soup('span')
print sum(int(tag.string) for tag in tags)