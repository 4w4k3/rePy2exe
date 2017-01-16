import urllib2
import os
import time

def down():
    os.system('clear')
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    print ' [*] Checking Updates...'
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    print '                              '
    print "Update Found"


def master():
	response = urllib2.urlopen('https://raw.githubusercontent.com/4w4k3/rePy2exe/master/rePy2exe.py')
	data = response.read()
	fileup = open("rePy2exe.py", 'w')
	fileup.write(data)
	fileup.close()

	response = urllib2.urlopen('https://raw.githubusercontent.com/4w4k3/rePy2exe/master/unpy2exe.py')
	data = response.read()
	fileup = open("unpy2exe.py", 'w')
	fileup.write(data)
	fileup.close()

def one():
	response = urllib2.urlopen('https://raw.githubusercontent.com/4w4k3/rePy2exe/master/version.txt')
	data = response.read()
	fileup = open("version2.txt", 'w')
	fileup.write(data)
	fileup.close()
one()

def two():
	updatechk = open('version2.txt', 'r')
	xd2 = updatechk.read()
	print updatechk.read()
	version = open('version.txt', 'r')
	xd = version.read()
	if xd2 != xd:
    	    down()
       	    os.popen('rm -Rf version2.txt')
	    choice = raw_input('You want update it ? (y/n) ')
	    if choice == 'Y':
	   	    os.popen('rm -Rf rePy2exe.py')
    	   	    os.popen('rm -Rf unpy2exe.py')
		    master()
	            print "UPDATED"
   		    time.sleep(2)
		    os.system('python2.7 rePy2exe')
	    elif choice == 'y':
	   	    os.popen('rm -Rf rePy2exe.py')
    	   	    os.popen('rm -Rf unpy2exe.py')
		    master()
    	            print "UPDATED"
		    time.sleep(2)
   		    os.system('python2.7 rePy2exe.py')
	    else:
		print "Ok"
		os.system('python2.7 rePy2exe.py')
	else:
	    print "Already Updated"
	    os.popen('rm -Rf version2.txt')
	    time.sleep(2)
	    os.system('python2.7 rePy2exe')
two()
