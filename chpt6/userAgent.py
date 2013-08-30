import mechanize

def testUserAgent(url,userAgent):
	browser=mechanize.Browser()
	browser.addheaders=userAgent
	page=browser.open(url)
	source_code=page.read()
	print source_code



url='http://whatismyuseragent.dotdoh.com/'
userAgent= [('User-agent', 'Lynx/2.8.8dev.3 libwww-FM/2.14 SSL-MM/1.4.1' )]
testUserAgent(url,userAgent)
