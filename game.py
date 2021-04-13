import os  
from player import Player
from cards import Cards
class Game:
    print("-----------------------------------")
    print("---------Wellcome to Coup----------")
    print("-----------------------------------\n")
    actions = ["Income", "Foreign Aid", "Coup", "Duke", "Assassin", "Ambassador", "Captain", "Contessa"]
    list_cards = ["Duke", "Assassin", "Ambassador", "Captian", "Contessa"]
    NUMBER_Players = 3  #int(input("Enter the number of playeres (3 or 4): "))
    card = Cards()
    players = []
    turn = 0
    action_played = 0 #card
    Number_Action = 0  # counter attack or challenge
    challenging_player = 0  # number player
    

    @classmethod
    def play(cls):
        cls.name_players()


        while True:
            os.system('cls||clear')
            
            cls.print_Coins()
            print("")
            cls.print_cards()  #borrar
            print("")

            cls.Player_Accion()
            cls.Select_Challenge_Counterattack()

            if cls.Number_Action == 1:
                cls.Challenge()

            elif cls.Number_Action == 2:
                
                cls.Counterattack()

            else:
                cls.Action()
            
            cls.Delete_player()

            if cls.turn == (len(cls.players)-1):
                cls.turn = 0
            else:
                cls.turn += 1

            if len(cls.players) == 1:
                break

        os.system('cls||clear')
        print("-----------------------------------")
        print("The winner is %s" % cls.players[0].player)
        print("-----------------------------------")




        
  
    @classmethod #ready
    def name_players(cls):
        for i in range(1, cls.NUMBER_Players + 1):
            
            name = input("Give the player's %d name: " % i)
            cls.players.append(Player(name, cls.card.randomCards()))

    @classmethod #ready
    def print_Coins(cls):
        print("Coins:")
        for i in range(len(cls.players)):
            cls.players[i].printCoins()

        print("")
    
    @classmethod  # Borrar depues
    def print_cards(cls):
        print("Cards:")
        for i in range(len(cls.players)):
            cls.players[i].printCard()

        print("")
        
    @classmethod
    def Player_Accion(cls):
        while True:
            print("It's %s's turn\n" % cls.players[cls.turn].player)

            if cls.players[cls.turn].coin >= 10:
                print("You have more than 10 coins, \nso you must use the coup action\n")
                input("Press any key to continue...")
                os.system('cls||clear')
                cls.action_played = "Coup"
                print("\n", cls.players[cls.turn].player, "select", cls.action_played, "\n")
                break
                

            
            else:
                for i in range(len(cls.actions)):
                    print(i, "=" , cls.actions[i])

                print("\nYour cards:", end = " ")
                cls.players[cls.turn].printCard()
                action = int(input("Select the accion number: "))

                if action >= 0 and action < 7:
                    cls.action_played = cls.actions[action]
                    os.system('cls||clear')

                    if cls.action_played == "Coup" and cls.players[cls.turn].coin < 7:
                        print("You don`t have 7 coins\n")

                    elif cls.action_played == "Assassin" and cls.players[cls.turn].coin < 3:
                        print("You don`t have 3 coins\n")

                    else:
                        print("\n",cls.players[cls.turn].player, "select", cls.actions[action], "\n")
                        cls.action_played = str(cls.actions[action])
                        break

                else:
                    os.system('cls||clear') 
                    print("Invalid accion number\n")
        
    @classmethod
    def Select_Challenge_Counterattack(cls):

        if cls.action_played == "Income": 
            input("Press any key to continue...")
            os.system('cls||clear')
            return

        elif cls.action_played == "Coup":
            input("Press any key to continue...")
            os.system('cls||clear')
            return
        
        elif cls.action_played == "Foreign Aid":
            while True:
                print("Some player wants to: \n")
                print("Action:\n 2 = Counterattack\n")
                print("\nPlayers:")

                for i in range(len(cls.players)):
                    if i == cls.turn:
                        continue
                    else:
                        print("", i, "=", cls.players[i].player)
                
                print("\nEnter the action number and the player number")
                print("Example: 2,1")
                print("To continue press 'c' ")
                select = input("---> ").split(',')
                os.system('cls||clear')

                if select[0] == "c":
                    break
                else:
                    cls.Number_Action = int(select[0])
                    cls.challenging_player = int(select[1])

        else:
            while True:
                print("Some player wants to: \n")
                print("Action:\n 1 = Challenge \n 2 = Counterattack\n")
                print("\nPlayers:")

                for i in range(len(cls.players)):
                    if i == cls.turn:
                        continue
                    else:
                        print("", i, "=", cls.players[i].player)
                        
                print("\nEnter the action number and the player number")
                print("Example: 1,2")
                print("To continue press 'c' ")
                select = input("---> ").split(',')
                os.system('cls||clear')

                if select[0] == "c":
                    break
                else:
                    cls.Number_Action = int(select[0])
                    cls.challenging_player = int(select[1])
        
    @classmethod
    def Challenge(cls):
        true_or_false = cls.players[cls.turn].compare_cards(cls.action_played)
        
        if true_or_false == False:  #Player turn Dont have the card
            print("The player %s dont`t have the card\n" %cls.players[cls.turn].player)
            cls.players[cls.turn].delete_one_card()

        elif true_or_false == True: #Player turn Have the car
            print("The player %s have the card" % cls.players[cls.turn].player)
            print(cls.action_played)
            
            print("The player %s lose one card" %cls.players[cls.challenging_player].player)
            cls.players[cls.challenging_player].delete_one_card()
            input("Press any key to continue")
            os.system('cls||clear') 
            
            print("The player %s change the card" % cls.players[cls.turn].player)
            card = cls.card.One_random_Card()
            cls.action()
            cls.players[cls.turn].add_one_card(card)

    @classmethod
    def Counterattack(cls):
        os.system('cls||clear')

        if cls.action_played == "Foreign Aid":  
            print("The only card to counterattck the Foreign Aid is:\n")
            print("0 = Duke\n")

        elif cls.action_played == 3:  # Duke
            pass

        elif cls.action_played == "Assassin":  
            print("The only card to counterattck the action Assassin is:")
            print("4 = Contessa\n")

        elif cls.action_played == 5:  # Ambassador
            pass

        elif cls.action_played == 6:  # Captain
            pass
        
        
        print("%s selecte the number card" % cls.players[cls.challenging_player].player)

    
        print("Your cards:", end=" ")
        cls.players[cls.turn].printCard()
        select = int(input("\nSelect the card number: "))
        os.system('cls||clear') 

        print("%s;" % cls.players[cls.turn].player)
        print(cls.players[cls.challenging_player].player,"say that he have the %s\n" % cls.list_cards[select])
        
        print("You have to options:")
        print("0 = Belive him\n1 = Not belive him\n")

        choose = int(input("Choose the option number: "))
        os.system('cls||clear') 

        if choose == 0:#Player turn Belive
            print(cls.players[cls.turn].player, "belive % s" % cls.players[cls.challenging_player].player)

        elif choose == 1: #Player turn Not belive
            true_or_false = cls.players[cls.turn].compare_cards(cls.list_cards[select])

            if true_or_false == False: #Other player donthave the card
                print("The player %s dont`t have the card" %cls.players[cls.challenging_player].player)
                cls.players[cls.challenging_player].delete_one_card()
                cls.action()

            elif true_or_false == True: #Other player have the card
                print("The player %s have the card" %cls.players[cls.challenging_player].player)
                print(cls.action_played)

                print("\nThe player %s lose one card" %cls.players[cls.turn].player)
                cls.players[cls.turn].delete_one_card()
                input("Press any key to continue")
                os.system('cls||clear')

                print("The player %s change the card" %cls.players[cls.challenging_player].player)
                card = cls.card.One_random_Card()
                cls.players[cls.challenging_player].add_one_card(card)


    @classmethod
    def Action(cls):  #corroborate inputs numbers

        if cls.action_played == "Income":  
            cls.players[cls.turn].add_one_coin()
        
        elif cls.action_played == "Foreign Aid":  
            cls.players[cls.turn].add_two_coin()
        
        elif cls.action_played == "Coup":  
           
            for i in range(len(cls.players)):
                if i == cls.turn:
                    continue
                else:
                    print(i, cls.players[i].player)
                
            select = int(input(("\nChoose the player to lose Influence:")))
            cls.players[select].delete_card()
            cls.players[cls.turn].pay_seven_coins()
                
        elif cls.action_played == "Duke":  #(tax)
            cls.players[cls.turn].add_three_coin()
        
        elif cls.action_played == "Assassin":  # (assassinate)
           
            for i in range(len(cls.players)):
                if i == cls.turn:
                    continue
                else:
                    print(i, cls.players[i].player)
                
            select = int(input(("Choose the player to lose Influence: ")))
            cls.players[select].delete_card()
            cls.players[cls.turn].pay_three_coins()
                
        elif cls.action_played == "Ambassador":  # (Exhange)
            card = cls.card.randomCards()
            cls.players[cls.turn].add_two_cards(card)
            cls.players[cls.turn].delete_two_cards()
            
        elif cls.action_played == "Captain":  # (Steal)
            for i in range(len(cls.players)):
                if i == cls.turn:
                    continue
                else:
                    print(i," = ",cls.players[i].player, "have",cls.players[i].coin, "coins")

            select = int(input(("Choose the player to lose 2 coins: ")))
            cls.players[select].delete_two_coins()
            cls.players[cls.turn].add_two_coin()

    @classmethod
    def Delete_player(cls):
        for i in range(len(cls.players)):
            if cls.players[i].len_cards() == 0: #contar cartas
                cls.players.remove(cls.players[i])
            else:
                continue

if __name__ == "__main__":
    Game.play()
