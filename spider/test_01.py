import sys, os
import urllib.error
import urllib.request


urllib.request.urlopen("http://www.baidu.com")

url = "http://www.baidu.com"

# ua = 'User-Agent:Mizilla/5.0 (Windows NT 6.1; WOW 64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.02454.101
# Safari/537.36'

ua = 'Mizilla/5.0 (Windows NT 6.1; WOW 64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.02454.101 Safari/537.36'

req = urllib.request.urlopen(url)

req.read()