from action import Action
from player import Player
from console import Console

class Challenge(Action):

    def __init__(self, select_challenge=0, challenging_players=0):
        self.select_challenge = 0
        self.challenging_players = []

    def select_challenge(self):  # challenge

        if self.action_played == "Income":
            Console.player_select(
                self.player_how_have_card.player, self.action_played)
            Console.press_to_continue()

        elif self.action_played == "Coup":
            Console.player_select(
                self.player_how_have_card.player, self.action_played)
            Console.pass_next_player(
                self.player_how_have_card.player)

        elif self.action_played == "Foreign Aid":
            pass

        else:
            while True:
                Console.player_select(
                    self.player_how_have_card.player, self.action_played)

                print("Some player wants to challenge: \n")
                print("\nPlayers:")
                
                for i in range(len(self.players)):

                    if self.players[i] == self.player_how_have_card:
                        continue
                    else:
                        print("", i, "=", self.players[i].player)

                select = Console.select_player_number()

                if select == "c":
                    return self.select_challenge

                else:
                    self.select_challenge = 1 
                    self.challenging_players.append(int(select)) 


    
