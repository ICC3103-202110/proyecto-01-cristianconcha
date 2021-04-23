from player import Player
from console import Console
from prints import Print
from log import Log
from coins import Coins
class Action:

    def __init__(self, players, player_how_have_card, card, log, turn, other_player=0, action_played=0, first_action=0,assassinate_or_steal=0):
        self.__players = players
        self.__player_how_have_card = player_how_have_card
        self.__card = card
        self.__turn = turn
        self.__log = log
        self.__other_player = other_player
        self.__actions = ["Income", "Foreign Aid", "Coup",
                        "Duke", "Assassin", "Ambassador", "Captain", "Contessa"]
        self.__action_played = action_played
        self.__first_action = first_action
        self.__assassinate_or_steal = assassinate_or_steal

    @property
    def players(self):
        return self.__players

    @players.setter
    def players(self, value):
        self.__players = value
    
    @property
    def player_how_have_card(self):
        return self.__player_how_have_card

    @player_how_have_card.setter
    def player_how_have_card(self, value):
        self.__player_how_have_card = value

    @property
    def card(self):
        return self.__card

    @card.setter
    def card(self, value):
        self.__players = value
    
    @property
    def turn(self):
        return self.__turn

    @turn.setter
    def turn(self, value):
        self.__turn = value
    
    @property
    def log(self):
        return self.__log

    @log.setter
    def log(self, value):
        self.__log = value

    @property
    def turn(self):
        return self.__turn

    @turn.setter
    def turn(self, value):
        self.__turn = value
    
    @property
    def other_player(self):
        return self.__other_player

    @other_player.setter
    def other_player(self, value):
        self.__other_player = value

    @property
    def actions(self):
        return self.__actions

    @actions.setter
    def actions(self, value):
        self.__actions = value
    
    @property
    def action_played(self):
        return self.__action_played

    @action_played.setter
    def action_played(self, value):
        self.__action_played = value
    
    @property
    def first_action(self):
        return self.__first_action
    
    @first_action.setter
    def first_action(self, value):
        self.__first_action = value

    @property
    def assassinate_or_steal(self):
        return self.__assassinate_or_steal

    @assassinate_or_steal.setter
    def assassinate_or_steal(self, value):
        self.__assassinate_or_steal = value


    def select_action(self):  

        while True:
            self.log.turn(self.player_how_have_card.player) 
            Console.player_turn(self.player_how_have_card.player)

            if self.player_how_have_card.coin >= 10:
                print("You have more than 10 coins, \nso you must use the coup action\n")
                Console.press_to_continue()
                self.action_played = "Coup"
                self.first_action = "Coup"

                select = Console.Coup_or_Assassin_choose(
                            self.players, self.player_how_have_card)
                self.assassinate_or_steal = self.players[select]
                Print.coup(self.player_how_have_card.player,
                           self.assassinate_or_steal.player)

                Coins.pay_seven_coins(self.player_how_have_card)
                self.log.more_coins(self.player_how_have_card.player)

                break

            else:
                Print.actions(self.actions)
                print("\n")
                action = Console.select_action()

                if action >= 0 and action < 7:
                    self.action_played = str(self.actions[action])
                    self.first_action = str(self.actions[action])
                    Console.clean()

                    if self.action_played == "Coup" and self.player_how_have_card.coin < 7:
                        print("You don`t have 7 coins\n")

                    elif self.action_played == "Assassin" and self.player_how_have_card.coin < 3:
                        print("You don`t have 3 coins\n")

                    else:
                          
                        if self.action_played == "Coup":
                            Coins.pay_seven_coins(self.player_how_have_card)

                            select = Console.Coup_or_Assassin_choose(
                                self.players, self.player_how_have_card)
                            self.assassinate_or_steal = self.players[select]
                            
                            self.log.action_selected(self.action_played,
                                                     self.player_how_have_card.player,
                                                     self.assassinate_or_steal.player)
                            self.log.pay_coup(self.player_how_have_card.player)
                            Console.clean()
                            Print.coup(self.player_how_have_card.player,
                                         self.assassinate_or_steal.player)
                            break

                        elif self.action_played == "Assassin":
                            Coins.pay_three_coins(self.player_how_have_card)

                            select = Console.Coup_or_Assassin_choose(
                                self.players, self.player_how_have_card)
                            self.assassinate_or_steal = self.players[select]
                            
                            self.log.action_selected(self.action_played,
                                                     self.player_how_have_card.player,
                                                     self.assassinate_or_steal.player)
                            self.log.pay_assassinate(self.player_how_have_card.player)
                            Console.clean()
                            Print.assassinate(self.player_how_have_card.player,
                                                self.assassinate_or_steal.player)
                            break

                        elif self.action_played == "Captain":
                        
                            select = Console.Coup_or_Assassin_choose(
                                self.players, self.player_how_have_card)
                            self.assassinate_or_steal = self.players[select]
                            
                            self.log.action_selected(self.action_played,
                                                     self.player_how_have_card.player,
                                                     self.assassinate_or_steal.player)
                            Console.clean()
                            Print.steal(self.player_how_have_card.player,
                                          self.assassinate_or_steal.player)
                            break

                        self.log.action_selected(self.action_played,
                                                 self.player_how_have_card.player,
                                                 None)
                        break
                
                elif action == 8:
                    Print.see_player_card(self.player_how_have_card)
                else:
                    Print.invalid_action()

        
    def run_action(self):
        
        if self.first_action == "Income":
            
            Coins.add_one_coin(self.players[self.turn])
            self.log.income(self.players[self.turn].player)

        elif self.first_action == "Foreign Aid":
            
            Coins.add_two_coins(self.players[self.turn])
            self.log.foreign_aid(self.players[self.turn].player)

        elif self.first_action == "Coup":

            Console.pass_next_player(self.assassinate_or_steal.player)
            card_lose = self.card.delete_one_card(self.assassinate_or_steal)
            self.card.card_lose_list(card_lose) 
            self.log.coup(self.players[self.turn].player,
                         self.assassinate_or_steal.player)

        elif self.first_action == "Duke":  # (tax)
            
            Coins.add_three_coins(self.players[self.turn])
            self.log.tax(self.players[self.turn].player)

        elif self.first_action == "Assassin":  # (assassinate)

            Console.pass_next_player(self.assassinate_or_steal.player)
            card_lose = self.card.delete_one_card(self.assassinate_or_steal)
            self.card.card_lose_list(card_lose) 
            self.log.assassinate(self.players[self.turn].player,
                                self.assassinate_or_steal.player)

        elif self.first_action == "Ambassador":  # (Exhange)

            self.card.add_two_cards(self.players[self.turn])
            cards = self.card.delete_two_cards(self.players[self.turn])

            if len(cards) > 0:
                self.card.add_two_cards_list(cards)
                
            self.log.exchange(self.players[self.turn].player)

        elif self.first_action == "Captain":  # (Steal)

            total_coins = Coins.select_the_coins_to_delete(self.assassinate_or_steal)
            Coins.add_coins(self.players[self.turn], total_coins)
            self.log.steal(self.players[self.turn].player,
                          self.assassinate_or_steal.player,
                          total_coins)

