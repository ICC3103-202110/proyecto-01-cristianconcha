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
    def select_action():
        action = int(input("Select the accion number: "))
        return action
    
    @staticmethod
    def select_card():
        card_number = int(input("\nSelect the card number: "))
        return card_number

    @staticmethod
    def select_player():
        player = int(input("---> "))
        return player
    
    @staticmethod
    def player_select(player, card):
        print(player," select ", card )

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


    
        
        
