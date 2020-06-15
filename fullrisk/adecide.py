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
		
		if self.x==1:
			self.t==attack()
			self.result=attack.war(self.t,na,nd)
		else:
			pass
		return self.x

