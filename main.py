from utils import * 
from settings import * 
from network import * 
from neuron import * 

network = Network() 

def main(): 
	network.draw_neurons(win) 
	while(True): 
		if(AUTOMATIC):
			for i in range(SENSORY_NEURONS): 
				network.get(i+1).lightup(INTENSITY)
		else: 
			click = get_click() 
			was_click_perceived(network,click[0],click[1]) 

	win.close() 

main() 