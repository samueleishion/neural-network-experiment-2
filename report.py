from settings import * 
from graphics import * 
from network import * 
from neuron import * 

class Report: 
	def __init__(self,win): 
		self.data = {}  
		self.totals = {} 
		self.drawn = False 
		self.win = win
		self.build_data()

	def build_data(self): 
		# draw gray background 
		w = WINDOW_X 
		h = WINDOW_Y 
		x = WINDOW_X-300 
		y = 0

		r = Rectangle(Point(x,y),Point(w,h))  
		gray = color_rgb(220,220,220)
		r.setFill(gray) 
		r.setOutline(gray)
		r.draw(win) 

		# draw graph 
		rows = SENSORY_NEURONS 
		cols = TERMINAL_NEURONS 
		gap = (SENSORY_NEURONS*2)+TERMINAL_NEURONS

		x = WINDOW_X-300 
		y = (WINDOW_Y/2)-150
		interval_x = 300/TERMINAL_NEURONS 
		interval_y = 300/SENSORY_NEURONS 
		ix = 0 
		iy = 0 

		for r in range(rows):
			self.data[r+1] = {}
			for c in range(cols): 
				p1 = Point(x+(interval_x*ix),y+(interval_y*iy)) 
				p2 = Point(p1.getX()+interval_x,p1.getY()+interval_y)
				rect = Rectangle(p1,p2)
				self.data[r+1][gap+c+1] = rect 
				self.data[r+1][gap+c+1].setFill(color_rgb(255,255,255)) 
				self.data[r+1][gap+c+1].draw(self.win) 
				ix += 1
			iy += 1
			ix = 0

	def draw(self,network,hits): 
		# counting totals
		for i in range(SENSORY_NEURONS):
			neuron = network[i] 

			if(not (neuron.id in self.totals)):
				self.totals[neuron.id] = 0 

			sub = 0 
			if(neuron.id in hits):
				for hit in hits[neuron.id]: 
					sub += hits[neuron.id][hit]
			self.totals[neuron.id] = sub

		# calculating weights 
		gap = (SENSORY_NEURONS*2)+TERMINAL_NEURONS
		for r in range(len(self.data)):
			for c in range(len(self.data[r+1])):
				weight = 0
				if(self.totals[r+1]>0):
					weight = (1.0*hits[r+1][gap+c+1])/self.totals[r+1] 
				color = self.get_color(weight) 
				self.data[r+1][gap+c+1].setFill(color) 

	def get_color(self,weight):
		gb = int(round(255-(255*weight))) 
		return color_rgb(255,gb,gb)
