#! /usr/bin/env python
import sys      
import os.path  

argv0, from_file, to_file = sys.argv

in_file = open(from_file)
data = in_file.read()

print "The input file is {} bytes long".format(len(data))

def quitIfNotY():
	print "Hit y to continue, others to abort."
	input = raw_input()
	if input != 'y':
		exit()

if os.path.exists(to_file):
  	print "\"{}\" exists...if this is OK,".format(to_file)
	quitIfNotY()

out_file = open(to_file, 'w')
out_file.write(data)

out_file.close()
in_file.close()