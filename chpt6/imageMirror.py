from anonBrowser import *
from BeautifulSoup import BeautifulSoup
import os , optparse

def mirrorImages(url , dir):
	ab=anonBrowser()
	ab.anonymize()
	html=ab.open(url)
	soup=BeautifulSoup(html)
	image_tags=soup.findAll('img')
	for image in image_tags:
		filename=image['src'].lstrip('http://')
		filename=os.path.join(dir,filename.replace('/','_'))
		print '[+] Saving'+str(filename)
		data= ab.open(image['src']).read()
		ab.back()
		save=open(filename,'wb')
		save.write(data)
		save.close()


def main():
	parser=optparse.OptionParser('usage %prog -u <targetUrl> -d <dest directory>')
	parser.add_option('-u' , dest='tgtURL' , type='string' , help='specify target url')
	parser.add_option('-d' , dest='dir',type='string',help='directory to download images')
	(options,args)=parser.parse_args()
	if options.tgtURL==None or options.dir==None:
		print parser.usage
		exit(0)
	else:
		try:
			mirrorImages(options.tgtURL,options.dir)
		except Exception , e:
			print '[-] Could not mirror images'
			print '[-]'+str(e)

if __name__=='__main__':
	main()
