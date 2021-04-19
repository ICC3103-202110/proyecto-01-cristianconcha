
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
        print("\nYour cards:", end=" ")
        for i in range(len(self.cards)):
            print(self.cards[i], end=" ")
        print("\n")

    def printCoins(self):
        print(self.player + ":", end = " ")
        print(self.coin, end=" | ")
    
    def print_len_cards(self):
        print(self.player + ":", end=" ")
        print(len(self.cards), end=" | ")
    
    #Add coins
    def add_one_coin(self):
        self.coin += 1
    
    def add_two_coins(self, total_coins):
        self.coin += total_coins
    
    def add_three_coins(self):
        self.coin += 3

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
        print("Choose the number card to delete:\n")
        for i in range(len(self.cards)):
            print(i, self.cards[i])

        delete = int(input("\n---> "))
        card = self.cards[delete]
        self.cards.pop(delete)
        return card
        
    def delete_two_cards(self):
        cards = []
        for a in range(2):
            print("Choose the number card to delete:\n")
            
            for i in range(len(self.cards)):
                print(i, self.cards[i])

            delete = int(input("\n---> "))
            cards.append(self.cards[delete])
            self.cards.pop(delete)
            print("")

        return cards
    
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




    








    
   
    
        











