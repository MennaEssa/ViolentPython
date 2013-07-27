import crypt 
 ##Old stuff
def bruteForce(pwd):
	salt=pwd[0:2]
	dictionary=open('dictionary.txt','r')
	for candidate in dictionary.readlines() :

		candidate=candidate.strip('\n')
 		crypted=crypt.crypt(candidate,salt)
		if(crypted == pwd):
			print "[+] Bingo!" + candidate 
			return
	print "[-] Nothing found .. "
	return

def main():
	passes=open('passwords.txt')
	for line in passes.readlines():
		if ":" in line :
			user=line.split(':')[0].strip(' ')
			pwd=line.split(':')[1].strip(' ')
			print "Attempting to crack user :" + user
			bruteForce(pwd)

if __name__=="__main__":
	main()
			
     
