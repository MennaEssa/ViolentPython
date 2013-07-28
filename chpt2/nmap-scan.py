import nmap
import optparse
from threading import *

Screenlck=Semaphore(value=1)
def nmapScan(host,port):
	nScan=nmap.PortScanner()
	nScan.scan(host,port)
	state=nScan[host]['tcp'][int(port)]['state']
	Screenlck.acquire()
	print "[*] {0} tcp/{1} {2}".format(host,port,state)
	Screenlck.release()
def main():

	parser=optparse.OptionParser('usage : %prog -H <host> -P <port>')
	parser.add_option('-H' , dest='thost' , type='string' , help='host ip')
	parser.add_option('-P' , dest='tport' , type='string' , help='port(s) separated by commas')
	(options,args)=parser.parse_args()
	host=options.thost
	ports=str(options.tport).split(',')
	if (host==None) | (ports==None):
		print parser.usage
		exit(0)
	for port in ports:
		t=Thread(target=nmapScan,args=(host,port))
		t.start()



if __name__=='__main__':
	main()
