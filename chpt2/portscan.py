import optparse
from socket import *
from threading import *

screenLck=Semaphore(value=1)
def connScan(host,port):
	try:

		sock=socket(AF_INET,SOCK_STREAM)
		sock.connect((host,port))
		sock.send("Peek a Boo\r\n ")
		results=sock.recv(100)
		screenLck.acquire()
		print '[+] {0}/TCP open\n'.format(port)
		print '[+] Banner: {0} \n'.format(str(results))
	except:
		screenLck.acquire()
		print '[-] {0}/TCP closed\n'.format(port)

	finally:
		screenLck.release()
		sock.close()
def portScan(host,ports):
	try:
		tIP=gethostbyname(host)
	except:
		print "[-] unable to resolve {0} : check IP ?\n".format(host)
		return

	try:
		tName=gethostbyaddr(tIP)
		print "[+] Scan results for host : {0}\n".format(tName)
 	except:
		print "[+] Scan results for IP : {0}\n".format(tIP)
	setdefaulttimeout(1)
	for tport in ports:
		print "Scanning port {0}\n".format(tport)
		t=Thread(target=connScan, args=(host , int(tport)))
		t.start()

def main():
	parser=optparse.OptionParser('usage : %prog -H <host> -P <port>')
	parser.add_option('-H',dest='hst',type='string',help='target host ip')
	parser.add_option('-P',dest='prt',type='string',help='target port(s) separated by commas.')
	(options,args)=parser.parse_args()
	target=options.hst
	ports=str(options.prt).split(',')
	if (target==None) | (ports  == None) :
		print parser.usage
		exit(0)
	portScan(target , ports)


if __name__=='__main__':
	main()
