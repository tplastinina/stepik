import requests
import re

res = requests.get("http://pastebin.com/raw/7543p0ns").text
#res = requests.get(input())
# str = "<a href=http://banner.rbc.ru/banredir.cgi?lid=firstpage_spec>"
# links = re.finditer(r'(\<a\s+href=[\'"](?P<proto>[a-zA-Z]+://)?)(?P<domain>[\w]+([.][\w]+)*)(.*[\'"])', res)
links = re.finditer(r'\<a.+href=[\'"](?P<proto>[a-zA-Z]+://)?(?P<domain>[\w\-]+(\.[\w\-]+)*).*[\'"]', res)
links = re.finditer(r'\<a.+href=[\'"](?P<proto>[a-zA-Z]+://)?(?P<domain>[\w\-]+(\.[\w\-]+)*)(?P<port>:[0-9]{1-5})?.*[\'"]', res)
links = re.finditer(r'\<a.+href=[\'"](?P<proto>[a-zA-Z]+://)?(?P<domain>[\w\-]+(\.[\w\-]+)*)(?P<port>:[0-9]{1-5})?[/]?(?P<path>[\w\-.]+)?(?P<query>[?]([\w\-.\[\]$]+=[\w\-.\[\]$]+)?(&[\w\-.\[\]$]+=[\w\-.\[\]$]+)*)?[\'"]', res)


# links = re.finditer(r'(\<a\s+href=[\'"](?P<proto>[a-zA-Z]+://)?(?P<domain>[\w]+([.][\w]+)+)(.*[\'"])', res)
domains = [m.groupdict()['domain'] for m in links]
[print(domain) for domain in sorted(set(domains))]
