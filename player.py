from cards import Cards

class Player:
    def __init__(self, player, cards= 0, money = 2):
        self.__player = player
        self.cards = cards
        self.money = money

    @property 
    def player(self):
        return self.__player

    def printCard(self):
        print(self.cards[0], end = ",")
        print(self.cards[1])

    def printMoney(self):
        print(self.player +":", end = " ")
        print(self.money, end = " | ")

    def addmoney(self):
        pass

    def losemoney(self):

        pass










