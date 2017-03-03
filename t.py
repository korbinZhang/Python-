#coding=utf-8
import urllib2
import re
import os
from bs4 import BeautifulSoup as bs
import threading
from multiprocessing import Pool
def gethtml(url):
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	html = response.read()
	#html = html.decode("utf-8")
	return html

#小说url
def geturl(html):
	reg = r'<a href="(http.+?)"'
	nreg = re.compile(reg)
	urls = nreg.findall(html)
	return urls

#获取一章内容
def getcontents(html):
	soup = bs(html,"html.parser")
	neirong = soup.find('div', attrs={'class': 'neirong'}).contents
	return neirong

# def getsummary(html):
	# soup = bs(html)
	# summary = soup.find('div', attrs={'class': 'summary'}).contents
	# return summary

#小说书名或者章节名即<h1>标签内容
def getnames(html):
	reg = r'<h1>(.+?)</h1>'
	t = re.compile(reg)
	title = t.findall(html)
	return title

#每一章url
def gettitleurls(html):
	reg = r'<li><a href=(.+?)title='
	ulist = re.compile(reg)
	urllist = ulist.findall(html)
	return urllist


#下载一本
def one(url):
	html = gethtml(url)
	names = getnames(html)
	name = names[0].decode("utf-8")
	urllist = gettitleurls(html)
	f = open(name+".txt","w+")
	f.write(name+"\n")
	print "download..."+name
	for i in urllist:
		url = i[1:len(i)-2]
		titles = getnames(gethtml(url))
		for title in titles:
			strtitle = title.decode("utf-8")
			#print strtitle
			f.write("\n"+strtitle.encode("GBK","ignore"))
		neirong = getcontents(gethtml(url))
		#长度为3有<br>标签否则没有
		# if len(neirong) == 3:
			# f.write(neirong[1].getText().encode("GBK","ignore"))
		# else:
			# for nr in neirong:
				# s = nr.string.encode("GBK","ignore")
				# f.write(s)
		#利用try语句遇到<br>标签时直接getText()
		for nr in neirong:
			try:
				s = nr.string.encode("GBK","ignore")
				f.write(s)
			except AttributeError:
				s = nr.getText()
				f.write(s.encode("GBK","ignore"))
	print name+"download success"
	f.close()

def main():
	yurl = "http://www.51shucheng.com/wuxia"
	html = gethtml(yurl)
	urls = geturl(html)
	print urls
	os.chdir("novel")
	#threads = []
	p = Pool()
	for url in urls:
		# one(url)
		# #Thread---多线程-------------------------------------------------------------------------------------------------
		# t = threading.Thread((),target=one,args(url,))
		# threads.append(t)
	# for t in threads:
		# t.setDaemon(True)
		# t.start()
		# #Thread---------------------------------------------------------------------------------------------------
		# 多进程-------------------------------------
		p.apply_async(one, args=(url,))
	print 'Waiting for all subprocesses done...'
	p.close()
	p.join()
	print 'All subprocesses done.'



if __name__ == '__main__':
	main()
	os.system('pause')