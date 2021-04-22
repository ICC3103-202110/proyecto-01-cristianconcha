from action import Action
from player import Player
from console import Console
from prints import Print
from numpy import random

class Challenge(Action):

    __select_challenge = 0
    __challenging_players = []

    def select_challenge(self):  

        if self.action_played == "Income":
            Print.player_select(
                self.player_how_have_card.player, self.action_played)
            Console.press_to_continue()

        elif self.action_played == "Coup":
            Print.player_select(
                self.player_how_have_card.player, self.action_played)
            Console.pass_next_player(
                self.player_how_have_card.player)

        elif self.action_played == "Foreign Aid":
            return 0

        else:
            while True:
                Print.player_select(
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
                    return self.__select_challenge

                else:
                    self.__select_challenge = 1 
                    self.__challenging_players.append(int(select)) 


    def select_the_challenging_player(self): 

        for i in range(len(self.__challenging_players)-1):
            number = random.randint(0, len(self.__challenging_players)-1)
            self.__challenging_players.pop(number)

        self.other_player = self.players[int(self.__challenging_players[0])]

        self.log.challenge(self.other_player.player,
                           self.player_how_have_card.player)
        Console.clean()
        print("%s was selected to challenge\n" %self.other_player.player)

       
    def start_challenge(self):  
        true_or_false = self.card.compare_cards(self.player_how_have_card,
        self.action_played)

        if true_or_false == False:  
            print("The player %s dont`t have the card\n" %self.player_how_have_card.player)
            Console.pass_next_player(self.player_how_have_card.player)
            card_lose = self.card.delete_one_card(self.player_how_have_card)
            self.card.card_lose_list(card_lose) 
            self.log.dont_have_card(self.player_how_have_card.player, self.action_played)
            self.log.player_lose_card(self.player_how_have_card.player, card_lose)

            return False

        elif true_or_false == True:

            print("The player %s" % self.player_how_have_card.player,
                  "have the %s" % self.action_played)
            self.log.have_card(self.player_how_have_card.player, self.action_played)

            print("\nThe player %s lose one card" %self.other_player.player)
            Console.pass_next_player(self.other_player.player)
            card_lose = self.card.delete_one_card(self.other_player)
            self.card.card_lose_list(card_lose) 
            self.log.player_lose_card(self.other_player.player, card_lose)
            Console.clean()

            print("The player %s change the card" %self.player_how_have_card.player)
            
            self.card.delete_card_played(self.action_played, self.player_how_have_card)
            self.card.add_card_list(self.action_played)
            self.log.change_card(self.player_how_have_card.player, self.action_played)
            self.card.add_one_card(self.player_how_have_card)

            return True

            Console.press_to_continue()
