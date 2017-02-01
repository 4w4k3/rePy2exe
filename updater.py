#!/usr/bin/env python
# -.- coding: utf-8 -.-
# Coded by: Alisson Moretto - 4w4k3 - 4w4k3@protonmail.com                        
# view more: https://github.com/4w4k3/rePy2exe

import sys
import urllib2
import os
import time

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'


def clear():
    os.system('clear')

def heading():
    sys.stdout.write(GREEN + """
 _  .-')    ('-.     _ (`-.                      ('-.  ) (`-.        ('-.   
( \( -O ) _(  OO)   ( (OO  )                   _(  OO)  ( OO ).    _(  OO)  
 ,------.(,------. _.`     \ ,--.   ,--.-----.(,------.(_/.  \_)-.(,------. 
 |   /`. '|  .---'(__...--''  \  `.'  / ,-.   \|  .---' \  `.'  /  |  .---' 
 |  /  | ||  |     |  /  | |.-')     /'-'  |  ||  |      \     /\  |  |     
 |  |_.' (|  '--.  |  |_.' (OO  \   /    .'  /(|  '--.    \   \ | (|  '--.  
 |  .  '.'|  .--'  |  .___.'|   /  /\_ .'  /__ |  .--'   .'    \_) |  .--'  
 |  |\  \ |  `---. |  |     `-./  /.__)       ||  `---. /  .'.  \  |  `---. 
 `--' '--'`------' `--'       `--'    `-------'`------''--'   '--' `------'  """ + END + BLUE +
    '\n' + '{1}R{0}everse {1}E{0}ngineering {1}Py2Exe{2}{3}'.format(YELLOW, RED, YELLOW, BLUE).center(90) +
    '\n' + 'by: {0}Alisson Moretto ({1}4w4k3{2})'.format(
        YELLOW, RED, YELLOW, BLUE).center(140) + 
    '\n' + '{0}4w4k3@protonmail.com'.format(
        BLUE).center(140) + END)

def down():
    clear()
    heading()
    print ' '
    sys.stdout.write(' [*] Checking Updates : ' + YELLOW + ' Update Found' + END)
    print ' '
    print ' '


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
	
	response = urllib2.urlopen('https://raw.githubusercontent.com/4w4k3/rePy2exe/master/version.txt')
	data = response.read()
	fileup = open("version.txt", 'w')
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
	version.close()
	updatechk.close()
	if xd2 != xd:
    	    down()
       	    os.popen('rm -Rf version2.txt')
	    choice = raw_input('You want update it ? (y/n) ')
	    if choice == 'Y':
	   	    os.popen('rm -Rf rePy2exe.py')
    	   	    os.popen('rm -Rf unpy2exe.py')
       	    	    os.popen('rm -Rf version.txt')
		    master()
                    clear()
                    heading()
                    print ' '
                    sys.stdout.write(GREEN + ' [*] Updated Version to : ' + END + str(xd2))
   		    time.sleep(2)
                    print ' '
                    raw_input('Press any key to return. ')
		    os.system('python2.7 rePy2exe.py')
	    elif choice == 'y':
	   	    os.popen('rm -Rf rePy2exe.py')
    	   	    os.popen('rm -Rf unpy2exe.py')
       	    	    os.popen('rm -Rf version.txt')
		    master()
                    clear()
                    heading()
                    print ' '
                    sys.stdout.write(GREEN + ' [*] Updated Version to : ' + END + str(xd2))
   		    time.sleep(2)
                    print ' '
                    raw_input('Press any key to return. ')
		    os.system('python2.7 rePy2exe.py')
		    
	    else:
		print "Ok"
		os.system('python2.7 rePy2exe.py')
	else:
            sys.stdout.write(GREEN + ' [*] You have latest Version : ' + END + str(xd2))
            print ' '
	    os.popen('rm -Rf version2.txt')
            raw_input('Press any key to return: ')
	    os.system('python2.7 rePy2exe.py')
two()
