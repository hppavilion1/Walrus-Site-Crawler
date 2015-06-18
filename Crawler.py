import robotparser
import requests
import urlparse
import re
import time

linkRegex = r'''</?a((s+w+(s*=s*(?:".*?"|'.*?'|[^'">s]+))?)+s*|s*)/?>w+</a>'''
linkPattern = re.compile(regexp_link)

def extract_urls(doc):
    return links = re.findall(pattern, html)

read = []
fetched = []
tofetch = []
baseurl = raw_input('Base URL (include trailing slash): ') #Get url to scrape

ua = raw_input('User Agent (leave blank for default (recommended)): ') #Set user-agent
if not ua:
    ua = 'WalrusCrawler'

rp = robotparser.RobotFileParser()
rp.seturl(baseurl+'robots.txt') #Get Robots.txt (for compliance purposes)

rp.read()

tofetch = extract_urls(requests.get(baseurl))
while len(tofetch) > 0:
    for x in tofetch:
        if rp.can_fetch(ua, x):
            if not x in fetched:
                fetched.append(x)
                tofetch += extract_urls(requests.get(x))
        read.append(x)
            
        
