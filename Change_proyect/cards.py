from numpy import random
from player import Player
from console import Console

class Cards:
    def __init__(self, cards=0, cards_lose=0):
        self.cards = ["Duke", "Assassin", "Ambassador", "Captain", "Contessa",
                        "Duke", "Assassin", "Ambassador", "Captain", "Contessa",
                        "Duke", "Assassin", "Ambassador", "Captain", "Contessa"]
        self.cards_lose = []

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
        self.cards_lose.sort()
    

    #Add player card
    def add_one_card(self, player):
        card = []
        number = random.randint(0, len(self.cards))
        card.append(self.cards[number])
        self.cards.pop(number)

        player.cards += card
    
    def add_two_cards(self, player):
        card = []
        number = random.randint(0, len(self.cards))
        card.append(self.cards[number])
        self.cards.pop(number)

        number = random.randint(0, len(self.cards))
        card.append(self.cards[number])
        self.cards.pop(number)

        player.cards += card
        
    
    #delete player card
    def delete_card_played(self, card, player):
        player.cards = player.cards.remove(card)

    def delete_one_card(self, player):
        while True:
            print("Choose the number card to delete:\n")
            for i in range(len(player.cards)):
                print(i, player.cards[i])

            delete = Console.select()

            if delete < len(player.cards):
                card = player.cards[delete]
                player.cards = player.cards.pop(delete)
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

            if delete < len(self.cards):
                cards.append(self.cards[delete])
                player.cards = player.cards.pop(delete)
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












    






