import pexpect 
import optparse

PROMPT=['#','>>>','> ',', ','\$ ']
def send_command(child,cmd):
	child.sendline(cmd)
	child.expect(PROMPT)
	print child.before

def connect(user,host,password):
	ssh_newkey='Are you sure you want to continue connecting'
	connStr='ssh {0}@{1}'.format(user,host)
	child=child=pexpect.spawn(connStr)
	ret=child.expect([pexpect.TIMEOUT,ssh_newkey,'[P|p]assword:'])
	if ret==0:
		print '[-] Connection failed.'
		return
	if ret==1:
		child.sendline('yes')
		ret=child.expect([pexpect.TIMEOUT,'[P|p]assword:'])
	if ret==0:
		print '[-] Connection failed.'
		return
	child.sendline(password)
	child.expect(PROMPT)
	return child

def main():
	parser=optparse.OptionParser("Usage: %prog -H host -U user -P password")
	parser.add_option('-H',dest='shost',type='string',help='host name or ip')
	parser.add_option('-U',dest='suser',type='string',help='user name')
	parser.add_option('-P',dest='spass',type='string',help='password')
	(options,args)=parser.parse_args()
	host=options.shost
	user=options.suser
	password=options.spass
	if (host==None) | (user==None)| (password==None):
		print parser.usage
		exit(0)

	child=connect(user,host,password)
	send_command(child , 'cat /etc/shadow | grep root')

if __name__=='__main__':
	main()
