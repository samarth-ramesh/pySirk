import territories
from territories import territories

class newTurn:

    
    def getTroops(self,player):
        self.y=0
        teritoryOwner=territories.owner 
        for self.x in teritoryOwner:
            if teritoryOwner[self.x]==player:
                self.y+=1
                #print("\t",self.x)
        if self.y<9:
            self.numTroops=3
        else:
            self.numTroops=int(self.y/3)
        print(self.numTroops)

     def placeTroops(self,player):
        teritoryOwner=territories.owner 
        self.myTroops={}
        for self.x in teritoryOwner:
            if teritoryOwner[self.x]==player:
                #self.myTroops[self.x]=territories.troops[self.x]
                
