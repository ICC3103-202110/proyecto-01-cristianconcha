from numpy import random

class Cards:
    def __init__(self, cards=0):
        self.cards = ["Duke", "Assassin", "Ambassador", "Captain", "Contessa",
                        "Duke", "Assassin", "Ambassador", "Captain", "Contessa",
                        "Duke", "Assassin", "Ambassador", "Captain", "Contessa"]


    def randomCards(self):
        card = []
        card.append(random.randint(0, len(self.cards)))
        self.cards.pop(card[0])
        card.append(random.randint(0, len(self.cards)))
        self.cards.pop(card[1])
        return card


    def printCard(self):
        #Imprimir las cartas al jugador
        pass

    def deleteCard(self):
        #eliminar carta
        pass



card = Cards()
card.randomCards()
