import attack
from attack import attack

import adecide
from adecide import adecide

import borders
from borders import test

import start
from start import GameCreate


def main():
    nump=int(input("number of players"))
    a=GameCreate()
    mappedOwner=a.giveTerritory(nump)
    for x in mappedOwner:
        a.giveTroops(x)
    
main()
