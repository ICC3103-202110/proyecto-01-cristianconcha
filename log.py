
class Log:

    def __init__(self, log=0, action=0):
        self.log = []
        self.action = action

    #Action selected
    def action_selected(self, action, player, player2):
        if action == "Income":
            self.log.append((player, "uses the action Income"))
            self.action = "Income"

        elif action == "Foreign Aid":
            self.log.append((player, "uses the action Foreign Aid"))
            self.action = "Foreign Aid"

        elif action == "Coup":
            self.log.append((player, "uses the action Coup against",player2))
            self.action = "Coup"

        elif action == "Duke":
            self.log.append((player, "uses the action Tax"))
            self.action = "Tax"
            
        elif action == "Assassin":
            self.log.append((player, "uses the action Assassinate against", player2))
            self.action = "Assassinate"

        elif action == "Ambassador":
            self.log.append((player, "uses the action Exchange"))
            self.action = "Exchange"

        elif action == "Captain":
            self.log.append((player, "uses the action Steal against", player2))
            self.action = "Steal"
    
    #Pays
    def pay_coup(self, player):
        self.log.append((player, "play 7 coins for delete one influence"))
    
    def pay_assassinate(self, player):
        self.log.append((player, "play 3 coins for assessinate one influence"))

    #10 or more coins
    def more_coins(self, player):
        self.log.append((player, "have more than 10 coins, and uses the Coup"))
        
    def challenge(self, player, player2):
        self.log.append((player, "challenge", player2, "for the action", self.action))

    def counterattack(self, player, player2):
        self.log.append((player, "counterattack", player2,"for the action", self.action))

    #Challenge
    #Counterattack
    #say is he wins or lose one card





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
    
    #print
    def print_log(self): #add this in the file game
        for i in range(len(self.log)):
            print(log[i])
