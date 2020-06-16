import borders
from borders import border

import random

class territories:
	numt=len(border.border)
	owner={}
	
	def deckmake(self,numter):
		self.deck=[]
		for self.x in range(numter):	
			self.deck.append(self.x+1)
		return self.deck
		
	def dealowner(self,nump):
		a=territories()
		self.deck=territories.deckmake(a,territories.numt)
		random.shuffle(self.deck)
		print(self.deck)
	def change_owner(self, sno, new):
		pass

def main():
	a=territories()
	territories.dealowner(a,4)
	
main()
