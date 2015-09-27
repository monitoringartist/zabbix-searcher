#!/usr/bin/env python

import os, sys, requests, json, base64

def github_query(url):
     
    headers = {'Authorization': 'token 1dc33912a4668751497d77bc536fe6f87d577965'}
            
    s = requests.get(url, headers=headers)
    if s.status_code != 200:
       s = json.loads(s.text)
       print s['message']
       return ''         
    return s.text

    
s = github_query('https://api.github.com/repos/zabbix/zabbix-community-repos/git/trees/master')
s = json.loads(s)
arr = {}
result = 1
for ofile in s['tree']:
    try: 
        ofile['path'].index('(')
    except:
        continue   
    #print str(result) + '. ' + ofile['path'] + ' - https://github.com/zabbix/zabbix-community-repos/tree/master/' + ofile['path']
    arr[ofile['path']] = {
      'url': 'https://github.com/zabbix/zabbix-community-repos/tree/master/' + ofile['path'],
      'keywords': ofile['path'].lower().replace('(','').replace(')','').split('-'),
      'name': ofile['path'][0:ofile['path'].index('(')].replace('-',' ') + ofile['path'][ofile['path'].index('('):] 
    }
#print arr    
print json.dumps(arr)         