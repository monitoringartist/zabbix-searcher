#!/usr/bin/env python

import os, sys, requests, json, re
files = [
  '../sources/github-community-repos.json',
  '../sources/share-zabbix.json',
  '../sources/zabbix-wiki.json',
]

for file in files:
    print 'FILE: %s' % file
    with open(file) as data_file:
        data = json.load(data_file)
        for id in data:
           try:
               s = requests.get(data[id]['url'])
               if s.status_code != 200:
                  print "File: %s, project %s" % (file, data[id]['name'])
                  print '  url - ' +  data[id]['url']
                  print '  ' + str(s)
               else:
                  if file ==  '../sources/github-community-repos.json':
                      # test link in README
                      matchObj = re.search( r'<a href="(.*)">Link -', s.text)
                      if matchObj:
                          s = requests.get(matchObj.group(1))
                          if s.status_code != 200:
                              print "File: %s, project %s" % (file, data[id]['name'])
                              print '  url - ' +  data[id]['url']
                              print '  README link - ' + matchObj.group(1)
                              print '  ' + str(s)
                      else:
                          print "File: %s, project %s" % (file, data[id]['name'])
                          print '  no "Link - *" found in README'
           except Exception as e:
               print "File: %s, project %s" % (file, data[id]['name'])
               print '  url - ' +  data[id]['url']
               print '  ' + str(e)

           if len(data[id]['name'].split(' '))<2:
               print "File: %s, project %s" % (file, data[id]['name'])
               print '  Rename project - too short name, recommended structure <type> <vendor> <model>, e.g. Template Cisco 2960'

           if len(data[id]['name'].split(' '))>11:
               print "File: %s, project %s" % (file, data[id]['name'])
               print '  Rename project - too long name'

           if data[id]['name'][0] != data[id]['name'][0].upper():
               print "File: %s, project %s" % (file, data[id]['name'])
               print '  Rename project - first letter should be uppercase'
