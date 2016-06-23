import os
import time
import re
from multiprocessing.pool import Pool

def wget_cookie(url):
	data = os.popen('wget -qO- --no-cookies --header "Cookie: PREF=ID=1111111111111111:FF=0:LD=en:TM=1436290443:LM=1436416084:GM=1:V=1:S=OAaQWZel2Z7y4x1p; NID=74=GLwB9lf6lZlA5_McRg8SlHSZ8yX1Kgyfg5Ws_8TxuMzk1PxAPTuo8rlQGSgiZMA-qLf30iwlQAtiz5rlitcVTHMOW7rOv9VvEATdigqequ1R7Vw-K2fDKYDXQx890ZeIr3VGCBpT_Y2qnVwkAQbuTeV96zbPOItcst2Vv65f3cWeL32iKowtBN-5plPXu8ryEhE-Y1mnSdfG9pO16fwPNP_xqMHM6nBVPu-7-Wxhd1Sva4RtZKJ7_mrIljfWbnb8pi3udFecv7HroY2L4N4Gg5npQbkJ789IdLmPy0QmZGpsXDEuq4CAat32c_EdmWSrXO0; SID=DQAAALkBAACNQ2_VECWVHHPvzPw5zeCz4i7sCGrZ-EPJnSstSx_bAHKaUK-sGsJz_NsCJarNpJ6qe-5Ts6fGe5c0FypLc0OKOcBiFEuNziFTPoNDFGVREU5RDBPd0s95-SrwlQyJYkIMbtad44X0QdEf52b9jX4sOFQ088XTCd3D5LBEycjM6Opsekt_ftzt1kp52LeDx8-jjBz4MW-_Z7TDlZaSNxoVy3w4IDFfll7gJf3u75Rc8EA78XTLUXh1DVfIq7oYtwGDQ36tZ6rnWHajS-toXtEDdUma1P5CRXr13OZ5pEwLAT8qGFc3q7GKelHa0l5HcSe6izm7BhoaZq_c4qspMOxfbDBBam3vGMOvqrzKBT6U7mIQuIidZYFWn--SePbFSN_JW3bExOGiwbvlagNX0M9LpU7CxdsbdNlxkcwq0466u-rI-eOnauauJWPvSVUuCIE_RxUsuDCw90lGGfT2wNFR5zBnMzC0VLctZFS-HhXjMkrs3-KxcUDYsRYEX2dbU4YV8uV9yg5JfEuufmMMKQNNqQKB-xBEmFScpVMvso9tmt3I7-0T7bXi9NaYcZ6cD0BZXFHJ7zmRQ_MVI6kXUTXZ; HSID=ATVQjd3hxGbpcRAUF; SSID=AZjLdgea1C8pxyeyc; APISID=soBn4_aazTI4Wywn/ADRCh3F_lHo-hPEXx; SAPISID=vhXD61-cvsSQwADN/A8hDmgS1-sePcS7Rp; _ga=GA1.3.1983500809.1437616179; OGPC=4061155-2:; PLAY_ACTIVE_ACCOUNT=ICrt_XL61NBE_S0rhk8RpG0k65e0XwQVdDlvB6kxiQ8=mounarajan@semantics3.com; PLAY_PREFS=CtwDCKrLu9TFChLSAwoCSU4Q8Pn0zZgqGpcDERITFBUWGNQB1QGDAqsC2QPCBMQE4wXlBegF1wbYBt4G3wbdD_APkJWBBpGVgQaSlYEGk5WBBpWVgQaXlYEGpJWBBq2VgQa4lYEGwZWBBsSVgQbFlYEGyJWBBs6VgQbPlYEG0JWBBtSVgQbZlYEG65WBBuyVgQbtlYEG8pWBBviVgQb5lYEGhpaBBoiWgQaMloEGj5aBBpCWgQaeloEGn5aBBqCWgQahloEGppaBBqeWgQaoloEGypeBBu6XgQbvl4EGgZiBBoWYgQa-mIEGiJqBBqObgQatm4EGy5uBBrudgQa8nYEGw52BBsSdgQbFnYEGxp2BBsedgQbdnYEG7J2BBpCegQbon4EG-5-BBoCggQakoIEG9aCBBoShgQaQoYEGwKGBBsuhgQbMoYEGzaGBBu6hgQbxoYEG4qKBBvOigQaxo4EGmqSBBrKkgQbvpIEGhKWBBq-lgQbqpYEGnaaBBsamgQa3p4EGx6eBBo-ogQbNqIEGvKyBBoOugQaZr4EG1q-BBtivgQbjr4EGlbCBBuD8nDEo8Pn0zZgqOiQxYTBmN2Q0Yy1hZDNlLTQ2NTAtYmU3Ny1jYmY1Njk3ZmI2YjQ:S:ANO1ljKOEhExS4ysyg; _gat=1;" %s'% url).read()
	print data

def wget_sepcial(url):
	data = os.popen('wget  -qO- --header="Accept: text/html" --user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:21.0) Gecko/20100101 Firefox/21.0"  %s'% url).read()
	return data

def extractUrls(url):
	f1 = open('cat_links.txt','a')
	f5 = open('app_links.txt','a')
	f2 = open('main_links.txt','a')
	url = re.sub(r'(?mis)[\s\n]*','',url)
	data = wget_sepcial(url)
	data = str(data)
	if re.search(r'(?mis)data\-uitype\=\"\d+\"\shref\=\"([^\"]*)\"\saria\-hidden\=\"true\"\stab',data):
		links1 = re.findall(r'data\-uitype\=\"\d+\"\shref\=\"([^\"]*)\"\saria\-hidden\=\"true\"\stab',data)
		for li in links1:
			if re.search(r'\/',li):
				li = re.sub(r'^','https://play.google.com',li)
				print li
				f5.write(li+"\n")
			else:
				print li 
				f5.write(li+"\n")
	if re.search(r'(?mis)data\-uitype\=\"290\"\shref\=\"([^\"]*c=apps)\"',data):
			latest_url = re.findall(r'(?mis)data\-uitype\=\"290\"\shref\=\"([^\"]*c=apps)\"',data)
			for li in latest_url:
				if re.search(r'\/',li):
					li = re.sub(r'^','https://play.google.com',li)
					print li
					f2.write(li+"\n")
				else:
					print li 
					f2.write(li+"\n")
	if re.search(r'(?mis)href\=\"([^\"]*)\"\stitle\=\"[^\"]*\"\sjsl\=\"[^\"]*\"\sjsan\=\"7',data):
		links = re.findall(r'(?mis)href\=\"([^\"]*)\"\stitle\=\"[^\"]*\"\sjsl\=\"[^\"]*\"\sjsan\=\"7',data)
		for li in links:
			if re.search(r'\/',li):
				li = re.sub(r'^','https://play.google.com',li)
				print li
				f1.write(li+"\n")
			else:
				print li 
				f1.write(li+"\n")
	num = 5
	extractUrls1("https://play.google.com/store/apps?start={0}&num=5".format(num),num)

def extractUrls1(url,num):
	f1 = open('dara.html','w')
	f2 = open('main_links.txt','a')
	f5 = open('app_links.txt','a')
	url = re.sub(r'(?mis)[\s\n]*','',url)
	print url
	data = wget_sepcial(url)
	data = str(data)
	f1.write(data)
	if re.search(r'(?mis)data\-uitype\=\"\d+\"\shref\=\"([^\"]*)\"\saria\-hidden\=\"true\"\stab',data):
		links1 = re.findall(r'data\-uitype\=\"\d+\"\shref\=\"([^\"]*)\"\saria\-hidden\=\"true\"\stab',data)
		for li in links1:
			if re.search(r'\/',li):
				li = re.sub(r'^','https://play.google.com',li)
				print li
				f5.write(li+"\n")
			else:
				print li 
				f5.write(li+"\n")
	if re.search(r'(?mis)data\-uitype\=\"290\"\shref\=\"([^\"]*c=apps)\"',data):
			latest_url = re.findall(r'(?mis)data\-uitype\=\"290\"\shref\=\"([^\"]*c=apps)\"',data)
			for li in latest_url:
				if re.search(r'\/',li):
					li = re.sub(r'^','https://play.google.com',li)
					print li
					f2.write(li+"\n")
				else:
					print li 
					f2.write(li+"\n")
	if re.search(r'(?mis)href\=\"[^\?]*\?start\=(\d+)\"\srel\=\"c',data):
		check = re.findall(r'(?mis)href\=\"[^\?]*\?start\=(\d+)\"\srel\=\"c',data)[0]
		print "printiing"
		check = int(check)
		print num
		if (num == check):
			print "yes"
			num = num + 5
			extractUrls1("https://play.google.com/store/apps?start={0}&num=5".format(num),num)
		else:
			pass

def assigneCategory():
	f2 = open('cat_links1.txt','r')
	f1 = open('main_links.txt','a')
	f3 = open('main_links.html','w')
	f5 = open('app_links.txt','a')
	for url in f2:
		url = re.sub(r'(?mis)[\s\n]*','',url)
		print url
		data = wget_sepcial(url)
		data = str(data)
		if re.search(r'(?mis)data\-uitype\=\"\d+\"\shref\=\"([^\"]*)\"\saria\-hidden\=\"true\"\stab',data):
			links1 = re.findall(r'data\-uitype\=\"\d+\"\shref\=\"([^\"]*)\"\saria\-hidden\=\"true\"\stab',data)
			for li in links1:
				if re.search(r'\/',li):
					li = re.sub(r'^','https://play.google.com',li)
					print li
					f5.write(li+"\n")
				else:
					print li 
					f5.write(li+"\n")
		if re.search(r'(?mis)data\-uitype\=\"290\"\shref\=\"([^\"]*)\"',data):
			print "yes"
			latest_url = re.findall(r'(?mis)data\-uitype\=\"290\"\shref\=\"([^\"]*)\"',data)
			for li in latest_url:
				if re.search(r'\/',li):
					li = re.sub(r'^','https://play.google.com',li)
					print li
					f1.write(li+"\n")
				else:
					print li 
					f1.write(li+"\n")


def extracctMainurls():
	f2 = open('main_links1.txt','r')
	f5 = open('app_links.txt','a')
	#f2 = ["https://play.google.com/store/apps/category/BOOKS_AND_REFERENCE/collection/topselling_paid","https://play.google.com/store/apps/category/BOOKS_AND_REFERENCE/collection/topselling_free"]
	for url in f2:
		url = re.sub(r'(?mis)[\s\n]*','',url)
		time.sleep(2)
		print url
		data = wget_sepcial(url)
		data = str(data)
		num = 0
		appe = "?start={0}&num=60".format(num)
		if re.search(r'(?mis)data\-uitype\=\"\d+\"\shref\=\"([^\"]*)\"\saria\-hidden\=\"true\"\stab',data):
			links1 = re.findall(r'data\-uitype\=\"\d+\"\shref\=\"([^\"]*)\"\saria\-hidden\=\"true\"\stab',data)
			for li in links1:
				if re.search(r'\/',li):
					li = re.sub(r'^','https://play.google.com',li)
					print li
					f5.write(li+"\n")
				else:
					print li 
					f5.write(li+"\n")

		if re.search(r'(?mis)card\-click\-target\"\shref\=\"([^\"]*)\"',data):
			links1 = re.findall(r'card\-click\-target\"\shref\=\"([^\"]*)\"',data)
			for li in links1:
				if re.search(r'\/',li):
					li = re.sub(r'^','https://play.google.com',li)
					print li
					f5.write(li+"\n")
				else:
					print li 
					f5.write(li+"\n")

		if re.search(r'(?mis)followup\=([^\"]*)\"',data):
			links1 = re.findall(r'(?mis)followup\=([^\"]*)\"',data)[0]
			if re.search(r'\/',links1):
				links1 = re.sub(r'^\/','https://play.google.com',links1)
				url = links1 + appe
				print url
				num = num + 60
				extracctMainurls1(url,num)
			else:
				url = links1 + appe
				print url
				num =  num +60
				extracctMainurls1(url,num)

def extracctMainurls1(url,num):
	f2 = [url]
	f5 = open('app_links.txt','a')
	appe = "?start={0}&num=60".format(num)
	for url in f2:
		url = re.sub(r'(?mis)[\s\n]*','',url)
		print url
		time.sleep(2)
		data = wget_sepcial(url)
		data = str(data)
		if re.search(r'(?mis)data\-uitype\=\"\d+\"\shref\=\"([^\"]*)\"\saria\-hidden\=\"true\"\stab',data):
			links1 = re.findall(r'data\-uitype\=\"\d+\"\shref\=\"([^\"]*)\"\saria\-hidden\=\"true\"\stab',data)
			for li in links1:
				if re.search(r'\/',li):
					li = re.sub(r'^','https://play.google.com',li)
					print li
					f5.write(li+"\n")
				else:
					print li 
					f5.write(li+"\n")

		if re.search(r'(?mis)card\-click\-target\"\shref\=\"([^\"]*)\"',data):
			links1 = re.findall(r'card\-click\-target\"\shref\=\"([^\"]*)\"',data)
			for li in links1:
				if re.search(r'\/',li):
					li = re.sub(r'^','https://play.google.com',li)
					print li
					f5.write(li+"\n")
				else:
					print li 
					f5.write(li+"\n")

		if re.search(r'(?mis)followup\=([^\"]*)\"',data):
			links1 = re.findall(r'(?mis)followup\=([^\"]*)\"',data)[0]
			links1 = re.sub(r'(.*)\?.*',r'\1',links1)
			if re.search(r'\/',links1):
				links1 = re.sub(r'^\/','https://play.google.com',links1)
				url = links1 + appe
				print url
				if re.search(r'(?mis).*aria-hidden="true" tabindex="-1">\s(\d+).*?Site\sTerms\sof\sService',data):
					check = re.findall(r'(?mis).*aria-hidden="true" tabindex="-1">\s(\d+).*?Site\sTerms\sof\sService',data)[0]
					print "printiing"
					print type(check)
					check = int(check)
					print type(check)
					print num
					print check
					if (num == check):
						print "yes"
						num = num + 60
						extracctMainurls1(url,num)
			else:
				url = links1 + appe
				print url
				if re.search(r'(?mis).*aria-hidden="true" tabindex="-1">\s(\d+).*?Site\sTerms\sof\sService',data):
					check = re.findall(r'(?mis).*aria-hidden="true" tabindex="-1">\s(\d+).*?Site\sTerms\sof\sService',data)[0]
					print "printiing"
					print type(check)
					check = int(check)
					print type(check)
					print num
					print check
					if (num == check):
						print "yes"
						num = num + 60
						extracctMainurls1(url,num)

def get_data():
	f2 = open('app_links1.txt','r')

	nprocs = 500 # nprocs is the number of processes to run
	ParsePool = Pool(nprocs)
	#ParsePool.map(btl_test,url)
	ParsedURLS = ParsePool.map(deatilsExtract,f2)
	ParsePool.close()
	ParsePool.join()

def get_urls1():
	f2 = open('app_links.txt','r')

	nprocs = 500 # nprocs is the number of processes to run
	ParsePool = Pool(nprocs)
	#ParsePool.map(btl_test,url)
	ParsedURLS = ParsePool.map(urlsDeatilsExtract,f2)

def links_pag(url):
	f2 = [url]
	f5 = open('app_links.txt','a')
	for url in f2:
		url = re.sub(r'(?mis)[\s\n]*','',url)
		# print url
		time.sleep(2)
		data = wget_sepcial(url)
		data = str(data)
		if re.search(r'(?mis)data\-uitype\=\"\d+\"\shref\=\"([^\"]*)\"\saria\-hidden\=\"true\"\stab',data):
			links1 = re.findall(r'data\-uitype\=\"\d+\"\shref\=\"([^\"]*)\"\saria\-hidden\=\"true\"\stab',data)
			for li in links1:
				if re.search(r'\/',li):
					li = re.sub(r'^','https://play.google.com',li)
					print li
					f5.write(li+"\n")
				else:
					print li 
					f5.write(li+"\n")
	

def urlsDeatilsExtract(url):
	url = re.sub(r'(?mis)[\s\n]*','',url)
	url = re.sub(r'\&','\&',url)
	print url 
	time.sleep(1)
	data = wget_sepcial(url)
	data = str(data)

	if re.search(r'(?mis)href\=\"([^\"]*)\"\saria\-label\=\"\sCheck\sout',data):
		li = re.findall(r'(?mis)href\=\"([^\"]*)\"\saria\-label\=\"\sCheck\sout',data)[0]
		print li
		if re.search(r'\/',li):
			li = re.sub(r'^','https://play.google.com',li)
			print li +" -   ---------"
			links_pag(li)
		else:
			links_pag(li) 
			print li +" - ------"

	elif re.search(r'(?mis)href\=\"([^\"]*)\"\saria\-label\=\"Take',data):
		li = re.findall(r'(?mis)href\=\"([^\"]*)\"\saria\-label\=\"Take',data)[0]
		print li
		if re.search(r'\/',li):
			li = re.sub(r'^','https://play.google.com',li)
			print li +" -   ---------"
			links_pag(li)
		else:
			links_pag(li) 
			print li +" - ------"
				
		

def deatilsExtract(url):

	f3 = open('crawled_email1','a')
	f4 = open('final_data.csv','at')
	url = re.sub(r'(?mis)[\s\n]*','',url)
	url = re.sub(r'\&','\&',url)
	#url = re.sub(r'\?','\?',url)
	#url = re.sub(r'\;','\;',url)
	print url
	time.sleep(1)
	data = wget_sepcial(url)
	data = str(data)

	if re.search(r'(?mis)numDownloads">\s*([^<]*)<',data):
		noi = re.findall(r'(?mis)numDownloads">\s*([^<]*)<',data)
		print noi
	else:
		noi = ""

	if re.search(r'(?mis)itemprop="genre">([^<]*)<',data):
		cat = re.findall(r'(?mis)itemprop="genre">([^<]*)<',data)[0]
		print cat
	else:
		cat = ""

	if re.search(r'(?mis)ratingCount\"\>[^>]*>([^<]*)<',data):
		rating = re.findall(r'(?mis)ratingCount\"\>[^>]*>([^<]*)<',data)[0]
		print rating
	else:
		rating = ""

	if re.search(r'(?mis)datePublished">([^<]*)<',data):
		dp = re.findall(r'(?mis)datePublished">([^<]*)<',data)[0]
		print dp
	else:
		dp = ""

	if re.search(r'(?mis)video-image"',data):
		vi = "Yes"
		print vi
	else:
		vi = "No"

	if re.search(r'(?mis)dev\-link\"\shref\=\"mailto\:([^\"]*)\"',data):
		email = re.findall(r'(?mis)dev\-link\"\shref\=\"mailto\:([^\"]*)\"',data)[0]
		print email
		f3.write(email+"\n")
		f4.write("{0},{1},{2},{3},{4},{5},{6},{7}".format(url,url,email,noi,cat,rating,dp,vi)+"\n")
	elif re.search(r'(?mis)dev\-link\"\shref\=\"mailto\:[^\"]*\"[^>]*>([^<]*)<',data):
		email = re.findall(r'(?mis)dev\-link\"\shref\=\"mailto\:([^\"]*)\"',data)[0]
		email = re.sub(r'(?mis)Email','',email)
		email = re.sub(r'(?mis)[\s\n]*','',email)
		print email
		f3.write(email+"\n")
		f4.write("{0},{1},{2},{3},{4},{5},{6},{7}".format(url,url,email,noi,cat,rating,dp,vi)+"\n")


	if re.search(r'(?mis)dev\-link\"\shref\=\"[^\?]*\?q\=([^\&]*)\&',data):
		visit_site = re.findall(r'(?mis)dev\-link\"\shref\=\"[^\?]*\?q\=([^\&]*)\&',data)[0]
		print visit_site
		crawl_fb_again_again(visit_site,url,noi,cat,rating,dp,vi)

def crawl_fb_again_again(url1,url,noi,cat,rating,dp,vi):
		#f1 = open('facebook_crawled_urls','r+')
	sleep = 1
	main_url = url
	f2 = open('facebook_crawled_again','a')
	f3 = open('crawled_email1','a')
	f4 = open('crawled_email_ugly','a')
	f5 = open('facebook-crawled1_email_ids_report.json','a')
	f6 = open('final_data.csv','at')
	if re.search(r'^htt',url1):
		lin = re.sub(r'(?mis)[\s\n]*','',url1)
		lin = re.sub(r'\&','\&',lin)
		#lin = re.sub(r'\?','\?',lin)
		#lin = re.sub(r'\;','\;',lin)
		#print (lin)
		try:
			data = wget_sepcial(lin)
			data = data 
			data = str(data)

			if re.search(r'(?ms)og\:url\"\scontent\=\"([^\"]*)\"',data):
				email = re.findall(r'(?ms)og\:url\"\scontent\=\"([^\"]*)\"',data)
				for fb in email:
					url2 = re.sub(r'\?.*','',fb)
					if re.search(r'^htt',url2):
						fb_cac = re.sub(r'\?.*','',fb)
						fb_cac = re.sub(r'.*sharer\.php$','',fb_cac)
						fb_cac = re.sub(r'.*\/2008\/fbml$','',fb_cac)
						f2.write(fb_cac+"\n")
						print (fb_cac)
						time.sleep(sleep)
						if re.search(r'^htt',fb_cac):
							#print (lin)
							first = "/info?tab=page_info"
							second = "/about?section=contact-info"
							url2 = fb_cac+first   
							print (url2)  
							try:                                                                                             
								data = wget_sepcial(url2)
								data = data 
								data = str(data)
								if re.search(r'(?ms)class\=\"\_50f4\"\>([^\<]*\&\#064\;.*?[^<]*)<\/div>',data):
									link = re.findall(r'(?ms)class\=\"\_50f4\"\>([^\<]*\&\#064\;.*?[^<]*)<\/div>',data)
									for mail in link:
										mail = re.sub(r'\&\#064\;','@',mail)
										f4.write(mail+"\n")
										fmail = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*))',mail)
										for smail in fmail:

											f3.write(smail+"\n")
											f6.write("{0},{1},{2},{3},{4},{5},{6},{7}".format(url,url1,smail,noi,cat,rating,dp,vi+"\n"))
											f5.write("{\""+lin+"\" => \""+smail+"\"}"+"\n")
											print (smail)
							except Exception: 
								pass    

			if re.search(r'(?mis)a\sclass\=\"\_8\_2\"\shref\=\"([^\"]*)',data):
				email = re.findall(r'(?mis)a\sclass\=\"\_8\_2\"\shref\=\"([^\"]*)',data)
				for fb in email:
					url2 = re.sub(r'\?.*','',fb)
					if re.search(r'^htt',url2):
						fb_cac = re.sub(r'\?.*','',fb)
						fb_cac = re.sub(r'.*sharer\.php$','',fb_cac)
						fb_cac = re.sub(r'.*\/2008\/fbml$','',fb_cac)
						f2.write(fb_cac+"\n")
						print (fb_cac)
						time.sleep(sleep)
						if re.search(r'^htt',fb_cac):
								#print (lin)
							first = "/info?tab=page_info"
							second = "/about?section=contact-info"
							url2 = fb_cac+first   
							print (url2)  
							try:                                                                                             
								data = wget_sepcial(url2)
								data = data 
								data = str(data)
								if re.search(r'(?ms)class\=\"\_50f4\"\>([^\<]*\&\#064\;.*?[^<]*)<\/div>',data):
									link = re.findall(r'(?ms)class\=\"\_50f4\"\>([^\<]*\&\#064\;.*?[^<]*)<\/div>',data)
									for mail in link:
										mail = re.sub(r'\&\#064\;','@',mail)
										f4.write(mail+"\n")
										fmail = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*))',mail)
										for smail in fmail:
											f3.write(smail+"\n")
											f6.write("{0},{1},{2},{3},{4},{5},{6},{7}\n".format(url,url1,smail,noi,cat,rating,dp,vi)+"\n")
											f5.write("{\""+lin+"\" => \""+smail+"\"}"+"\n")
											print (smail)
							except Exception: 
								pass


			else: 
				print ("not found")
				f5.write("{\""+lin+"\" => \""+"not found"+"\"}"+"\n")
		except Exception: 
			pass


	if re.search(r'^\w',url1):
		lin = re.sub(r'(?mis)[\s\n]*','',url1)
		lin = re.sub(r'\&','\&',lin)
		#lin = re.sub(r'\?','\?',lin)
		#lin = re.sub(r'\;','\;',lin)
		try:
			url_lin = re.sub(r'(.*?\/)',r"\1",lin)
			print (url_lin)
			data = wget_sepcial(url_lin)
			data = data 
			data = str(data) 
				
			if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
				email = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)[0]
				if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',email):
					email = re.sub(r'(.*)\/',r"\1",email)
					f3.write(email+"\n")
					f6.write("{0},{1},{2},{3},{4},{5},{6},{7}".format(url,url1,email,noi,cat,rating,dp,vi)+"\n")
											#f4.write("{\""+lin+"\" => \""+email+"\"}"+"\n")
					print (email)

			if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
				email = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)
				for mail in email:
					if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',mail):
						mail = re.sub(r'(.*)\/',r"\1",mail)
						f3.write(mail+"\n")
						f6.write("{0},{1},{2},{3},{4},{5},{6},{7}".format(url,url1,mail,noi,cat,rating,dp,vi)+"\n")
								#f4.write("{\""+lin+"\" => \""+mail+"\"}"+"\n")
						print (mail)
			if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
				must = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)
				for mail in must:
					if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',mail):
						mail = re.sub(r'(.*)\/',r"\1",mail)
						f3.write(mail+"\n")
						f6.write("{0},{1},{2},{3},{4},{5},{6},{7}".format(url,url1,mail,noi,cat,rating,dp,vi)+"\n")
								#f4.write("{\""+lin+"\" => \""+mail+"\"}"+"\n")
						print (mail)

			if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\+]*))',data):
				ear = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\_\-\+]*))',data)[0]
				ear = re.sub(r'(.*)\/',r"\1",ear)
				f3.write(ear+"\n")
				f6.write("{0},{1},{2},{3},{4},{5},{6},{7}".format(url,url1,mail,noi,cat,rating,dp,vi)+"\n")
						#f4.write("{\""+lin+"\" => \""+ear+"\"}"+"\n")
				print (ear)

			if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*))',data):
				ear = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\_\-\+]*))',data)
				for mail in ear:
					if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\+\_\-]*)',mail):
						mail = re.sub(r'(.*)\/',r"\1",mail)
						f3.write(mail+"\n")
						f6.write("{0},{1},{2},{3},{4},{5},{6},{7}".format(url,url1,mail,noi,cat,rating,dp,vi)+"\n")

			if re.search(r'(?msi)<a\s*href\=\"([^\"]*[\/]*contact.*?[^\"]*)\"',data):
				ear = re.findall(r'(?msi)<a\s*href\=\"([^\"]*[\/]*contact.*?[^\"]*)\"',data)
				#print (ear)
				if re.search(r'(?ms)^\/',ear[0]):
					ear = re.sub(r'(.*)\/',r"%s\1"%url_lin,ear[0])
					print (ear)
					link_again(ear,sleep,main_url,noi,cat,rating,dp,vi)
				if re.search(r'(?mis)^.*',ear[0]):
					ear = re.sub(r'(.*)',r"%s/\1"%url_lin,ear[0])
					print (ear)
					link_again(ear,sleep,main_url,noi,cat,rating,dp,vi)
				
					print (ear)
					link_again(ear[0],sleep,main_url,noi,cat,rating,dp,vi)

			if re.search(r'(?msi)<a\s*href\=\"([^\"]*[\/]*about.*?[^\"]*)\"',data):
				ear = re.findall(r'(?msi)<a\s*href\=\"([^\"]*[\/]*about.*?[^\"]*)\"',data)
				if re.search(r'(?ms)^\/',ear[0]):
					ear = re.sub(r'(.*)\/',r"%s\1"%url_lin,ear[0])
					print (ear)
					link_again(ear,sleep,main_url,noi,cat,rating,dp,vi)
				if re.search(r'(?mis)^.*',ear[0]):
					ear = re.sub(r'(.*)',r"%s/\1"%url_lin,ear[0])
					print (ear)
					link_again(ear,sleep,main_url,noi,cat,rating,dp,vi)
					
				print (ear)
				link_again(ear[0],sleep,main_url,noi,cat,rating,dp,vi)

			if re.search(r'(?msi)<a.*?href\=\"([^\"]*[\/]*contact.*?[^\"]*)\"',data):
				ear = re.findall(r'(?msi)<a.*?href\=\"([^\"]*[\/]*contact.*?[^\"]*)\"',data)[0]
				#print (ear)
				#if re.search(r'(?ms)^\/',ear[0]):
				
				print (ear)
				link_again(ear,sleep,main_url,noi,cat,rating,dp,vi)
				#if re.search(r'(?mis)^.*',ear[0]):
				#	ear = re.sub(r'(.*)',r"%s/\1"%url_lin,ear[0])
				#	print (ear)
				#	link_again(ear,sleep,main_url)
				

			if re.search(r'(?msi)<a.*?href\=\"([^\"]*[\/]*about.*?[^\"]*)\"',data):
				ear = re.findall(r'(?msi)<a\s*href\=\"([^\"]*[\/]*about.*?[^\"]*)\"',data)[0]
				#if re.search(r'(?ms)^\/',ear[0]):
				#ear = re.sub(r'(.*)\/',r"%s\1"%url_lin,ear[0])
				print (ear)
				link_again(ear,sleep,main_url,noi,cat,rating,dp,vi)
				#if re.search(r'(?mis)^.*',ear[0]):
				#	ear = re.sub(r'(.*)',r"%s/\1"%url_lin,ear[0])
				#	print (ear)
				#	link_again(ear,sleep,main_url)
					
				#print (ear)
				#link_again(ear[0],sleep,main_url)

		except Exception: 
			pass  

def link_again(url,sleep,main_url,noi,cat,rating,dp,vi):
		f2 = open('facebook_crawled_again','a')
		f3 = open('crawled_email1','a')
		f4 = open('crawled_email_ugly','a')
		f5 = open('facebook-crawled_email_ids_report.json','a')
		f6 = open('contact-links','a')
		f7 = open('final_data.csv','at')
											#f4.write("{\""+lin+"\" => \""+email+"\"}"+"\n")

		if re.search(r'^\w',url):
			lin = re.sub(r"\s*","",url)
			print (lin)
			try:
				data = wget_sepcial(lin)
				data = str(data) 

				if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
					email = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)[0]
					if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',email):
						email = re.sub(r'(.*)\/',r"\1",email)
						f3.write(email+"\n")
						f7.write("{0},{1},{2},{3},{4},{5},{6},{7}".format(main_url,url,mail,noi,cat,rating,dp,vi)+"\n")				#f4.write("{\""+lin+"\" => \""+email+"\"}"+"\n")
						print (email)

				if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
					email = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)
					for mail in email:
						if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',mail):
							mail = re.sub(r'(.*)\/',r"\1",mail)
							f3.write(mail+"\n")
							f7.write("{0},{1},{2},{3},{4},{5},{6},{7}".format(main_url,url,mail,noi,cat,rating,dp,vi)+"\n")	
									#f4.write("{\""+lin+"\" => \""+mail+"\"}"+"\n")
							print (mail)
				if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
					must = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)
					for mail in must:
						if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',mail):
							mail = re.sub(r'(.*)\/',r"\1",mail)
							f3.write(mail+"\n")
							f7.write("{0},{1},{2},{3},{4},{5},{6},{7}".format(main_url,url,mail,noi,cat,rating,dp,vi)+"\n")		
									#f4.write("{\""+lin+"\" => \""+mail+"\"}"+"\n")
							print (mail)

				if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\+]*))',data):
					ear = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\_\-\+]*))',data)[0]
					ear = re.sub(r'(.*)\/',r"\1",ear)
					f3.write(ear+"\n")
					f7.write("{0},{1},{2},{3},{4},{5},{6},{7}".format(main_url,url,mail,noi,cat,rating,dp,vi)+"\n")	
							#f4.write("{\""+lin+"\" => \""+ear+"\"}"+"\n")
					print (ear)

				if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*))',data):
					ear = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\_\-\+]*))',data)
					for mail in ear:
						if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\+\_\-]*)',mail):
							mail = re.sub(r'(.*)\/',r"\1",mail)
							f3.write(mail+"\n")
							f7.write("{0},{1},{2},{3},{4},{5},{6},{7}".format(main_url,url,mail,noi,cat,rating,dp,vi)+"\n")	

			except Exception: 
				pass  

		
def dedupUrls():
	with open('cat_links.txt') as result:
		uniqlines = set(result.readlines())
		with open('cat_links1.txt', 'w') as rmdup:
			rmdup.writelines(set(uniqlines))

def dedupUrls1():
	with open('main_links.txt') as result:
		uniqlines = set(result.readlines())
		with open('main_links1.txt', 'w') as rmdup:
			rmdup.writelines(set(uniqlines))

def dedupUrls2():
	with open('crawled_email1') as result:
		uniqlines = set(result.readlines())
		with open('crawled_email1', 'w') as rmdup:
			rmdup.writelines(set(uniqlines))

def dedupUrls3():
	with open('final_data.csv') as result:
		uniqlines = set(result.readlines())
		with open('final_data1.csv', 'w') as rmdup:
			rmdup.writelines(set(uniqlines))





extractUrls("https://play.google.com/store/apps")
dedupUrls()

assigneCategory()
dedupUrls1()
#extracctMainurls()
#deatilsExtract("https://play.google.com/store/apps/details?id=com.tocaboca.tocakitchen2")
#urlsDeatilsExtract("https://play.google.com/store/apps/details?id=com.issess.flashplayerpro")
get_urls1()
#dedupUrls2()
get_data()
#dedupUrls3()

	
