from anonBrowser import *
from BeautifulSoup import BeautifulSoup
import os , optparse
def printLinks(url):
	ab=anonBrowser()
	ab.anonymize()
	page=ab.open(url)
	html=page.read()
	try:
		soup=BeautifulSoup(html)
		links = soup.findAll(name='a')
		for link in links:
			if link.has_key('href'):
				print link['href']
	except:
		pass


def main():
	parser=optparse.OptionParser("usage %prog -u <targe url>")
	parser.add_option('-u',dest='turl',type='string',help='Specify target url')
	(options,args)=parser.parse_args()
	if options.turl==None:
		print parser.usage
		exit(0)
	else:
		printLinks(options.turl)
	
if __name__=='__main__':
	main()
