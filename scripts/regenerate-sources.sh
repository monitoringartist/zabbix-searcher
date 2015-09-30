python gen-source-github.py > ../sources/github-community-repos.json
python gen-source-share.py > ../sources/share-zabbix.json 
python gen-source-wiki.py > ../sources/zabbix-wiki.json
DATE=`date +%Y-%m-%d`
git commit -am "Source update $DATE"
#git push origin gh-pages 
