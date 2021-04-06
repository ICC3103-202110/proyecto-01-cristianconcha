from numpy import random

class Cards:
    def __init__(self, cards=0):
        self.cards = ["Duke", "Assassin", "Ambassador", "Captain", "Contessa",
                        "Duke", "Assassin", "Ambassador", "Captain", "Contessa",
                        "Duke", "Assassin", "Ambassador", "Captain", "Contessa"]


    def randomCards(self):
        card = []
    
        number = random.randint(0, len(self.cards))
        card.append(self.cards[number])
        self.cards.pop(number)

        number = random.randint(0, len(self.cards))
        card.append(self.cards[number])
        self.cards.pop(number)
        return card


    def printCard(self):
        #Imprimir las cartas al jugador
        pass

    def deleteCard(self):
        #eliminar carta
        pass




