python gen-source-github.py > ../sources/github-community-repos.json
#python gen-source-share.py > ../sources/share-zabbix.json
#python gen-source-wiki.py > ../sources/zabbix-wiki.json
#python gen-source-zabbix.py > ../sources/zabbix-com.json
DATE=$(date -u +"%Y-%m-%d %H:%M:%S UTC")
sed -i -e "s/Updated on .*\./Updated on $DATE./g" ../index.html
