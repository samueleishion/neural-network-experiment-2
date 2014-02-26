from settings import * 
from graphics import * 

SENSORIAL 	= 0 
TRANSMITTER = 1 
TERMINAL 	= 2 
MOTOR 		= 3 

win = GraphWin("Neural Network Graph",WINDOW_X,WINDOW_Y) 

def flip(n): 
	return 1 if n==0 else 0 

def get_click(): 
	click = win.getMouse() 
	x = click.getX() 
	y = click.getY() 
	Point(x,y).draw(win) 
	return x,y 

def was_click_perceived(network,x,y): 
	for i in range(network.size()): 
		item = network.get(i)
		nr = item.body.getRadius() 
		nx, ny = item.get_coords() 

		if(( nx-nr <= x <= nx+nr ) and ( ny-nr <= y <= ny+nr )): 
			if(item.is_sensorial()): 
				# print str(item.id)+" \t"+str(item.type)
				item.lightup(INTENSITY) 
				return True 

	return False 
