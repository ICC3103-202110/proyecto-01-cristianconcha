import os

class Console: #inputs or clean console
        
    @staticmethod
    def clean():
        os.system('cls || clear')
    
    @staticmethod
    def number_of_players(): #change
        return 3  # int(input("Enter the number of playeres (3 or 4): "))
        
    @staticmethod
    def select_action():
        return int(input("Select the accion number: "))
 
    @staticmethod
    def select_card():
        return int(input("\nSelect the card number: "))

    @staticmethod
    def select_player():
        return int(input("\n---> "))
        
    @staticmethod
    def select_player_number():
        print("\nEnter the player number to chanllenge or")
        print("press 'c' to continue")
        select = input("---> ")
        os.system('cls || clear')
        return select
    
    @staticmethod
    def press_to_continue():
        input("Press any key to continue...")
        os.system('cls || clear')

    @staticmethod
    def player_turn(player_name):
        print("\nIt's %s's turn\n" % player_name)
        input("Press any key to continue...")
        os.system('cls || clear')
    
    @staticmethod
    def pass_next_player(player_name):
        print("\nPass the computer to %s \n" % player_name)
        input("Press any key to continue... ")
        os.system('cls || clear')
    
    @staticmethod
    def pass_next_player_cards(player_name):
        print("\nPass the computer to %s to see his cards" % player_name)
        input("Press any key to continue... ")
        os.system('cls || clear')
    
    #action selection
    @staticmethod
    def Coup_or_Assassin_choose(players, player):
        while True:
            print("Choose the player to lose Influence \n")
            for i in range(len(players)):
                if players[i] == player:
                    continue
                else:
                    print(i, players[i].player)

            select = int(input("\n---> "))
            if players[select] != player and select < len(players):
                return select
            else:
                Console.clean()
                print("The number is invalid\n")

    @staticmethod
    def Captain_choose(players, player):
        while True:
            print("Choose the player to lose 2 coins \n")
            for i in range(len(players)):
                if players[i] == player:
                    continue
                else:
                    print(i, " = ", players[i].player,
                          "have", players[i].coin, "coins")

            select = int(input("\n---> "))
            if players[select] != player and select < len(players):
                return select
            else:
                Console.clean()
                print("The number is invalid\n")

    #Counterattack
    @staticmethod
    def counterattack_foreign_aid():
        print("The only card to counterattack the Foreign Aid is:\n")
        print("3 = Duke\n")

        while True:
            select = int(input("Select the card number: "))
            if select == 3:
                return select
            else:
                print("The number is invalid\n")

    @staticmethod
    def counterattack_captain():
        print("The cards to counterattack the Captain is:\n")
        print("5 = Ambaddassor")
        print("6 = Captain\n")

        while True:
            select = int(input("Select the card number: "))
            if select == 5 or select == 6:
                return select
            else:
                print("The number is invalid\n")
    
    @staticmethod
    def counterattack_assassin():
        print("The only card to counterattack the action Assassin is:\n")
        print("7 = Contessa\n")
        while True:
            select = int(input("Select the card number: "))

            if select == 7:
                return select
            else:
                print("The number is invalid\n")



    
    





    
        
        
