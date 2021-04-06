from cards import Cards
class Game:
    def play(self):

        while True:
            numberOfPlayers = int(input("Insert the number of players (3 or 4): "))
            card = Cards()
            if numberOfPlayers == 3:
                player1Card = card.randomCards()
                player2Card = card.randomCards()
                player3Card = card.randomCards()
                break
            
            elif numberOfPlayers == 4:
                player1Card = card.randomCards()
                player2Card = card.randomCards()
                player3Card = card.randomCards()
                player4Card = card.randomCards()
                break

            else:
                print("The game is 3 or 4 players") 












