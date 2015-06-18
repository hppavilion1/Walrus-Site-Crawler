import robotparser
import requests
import urlparse
import re
import time
import warnings
warnings.catch_warnings()

linkRegex = r'''/(\S+\.(com|net|org|edu|gov)(\/\S+)?)/'''
linkPattern = re.compile(linkRegex)

def extract_urls(doc):
    return [x[0][1:] for x in re.findall(linkPattern, doc)]

read = []
fetched = []
tofetch = []
baseurl = 'http://'+raw_input('Base URL: ').strip('/') #Get url to scrape

ua = raw_input('User Agent (leave blank for default (recommended)): ') #Set user-agent
if not ua:
    ua = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0'

rp = robotparser.RobotFileParser()
rp.set_url(baseurl+'/'+'robots.txt') #Get Robots.txt (for compliance purposes)

rp.read()

tofetch = extract_urls(requests.get(baseurl).text)

while len(tofetch) > 0:
    for x in tofetch:
        if rp.can_fetch(ua, x):
            if not x in fetched:
                fetched.append(x)
                try:
                    tofetch += extract_urls(requests.get('http://'+x).text)
                    print x
                except:
                    pass
                tofetch = [y for y in tofetch if y != x]
        read.append(x)
            
        
