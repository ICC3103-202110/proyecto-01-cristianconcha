from cards import Cards
class Player:
    def __init__(self, player, cards, coin = 7): #cambiar coins
        self.__player = player
        self.cards = cards
        self.coin = coin

    @property 
    def player(self):
        return self.__player
    
    def printCard(self):
        for i in range(len(self.cards)):
            print(self.cards[i], end=" ")
        print("")

    def printCoins(self):
        print(self.player + ":", end = " ")
        print(self.coin, end = " | ")

    def add_one_coin(self):
        self.coin += 1
    
    def add_two_coin(self):
        self.coin += 2
    
    def add_three_coin(self):
        self.coin += 3
    
    def delete_two_coins(self):
        self.coin -= 2

    def pay_three_coins(self):
        self.coin -= 3

    def pay_seven_coins(self):
        self.coin -= 7

    def delete_card(self):
        self.cards.pop()
    
    def add_two_cards(self, card):
        self.cards += card
    
    def delete_two_cards(self):
        for a in range(2):
            for i in range(len(self.cards)):
                print(i, self.cards[i])
            
            delete = int(input("Choose the number card to delete: "))
            self.cards.pop(delete)
            print("")

    








    
   
    
        











