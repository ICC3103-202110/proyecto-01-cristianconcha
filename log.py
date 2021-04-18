
class Log:

    def __init__(self, log=0):
        self.log = []
    
    #Accions
    @staticmethod
    def income(self, player):
        self.log.append(player,"take 1 coin for Income")
        
    @staticmethod
    def foreign_aid(self,player):
        self.log.append(player,"take 2 coins for Foreign Aid")
    
    @staticmethod
    def coup(self, player, player2):
        self.log.append(player, "pay 7 coins to eliminate one influence of", player2, "for Coup")

    @staticmethod
    def tax(self, player):
        self.log.append(player,"take 3 coins for Duke")

    @staticmethod
    def assassinate(self, player, player2):
        self.log.append(player, "pay 3 coins to eliminate one influence of", player2, "for Assassin")

    @staticmethod
    def exchange(self, player):
        self.log.append(player, "exchange 2 cards for Ambassador")
    
    @staticmethod
    def steal(self, player, player2, coins):
        self.log.append(player, "take",coins,"coins of", player2, "for Captain")
    
