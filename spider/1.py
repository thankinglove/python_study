#!/usr/bin/env python

import re
from urllib.request import urlopen
from urllib.request import urlretrieve


def getHtml(url):
    return urlopen(url).read().decode('utf-8')


def getImage(html):
    re_img = re.compile(r'<img class="BDE_Image" src="(.*?)".*?>')
    img_list = re_img.findall(html)
    return img_list


def downImg(list_img):
    i = 1
    for item in list_img:
        print(item)
        urlretrieve(item, filename="%s.jpg" % i)
        i += 1


if __name__ == "__main__":
    url = "http://tieba.baidu.com/p/4229162765"
    page = getHtml(url)
    img = getImage(page)
    print(img)
    # for item in img:
    #     print(item)
    downImg(img)
