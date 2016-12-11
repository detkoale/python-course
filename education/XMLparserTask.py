import urllib
import xml.etree.cElementTree as ET

serviceurl = "http://python-data.dr-chuck.net/comments_233206.xml"

uh = urllib.urlopen(serviceurl)
data = uh.read()
print 'Retrieved', len(data), 'characters'

tree = ET.fromstring(data)
counts = tree.findall('.//count')
print sum(int(count.text) for count in counts)
#answer = 0

#for count in counts:
#    answer = answer + int(count.text)

#print answer