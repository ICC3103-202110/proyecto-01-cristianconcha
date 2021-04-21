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
    def see_player_cards(players):  #delete
        for i in range(len(players)):
            print("\nYour cards:", end=" ")
            cards = players[i].cards

            for a in range(len(cards)):
                print(cards[a], end=" ")

            print("\n")
    @staticmethod
    def see_player_card(players):
            print("\nYour cards:", end=" ")
            cards = players.cards

            for i in range(len(cards)):
                print(cards[i], end=" ")

            print("\n")

    @staticmethod
    def see_player_card(player):
        print("\nYour cards:", end=" ")
        cards = player.cards
        for i in range(len(player.cards)):
            print(cards[i], end=" ")
        print("\n")

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

    @staticmethod
    def cards_lose(cards_lose):
        print("Lost Cards:")
        for i in range(len(cards_lose)):
            print(cards_lose[i], end=", ")
        print("\n")
    
    @staticmethod
    def player_card(player):
        print("\nYour cards:", end=" ")
        cards = player.cards
        for a in range(len(cards)):
            print(cards[a], end=" ")

        print("\n")

    @staticmethod
    def actions(action):
        print("Actions:\n")
        for i in range(len(action)):
            print(i, "=", action[i])
        print("8 = If you want to see your cards")
    
    @staticmethod
    def log(logs):
        count = 0
        for i in range(len(logs)):

            if logs[i] == 1:
                print("\n")
                count += 1
            elif count == 1:
                print(logs[i])
                count -= 1
            else:
                print("- ", logs[i])
                
        print("\n")
    
    @staticmethod 
    def invalid_action():
        Console.clean()
        print("Invalid action number\n")
    
    @staticmethod  
    def player_select(player, card):
        print(player, "select", card, "\n")
    
    #select steal
    @staticmethod 
    def steal(player, player2):
        print(player, "want to take 2 coins of", player2)
    
    #select assassinate
    @staticmethod
    def coup(player, player2): 
        print(player, "select", player2, "to lost one influence")

    @staticmethod  
    def assassinate(player, player2):
        print(player, "select", player2, "to lost one influence (Assassinate)")
    
    @staticmethod
    def winner(player):
        Console.clean()
        print("\n\nThe winner is %s \n\n" % player)
        print("Thanks for play coup !")
    


    
    
    

    
