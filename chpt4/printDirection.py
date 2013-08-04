import dpkt 
import socket , pygeoip , optparse

gi=pygeoip.GeoIP('/home/maj00/GeoLiteCity.dat')

def retGeoStr(ip):
	try:
		rec=gi.record_by_name(ip)
		city=rec['city']
		country=rec['country_code3']
		if(city != ''):
			geoLoc= city+" ,"+country
		else:
			geoLoc=country
		return geoLoc

	except Exception,e:
		return "unknown location"


def printPcap(pcap):
	for(ts , buf) in pcap:
		try:
			eth=dpkt.ethernet.Ethernet(buf)
			ip=eth.data
			src=socket.inet_ntoa(ip.src)
			dst=socket.inet_ntoa(ip.dst)
			print "\n[+] [{0}] src : {1} [{2}]==> Dst : {3} [{4}] ".format(ts,src,retGeoStr(src),dst,retGeoStr(dst))
		except:
			pass

def main():

	parser=optparse.OptionParser('usage %prog -p <pcap file>')
	parser.add_option('-p',dest='pcap_file',type='string',help='pcap file')
	(options,args)=parser.parse_args()
	if options.pcap_file==None:
		print parser.usage
		exit(0)
	f=open(options.pcap_file)
	pcap=dpkt.pcap.Reader(f)
	printPcap(pcap)
	print "done.."


if __name__=='__main__':
	main()
