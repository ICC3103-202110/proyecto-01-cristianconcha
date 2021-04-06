from cards import Cards
from player import Player
class Game:
    def play(self):

        while True:
            numberOfPlayers = 4 #int(input("Insert the number of players (3 or 4): "))

            card = Cards()
            
            if numberOfPlayers == 3 or numberOfPlayers == 4:
                player1Card = card.randomCards()
                player1 = Player("Player 1", player1Card)

                player2Card = card.randomCards()
                player2 = Player("Player 2", player2Card)

                player3Card = card.randomCards()
                player3 = Player("Player 3", player3Card)
                
                if numberOfPlayers == 4:
                    player4Card = card.randomCards()
                    player4 = Player("Player 4", player4Card)

                break

            else:
                print("The game is 3 or 4 players") 


        #while
        player1.printCard()
        player2.printCard()
        player3.printCard()
        player4.printCard()
        











