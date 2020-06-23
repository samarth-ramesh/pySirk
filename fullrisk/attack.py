import random
class attack:
	def war(self,na,nd,mt):
		self.a=0
		self.m=0
		while ((na>=mt)):
			#print("war!")
			self.m=self.m+1
			if self.win(self.l,nd)>0:
				self.k=1
				break
			else:
				self.k=0
				self.numadie=self.numadie( na)
				self.numddie=self.numddie( nd)
				self.aroll=self.aroll( self.numadie)
				self.droll=self.droll( self.numddie)
				self.out=self.compare( self.aroll,self.droll)
				na=self.aresult( self.out,na)
				nd=self.dresult( self.out,nd)
		print("numturns= ",self.m)
		return self.k
	def numadie(self,na):
		if na>3:
			self.numadie=3
		else:
			self.numadie=na-1
		#print("numadie= ",self.numadie)
		return self.numadie
	def numddie(self,nd):
		if nd>1:
			self.numddie=2
		elif nd==1:
			self.numddie=1
		else:
			self.numddie=0
		#print("numddie= ",self.numddie)
		return self.numddie
		
	def diecreate(self,num):
		self.out=[]
		for self.x in range(num):
			self.out.append(0)
		#print("diecreated= ",self.out)
		return self.out
	
	def aroll(self,num):
		self.aroll=self.diecreate( num)
		for self.x in range(num):
			self.aroll[self.x]=random.randint(1,6)
		self.aroll.sort(reverse=True)
		#print("aroll= ",self.aroll)
		return self. aroll
	
	def droll(self,num):
		self.droll=self.diecreate( num)
		for self.x in range(num):
			self.droll[self.x]=random.randint(1,6)
		self.droll.sort(reverse=True)
		#print("droll= ",self.droll)
		return self.droll
	
	def compare(self,aroll,droll):
		self.out=[0,0]
		for self.x in range(len(droll)):
			if aroll[self.x] > droll[self.x]:
				self.out[1]=self.out[1]-1
				#print("defense lost 1")
			else:
				self.out[0]=self.out[0]-1
				#print("attack lost1")
			self.x=self.x+1
		#print("out= ", self.out)
		return self.out
	
	def aresult(self,out,na):
		na=na+out[0]
		#print("aresult= ",na)
		return na
	def dresult(self,out,nd):
		nd=nd+out[1]
		#print("dresult= ",nd)
		return nd
	def win(nd):
		if nd == 0:
			self.result=1
		else self.result=0
def main():
	na= input("na\t")
	nd=input("nd\t")
	mt=input("mt\t")
	

