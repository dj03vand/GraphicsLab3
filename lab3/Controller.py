# File: Controller.py

import viz
from Ball import *

# Controller class inherits event handling methods from viz.EventClass
class Controller(viz.EventClass):
	
	def __init__(self):
		
		# must call constructor of EventClass first!!
		viz.EventClass.__init__(self)
		self.ball = Ball()
		
		self.ballList = []
		self.ballList.append(self.ball)
		
		self.callback(viz.KEYDOWN_EVENT, self.onKeyPress)
		self.callback(viz.TIMER_EVENT, self.onTimer)
		
		self.starttimer(1, 0.04, viz.FOREVER)
	
	def onTimer(self,num):
		for i in self.ballList:
			x = i.getX()
			y = i.getY()
			x = i.getVX() + x
			y = i.getVY() + y
			if(x + 10  > 100 or x - 10 < -100):
				# set the vector to bounce off walls
				i.setVXVY(i.getVX() * -1, i.getVY())
				x = i.getVX() + x
				viz.playSound('cartoon053.wav')
			if(y + 10 > 100 or y - 10 < -100):
				i.setVXVY(i.getVX(), i.getVY() * -1)
				y = i.getVY() + y
				viz.playSound('cartoon053.wav')
			i.setXY(x, y)
			print("X is " + str(x) + " and Y is " + str(y))
	
	def onKeyPress(self,key):
		if(key == " "):
			self.ball = Ball()
			self.ballList.append(self.ball)
			
		elif(key == viz.KEY_DOWN):
			for i in self.ballList:
				y = i.getVY()*.95
				x = i.getVX()*.95
				i.setVXVY(x, y)
				
		elif(key == viz.KEY_UP):
			for i in self.ballList:
				y = i.getVY()*1.05
				x = i.getVX()*1.05
				i.setVXVY(x, y)
