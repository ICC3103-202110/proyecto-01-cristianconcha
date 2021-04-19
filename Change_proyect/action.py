from player import Player
from console import Console
from prints import Print
from log import Log
class Action:

    def __init__(self,players ,player_how_have_card, card, log, action_played=0, assassinate_or_steal=0):
        self.players = players
        self.player_how_have_card = player_how_have_card
        self.card = card
        self.log = log
        self.actions = ["Income", "Foreign Aid", "Coup",
                        "Duke", "Assassin", "Ambassador", "Captain", "Contessa"]
        self.action_played = action_played
        self.assassinate_or_steal = assassinate_or_steal


    def select_action(self):  

        while True:
            print("\nTurn: ")  # delete ###########

            Console.player_turn(self.player_how_have_card.player)

            if self.player_how_have_card.coin >= 10:
                print("You have more than 10 coins, \nso you must use the coup action\n")
                Console.press_to_continue()
                self.action_played = "Coup"

                self.player_how_have_card.pay_seven_coins()
                self.log.more_coins(player_how_have_card.player)
                self.player_how_have_card.player
                break

            else:
                Print.actions(self.actions)
                Print.player_card(self.player_how_have_card)
                action = Console.select_action()

                if action >= 0 and action < 7:
                    self.action_played = str(self.actions[action])
                    Console.clean()

                    if self.action_played == "Coup" and self.player_how_have_card.coin < 7:
                        print("You don`t have 7 coins\n")

                    elif self.action_played == "Assassin" and self.player_how_have_card.coin < 3:
                        print("You don`t have 3 coins\n")

                    else:
                        self.log.action_selected(self.action_played,
                                                self.player_how_have_card.player,
                                                self.assassinate_or_steal.player)  # change this
                        

                        if self.action_played == "Coup":
                            self.player_how_have_card.pay_seven_coins()

                            self.assassinate_or_steal = Console.Coup_or_Assassin_choose(
                                self.players, self.player_how_have_card)

                            self.log.pay_coup(self.player_how_have_card.player)
                            Console.clean()
                            Console.coup(self.player_how_have_card.player,
                                         self.assassinate_or_steal.player)

                        elif self.action_played == "Assassin":
                            self.player_how_have_card.pay_three_coins()

                            self.assassinate_or_steal = Console.Coup_or_Assassin_choose(
                                self.players, self.player_how_have_card)

                            self.log.pay_assassinate(self.player_how_have_card.player)
                            Console.clean()
                            Console.assassinate(self.player_how_have_card.player,
                                                self.assassinate_or_steal.player)

                        elif self.action_played == "Captain":
                            self.player_how_have_card.pay_seven_coins()

                            self.assassinate_or_steal = Console.Captain_choose(
                                self.players, self.player_how_have_card)

                            Console.clean()
                            Console.steal(self.player_how_have_card.player,
                                          self.assassinate_or_steal.player)


                        return

                else:
                    Console.invalid_action()

