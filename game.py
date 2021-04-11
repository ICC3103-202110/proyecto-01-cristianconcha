#import os  # os.system('cls||clear') limpia el tablero
from player import Player
from cards import Cards
class Game:
    print("-----------------------------------")
    print("---------Wellcome to Coup----------")
    print("-----------------------------------\n")
    NUMBER_Players = 3#int(input("Enter the number of playeres (3 or 4): "))
    players = []
    


    @classmethod
    def play(cls):
        cls.name_players()

        #while
        cls.print_money()
        




        







    @classmethod
    def name_players(cls):
        for i in range(1, cls.NUMBER_Players + 1):
            card = Cards()
            name = input("Give the player's %d name: " % i)
            cls.players.append(Player(name, card.randomCards()))

  

    @classmethod
    def print_money(cls):
        print("Money:")
        for i in range(cls.NUMBER_Players):
            cls.players[i].printMoney()

        print("")    







if __name__ == "__main__":
    Game.play()
