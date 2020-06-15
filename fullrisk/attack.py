import random
import adecide
from adecide import adecide
class attack:
	def start(self,na,nd):
		self.x=0
		self.l=adecide()
		self.m=attack()
		if adecide.decide(self.l,na,nd)==1:
			self.x=adecide.war(self.m,na,nd)
		else:
			pass
		return self.x
		
	def war(self,na,nd):
		self.a=0
		self.m=0
		while ((self.a==0)):
			self.t=attack()
			#print("war!")
			self.m=self.m+1
			if attack.win(self.t,nd)>0:
				self.k=1
				break
			else:
				self.k=0
				self.numadie=attack.numadie(self.t,na)
				self.numddie=attack.numddie(self.t,nd)
				self.aroll=attack.aroll(self.t,self.numadie)
				self.droll=attack.droll(self.t,self.numddie)
				self.out=attack.compare(self.t,self.aroll,self.droll)
				na=attack.aresult(self.t,self.out,na)
				nd=attack.dresult(self.t,self.out,nd)
				self.a=attack.cont(self.t,na,nd)
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
		self.j=attack()
		self.aroll=attack.diecreate(self.j,num)
		for self.x in range(num):
			self.aroll[self.x]=random.randint(1,6)
		self.aroll.sort(reverse=True)
		print("aroll= ",self.aroll)
		return self. aroll
	
	def droll(self,num):
		self.j=attack()
		self.droll=attack.diecreate(self.j,num)
		for self.x in range(num):
			self.droll[self.x]=random.randint(1,6)
		self.droll.sort(reverse=True)
		print("droll= ",self.droll)
		return self.droll
	
	def compare(self,aroll,droll):
		self.out=[0,0]
		for self.x in range(len(droll)):
			if aroll[self.x] > droll[self.x]:
				self.out[1]=self.out[1]-1
				print("defense lost 1")
			else:
				self.out[0]=self.out[0]-1
				print("attack lost1")
			self.x=self.x+1
		print("out= ", self.out)
		return self.out
	
	def aresult(self,out,na):
		na=na+out[0]
		print("aresult= ",na)
		return na
	def dresult(self,out,nd):
		nd=nd+out[1]
		print("dresult= ",nd)
		return nd
	
	def win(self,nd):
		if nd>0:
			self.victory=0
		else:
			self.victory=1
		return self.victory
	
	def  cont(self,na,nd):
		a=attack()
		if ((na-nd>5) or (nd<2 and na>4)):
			self.x=0
		else:
			self.x=1
		return self.x
	
	
def main():
	#na=int(input("na"))
	#nd=int(input("nd")) 
	na=1000
	nd=20
	a=attack()
	print(attack.war(a,na,nd))
main()
