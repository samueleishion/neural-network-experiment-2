from utils import * 
from settings import * 
from network import * 
from neuron import * 
from report import *

network = Network(win) 

def main(): 
	# if(GRAPH):
	# 	network.show_hits(win) 
	network.draw_neurons(win) 
	# draw_report_button() 
	while(True): 
		if(AUTOMATIC):
			for i in range(SENSORY_NEURONS): 
				neuron = network.get(i) 
				network.use(neuron.id) 
				neuron.lightup(INTENSITY) 
				network.get_hits() 
		else: 
			click = get_click() 
			was_click_perceived(network,click[0],click[1]) 
			network.get_hits() 

		if(GRAPH):
			network.show_hits(win) 

	win.close() 

	# if(REPORT): 
	# 	report = Report(network) 

main() 