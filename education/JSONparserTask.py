import urllib
import json

serviceurl = 'http://python-data.dr-chuck.net/comments_233210.json'
connection = urllib.urlopen(serviceurl)
data = connection.read()
print 'Retrieved', len(data),'characters'
jsonResponse = json.loads(data)

comments = jsonResponse["comments"]
print 'Count:', len(comments)
print 'Sum:', sum(int(comment["count"]) for comment in comments)