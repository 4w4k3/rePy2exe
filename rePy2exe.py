#!/usr/bin/env python
# -.- coding: utf-8 -.-
# Coded by: Alisson Moretto - 4w4k3 - 4w4k3@protonmail.com                        
# view more: https://github.com/4w4k3/rePy2exe


import time, os, sys

def clear():
	os.system('clear')


BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

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
        BLUE).center(140) + '\n' + 'Version: {0}0.3{1}\n'.format(YELLOW, END).center(145))

def optionBanner():
    print('\nChoose option from menu:\n')
    time.sleep(0.2)
    print('\t{0}[{1}1{2}]{3} Reverse Exe -> Py').format(YELLOW, RED, YELLOW, WHITE)
    time.sleep(0.2)
    print('\t{0}[{1}2{2}]{3} Reverse Exe -> Pyc').format(YELLOW, RED, YELLOW, WHITE)
    time.sleep(0.2)
    print('\t{0}[{1}3{2}]{3} Reverse Pyc -> Py').format(YELLOW, RED, YELLOW, WHITE)
    time.sleep(0.2)
    print('\n\t{0}[{1}Q{2}]{3} Quit    {0}[{1}U{2}]{3} Update \n').format(YELLOW, RED, YELLOW, WHITE)

def exe2pyc():
    s = raw_input("Type the path of your exe: ")
    ff = str(s)
    check = os.path.isfile(ff)
    if check == True:
        os.popen('python unpy2exe.py ' + s)
        c = str(s.split('.exe')[0])
        d = '.py.pyc' 
        z = c + d
        os.popen('mv single.py.pyc ' + z)
        cwd = str(os.getcwd())
        clear()
        heading()
        print ' '
        print 'Processing the EXEcutable...'
        sys.stdout.write(YELLOW + ' [*] Working : ' + END + cwd + '/' + str(s))
        print ' '
        time.sleep(5)
        clear()
        heading()
        print ' '
        print 'Everything is OK!'
        sys.stdout.write(GREEN + ' [*] Done : ' + END + cwd + '/' + c + '.py.pyc')
        print ' ' 
        sys.exit(0)
    else:
        print ' '
        sys.stdout.write(RED + ' [!] File not found : ' + END + str(s))
        print ' '
        print ' '
        enter = raw_input("Press any key to return ")
        clear()
        heading()
        print ' '

def pyc2py():
    cwd = str(os.getcwd())
    s = raw_input("Type the path of your .pyc: ")
    ff = str(s)
    check = os.path.isfile(ff)
    if check == True:
        new = raw_input("Type a name to save your .py: ")
        clear()
        heading()
        print ' '
        sys.stdout.write(YELLOW + ' [*] Working : ' + END + str(s))
        os.popen('./pycdc/pycdc ' + s + ' >> ' + new + '.py')
        print ' '
        time.sleep(3)
        clear()
        heading()
        print ' '
        print 'Everything is OK!'
        sys.stdout.write(GREEN + ' [*] Done : ' + END + cwd + '/' + str(new) + '.py')
        print ' ' 
        sys.exit(0)
    else:
        print ' '
        sys.stdout.write(RED + ' [!] File not found : ' + END + str(s))
        print ' '
        print ' '
        enter = raw_input("Press any key to return ")
        clear()
        heading()
        print ' '

def exe2py():
    cwd = str(os.getcwd())
    s = raw_input("Type the path of your .exe: ")
    ff = str(s)
    check = os.path.isfile(ff)
    if check == True:
        clear()
        heading()
        print ' '
        os.popen('python unpy2exe.py ' + s)
        clear()
        heading()
        print ' '
        new = raw_input("Type a name to save your .py: ")
        os.popen('./pycdc/pycdc ' + 'single.py.pyc' + ' >> ' + new + '.py')
        clear()
        heading()
        print ' '
        sys.stdout.write(YELLOW + ' [*] Working : ' + END + str(s))
        print ' '
        time.sleep(3)
        clear()
        heading()
        print ' '
        print 'Everything is OK!'
        sys.stdout.write(GREEN + ' [*] Done : ' + END + cwd + '/' + str(new) + '.py')
        os.popen('rm -Rf single.py.pyc')
        print ' '
        sys.exit(0)
    else:
        print ' '
        sys.stdout.write(RED + ' [!] File not found : ' + END + str(s))
        print ' '
        print ' '
        enter = raw_input("Press any key to return ")
        clear()
        heading()
        print ' '
        
def updater():
    os.system('python2.7 updater.py')

def pp():
    print """
            ....
         ,''. :   __
             \|_.'  `:       _.----._//_
            .'  .'.`'-._   .'  _/ -._ \)-.----O
           '._.'.'      '--''-'._   '--..--'-`
            .'.'___    /`'---'. / ,-'`
  *       _<__.-._))../ /'----'/.'_____:'.
   \_    :            \ ]              :  '.
     \___:   SEE YOU   \\   LATER !     :    '.
         :              \\__            :    .'
         :_______________|__]__________:  .'
                    .' __ '.           :.'
                  .' .'  '. '.
                .' .'      '. '.      #rePy2exe
              .' .'          '. '.
           _.' .'______________'. '._
          [_0______________________0_]
"""


def main():

    clear()

    path = 'pycdc'

    if os.path.isdir(path):
        pass

    else:
	heading()
	print ' '
        sys.stdout.write(YELLOW + ' [*] NotFound : ' + END + 'pycdc')
	print ' '
	choice = raw_input('Dependencies not found, want clone it? (y/n)')
	if choice == 'y':
		clear()
		print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
		print ' [*] Searching Cmake...'
		print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
		print '                              '
		abc = os.system('which cmake')
		if abc == 256:
			clear()
			heading()
			print ' '
			sys.stdout.write(YELLOW + ' [*] Searching Cmake : ' + END + RED + 'Not Found' + END)
			print ' '
			print ' '
			print '   Please install it :     https://cmake.org      '
			sys.exit(0)
		else:
			print "OK"
		print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
		print ' [*] Cloning Dependencies...'
		print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
		print '                              '
        	os.popen('git clone https://github.com/4w4k3/pycdc.git')
		clear()
		print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
		print ' [*] Compiling Dependencies...'
		print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
		print '                              '
		os.system('cd pycdc && cmake ../pycdc/ && make')
	elif choice == 'Y':
		print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
		print ' [*] Searching Cmake...'
		print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
		print '                              '
		abc = os.system('which cmake')
		if abc == 256:
			clear()
			heading()
			print ' '
			sys.stdout.write(YELLOW + ' [*] Searching Cmake : ' + END + RED + 'Not Found' + END)
			print ' '
			print ' '
			print '   Please install it :     https://cmake.org      '
			sys.exit(0)
		else:
			print "OK"
		print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
		print ' [*] Cloning Dependencies...'
		print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
		print '                              '
        	os.popen('git clone https://github.com/4w4k3/pycdc.git')
		clear()
		print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
		print ' [*] Compiling Dependencies...'
		print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
		print '                              '
		os.system('cd pycdc && cmake ../pycdc/ && make')
	else:
		sys.exit(0)

    clear()

    heading()

    try:

        while True:

            optionBanner()

            header = ('{0}rePy2exe{1}> {2}'.format(BLUE, WHITE, END))
            choice = raw_input(header)

            if choice.upper() == 'Q' or choice.upper() == 'EXIT':
		clear()
		pp()

		print('\t{0} And that\'s all, folks. xD').format(YELLOW, RED, YELLOW, WHITE)
		print '**************************************************'
                raise SystemExit
            elif choice == '1':
                exe2py()
            elif choice == '2':
                exe2pyc()
            elif choice == '3':
                pyc2py()	
	    elif choice.upper() == 'UPDATE':
		updater()
	    elif choice.upper() == 'U':
		updater()		
            else:
	 	clear()
		print 'Invalid Option'
		time.sleep(1)
		clear()
		heading()
		print ' '

    except KeyboardInterrupt:
	clear()
	pp()

	print('\t{0} And that\'s all, folks. xD').format(YELLOW, RED, YELLOW, WHITE)
	print '**************************************************'

if __name__ == '__main__':

    main()
