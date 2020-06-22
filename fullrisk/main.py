import attack
from attack import attack

import adecide
from adecide import adecide

import borders
from borders import test

import start
from start import GameCreate

import territories
from territories import territories

import newTurn
from newTurn import newTurn

def main():
    
    
    nump=int(input("number of players=\t"))
    a=GameCreate()
    mappedOwner=a.giveTerritory(nump)
    b=territories()
    b.initOwner(mappedOwner)
    for x in mappedOwner:
        a.giveTroops(x)
    
    #print(b.troops,mappedOwner)
    b
    c=newTurn()
    c.getMaxTroops(1)


main()
