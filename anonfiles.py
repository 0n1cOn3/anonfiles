import sys
import os
import urllib2

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
	print 'Your Secret Code To download file is: '+a[15:len(a)]
	return

def download():
	key=raw_input('Enter the Key To Download the file : ')
	
	url='https://0x0.st/'+key.strip()
	if urllib2.urlopen(url).code == 200:
		print 'File Found !!!'
		fn=raw_input('Enter File Name ( With Extension) to save: ')
		os.system('curl '+url+' -o '+fn)
	else:
		print 'File Not Found !!'
		print 'Remember files Last only for 30 days in free version'

while True:
	os.system('figlet -f ascii12 AnonFiles')
	print '\n\n\nPress 1 to upload file'
	print 'Press 2 to download file'
	print 'Press 3 to exit'
	ip=raw_input('->')
	ip=ip.strip()
	if ip=='1':
		upload()
	elif ip=='2':
		download()
	elif ip=='3':
		print 'Thanks For Using SpeedX Programs'
		break
	else:
		print 'Invalid Input !!\nTry Again!!\nPress Enter To Continue...'
		raw_input()

