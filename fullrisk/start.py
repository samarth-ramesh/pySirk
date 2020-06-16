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
				#owner[self.deck[(nump*x)+y]]=y
				pass
		if (territories.numt%nump !=0):
			for x in range(territories.numt%nump):
				#owner[self.deck[(territories.numt-x)]]=random.randint(0,nump-1)
				pass
		print(len(self.deck))
		

def main():
	a=creatg()
	creatg.dealowner(a,4)
main()
