from cards import Cards
from player import Player
class Game:
    def play(self):

        while True:
            numberOfPlayers = 4 #int(input("Insert the number of players (3 or 4): "))

            card = Cards()
            
            if numberOfPlayers == 3 or numberOfPlayers == 4:
                player1Card = card.randomCards()
                player1 = Player("P1", player1Card)

                player2Card = card.randomCards()
                player2 = Player("P2", player2Card)

                player3Card = card.randomCards()
                player3 = Player("P3", player3Card)
                
                if numberOfPlayers == 4:
                    player4Card = card.randomCards()
                    player4 = Player("P4", player4Card)

                break

            else:
                print("The game is 3 or 4 players") 


        #while
        player1.printMoney()
        player2.printMoney()
        player3.printMoney()
        player4.printMoney()
        print(" ")
        












