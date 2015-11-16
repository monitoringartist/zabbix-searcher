#!/usr/bin/env python

from pyquery import PyQuery as pq
from lxml import etree
from collections import OrderedDict
import urllib, json, ziconizing

arr = {}
d = pq(url='http://www.zabbix.com/third_party_tools.php')
for a in d('strong a'):
    name =  a.text.strip()
    url =  a.get('href').strip()
    if 'github' in url:
        continue                       
    arr[name.replace(' ','-')] = {
      'name': name,
      'url': url,
      'keywords': name.lower().split(' '),
      'icon':  ziconizing.iconizing(name, name.lower().split(' '))
    }

print json.dumps(OrderedDict(sorted(arr.items(), key=lambda t: t[0])))

