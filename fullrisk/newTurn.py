import territories
from territories import territories

class newTurn:
    def getMaxTroops(self,player):
        self.y=0
        teritoryOwner=territories.owner 
        for self.x in teritoryOwner:
            if teritoryOwner[self.x]==player:
                self.y+=1
        if self.y<9:
            self.numTroops=3
        else:
            self.numTroops=int(self.y/3)
        print(self.numTroops)
