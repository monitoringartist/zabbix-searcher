#!/usr/bin/env python

import os, sys, requests, json, ziconizing
from collections import OrderedDict

def github_query(url):
     
    s = requests.get(url)
    if s.status_code != 200:
       s = json.loads(s.text)
       print s['message']
       return ''         
    return s.text

s = github_query('https://api.github.com/repos/monitoringartist/zabbix-community-repos/git/trees/master')
s = json.loads(s)
arr = {}
top = {}
result = 1
for ofile in s['tree']:
    try: 
        ofile['path'].index('(')
    except:
        continue   
    #print str(result) + '. ' + ofile['path'] + ' - https://github.com/monitoringartist/zabbix-community-repos/tree/master/' + ofile['path']
    if 'monitoringartist' in ofile['path']:
        top[ofile['path']] = {
          'url': 'https://github.com/monitoringartist/zabbix-community-repos/tree/master/' + ofile['path'],
          'keywords': ofile['path'].lower().replace('(','').replace(')','').split('-'),
          'name': ofile['path'][0:ofile['path'].index('(')].replace('-',' ') + ofile['path'][ofile['path'].index('('):],
        }
        top[ofile['path']]['icon'] = ziconizing.iconizing(top[ofile['path']]['name'], top[ofile['path']]['keywords'])
    else:  
        arr[ofile['path']] = {
          'url': 'https://github.com/monitoringartist/zabbix-community-repos/tree/master/' + ofile['path'],
          'keywords': ofile['path'].lower().replace('(','').replace(')','').split('-'),
          'name': ofile['path'][0:ofile['path'].index('(')].replace('-',' ').replace('  ',' ') + ofile['path'][ofile['path'].index('('):],
        }
        arr[ofile['path']]['icon'] = ziconizing.iconizing(arr[ofile['path']]['name'], arr[ofile['path']]['keywords'])
print json.dumps(OrderedDict(sorted(top.items(), key=lambda t: t[0])+sorted(arr.items(), key=lambda t: t[0])))
