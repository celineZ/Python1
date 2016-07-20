import urllib
import xml.etree.ElementTree as ET




url = raw_input('Enter url: ')
       
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
#print data
tree = ET.fromstring(data)

counts = tree.findall('.//count')

total = 0
for i in counts:
    total += int(i.text)

    
print "count:", len(counts)    
print "sum:", total

