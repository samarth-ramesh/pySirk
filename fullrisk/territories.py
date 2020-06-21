import borders
from borders import test

import random

class territories:
	def  __init__(self):
		self.numt=len(test.border)
	owner={}
	troops={}
	
	def getTerritories(self):
		return self.numt
	
	def initOwner(self,new):
		territories.owner=new
	
	def change_owner(self, sno, new):
		territories.owner[sno]=new
		print("new owner of territory with number", sno,"is",territories.owner[sno])

	def setTroops(self,sno,num):
		self.troops[sno]=num
        

