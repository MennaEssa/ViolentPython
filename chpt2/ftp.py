import ftplib

def anonLogin(hostname):
	try:
		ftp=ftplib.FTP(hostname)
		ftp.login('anonymous','me@your.com')
		print('[*] Logged in..')
		ftp.quit()
		return True

	except Exception,e:
		print ('[-] Login failed')
		return False

host="192.168.1.17"
anonLogin(host)

