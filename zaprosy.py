# import requests

# res = requests.get("https://yandex.ru/search/", 
#                    params={
#                        "text": "Stepic",
#                        "test": "test1",
#                        "name": "Name With Spaces",
#                        "list": ["test2", "test3"]
#                     })
# print(res.status_code)
# print(res.headers['Content-Type'])
# print(res.url)
# print(res.text)

import requests
import re

A = input().replace('stepic.org', 'stepik.org')
B = input().replace('stepic.org', 'stepik.org')
all_links = []
site = requests.get(A).text
links = re.findall("href=[\"\'](.*?)[\"\']", site)
for link in links:
    html = requests.get(link.replace('stepic.org', 'stepik.org')).text
    cycle_sites = re.findall("href=[\"\'](.*?)[\"\']", html)
    cycle_sites = list(map(lambda x: x.replace('stepic.org', 'stepik.org'), cycle_sites))
    all_links.extend(cycle_sites)
if B in all_links:
    print('Yes')
else:
    print('No')