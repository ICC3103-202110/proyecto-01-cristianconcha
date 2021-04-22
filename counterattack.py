from action import Action
from player import Player
from console import Console
from numpy import random
from prints import Print
class Counterattack(Action):

    
    __select_counterattack = 0
    __counterattack_players = []

    def select_counterattack(self):
        if self.action_played == "Income":
            return 0

        elif self.action_played == "Coup":
            return 0
        
        elif self.action_played == "Duke":
            return 0
        
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
                    return self.__select_counterattack

                else:
                    self.__select_counterattack = 2
                    self.__counterattack_players.append(int(select))

    
    def select_the_counterattack_player(self):  
        for i in range(len(self.__counterattack_players)-1):
            number = random.randint(0, len(self.__counterattack_players)-1)
            self.__counterattack_players.pop(number)
        
        self.log.counterattack(self.players[int(self.__counterattack_players[0])].player,
                               self.player_how_have_card.player)

        self.player_how_have_card = self.players[int(self.__counterattack_players[0])]

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
        
        
        
