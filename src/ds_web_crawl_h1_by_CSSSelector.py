import lxml.html
from lxml.cssselect import CSSSelector
import requests
req = requests.get('http://python.org/')

html = lxml.html.fromstring(req.text)
selec=CSSSelector('a[href]')

nodes = selec(html)
print len(nodes)
for i, node in enumerate(nodes):
    if i<30 :
        print i, node.get('href'), node.text