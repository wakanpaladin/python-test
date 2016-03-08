import json
import sys      
import os.path 

filename = 'products.txt'

class Product(object):
	pass

def readInt():
	try:
		return int(raw_input())
	except:
		print 'Please enter an integer'
		return readInt()

def createProduct():
	p = {}
	print 'Enter product name'
	p['name'] = raw_input()
	print 'Enter price'

	p['price'] = readInt()

	pstr = json.dumps(p)
	_writeToFile(pstr + '\n')

	print 'product created'


def list():
	#another way is file.readlines()
	with open(filename, 'r') as file:
		for l in file:
			p = json.loads(l)
			print 'Name: ' + p['name'] + ' Price:' + str(p['price'])
	print	

def _writeToFile(str):
	with open(filename, 'a') as file: 
		file.write(str)

