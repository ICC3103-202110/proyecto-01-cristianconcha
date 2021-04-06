
class Player:
    def __init__(self, player, cards= 0, money = 2):
        self.__player = player
        self.cards = cards
        self.money = money

    @property 
    def player(self):
        return self.__player

    




player1 = Player("player1")
player2 = Player("player2")
player3 = Player("player3")
player4 = Player("player4")

