import json
import urllib

url = raw_input('Enter url')
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()

print 'Retrieved', len(data), 'charachters'

info = json.loads(str(data))

print 'Count:', len(info['comments'])

total = 0
for i in info['comments']:
    total += int(i['count'])
    
print 'sum: ', total
   
