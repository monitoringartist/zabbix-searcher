#!/usr/bin/env python

from pyquery import PyQuery as pq
from lxml import etree
import urllib, json, ziconizing

arr = {}
d = pq(url='http://zabbix.org/wiki/Zabbix_Templates')
for tr in d('table.wikitable.sortable tr'):
                       
    i = 1
    name = ''
    url = ''
    vendor = ''
    for td in tr.getchildren():
        if td.tag == 'th':
            continue
            
        if i == 1:
            name = 'Template ' + td.text.strip()
            vendor =  td.text.strip()
        
        try: 
            # TODO
            if i == 2:
                a = td.getchildren()[0]
                if a.text.strip().startswith(vendor):
                    name =  'Template ' + a.text.strip()
                else:
                    name = name + ' ' + a.text.strip()
                url =  a.get('href')
                if url[0] == '/':
                    url = 'http://zabbix.org' + url
        except:
            continue                
                    
        i += 1
        if i > 2:
            break
    if name == '' or name == 'Template ':
        continue
    arr[name.replace(' ','-')] = {
      'name': name,
      'url': url,
      'keywords': name.lower().split(' '),
      'icon':  ziconizing.iconizing(name, name.lower().split(' '))
    }
print json.dumps(arr)

