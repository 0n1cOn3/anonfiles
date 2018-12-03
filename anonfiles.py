import sys
import os
import urllib2
import base64

def upload():
	ifile=raw_input( 'Enter the file path to upload: ')
	exists = os.path.isfile(ifile)
	if not exists:
	        print "The File "+ifile+" Doesn't exists !!!"
	        print "Try Again !!!"
	        print "Press Enter To Continue..."
	        raw_input()
	        return
	k=os.popen('curl -F \'file=@'+ifile+'\' https://0x0.st')
	a=k.read()
	k.close()
	print a
	print 'Your Secret Code To download file is: '+enc(a[15:len(a)])
	return
def miniup(String ifile):
	exists = os.path.isfile(ifile)
	if not exists:
	        print "The File "+ifile+" Doesn't exists !!!"
	        return
	k=os.popen('curl -F \'file=@'+ifile+'\' https://0x0.st')
	a=k.read()
	k.close()
	print 'Your Secret Code To download file is: '+enc(a[15:len(a)])
	return
def minidown(String key):
	try:
		url='https://0x0.st/'+dec(key.strip())
		if urllib2.urlopen(url).code == 200:
			print 'File Found !!!'
			fi=dec(key.strip())
			os.system('curl '+url+' -o '+fi)
			print '\n\nFile Saved With Name: '+fi
		else:
			print 'File Not Found !!'
			print 'Remember files Last only for 30 days in free version'
	except:
		print 'Some error occured!!\nPlease check your key\nFile was not found!!\nRemember files Last only for 30 days in free version'
def download():
	key=raw_input('Enter the Key To Download the file : ')
	try:
		url='https://0x0.st/'+dec(key.strip())
		if urllib2.urlopen(url).code == 200:
			print 'File Found !!!'
			fn=raw_input('Enter File Name ( With Extension) to save: ')
			os.system('curl '+url+' -o '+fn)
		else:
			print 'File Not Found !!'
			print 'Remember files Last only for 30 days in free version'
	except:
		print 'Some error occured!!\nPlease check your key\nFile was not found!!\nRemember files Last only for 30 days in free version'
def enc(String s):
	key=b64.encode(s)
	return key
def dec(String s):
	key=b64.encode(s)
	if key.find('.')==-1:
		key+='.txt'
	return key

if not (len(sys.argv)==3 or len(sys.argv)==1):
	print 'Invalid Parameters'
	print 'Check Help Section'
	exit()
if len(sys.argv)==3:
	t=sys.argv[1]
	p=sys.argv[2]
	if t.find('-u')!=-1:
		miniup(p)
	elif t.find('-d')!=-1:
		minidown(p)
	else:
		print 'Invalid Parameters\nSee Help'
	exit()
while True:
	os.system('figlet -f ascii12 AnonFiles')
	print '\nThis Service is owned by SpeedX Production!!!\nIts Under Beta Mode!!!\n\n  1 -  Upload File'
	print '  2 - Download File'
	print '  3 - Help'
	print '  4 - Exit'
	ip=raw_input('->')
	ip=ip.strip()
	if ip=='1':
		upload()
	elif ip=='2':
		download()
	elif ip=='3':
		print 'This Service Was Created By SpeedX !!'
		print 'Type python2 anonfiles.py -u <file> to upload files'
		print 'Type python2 anonfiles.py -u <key> to download files'
	elif ip=='4':
		print 'Thanks For Using SpeedX Programs!!'
		break
	else:
		print 'Invalid Input !!\nTry Again!!\nPress Enter To Continue...'
		raw_input()

