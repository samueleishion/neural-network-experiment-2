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
	# if(x<=45 and y<=20 and REPORT):
	for i in range(network.size()): 
		item = network.get(i)
		nr = item.body.getRadius() 
		nx, ny = item.get_coords() 

		if(( nx-nr <= x <= nx+nr ) and ( ny-nr <= y <= ny+nr )): 
			if(item.is_sensorial()): 
				# print str(item.id)+" \t"+str(item.type)
				network.use(item.id) 
				item.lightup(INTENSITY) 
				network.get_hits() 
				return True 

	return False 

def draw_report_button(): 
	point = Point(24,12) 
	text = Text(point,"Report") 
	text.draw(win) 
	point = Point(45,20) 
	point.draw(win) 
