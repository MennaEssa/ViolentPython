import ftplib

def retDef(ftp):
	try:
		dirList=ftp.nlst()
	except:
		dirList=[]
		print '[-] Failed to list directory , skipping'
	retList=[]
	for fileName in dirList:
		fn=fileName.lower()
		if '.php' in fn or '.htm' in fn or '.asp' in fn:
			retList.append(fileName)
			print '[+] found default page ' + fileName
	return retList

#replace those with whatever you want
#this was just for testing no harm intended
#tested on an anonymous server , too lazy to setup a new VM 

host ="192.168.17"
userName="anonymous"
passowrd="me@your.com"

ftp=ftplib.FTP(host)
ftp.login(userName,password)
print "[*] Logged in , scanning dirs "
retDef(ftp)



