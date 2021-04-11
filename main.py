from three_players_game import Three_Players_Game
from four_players_game import Four_Players_Game


def main():

    print("-----------------------------------")
    print("---------Wellcome to Coup----------")
    print("-----------------------------------\n")
    
    #Hacer un while para que se reita si esta malo el valor
    players = int(input("Enter the number of playeres (3 or 4): "))
    print()

    if players == 3:
        game3 = Three_Players_Game()
    elif players == 4:
        game4 = Four_Players_Game()
    
    else:
        print("Invalid number, you must enter 3 or 4")
    

    
if __name__ == "__main__": 
    main()





    
