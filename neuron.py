class Neuron: 
	def __init__(self,x1,x2,w1,w2): 
		self.th = 0.5 # threshold 
		self.lr = 0.2 # learning rate 
		self.x1 = x1 # sensor values 
		self.x2 = x2 
		self.z = 1 if bool(x1 or x2) else 0 # desired output 
		self.w1 = w1 # weights 
		self.w2 = w2 
		self.c1 = self.x1*self.w1 # calculated 
		self.c2 = self.x2*self.w2 
		self.s = self.c1+self.c2 # sum 
		self.n = 1 if self.s>self.th else 0 # network 
		self.e = self.z-self.n # error 
		self.r = self.lr*self.e #correction 
		# self.w1 = self.r+self.w1 # final weights 
		# self.w2 = self.r+self.w2 

	def show(self): 
		print str(self.th)+"\t"+str(self.lr)+"\t"+str(self.x1)+"\t"+str(self.x2)+"\t"+str(self.z)+"\t"+str(self.w1)+"\t"+str(self.w2)+"\t"+str(self.c1)+"\t"+str(self.c2)+"\t"+str(self.s)+"\t"+str(self.n)+"\t"+str(self.e)+"\t"+str(self.r)+"\t"+str(self.r+self.w1)+"\t"+str(self.r+self.w2)  


def flip(n): 
	return 1 if n==0 else 0 

def main(): 
	print "TH\tLR\tX1\tX2\tZ\tW1\tW2\tC1\tC2\tS\t N\t E\t R\tW1\tW2" 

	x1mult = 0 
	x2mult = 0 
	wmult = 0 

	x1 = 1

	for i in range(12): 
		x1 = flip(x1) if (x1mult%4==0 or x1mult%4==2) else x1 
		x2 = 0 if x2mult%2==0 else 1 
		if(wmult<2): 
			w1 = 0.1 
		elif(wmult<3): 
			w1 = 0.3 
		elif(wmult<7): 
			w1 = 0.5 
		else: 
			w1 = 0.7 
		w2 = w1+0.2 

		n = Neuron(x1,x2,w1,w2) 
		n.show() 

		x1mult+=1 
		x2mult+=1 
		wmult+=1 

main() 
