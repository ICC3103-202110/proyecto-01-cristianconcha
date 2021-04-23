
class Player:
    def __init__(self, player, cards, coin = 2): 
        self.__player = player
        self.__cards = cards
        self.__coin = coin

    @property 
    def player(self):
        return self.__player
    
    @property
    def cards(self):
        return self.__cards

    @cards.setter
    def cards(self, card):
        self.__cards = card
    
    @property
    def coin(self):
        return self.__coin

    @coin.setter
    def coin(self, coin):
        self.__coin = coin
    

        

    



    








    
   
    
        











