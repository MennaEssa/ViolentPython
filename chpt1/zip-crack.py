import zipfile
import optparse
from threading import Thread

def extract(zFile, password):
	try:
		zip_file.extractall(pwd=password)
		password = 'Password found: %s' % password
	except:
		pass


def main():
	"""
	Dictionary attack.
	"""
	parser=optparse.OptionParser("usage %prog -f <zipfile> -d <dictionary>")
	parser.add_option('-f' , dest='zfile' , type = 'string' , help = 'zip file name')
	parser.add_option('-d' , dest='dfile' , type = 'string' , help = 'dictionary file name')
	(options , args ) = parser.parse_args()
	if (options.zfile == None) | (options.dfile == None):
		print parser.usage
		exit(0)
	zipfilename = options.zfile
	dictionary = options.dfile
	password = None
	zip_file = zipfile.ZipFile(zipfilename)
	f=open(dictionary, 'r')
	for line in f.readlines():
	 	password = line.strip('\n')
   		t=Thread(target=extract , args=(zip_file,password))
		t.start()

	print password

if __name__ == '__main__':
	main()
