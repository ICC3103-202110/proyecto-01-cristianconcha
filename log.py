
class Log:

    def __init__(self, log=0):
        self.log = []
    
    #Actions

    def income(self, player):
        self.log.append(player,"take 1 coin for Income")
        

    def foreign_aid(self,player):
        self.log.append(player,"take 2 coins for Foreign Aid")

    def coup(self, player, player2):
        self.log.append(player, "pay 7 coins to eliminate one influence of", player2, "for Coup")


    def tax(self, player):
        self.log.append(player,"take 3 coins for Tax")


    def assassinate(self, player, player2):
        self.log.append(player, "pay 3 coins to eliminate one influence of", player2, "for Assassinate")


    def exchange(self, player):
        self.log.append(player, "exchange 2 cards for Exchange")
    
    def steal(self, player, player2, coins):
        self.log.append(player, "take",coins,"coin(s) of", player2, "for Steal")
    
