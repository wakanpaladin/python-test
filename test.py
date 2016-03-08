#! /usr/bin/env python
class Car(object):
	brand = 'Unknown'
	def __init__(self):
		self.started = False
	def start(self):
		self.started = True	
		print 'Car started'
	def isStarted(self):
		print "Car started: " + str(self.started)
		return self.started	

class Lexus(Car):
	brand = 'Lexus'
	def start(self):
		if Car.isStarted(self):
			print 'Already started'
		else:
			print 'Lexus started'
			Car.start(self)

c = Lexus()
c.start()
c.start()

c1 = Lexus()
c1.start()

#c.isStarted()