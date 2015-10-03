#!/usr/bin/env python

import urllib, json, ziconizing
from collections import OrderedDict

url = "https://share.zabbix.com/templates/beez3/html/mod_mt_search/live_search.php?term=%25"
response = urllib.urlopen(url)
data = json.loads(response.read())
arr = {}
for item in data['list']:
  arr[item['name'].replace(' ','-')] = {
    'url': 'https://share.zabbix.com' + item['link'],
    'keywords': item['name'].lower().replace('_',' ').split(' '), 
    'name': item['name'],
    'icon': ziconizing.iconizing(item['name'], item['name'].lower().replace('_',' ').split(' ')) 
  }
print json.dumps(OrderedDict(sorted(arr.items(), key=lambda t: t[0])))

