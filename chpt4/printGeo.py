import pygeoip

gi=pygeoip.GeoIP('/home/maj00/GeoLiteCity.dat')

def printRecord(target):
	rec=gi.record_by_name(target)
	city=rec['city']
	region=rec['region_code']
	country=rec['country_name']
	longt=rec['longitude']
	lat=rec['latitude']

	print '[*] Target :' + target
	print '[+] {0} , {1} , {2} \n[+] Latitude:{3}, longitude: {4}'.format(city,region,country,lat,longt)


target='193.227.50.3'
printRecord(target)

