# coding=utf-8

import mechanize
import urllib
import os
from BeautifulSoup import BeautifulSoup

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36")]
br.open('https://edas.info/')
br.select_form(nr=0)
br["username"] = "username"
br["password"] = "password"
br.submit()
my_list = [
	#docIds
]
for docid in my_list:
	soup = BeautifulSoup(br.open('https://edas.info/showPaper.php?m='+docid).read())
	status = soup.find(attrs={'title': "Change paper status"})
	if status.text == "accepted":
		table = soup.find(attrs={'class': "authors"})
		os.makedirs(docid)
		br.retrieve('https://edas.info/showManuscript.php?type=final&m='+docid+'&ext=pdf',docid+'/doc.pdf')[0]
		f = open(docid+'/title.txt', 'w')
		f.write(soup.title.text)
		f = open(docid+'/authors.txt', 'w')
		f.write(str(table))