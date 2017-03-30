
# coding: utf-8

# In[3]:

import lxml.html
from lxml.cssselect import CSSSelector
import requests
req = requests.get('http://www.ieee.org/conferences_events/conferences/search/index.html')

html = lxml.html.fromstring(req.text)


# In[6]:

for node in nodes[:10]:
    print node.text
    print "----------"


# In[8]:

get_ipython().run_cell_magic(u'writefile', u'src/ds_web_crawl_ieee.py', u'# coding: utf-8\nimport lxml.html\nfrom lxml.cssselect import CSSSelector\nimport requests\nreq = requests.get(\'http://www.ieee.org/conferences_events/conferences/search/index.html\')\n\nhtml = lxml.html.fromstring(req.text)\nsel=CSSSelector(\'div.content-r-full table.nogrid-nopad tr p>a[href]\')\nnodes = sel(html)\nfor node in nodes:\n    print node.text\n    print "----------"')


# In[10]:

get_ipython().system(u'python src/ds_web_crawl_ieee.py')

