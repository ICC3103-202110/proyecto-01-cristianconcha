from action import Action
from player import Player
from console import Console
class Counterattack(Action):

    def __init__(self, select_counterattack=0, counterattack_players=0):
        self.select_counterattack_ = 0
        self.challenging_players = []

    def select_counterattack(self):
        if self.action_played == "Income":
            pass

        elif self.action_played == "Coup":
            pass

        else:
            while True:
                Console.player_select(
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

