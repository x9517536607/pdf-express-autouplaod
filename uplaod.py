# coding=utf-8

import mechanize
import urllib
import os
from BeautifulSoup import BeautifulSoup


#login
br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36")]
br.open('http://www.pdf-express.org/')
br.select_form(nr=0)
br["SiteID"] = "ID"
br["email"] = "email"
br["password"] = "password"
br.submit()





my_list = [
	#"docIds"
]
for docid in my_list:
	#if os.path.exists(docid):
	br.open('https://www.pdf-express.org/uploadprep.asp')
	br.select_form(nr=0)
	br.set_value(docid, type="textarea", nr=0)
	br.submit()
	br.select_form(nr=0)
	br.add_file(open(docid+'/doc.pdf'), 'application/pdf', 'doc.pdf')#upload file
	br.set_all_readonly(False)
	br.submit()
	#else:
	#	print docid+"\n"