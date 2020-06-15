class adecide:
	def  decide(self,na,nd):
		if nd>15:
			self.x=0
		elif nd<10 and na>15:
			self.x=1
		elif na>6 and na>(2*nd):
			self.x=0
		else:
			self.x=0
		
		return self.x
	
	def win(self,nd):
		if nd>0:
			self.victory=0
		else:
			self.victory=1
		return self.victory
	
	def  cont(self,na,nd):
		self.t=adecide()
		if ((na-nd>5) or (nd<2 and na>4)or(adecide.decide(self.t,na,nd))):
			self.x=0
		else:
			self.x=1
		return self.x
