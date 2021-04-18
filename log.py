
class Log:

    def __init__(self, log=0):
        self.log = []

    #Action selected
    def action_selected(self, action, player, player2):
        if action == "Income":
            self.log.append((player, "uses the action Income"))
            
        elif action == "Foreign Aid":
            self.log.append((player, "uses the action Foreign Aid"))

        elif action == "Coup":
            self.log.append((player, "uses the action Coup against",player2))

        elif action == "Duke":
            self.log.append((player, "uses the action Tax"))
            
        elif action == "Assassin":
            self.log.append((player, "uses the action Assassinate against", player2))

        elif action == "Ambassador":
            self.log.append((player, "uses the action Exchange"))

        elif action == "Captain":
            self.log.append((player, "uses the action Steal against", player2))
    
    #Final Action
    def income(self, player):
        self.log.append((player,"take 1 coin for Income"))
        
    def foreign_aid(self,player):
        self.log.append((player,"take 2 coins for Foreign Aid"))

    def coup(self, player, player2):
        self.log.append((player, "pay 7 coins to eliminate one influence of", player2, "for Coup"))

    def tax(self, player):
        self.log.append((player,"take 3 coins for Tax"))

    def assassinate(self, player, player2):
        self.log.append((player, "pay 3 coins to eliminate one influence of", player2, "for Assassinate"))

    def exchange(self, player):
        self.log.append((player, "exchange 2 cards for Exchange"))
    
    def steal(self, player, player2, coins):
        self.log.append((player, "take",coins,"coin(s) of", player2, "for Steal"))
    

