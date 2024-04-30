import sys
import xml.etree.ElementTree as etree
import re

def get_attr_number(node):
    count = 0
    for tag in node:
        count = count + get_attr_number(tag)
    return count + len(node.attrib)
    

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))


#---------------sample input---------------

# 6
# <feed xml:lang='en'>
#     <title>HackerRank</title>
#     <subtitle lang='en'>Programming challenges</subtitle>
#     <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
#     <updated>2013-12-25T12:00:00</updated>
# </feed>

#---------------OUTPUT---------------

#5