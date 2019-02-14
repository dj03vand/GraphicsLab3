# File: Ball.py
# Logan Brandt, Daniel Van Dyke

import viz
import math
import random

# Ball class inherits event handling methods from viz.EventClass
class Ball:

	# Constructor 
	def __init__(self):
		
		# Initialize Ball Instance Variables
		# radius 
		self.radius = 10
		# number of sides of regular polygon representing the ball
		self.sides = 20
		# velocity vector describing its direction and speed
		
		randomVal = random.random()*360
		
		self.vx = 2*math.cos(randomVal)
		self.vy = 2*math.sin(randomVal)
		
		# center location 
		self.x = 0
		self.y = 0
		
		# create layer for a circle, centered at (0,0)
		viz.startLayer(viz.POLYGON)
		viz.vertexColor(1,1,0)
		for i in range(0, 360, self.sides):
			x = math.cos( math.radians(i) ) * self.radius
			y = math.sin( math.radians(i) ) * self.radius
			viz.vertex(x, y)
		# saves layer of vertices in instance variable called vertices
		self.vertices = viz.endLayer()
		
	def getX(self):
		return self.x
		
	def getY(self):
		return self.y
		
	def getVX(self):
		return self.vx
		
	def getVY(self):
		return self.vy
		
	def setXY(self,x,y):
		self.x = x
		self.y = y
		mat = viz.Matrix()
		mat.postTrans(self.x, self.y)
		self.vertices.setMatrix(mat)
		
	def setVXVY(self,vx,vy):
		self.vx = vx
		self.vy = vy
		
		
	