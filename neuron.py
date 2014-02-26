# Neural Network Model: 
# 	http://en.wikipedia.org/wiki/Artificial_neuron#Spreadsheet_example 

from utils import * 
from graphics import * 
from time import sleep 
import random 

class Neuron: 
	def __init__(self,ntype,weight,idnum): 
		self.type = ntype
		self.id = idnum
		self.th = 0.5 # threshold 
		self.lr = 0.2 # learning rate 
		self.weight = weight # weight value 
		self.axon = [] # connection to other neurons 
		self.sub = 0 # subtotal value of sensor and weight 
		self.x = 0 
		self.y = 0 

	def lightup(self,sensor): 
		if(self.is_terminal() or sensor>0):
			gb = 0 
			self.body.setFill(self.get_color(gb)) 
			self.send(sensor) 
			while(gb<=255): 
				self.body.setFill(self.get_color(gb)) 
				sleep(0.03) 
				gb += 51 

	def send(self,sensor): 
		expected = 1 if bool(sensor) else 0 # desired output 
		self.sub += sensor*self.weight # accumulated value 

		# determine whether there's value to send 
		# print str(self.sub)+">"+str(self.th) 
		while(self.sub>self.th): 
			out = 1 
			self.sub -= self.th # correct weight value based on error margin 
			error = expected-out 
			correction = self.lr*error 
			self.weight += correction 

			# print str(self.id)+"->"+str(out) 
			for synapse in self.axon: 
				synapse.lightup(out) 

	def add_synapse(self,neuron): 
		self.axon.append(neuron) 

	def draw(self,win,x,y): 
		self.x = x 
		self.y = y 
		point = Point(x,y) 
		self.body = Circle(point,20) 

		self.body.draw(win) 

		if(self.id>0): 
			text = Text(point,str(self.id))
			text.draw(win) 

	def get_coords(self):
		return self.x,self.y

	def is_sensorial(self): 
		return self.type==SENSORIAL 

	def is_transmitter(self): 
		return self.type==TRANSMITTER 

	def is_terminal(self): 
		return self.type==TERMINAL 

	def is_motor(self): 
		return self.type==MOTOR 

	def get_color(self,gb): 
		if(self.is_sensorial()): 
			return color_rgb(255,gb,gb) 
		elif(self.is_terminal()): 
			return color_rgb(gb,gb,255) 
		elif(self.is_transmitter()): 
			return color_rgb(255,255,gb) 
		else: 
			return color_rgb(gb,255,gb) 

	def __str__(self): 
		out = "N#"+str(self.id)+"\n" 

		for synapse in self.axon: 
			out += "\t"+str(synapse.id)+"\n"  

		return out 

