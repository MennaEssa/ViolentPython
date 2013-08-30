import mechanize

def testProxy(url, proxy):
	browser=mechanize.Browser()
	browser.set_proxies(proxy)
	page=browser.open(url)
	source_code=page.read()
	print source_code

url='http://whatismyip.com'
proxy={'http':'108.61.89.152:8089'}
testProxy(url,proxy)
