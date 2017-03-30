
# coding: utf-8

# In[3]:

import lxml.html
from lxml.cssselect import CSSSelector
import requests
r = requests.get('http://python.org/')

html = lxml.html.fromstring(r.text)
selec=CSSSelector('a[href]')
nodes = selec(html)


# In[5]:

print len(nodes)
for i, node in enumerate(nodes):
    if i < 30:
        print i, node.get('href'), node.text

