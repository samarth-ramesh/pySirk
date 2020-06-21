import borders
from borders import border

import random

class territories:
	def  __init__(self):
		self.numt=len(border.border)
		owner={}
		troops={}
	
	def getTerritories(self):
		return self.numt
	
	def owner(self,new):
		territories.owner=new
	
	def change_owner(self, sno, new):
		territories.owner[sno]=new
		print("new owner of territory with number", sno,"is",territories.owner[sno])

    def setTroops(self,sno,num):
        troops[sno]=num
        

