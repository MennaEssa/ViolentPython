import time
import optparse
from scapy.all import *
from IPy import IP as IPTEST

ttlValues={}
THRESH=5

def checkTTL(ipsrc,ttl):
	if IPTEST(ipsrc).iptype()=='PRIVATE':
		return 
	if not ttlValues.has_key(ipsrc):
		pkt=sr1(IP(dst=ipsrc)/ICMP(), retry=0 , timeout=1 , verbose=0)
		ttlValues[ipsrc]=pkt.ttl
		if abs(int(ttl)-int(ttlValues[ipsrc]))> THRESH:
			print '[!]Detected Possible Spoofed packet :\n'+ ipsrc
			print '[!]TTL : '+ ttl +' , Actual TTL: ' + str(ttlValues[ipsrc])


def testTTL(pkt):
	if pkt.haslayer(IP):
		try:

			ipsrc=pkt.getlayer(IP).src
			ttl=str(pkt.ttl)
			checkTTL(ipsrc,ttl)
		except:
			pass




def main():
	parser=optparse.OptionParser("usage%prog -i <interface> -t <threshold>")
	parser.add_option('-i', dest="iface" , type="string" , help="Network interface , eth0 by default")
	parser.add_option('-t' , dest="thresh",type="int" , help="Threshold count (max difference to expect)")
	(options,args) = parser.parse_args()
	if options.iface==None:
		conf.iface='eth0'
	else:
		conf.iface=options.iface

	if options.thresh == None:
		THRESH=5
	else:
		THRESH = options.thresh

	sniff(prn=testTTL , store=0)


if __name__ == "__main__":
	main()
		

