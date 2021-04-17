
class Player:
    def __init__(self, player, cards, coin = 7): #change coins
        self.__player = player
        self.cards = cards
        self.coin = coin

    @property 
    def player(self):
        return self.__player
    
    #Print
    def printCard(self):
        for i in range(len(self.cards)):
            print(self.cards[i], end=" ")
        print("")

    def printCoins(self):
        print(self.player + ":", end = " ")
        print(self.coin, end=" | ")
    
    def print_len_cards(self):
        print(self.player + ":", end=" ")
        print(len(self.cards), end=" | ")

    #Add coins
    def add_one_coin(self):
        self.coin += 1
    
    def add_two_coin(self):
        self.coin += 2
    
    def add_three_coin(self):
        self.coin += 3

    #Delete coins
    def delete_two_coins(self):
        if self.coin == 1:
            self.coin -= 1

        elif self.coin >= 2:
            self.coin -= 2
    

    def pay_three_coins(self):
        self.coin -= 3

    def pay_seven_coins(self):
        self.coin -= 7

    #Add card
    def add_one_card(self, card):#are the same
        self.cards += card

    def add_two_cards(self, card):
        self.cards += card

    #Delete card
    def delete_card(self):
        if len(self.cards) == 0:
            return
        else:
            self.cards.pop()
    
    def delete_one_card(self):
        for i in range(len(self.cards)):
            print(i, self.cards[i])

        delete = int(input("Choose the number card to delete: "))
        card = self.cards[delete]
        self.cards.pop(delete)
        return card
        

    def delete_two_cards(self):
        for a in range(2):
            for i in range(len(self.cards)):
                print(i, self.cards[i])
            delete = int(input("Choose the number card to delete: "))
            self.cards.pop(delete)
            print("")
    
    #Compare Card
    def compare_cards(self, card):
        count = self.cards.count(card)
        if count == 0:
            return False
        else:
            #Cambiar:debo elgir con cual me quedo
            self.cards.remove(card)
            return True
    
    #len cards
    def len_cards(self):
        return len(self.cards)



    








    
   
    
        











