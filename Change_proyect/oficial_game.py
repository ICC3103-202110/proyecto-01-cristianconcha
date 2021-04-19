from console import Console
from player import Player
from prints import Print
from cards import Cards
from action import Action
from challenge import Challenge
from log import Log

class Game:

    NUMBER_PLAYERS = None
    card = Cards()
    challenge = Challenge()
    counterattack = Counterattack()
    log = Log()

    players = []
    losers = []
    turn = 0


    @classmethod
    def play(cls):
        Print.wellcome()
        cls.number_of_players()
        cls.name_players()

        #Print.see_players_cards(cls.players)

        while True:
            Console.clean()
            Print.coins(cls.players)
            Print.len_cards(cls.players)
            Print.print_losers(cls.losers)
            Print.cards_lose(cls.card.cards_lose)

            log.turn(cls.turn)  # change
            action = Action(cls.players, cls.players[cls.turn], cls.log)
            action.select_action()

            select_challenge = challenge.select_challenge()
            select_counterattack = counterattack.select_counterattack()

            










            break
            



    @classmethod
    def number_of_players(cls):
        while True:
            number = Console.number_of_players()
            if number == 3 or number == 4:
                cls.NUMBER_PLAYERS= number
                break
            else:
                print("The game only accept 3 or 4 players")

    @classmethod
    def name_players(cls):
        """#change
        for i in range(1, cls.NUMBER_Players + 1):
            
            name = input("Give the player's %d name: " % i)
            cls.players.append(Player(name, cls.card.randomCards()))
        """
        cls.players.append(Player("Amelia", ["Contessa", "Duke"]))  # delete
        cls.players.append(Player("Bernabé", ["Captain", "Contessa"]))  # delete
        cls.players.append(Player("Carmen", ["Duke", "Assassin"]))  # delete

    
if __name__ == "__main__":
    Game.play()
