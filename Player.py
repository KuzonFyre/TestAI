# Model limits to decrease complexity
# Ignore confession card
# Limit wounds on vampire up to 4
# Ignore face up cards from Suspicion
# Other state to consider
# - Number of face down cards

class Player:
    def __init__(self, role, ID):
        self.damage = 0 # Public {state}
        self.role = role # Conditional Private {state}
        self.roleRevealed = False # public {state}
        # TODO: if a player is no longer alive, all players should be able to see their role and other private information
        self.isAlive = True # public
        self.isBitten = False # public {state}
        self.ID = ID # private
        self.hand = [] # private
        self.isCursed = False # public {state}
        self.suspicion = 0 # public {state} Defined between 0 and 3
        self.faceDownCards = [] # private
        self.faceUpCards = [] # public
        # TODO: I could see the number of biteTokens potentially being relevant info to state. If a player has 2 bite tokens, the other players might be more inclined to play a turned card on them
        self.biteTokens = 0 # public

    def cycle_hand(self, new_hand):
        self.hand = new_hand

    def __str__(self):
        st = "Damage: {}\n".format(self.damage)
        st += "Alive: {}\n".format(self.isAlive)
        st += "Bitten: {}\n".format(self.isBitten)
        st += "Role: {}".format(self.role)
        return st

    def isEmpty(self):
        if self.faceDownCards == []:
            return True