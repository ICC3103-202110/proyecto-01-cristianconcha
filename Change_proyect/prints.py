from console import Console
from player import Player
class Print():

    @staticmethod
    def wellcome():
        Console.clean
        print("-----------------------------------")
        print("---------Wellcome to Coup----------")
        print("-----------------------------------\n")
    
    @staticmethod
    def see_players_cards(players):
        Console.clean()
        for i in range(len(players)):
            print("\nYour cards:", end=" ")
            cards = players[i].cards

            for a in range(len(cards)):
                print(cards[a], end=" ")

            print("\n")
                
            Console.pass_next_player_cards(players[i].player)
            Console.press_to_continue()

    @staticmethod
    def coins(players):
        print("Coins    ", end="| ")
        for i in range(len(players)):
            print(players[i].player + ":", end=" ")
            print(players[i].coin, end=" | ")
        print("")
    
    @staticmethod
    def len_cards(players):
        print("Influence", end="| ")
        for i in range(len(players)):
            print(players[i].player + ":", end=" ")
            print(len(players[i].cards), end=" | ")
        print("\n")

    @staticmethod
    def print_losers(losers):
        print("Losers: ")
        for i in range(len(losers)):
            print(losers[i].player + ":", end=", ")   
        print("\n")
    
    
    

    
