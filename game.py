import os  
from player import Player
from cards import Cards
class Game:
    print("-----------------------------------")
    print("---------Wellcome to Coup----------")
    print("-----------------------------------\n")
    NUMBER_Players = 3  #int(input("Enter the number of playeres (3 or 4): "))
    card = Cards()
    players = []
    turn = 0
    Number_Action = 0
    selection = 0
    


    @classmethod
    def play(cls):
        cls.name_players()
        os.system('cls||clear')


        #while len(players)
        cls.print_Coins()
        print("")
        cls.Number_Action = cls.Player_Accion()
        print("")
        cls.Select_Challenge_Counterattack()

        if cls.selection[0] == 1:
            cls.Challenge()
            pass

        elif cls.selection[0] == 2:
            cls.Counterattack()
            pass

        else:
            cls.Action()

        #cls.print_Coins()
        
  
        
        

       
        




    
    @classmethod
    def name_players(cls):
        for i in range(1, cls.NUMBER_Players + 1):
            
            name = input("Give the player's %d name: " % i)
            cls.players.append(Player(name, cls.card.randomCards()))

    @classmethod
    def print_Coins(cls):
        print("Coins:")
        for i in range(cls.NUMBER_Players):
            cls.players[i].printCoins()

        print("")
        
    @classmethod
    def Player_Accion(cls):
        while True:
            list_action = ["Income", "Foreign Aid", "Coup", "Duke", "Assassin",
                           "Ambassador", "Captian"]
            print("It's %s's turn\n" % cls.players[cls.turn].player)

            print("Accions:")
            print("1 = Income")
            print("2 = Foreign Aid")
            print("3 = Coup")
            print("4 = Duke (tax)")
            print("5 = Assassin (Assassinate)")
            print("6 = Ambassador (Exhange)")
            print("7 = Captian (Steal)\n")
        
            print("Your cards:", end = " ")
            cls.players[cls.turn].printCard()
            
            action = int(input("Select the accion number: "))
            if action > 0 and action < 8:
                os.system('cls||clear')
                print("\n",cls.players[cls.turn].player, "select", list_action[action-1], "\n")
                return action
            else:
                os.system('cls||clear') 
                print("Invalid accion number\n")
    
    @classmethod
    def Select_Challenge_Counterattack(cls):
        while True:
            print("Some player wants to: \n")
            print("Action:\n 1 = Challenge \n 2 = Counterattack\n")
            print("\nPlayers:")
            for i in range(cls.NUMBER_Players):
                if i == cls.turn:
                    continue
                else:
                    print("",i,"=", cls.players[i].player)
            print("\nEnter the action number and the player number")
            print("Example: 1,2")
            print("To continue press 'c' ")
            select = input("---> ")
            os.system('cls||clear')

            if select == "c":
                break
            else:
                cls.selection = select.split(",")
        

    @classmethod
    def Challenge(cls):
        pass

    @classmethod
    def Counterattack(cls):
        pass

        
        

        
        


    





    @classmethod
    def Action(cls): #corroborate inputs numbers
        if cls.Number_Action == 1: #Income
            cls.players[cls.turn].add_one_coin()
        
        elif cls.Number_Action == 2:  # Foreign Aid
            cls.players[cls.turn].add_two_coin()
        
        elif cls.Number_Action == 3:  # Coup
            if cls.players[cls.turn].coin >= 7:
                for i in range(cls.NUMBER_Players):
                    if i == cls.turn:
                        continue
                    else:
                        print(i, cls.players[i].player)
                
                select = int(input(("Choose the player to lose Influence:")))
                cls.players[select].delete_card()
                cls.players[cls.turn].pay_seven_coins()
                
            else:
                print("You don`t have 7 coins")
                #Hacer que se repita el ciclo
        
        elif cls.Number_Action == 4:  # Duke (tax)
            cls.players[cls.turn].add_three_coin()
        
        elif cls.Number_Action == 5:  # Assassinate (assassinate)
            if cls.players[cls.turn].coin >= 3:
                for i in range(cls.NUMBER_Players):
                    if i == cls.turn:
                        continue
                    else:
                        print(i, cls.players[i].player)
                
                select = int(input(("Choose the player to lose Influence:")))
                cls.players[select].delete_card()
                cls.players[cls.turn].pay_three_coins()
                
            else:
                print("You don`t have 3 coins")
                #Hacer que se repita el ciclo

        elif cls.Number_Action == 6:  # Ambassador (Exhange)
            card = cls.card.randomCards()
            cls.players[cls.turn].add_two_cards(card)
            cls.players[cls.turn].delete_two_cards()
            
        elif cls.Number_Action == 7:  # Ambassador (Steal)
            for i in range(cls.NUMBER_Players):
                if i == cls.turn:
                    continue
                else:
                    print(i, cls.players[i].player, "have",cls.players[i].coin, "coins")

            select = int(input(("Choose the player to lose 2 coins:")))
            cls.players[select].delete_two_coins()
            cls.players[cls.turn].add_two_coin()
        

if __name__ == "__main__":
    Game.play()
