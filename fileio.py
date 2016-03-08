#! /usr/bin/env python
import sys      
import os.path  
import tempfile

argv0, from_file, to_file = sys.argv

def quitIfNotY():
	print "Hit y to continue, others to abort."
	input = raw_input()
	if input != 'y':
		print 'Exiting...'
		exit()

if os.path.exists(to_file):
  	print "\"{}\" exists...if this is OK,".format(to_file)
	quitIfNotY()
	f = tempfile.NamedTemporaryFile(mode='w+b', delete=False)
	to_file = f.name.replace(r'/','') + '.py'
	f.close()

in_file = open(from_file)
data = in_file.read()

print "The input file is {} bytes long".format(len(data))	

out_file = open(to_file, 'w')
out_file.write(data)
print 'to file name: ' + to_file

out_file.close()
in_file.close()