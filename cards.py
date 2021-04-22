from numpy import random
from player import Player
from console import Console

class Cards:
    def __init__(self, cards=0, cards_lose=0):
        self.__cards = ["Duke", "Assassin", "Ambassador", "Captain", "Contessa",
                        "Duke", "Assassin", "Ambassador", "Captain", "Contessa",
                        "Duke", "Assassin", "Ambassador", "Captain", "Contessa"]
        self.__cards_lose = []
    
    @property
    def cards(self):
        return self.__cards

    @cards.setter
    def cards(self, value):
        self.__cards = value

    @property
    def cards_lose(self):
        return self.__cards_lose

    @cards_lose.setter
    def cards_lose(self, value):
        self.__cards_lose = value

    #random cards
    def two_random_cards(self):
        card = []
        number = random.randint(0, len(self.cards))
        card.append(self.cards[number])
        self.cards.pop(number)

        number = random.randint(0, len(self.cards))
        card.append(self.cards[number])
        self.cards.pop(number)
        return card
    
    #list
    def add_card_list(self, card): 
        self.cards.append(card)
    
    def add_two_cards_list(self, card):
        self.cards += card
        
    def card_lose_list(self, card):
        self.cards_lose.append(card)    

    #Add player card
    def add_one_card(self, player):
        if len(self.cards) >= 1:
            card = []
            number = random.randint(0, len(self.cards))
            card.append(self.cards[number])
            self.cards.pop(number)
            player.cards = player.cards + card

        else:
            print("No cards left in the desk")
       
    def add_two_cards(self, player):
        if len(self.cards) > 1:
            card = []
            number = random.randint(0, len(self.cards))
            card.append(self.cards[number])
            self.cards.pop(number)

            number = random.randint(0, len(self.cards))
            card.append(self.cards[number])
            self.cards.pop(number)

            player.cards = player.cards + card
        
        elif len(self.cards) == 1:
            card = []
            number = random.randint(0, len(self.cards))
            card.append(self.cards[number])
            self.cards.pop(number)
            player.cards = player.cards + card
        
        else:
            print("No cards left in the desk")

    #delete player card
    def delete_card_played(self, card, player):
        cards = player.cards.remove(card)

    def delete_one_card(self, player):
        if len(player.cards) > 0:
            while True:
                print("Choose the number card to delete:\n")
                for i in range(len(player.cards)):
                    print(i, player.cards[i])

                delete = Console.select()

                if delete < len(player.cards):
                    card = player.cards[delete]
                    player.cards.pop(delete)
                    return card
                else:
                    print("The number is invalid\n")
    
    def delete_two_cards(self,player):
        cards = []
        len_card = 0

        while True:
            print("Choose the number card to delete:\n")

            for i in range(len(player.cards)):
                print(i, player.cards[i])

            delete = Console.select()

            if delete < len(player.cards):
                cards.append(self.player.cards[delete])
                player.cards.pop(delete)
    
                len_card += 1
                if len_card == 2:
                    return cards
            else:
                print("The number is invalid\n\n")
        
    #Compare Card
    def compare_cards(self,player, card):
        count = player.cards.count(card)
        if count == 0:
            return False
        else:
            return True

    #len cards
    def len_cards(self, player):
        return len(player.cards)












    






