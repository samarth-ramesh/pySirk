import borders
from borders import border

import random

class territories:
	numt=len(border.border)
	owner={}
	
	def owner(self,new):
		territories.owner=new
	
	def change_owner(self, sno, new):
		territories.owner[sno]=new
		print("new owner of territory with number", sno,"is",territories.owner[sno])


	
