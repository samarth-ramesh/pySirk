import attack
from attack import attack

import adecide
from adecide import adecide

def main():
	na=int(input("na= \t"))
	nd=int(input("nd= \t")) 
	#na=1000
	#nd=20
	a=attack()
	print(attack.war(a,na,nd))

main()
