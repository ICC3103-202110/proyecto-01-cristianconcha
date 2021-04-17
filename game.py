from numpy import random
from player import Player
from cards import Cards
from console import Console
class Game:
    print("-----------------------------------")
    print("---------Wellcome to Coup----------")
    print("-----------------------------------\n")
    actions = ["Income", "Foreign Aid", "Coup", "Duke", "Assassin", "Ambassador", "Captain", "Contessa"]
    NUMBER_Players = 3  #int(input("Enter the number of playeres (3 or 4): "))
    card = Cards()
    players = []
    turn = 0

    player_how_have_card = None
    other_player = None

    action_played = None  #card
    
    select_challenge = None  # counter attack or challenge
    select_counterattack = None

    challenging_players = []  # Player to challenge
    counterattack_players = [] #Player to counter attack
    

    @classmethod
    def play(cls):
        cls.name_players()

        while True:
            Console.clean()
            
            cls.print_Coins()
            cls.print_players_cards()
            print("")
            cls.print_cards()  #borrar
            print("")


            cls.Player_Accion()
            cls.Select_Challenge()
            cls.Select_Counterattack()

            if cls.select_challenge == 1:
                cls.select_the_challenging_player()
                cls.Challenge()

            elif cls.select_counterattack == 2:
                cls.select_the_counterattack_player()
                cls.Counterattack()

            else:
                cls.Action()
            
            cls.Delete_player()
            cls.Clean_values()
            cls.player_turn()


            if len(cls.players) == 1:
                break

        Console.clean()
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
        print("Coins    ", end="| ")
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
    def print_players_cards(cls):
        print("Influence", end="| ")
        for i in range(len(cls.players)):
            cls.players[i].print_len_cards()
        print("")
        
    @classmethod
    def Player_Accion(cls):
        while True:
            cls.player_how_have_card = int(cls.turn)
            
            print("\n\nTurn: ",cls.turn)
            print("\n\nIt's %s's turn\n" %cls.players[cls.player_how_have_card].player)

            if cls.players[cls.player_how_have_card].coin >= 10:
                print("You have more than 10 coins, \nso you must use the coup action\n")
                input("Press any key to continue...")
                Console.clean()
                cls.action_played = "Coup"
                cls.players[cls.player_how_have_card].pay_seven_coins()
                print("\n", cls.players[cls.player_how_have_card].player,"select", cls.action_played, "\n")
                break
                
            else:
                for i in range(len(cls.actions)):
                    print(i, "=" , cls.actions[i])

                print("\nYour cards:", end = " ")
                cls.players[cls.player_how_have_card].printCard()
                action = int(input("Select the accion number: "))

                if action >= 0 and action < 7:
                    cls.action_played = str(cls.actions[action])
                    Console.clean()

                    if cls.action_played == "Coup" and cls.players[cls.player_how_have_card].coin < 7:
                        print("You don`t have 7 coins\n")

                    elif cls.action_played == "Assassin" and cls.players[cls.player_how_have_card].coin < 3:
                        print("You don`t have 3 coins\n")

                    else:
                        print("\n", cls.players[cls.player_how_have_card].player, "select", cls.actions[action], "\n")

                        if cls.action_played == "Assassin":
                            cls.players[cls.player_how_have_card].pay_three_coins()

                        elif cls.action_played == "Coup":
                            cls.players[cls.player_how_have_card].pay_seven_coins()
                            
                        break

                else:
                    Console.clean()
                    print("Invalid accion number\n")
        
    @classmethod
    def Select_Challenge(cls):

        if cls.action_played == "Income":
            input("Press any key to continue...")
            Console.clean()
            return

        elif cls.action_played == "Coup":
            input("Press any key to continue...")
            Console.clean()
            return
        
        elif cls.action_played == "Foreign Aid":
            return
                    
        else:
            while True:
                print("Some player wants to challenge: \n")
                
                print("\nPlayers:")

                for i in range(len(cls.players)):
                    if i == cls.player_how_have_card:
                        continue
                    else:
                        print("", i, "=", cls.players[i].player)
                
                print("\nEnter the player number to chanllenge or")
                print("press 'c' to continue")
                select = input("---> ")
                Console.clean()

                if select[0] == "c":
                    break
                else:
                    cls.select_challenge = 1
                    cls.challenging_players.append(int(select))
    
    @classmethod
    def Select_Counterattack(cls):
        if cls.action_played == "Income":
            return

        elif cls.action_played == "Coup":
            return

        else:
            while True:
                print("Some player wants to counterattack: \n")

                print("Players:")

                for i in range(len(cls.players)):
                    if i == cls.player_how_have_card:
                        continue
                    else:
                        print("", i, "=", cls.players[i].player)

                print("\nEnter the player number to counterattack or")
                print("press 'c' to continue")
                select = input("---> ")
                Console.clean()

                if select[0] == "c":
                    break
                else:
                    cls.select_counterattack = 2
                    cls.counterattack_players.append(int(select))
        
    @classmethod
    def Challenge(cls):

        Console.clean()
        print("%s was selected to challenge\n" %cls.players[cls.other_player].player)
        input("Press any key to continue")
        Console.clean()

        true_or_false = cls.players[cls.player_how_have_card].compare_cards(cls.action_played)
        
        if true_or_false == False:  #Player turn Dont have the card
            print("The player %s dont`t have the card\n" %cls.players[cls.player_how_have_card].player)
            card_lose = cls.players[cls.player_how_have_card].delete_one_card()
            cls.card.card_lose(card_lose)


        elif true_or_false == True: #Player turn Have the car
            print("The player %s have the card" %cls.players[cls.player_how_have_card].player)
            print(cls.action_played)
            input("Press any key to continue")
            Console.clean()
            
            print("The player %s lose one card" %cls.players[cls.other_player].player)
            card_lose = cls.players[cls.other_player].delete_one_card()
            cls.card.card_lose(card_lose)
            input("Press any key to continue")
            Console.clean()
            
            print("The player %s change the card" %cls.players[cls.player_how_have_card].player)
            card = cls.card.One_random_Card()
            cls.players[cls.player_how_have_card].add_one_card(card)
            
            cls.Action()
            input("Press any key to continue")
            Console.clean()

    @classmethod
    def Counterattack(cls):
        Console.clean()

        print("%s was selected to Counterattack" %cls.players[cls.other_player].player)
        input("Press any key to continue")
        Console.clean()

        if cls.action_played == "Foreign Aid":  
            print("The only card to counterattck the Foreign Aid is:\n")
            print("3 = Duke\n")

        elif cls.action_played == "Assassin":  
            print("The only card to counterattck the action Assassin is:")
            print("7 = Contessa\n")

        elif cls.action_played == "Captain":  
            print("The cards to counterattck the Captain is:\n")
            print("5 = Ambaddassor")
            print("6 = Captain")
        
        print("%s selecte the number card" % cls.players[cls.other_player].player)

        print("Your cards:", end=" ")
        cls.players[cls.other_player].printCard()
        select = int(input("\nSelect the card number: "))
        cls.action_played = cls.actions[select]
        Console.clean()

        print(cls.players[cls.other_player].player, "say that he have the %s\n" % cls.action_played)
        input("Press any key to continue")
        Console.clean()

        cls.Select_Challenge()
        cls.Challenge()
    
    @classmethod
    def select_the_challenging_player(cls):
        for i in range(len(cls.challenging_players)-1):
            number = random.randint(0, len(cls.challenging_players))
            cls.challenging_players.pop(number)

        cls.other_player = int(cls.challenging_players[0])

    @classmethod
    def select_the_counterattack_player(cls):
        for i in range(len(cls.counterattack_players)-1):
            number = random.randint(0, len(cls.counterattack_players))
            cls.counterattack_player.pop(number)

        cls.other_player = int(cls.counterattack_players[0])
    
    @classmethod
    def Action(cls):  #corroborate inputs numbers

        if cls.action_played == "Income":  
            cls.players[cls.player_how_have_card].add_one_coin()
        
        elif cls.action_played == "Foreign Aid":  
            cls.players[cls.player_how_have_card].add_two_coin()
        
        elif cls.action_played == "Coup":
            
            for i in range(len(cls.players)):
                if i == cls.player_how_have_card:
                    continue
                else:
                    print(i, cls.players[i].player)
                
            select = int(input(("\nChoose the player to lose Influence:")))
            Console.clean()
            input("Press any key to continue")
            Console.clean()
            cls.players[select].delete_one_card()
                
        elif cls.action_played == "Duke":  #(tax)
            cls.players[cls.player_how_have_card].add_three_coin()
        
        elif cls.action_played == "Assassin":  # (assassinate)
            
            for i in range(len(cls.players)):
                if i == cls.player_how_have_card:
                    continue
                else:
                    print(i, cls.players[i].player)
                
            select = int(input(("Choose the player to lose Influence: ")))
            Console.clean()
            input("Press any key to continue")
            Console.clean()
            cls.players[select].delete_one_card()
                
        elif cls.action_played == "Ambassador":  # (Exhange)
            cards = cls.card.randomCards()
            cls.players[cls.player_how_have_card].add_two_cards(cards)
            cls.players[cls.player_how_have_card].delete_two_cards()
            
        elif cls.action_played == "Captain":  # (Steal)
            for i in range(len(cls.players)):
                if i == cls.player_how_have_card:
                    continue
                else:
                    print(i," = ",cls.players[i].player, "have",cls.players[i].coin, "coins")

            select = int(input(("Choose the player to lose 2 coins: "))) 
            cls.players[select].delete_two_coins()
            cls.players[cls.player_how_have_card].add_two_coin()

    @classmethod
    def Clean_values(cls):
        cls.player_how_have_card = None
        cls.other_player = None
        cls.action_played = None  
        cls.select_challenge = None  
        cls.select_counterattack = None
        cls.challenging_player = [] 
        cls.counterattack_player = []  
      
    @classmethod
    def Delete_player(cls):
        delete = []
        for i in range(len(cls.players)):
            if cls.players[i].len_cards() == 0: #contar cartas
                delete.append(cls.players[i])
            else:
                continue

        if len(delete) > 0:
            for i in range(len(delete)):  
                cls.players.remove(delete[i])
                cls.NUMBER_Players -= 1


    @classmethod
    def player_turn(cls):
        
        if cls.turn == cls.NUMBER_Players - 1:
            cls.turn = 0

        elif len(cls.players)-1 < cls.NUMBER_Players-1:
            cls.turn -= 1

        else:
            cls.turn += 1
                
                    
if __name__ == "__main__":
    Game.play()
