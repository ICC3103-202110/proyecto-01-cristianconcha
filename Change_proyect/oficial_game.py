from console import Console
from player import Player

class Game:

    NUMBER_PLAYERS = None
    players = []
    losers = []


    @classmethod
    def play(cls):


        pass





    @classmethod
    def number_of_players(cls):
        while True:
            number = Console.number_of_players()
            if number == 3 or number == 4:
                cls.NUMBER_PLAYERS= number
                break
            else:
                print("The game only accept 3 or 4 players")

    @classmethod
    def name_players(cls):
        """#change
        for i in range(1, cls.NUMBER_Players + 1):
            
            name = input("Give the player's %d name: " % i)
            cls.players.append(Player(name, cls.card.randomCards()))
        """
        cls.players.append(Player("Amelia", ["Contessa", "Duke"]))  # delete
        cls.players.append(Player("Bernabé", ["Captain", "Contessa"]))  # delete
        cls.players.append(Player("Carmen", ["Duke", "Assassin"]))  # delete

    


if __name__ == "__main__":
    Game.play()
