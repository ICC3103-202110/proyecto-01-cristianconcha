from cards import Cards
class Player:
    def __init__(self, player, cards= 0, coin = 7):
        self.__player = player
        self.cards = cards
        self.coin = coin

    @property 
    def player(self):
        return self.__player
    


    def printCard(self):
        for i in range(len(self.cards)):
            print(self.cards[i])

    def printCoins(self):
        print(self.player + ":", end = " ")
        print(self.coin, end = " | ")

    def add_one_coin(self):
        self.coin += 1
    
    def add_two_coin(self):
        self.coin += 2
    
    def pay_7_coins(self):
        self.coin -= 7

    def delete_card(self):
        self.cards.pop()
    
   
    
        











