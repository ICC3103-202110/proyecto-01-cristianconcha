from numpy import random

class Cards:
    def __init__(self, cards=0, cards_lose=0):
        self.cards = ["Duke", "Assassin", "Ambassador", "Captain", "Contessa",
                        "Duke", "Assassin", "Ambassador", "Captain", "Contessa",
                        "Duke", "Assassin", "Ambassador", "Captain", "Contessa"]
        self.cards_lose = []


    def randomCards(self):
        card = []
        number = random.randint(0, len(self.cards))
        card.append(self.cards[number])
        self.cards.pop(number)

        number = random.randint(0, len(self.cards))
        card.append(self.cards[number])
        self.cards.pop(number)
        return card
    
    def One_random_Card(self):
        card = []
        number = random.randint(0, len(self.cards))
        card.append(self.cards[number])
        self.cards.pop(number)
        return card

    def add_card(self, card):
        self.cards.append(card)
    
    def add_two_cards(self, card):
        self.cards += card
        
    def card_lose(self, card):
        self.cards_lose.append(card)

    def print_cards_lose(self):
        print("Lost Cards:")
        self.cards_lose.sort()
        for i in range(len(self.cards_lose)):
            print(self.cards_lose[i], end=", ")
        print("\n")



    






