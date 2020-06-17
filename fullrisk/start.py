import borders
from borders import border

import territories
from territories import territories

import random

class creatg:
	
	def deckmake(self,numter):
		self.deck=[]
		for self.x in range(numter):	
			self.deck.append(self.x+1)
		return self.deck
		
	def dealowner(self,nump):
		a=creatg()
		owner={}
		self.deck=creatg.deckmake(a,territories.numt)
		random.shuffle(self.deck)
		self.rng=territories.numt//nump
		for x in range(1,((1+self.rng))):
			for y in range(nump):
                            if ((nump*x)+y>territories.numt):
                                pass
                            else:
                                owner[self.deck[((nump*x)-1)+y]]=y
				
		if (territories.numt%nump !=0):
			for x in range(territories.numt%nump):
				owner[self.deck[(territories.numt)-1]]=random.randint(0,nump-1)
			
		print(owner)
		

def main():
	a=creatg()
	creatg.dealowner(a,4)
main()
