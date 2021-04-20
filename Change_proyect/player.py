
class Player:
    def __init__(self, player, cards, coin = 7): #change coins
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
        self.__cards = cards
    
    @property
    def coin(self):
        return self.__coin

    @coin.setter
    def coin(self, coin):
        self.__coin = coin
    

    def add_two_coins(self, total_coins):
        self.coin += total_coins

    
    """
    #Delete coins
    def delete_two_coins(self):
        total_coins = 0
        if self.coin == 1:
            self.coin -= 1
            total_coins += 1
            
        elif self.coin >= 2:
            self.coin -= 2
            total_coins += 2
            
        return total_coins
    
    def pay_three_coins(self):
        self.coin -= 3

    def pay_seven_coins(self):
        self.coin -= 7

    #Add card
    def add_one_card(self, card):
        self.cards += card

    def add_two_cards(self, card):
        self.cards += card

    #Delete card
    def delete_card(self):  #see if i use this
        if len(self.cards) == 0:
            return
        else:
            self.cards.pop()
    
    def delete_one_card(self):
        while True:
            print("Choose the number card to delete:\n")
            for i in range(len(self.cards)):
                print(i, self.cards[i])

            delete = int(input("\n---> "))

            if delete < len(self.cards):
                card = self.cards[delete]
                self.cards.pop(delete)
                return card
            else:
                print("The number is invalid\n")
        
    def delete_two_cards(self):
        cards = []
        len_card = 0
        while True:
            print("Choose the number card to delete:\n")
            
            for i in range(len(self.cards)):
                print(i, self.cards[i])

            delete = int(input("\n---> "))

            if delete < len(self.cards):
                cards.append(self.cards[delete])
                self.cards.pop(delete)
                len_card += 1
                if len_card == 2:
                    return cards
            else:
                print("The number is invalid\n\n")
 
    def delete_card_played(self,card):
        self.cards.remove(card)
    
    #Compare Card
    def compare_cards(self, card):
        count = self.cards.count(card)
        if count == 0:
            return False
        else:
            return True
    
    #len cards
    def len_cards(self):
        return len(self.cards)

    """


    








    
   
    
        











