from player import Player
from console import Console
from log import Log
class Action:

    def __init__(self, player_how_have_card,log, action_played=0):
        self.player_how_have_card = player_how_have_card
        self.log = log
        self.action_player = action_played


    def player_action(self):  # action
        
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
                print("Actions:\n")
                for i in range(len(cls.actions)):
                    print(i, "=", cls.actions[i])

                cls.players[cls.player_how_have_card].printCard()
                action = Console.select_action()

                if action >= 0 and action < 7:
                    cls.action_played = str(cls.actions[action])
                    Console.clean()

                    if cls.action_played == "Coup" and cls.players[cls.player_how_have_card].coin < 7:
                        print("You don`t have 7 coins\n")

                    elif cls.action_played == "Assassin" and cls.players[cls.player_how_have_card].coin < 3:
                        print("You don`t have 3 coins\n")

                    else:
                        cls.log.action_selected(cls.action_played,
                                                cls.players[cls.player_how_have_card].player,
                                                cls.players[cls.assassinate_or_steal].player)

                        if cls.action_played == "Coup":
                            cls.players[cls.player_how_have_card].pay_seven_coins()
                            cls.assassinate_or_steal = cls.Coup_or_Assassin_choose()
                            cls.log.pay_coup(
                                cls.players[cls.player_how_have_card].player)
                            Console.clean()
                            Console.coup(cls.players[cls.player_how_have_card].player,
                                         cls.players[cls.assassinate_or_steal].player)

                        elif cls.action_played == "Assassin":
                            cls.players[cls.player_how_have_card].pay_three_coins()
                            cls.assassinate_or_steal = cls.Coup_or_Assassin_choose()
                            cls.log.pay_assassinate(
                                cls.players[cls.player_how_have_card].player)
                            Console.clean()
                            Console.assassinate(cls.players[cls.player_how_have_card].player,
                                                cls.players[cls.assassinate_or_steal].player)

                        elif cls.action_played == "Captain":
                            cls.players[cls.player_how_have_card].pay_seven_coins()
                            cls.assassinate_or_steal = cls.Captain_choose()
                            Console.clean()
                            Console.steal(cls.players[cls.player_how_have_card].player,
                                          cls.players[cls.assassinate_or_steal].player)

                        break

                else:
                    Console.invalid_action()

        
