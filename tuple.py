#! /usr/bin/env python
list = [32,11,42]
nxlist = []
count = 1
for index, item in enumerate(list):
	nxlist.append((item, "The " + str(index+1) + " number is "))

for item in nxlist:
	print item[1] + str(item[0])

lottery_tuple = (32,43,2)
for index, lottery_number in enumerate(lottery_tuple):
	print "Lottery number {}: is {}".format(index+1, lottery_number)