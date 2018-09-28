import string
from quopri import quote
from urllib import request
from urllib.request import urlopen


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        # response = urlopen(url)
        url_ = quote(url, safe=string.printable)
        response = request.urlopen(url_)
        if response.getcode() != 200:
            return None
        return response.read()