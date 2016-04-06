#!/usr/bin/env python

import os, sys, requests, json, re
files = [
  '../sources/github-community-repos.json',
#  '../sources/zabbix-wiki.json',
#  '../sources/share-zabbix.json',
#  '../sources/zabbix-com.json',
]

ecode = 0

for file in files:    
    with open(file) as data_file:
        data = json.load(data_file)
        print '=== FILE: %s (%d projects) ===' % (file, len(data))
        if len(data) < 100:
            print 'Problem with parsing data for ' + file
            if 'share' not in file and 'zabbix-com' not in file:
                ecode = 1
        for id in data:
           try:
               s = requests.get(data[id]['url'])
               if s.status_code != 200:
                  print "File: %s, project %s" % (file, data[id]['name'])
                  print '  url - ' +  data[id]['url']
                  print '  ' + str(s)
                  ecode = 1
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
                              if 'share' not in file and 'zabbix-com' not in file:
                                  ecode = 1

                      else:
                          print "File: %s, project %s" % (file, data[id]['name'])
                          print '  no "Link - *" found in README'
                          if 'share' not in file and 'zabbix-com' not in file:
                              ecode = 1

           except Exception as e:
               print "File: %s, project %s" % (file, data[id]['name'])
               print '  url - ' +  data[id]['url']
               print '  ' + str(e)
               if 'share' not in file and 'zabbix-com' not in file:
                   ecode = 1

           if len(data[id]['name'].split(' '))<2:
               print "File: %s, project %s" % (file, data[id]['name'])
               print '  Rename project - too short name, recommended structure <type> <vendor> <model>, e.g. Template Cisco 2960'
               if 'share' not in file and 'zabbix-com' not in file:
                  ecode = 1
 

           if len(data[id]['name'].split(' '))>11:
               print "File: %s, project %s" % (file, data[id]['name'])
               print '  Rename project - too long name'
               if 'share' not in file and 'zabbix-com' not in file:
                   ecode = 1

           if data[id]['name'][0] != data[id]['name'][0].upper():
               print "File: %s, project %s" % (file, data[id]['name'])
               print '  Rename project - first letter should be uppercase'
               if 'share' not in file and 'zabbix-com' not in file:
                   ecode = 1

sys.exit(ecode)
