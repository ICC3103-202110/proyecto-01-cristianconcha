import os

class Console:

    @staticmethod
    def wellcome():
        os.system('cls || clear')
        print("-----------------------------------")
        print("---------Wellcome to Coup----------")
        print("-----------------------------------\n")

    @staticmethod
    def winner(winner):
        os.system('cls || clear')
        print("\n\nThe winner is %s \n\n" % winner)
        print("Thanks for play coup !")
        
    @staticmethod
    def clean():
        os.system('cls || clear')
    
    @staticmethod
    def number_of_players(): #change
        number = 3 #int(input("Enter the number of playeres (3 or 4): "))
        return number

    @staticmethod
    def select_action():
        action = int(input("Select the accion number: "))
        return action
    
    @staticmethod
    def select_card():
        card_number = int(input("\nSelect the card number: "))
        return card_number

    @staticmethod
    def select_player():
        player = int(input("\n---> "))
        return player
    
    @staticmethod
    def player_select(player, card):
        print(player,"select", card, "\n" )

    @staticmethod
    def invalid_action():
        os.system('cls || clear')
        print("Invalid action number\n")

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

    #select assassinate
    @staticmethod
    def coup(player, player2):
        print(player, "select",player2, "to lost one influence")

    @staticmethod
    def assassinate(player, player2):
        print(player, "select", player2, "to lost one influence (Assassinate)")
    
    #select steal
    @staticmethod
    def steal(player, player2):
        print(player, "want to take 2 coins of", player2)


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

    @staticmethod
    def print_losers(player):
        print(player, end=", ")


    
    





    
        
        
