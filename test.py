#coding=utf-8
import re
import urllib2
from bs4 import BeautifulSoup as bs
 
#获取网页内容
def gethtml(url):
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    html = response.read()
    return html
 
#获取文章主内容，使用BeautifulSoup
def getcontents(html):
    soup = bs(html)
    neirong = soup.find('div', attrs={'class': 'neirong'}).contents
    return neirong
 
#获取每一章链接url
def gettitleurl(url):
    html = gethtml(url)
    reg = r'<li><a href=(.+?)title='
    ulist = re.compile(reg)
    urllist = ulist.findall(html)
    return urllist
 
#获取每一章标题<h1>
def gettitle(url):
    html = gethtml(url)
    reg = r'<h1>(.+?)</h1>'
    t = re.compile(reg)
    title = t.findall(html)
    return title
 
if __name__ == '__main__':
    url = "https://www.51shucheng.com/kehuan/liucixinduanpian"
    f = open('santi.txt', 'w+')
    urllist = gettitleurl(url)
    for i in urllist:
        print i
        url = i[1:len(i)-2]
        print url
        title = gettitle(url)
        for j in title:
            print 'downloading... '+str(j.decode('utf-8'))
            f.write('\n\n'+j)
        neirong = getcontents(gethtml(url))
        for nr in neirong:
            print type(nr)
            print type(nr.string)
            s = nr.string.encode('utf-8')
            f.write(s)
    print 'download success'
    f.close()