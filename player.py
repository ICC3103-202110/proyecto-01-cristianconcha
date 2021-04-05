
class Player:
    def __init__(self, player, cards= 0, money = 2):
        self.__player = player
        self.__cards = cards
        self.__money = money

    @property 
    def player(self):
        return self.__player

    



