class attack:
      #methods for attacking
        #number of troops
        #possible defenders from territories
        #number of defenders, from class defenders for decision making
        #war, boolean describing state of war, sets defender.
        #rolling and computing, a subclass
           #number of attacker dies(list)
           #number of defender dies(list)
           #list of attacker values(list)
           #list of defender values(list)
           #compare(list)
           #effect(int)
    pass    


class defend:


    #methods for defending
        #number of troops(int)
    
    pass


class armies:


    :#methods for armies(nations)
        #number of territories(int)
        #number of new troops available(int)
        #mission(future only)(int)
    pass


class territories:


    :#methods for territories
        #owner of territories(int)
        #number of troops at territory(int)
        #is defender(bool)
        #number of defender troops at borders(dict)
    pass


class borders:


#the different territories are stored as a dictionary with a serial no. as a key and the owner as a value
#the bordering nations are then stored as a dictionary, stored within a list. the key of the dictionary being the serial no. and the value being the number of troops     
    pass
