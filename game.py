import os  
from player import Player
from cards import Cards
class Game:
    print("-----------------------------------")
    print("---------Wellcome to Coup----------")
    print("-----------------------------------\n")
    NUMBER_Players = 3#int(input("Enter the number of playeres (3 or 4): "))
    players = []
    turn = 0
    Accion = 0
    


    @classmethod
    def play(cls):
        cls.name_players()
        print("")

        #while
        cls.print_money()
        print("")
        cls.Accion = cls.Player_Accion()
        
       
        




        







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
        
    @classmethod
    def Player_Accion(cls):
        while True:
            print("It's %s's turn\n" % cls.players[cls.turn].player)

            print("Accions:")
            print("1 = Income")
            print("2 = Foreign Aid")
            print("3 = Coup")
            print("4 = Tax (Duke)")
            print("5 = Assassinate (Assassin)")
            print("6 = Exhange (Ambassador)")
            print("7 = Steal (Captian)\n")
        
            print("Your cards:", end = " ")
            cls.players[cls.turn].printCard()
            
            action = int(input("Select the accion number: "))
            if action > 0 and action < 8:
                return action
            else:
                os.system('cls||clear') 
                print("Invalid accion number\n")

if __name__ == "__main__":
    Game.play()
