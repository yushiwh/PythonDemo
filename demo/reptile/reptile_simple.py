# 简单的爬虫例子
# coding =utf-8

import urllib.request
import re


def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html


def getImg(html):
    # 用正则表达式进行匹配
    reg = 'src="(.*?)\.jpg"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html.decode('utf-8'))
    # 打印所有的爬到的图片的url
    #  return imglist
    x = 0
    print("开始下载图片")
    for imgurl in imglist:

        # 处理一下非标准的图片  /static/images/newFront/floot_01.jpg
        if "https://" in imgurl or "http://" in imgurl:
            imgurl = imgurl + '.jpg'
        else:
            if ".jpg" in imgurl:
                imgurl = "http://test-site.ehaoyao.com/" + imgurl
            else:
                imgurl = "http://test-site.ehaoyao.com/" + imgurl + ".jpg"

        print(imgurl)

        resp = urllib.request.urlopen(imgurl)
        respHtml = resp.read()
        picFile = open('downimg/' + '%s.jpg' % x, "wb")
        picFile.write(respHtml)
        picFile.close()
        x = x + 1
        # print('x==' + x)
    print('图片下载完成')


html = getHtml("http://test-site.ehaoyao.com/")

getImg(html)
