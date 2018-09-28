# #!/usr/bin/env python
#
# from urllib.request import urlopen
# from urllib.request import Request
# from urllib import parse
# import re
# import urllib.request
# import urllib.error
#
# page = 1
# # url = "https://www.qiushibaike.com/8hr/page/" + str(page)
# url = "https://www.qiushibaike.com/"
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0',
#     "hosts":"https://www.qiushibaike.com"
#     }
# dict  = {
#     "name":"Germey"
# }
# try:
#     data = bytes(parse.urlencode(dict), encoding='utf-8')
#     request = Request(url=url, data=data, headers=headers, method="POST")
#     response = urlopen(request)
#     print(response.read().decode('utf-8'))
# except urllib.error as e:
#     if hasattr(e, "code"):
#         print(e.code)
#     if hasattr(e, "reason"):
#         print(e.reason)
#
#
#
# request =urllib.request.Request("https://www.qiushibaike.com/")
# response = urllib.request.urlopen(request)
# print(response.read().decode("utf-8"))


from urllib import request,parse
url = "http://httpbin.org/post"
headers = {
    #伪装一个火狐浏览器
    "User-Agent":'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    "host":'httpbin.org'
}
dict = {
    "name":"Germey"
}
data = bytes(parse.urlencode(dict),encoding="utf8")
req = request.Request(url=url,data=data,headers=headers,method="POST")
response = request.urlopen(req)
print(response.read().decode("utf-8"))