#! /usr/bin/env python
import product as p

def listOptions():
	print '\n' + 'Please Choose: '
	for key in keys:
		print str(key) + ': ' + options[key][0] 
	try:
		nextCmd()
	except Exception as err:
		print str(err)

options = {1:['Create Product', p.createProduct], 2:['List Products', p.list], 3: ['List Options', listOptions], 4:['Exit', exit]}
keys = options.keys()


def nextCmd():
	input = p.readInt()
	options[input][1]()
	print 'Next command?'
	nextCmd()

listOptions()