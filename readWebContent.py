import urllib3
import datetime
import certifi
import re
import datetime
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())
try:
    appStartTime = datetime.datetime..now
    r = http.request('GET','https://www.google.com/finance?q=ashokley')
    timeToFetchData = datetime.datetime.now-appStartTime
    m = re.search('id="ref_7147553_l".*?>(.*?)<', str(r.data))
    timeToParseData = datetime.datetime.now-timeToFetchData
    if m:
        print (m.group(1))
    else:
        print("No quote available")
print(""
    
except Exception as e:
    print(e)

