from cards import Cards

class Player:
    def __init__(self, player, cards= 0, money = 2):
        self.__player = player
        self.cards = cards
        self.money = money

    @property 
    def player(self):
        return self.__player

    def addmoney(self):
        pass

    def losemoney(self):
        print(player1.money)
        print(player4.money)
        pass










