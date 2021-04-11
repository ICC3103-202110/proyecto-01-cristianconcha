#import os  # os.system('cls||clear') limpia el tablero
from player import Player
class Game:
    print("-----------------------------------")
    print("---------Wellcome to Coup----------")
    print("-----------------------------------\n")
    NUMBER_Players = 3#int(input("Enter the number of playeres (3 or 4): "))
    players = []
    


    @classmethod
    def play(cls):
        cls.name_players()
        cls.players[0].printMoney()

        #while

        
        







    @classmethod
    def name_players(cls):
        for i in range(1, cls.NUMBER_Players + 1):
            name = input("Give the player's %d name: " % i)
            cls.players.append(Player(name))
        


if __name__ == "__main__":
    Game.play()
