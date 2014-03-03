from utils import * 
from neuron import * 
from settings import * 
from report import * 

class Network: 
	def __init__(self,win): 
		self.network = [] 
		self.hits = {} 
		self.total = (2*SENSORY_NEURONS)+(2*TERMINAL_NEURONS)
		self.report = Report(win)

		# creating neurons 
		ntype = SENSORIAL 
		for i in range(self.total): 
			if(i==SENSORY_NEURONS):
				ntype = TRANSMITTER 
			elif(i==((2*SENSORY_NEURONS)+TERMINAL_NEURONS)): 
				ntype = TERMINAL 

			weight = 0 
			while(weight==0 or weight==1):
				weight = random.uniform(0.0,0.1) 
			neuron = Neuron(ntype,weight,i+1) 
			self.network.append(neuron) 

		# connecting neurons 
		transmitters = len(self.network)-SENSORY_NEURONS-TERMINAL_NEURONS 
		for i in range(SENSORY_NEURONS):
			for j in range(transmitters): 
				rand = random.randint(0,2) 
				if(rand==0): 
					self.network[i].add_synapse(self.network[SENSORY_NEURONS+j])
		for i in range(transmitters): 
			for j in range(transmitters+TERMINAL_NEURONS): 
				rand = random.randint(0,50) if i==j else random.randint(0,5) 
				if(rand==0): 
					self.network[SENSORY_NEURONS+i].add_synapse(self.network[SENSORY_NEURONS+j])

	def draw_neurons(self,win): 
		sensorials = SENSORY_NEURONS
		terminals = TERMINAL_NEURONS 
		report_space = 0
		if(GRAPH):
			report_space = 300
		margin = 30 
		space = win.getWidth()-report_space-margin 

		# draw sensorial neurons 
		padding = space/sensorials  
		x = margin*2 
		y = 50 
		for i in range(sensorials): 
			self.network[i].draw(win,x,y) 
			x = x+padding 

		# draw transmitter neurons 
		transmitters = sensorials+terminals 
		padding = space/transmitters 
		offset = sensorials 
		for i in range(transmitters): 
			x = random.randint(margin,space) 
			y = random.randint(100,win.getHeight()-80) 
			self.network[offset+i].draw(win,x,y) 

		# draw terminal neurons 
		padding = space/terminals 
		x = margin*2 
		y = win.getHeight()-40 
		offset = sensorials+transmitters 
		for i in range(terminals): 
			self.network[offset+i].draw(win,x,y) 
			x = x+padding 

		# draw axons 
		# print "drawing axons"
		for neuron in self.network: 
			# print "   for neuron "+str(neuron.id)+" ("+str(len(neuron.axon))+")"
			for synapse in neuron.axon: 
				x,y = neuron.get_coords() 
				p1 = Point(x,y) 
				# print "    "+str(x)+","+str(y)+" => ",
				x,y = synapse.get_coords() 
				p2 = Point(x,y) 
				# print str(x)+","+str(y)

				line = Line(p1,p2) 
				line.setFill(color_rgb(200,200,200))
				line.draw(win) 

	def size(self): 
		return len(self.network) 

	def get(self,i): 
		return self.network[i] 

	def use(self,neuronid): 
		self.using = neuronid 
		if(not (self.using in self.hits)): 
			self.hits[self.using] = {} 

	def get_hits(self): 
		offset = (2*SENSORY_NEURONS)+TERMINAL_NEURONS 
		for i in range(TERMINAL_NEURONS): 
			neuron = self.network[offset+i] 
			if(not (neuron.id in self.hits[self.using])): 
				self.hits[self.using][neuron.id] = 0 
			else: 
				self.hits[self.using][neuron.id] += neuron.hits 
				neuron.hits = 0 

			# print "Neuron "+str(self.using)+" reached terminal "+str(neuron.id)+" "+str(self.hits[self.using][neuron.id])+" times." 


			# if(neuron.id in self.hits[self.using]): 
			# 	total = self.hits[self.using][neuron.id]+neuron.hits
			# 	self.hits[self.using][neuron.id] = total 
			# else: 
			# 	self.hits[self.using][neuron.id] = 0 
			# neuron.hits = 0 

	def show_hits(self,win): 
		# for h in self.hits: 
		# 	print str(h)+", "
		self.report.draw(self.network,self.hits) 
		# for i in range(SENSORY_NEURONS): 
		# 	neuron = self.network[i]
		# 	print str(neuron.id)+" => ", 
		# 	if(neuron.id in self.hits): 
		# 		for hit in self.hits[neuron.id]:
		# 			print "   "+str(hit)+": "+str(self.hits[neuron.id][hit])
		# 	else: 
		# 		print "   x"+str(neuron.id) 
