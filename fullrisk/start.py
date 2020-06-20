import borders
from borders import border

import territories
from territories import territories

import random


class GameCreate:
	
	def getTerritories(self):
		getTerritoryNum=territories()
		self.numt=getTerritoryNum.getTerritories()
		return self.numt
	
	def makeDeck(self):
		self.deck=[]
		self.y=0
		for self.x in range(self.getTerritories()):
			self.deck.append(self.x)
		return self.deck
	
	def shuffleDeck(self,deck):
		random.shuffle(deck)
		return deck
		
	def giveTerritory(self,nump):
		deck=self.makeDeck()
		self.owner={}
		shuffledDeck=self.shuffleDeck(deck)
		for self.x in range(1,self.getTerritories()+1):
			self.owner[shuffledDeck[self.x-1]+1]=(self.x%nump)+1
			print(self.numtpp)
		return self.owner
				


