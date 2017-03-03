#coding=utf-8
#测试输出
import os
# name = "小说名字"
# section = "章节名字"
# content = "小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容小说内容"
# s = os.getcwd()
# #os.mkdir("novel")
# os.chdir("novel")
# f = open(name+".txt","w+")
# f.write(name+"\n")

import urllib2
from bs4 import BeautifulSoup as bs
#获取文章主内容，使用BeautifulSoup
def getcontents(html):
	soup = bs(html,"html.parser")
	print type(soup)
	neirong = soup.find('div', attrs={'class': 'neirong'}).contents
	return neirong

def gethtml(url):
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	html = response.read()
	#html = html.decode("utf-8")
	return html
url = "https://www.51shucheng.com/wuxia/bixuejian/1053.html"


f = open("santi.txt","w+")
neirong = getcontents(gethtml(url))
#长度为3有<br>标签否则没有
# if len(neirong) == 0:
	# s = neirong[1].getText()
	# f.write(s.encode("GBK","ignore"))
	# print s
	# print type(s)
# else:
	# for nr in neirong:
		# s = nr.string.encode("GBK","ignore")
		# f.write(s.encode("GBK","ignore"))
#利用try语句遇到<br>标签时直接getText()
for nr in neirong:
	try:
		s = nr.string.encode("GBK","ignore")
		f.write(s)
	except AttributeError:
		s = nr.getText()
		f.write(s.encode("GBK","ignore"))
f.close()






input("asdf")

