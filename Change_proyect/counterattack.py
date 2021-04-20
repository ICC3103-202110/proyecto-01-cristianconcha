from action import Action
from player import Player
from console import Console
from numpy import random
from prints import Print
class Counterattack(Action):

    
    select_counterattack_ = 0
    counterattack_players = []

    def select_counterattack(self):
        if self.action_played == "Income":
            return

        elif self.action_played == "Coup":
            return

        else:
            while True:
                Print.player_select(
                    self.player_how_have_card.player, self.action_played)

                print("Some player wants to counterattack: \n")
                print("\nPlayers:")

                for i in range(len(self.players)):
                    if self.players[i] == self.player_how_have_card:
                        continue
                    else:
                        print("", i, "=", self.players[i].player)

                select = Console.select_player_number()

                if select == "c":
                    return self.select_counterattack

                else:
                    self.select_counterattack = 2
                    self.counterattack_players.append(int(select))

    
    def select_the_counterattack_player(self):  
        for i in range(len(self.counterattack_players)-1):
            number = random.randint(0, len(self.counterattack_players)-1)
            self.counterattack_player.pop(number)
        
        self.log.counterattack(self.players[int(self.counterattack_players[0])].player,
                               self.player_how_have_card.player)

        self.player_how_have_card = self.players[int(self.counterattack_players[0])]

        Console.clean()
        print("%s was selected to Counterattack\n" % self.player_how_have_card.player)
        
       
    def start_counterattack(self): 
        Console.pass_next_player(self.player_how_have_card.player)

        if self.action_played == "Foreign Aid":  
            select = Console.counterattack_foreign_aid()

        elif self.action_played == "Captain":
            select = Console.counterattack_captain()

        elif self.action_played == "Assassin":  
            select =Console.counterattack_assassin()
        
        self.action_played = self.actions[select]
        Console.clean()

        print(self.player_how_have_card.player, "say that he have the %s\n" % self.action_played)
        self.log.said_that_have(self.player_how_have_card.player, self.action_played)
        Console.press_to_continue()
        
        
        
