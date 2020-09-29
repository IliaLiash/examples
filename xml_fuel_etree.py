import re
from xml.etree import ElementTree
root = ElementTree.parse('map2.osm').getroot()
count = 0
for child in root:
    for child1 in child:
        if 'fuel' in child1.attrib.values() and child.tag != 'way':
            count += 1        
print(count)