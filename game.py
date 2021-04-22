from console import Console
from player import Player
from prints import Print
from cards import Cards
from total_actions import Total_actions #action,challenge and countterattack
from log import Log

class Game:

    NUMBER_PLAYERS = None

    __players = []
    __player_how_have_card = None
    __card = Cards()
    __log = Log()
    __action_played = None

    __losers = []
    __turn = 0
    
    @classmethod
    def play(cls):
        Print.wellcome()
        cls.__number_of_players()
        cls.__name_players()

        #Print.see_players_cards(cls.players) #commit

        while True:
            Console.clean()
            Print.coins(cls.__players)
            Print.len_cards(cls.__players)
            Print.print_losers(cls.__losers)
            Print.cards_lose(cls.__card.cards_lose)
            Print.see_player_cards(cls.__players) #change

            total_actions = Total_actions(cls.__players, cls.__players[cls.__turn], cls.__card, cls.__log, cls.__turn)
            total_actions.select_action()

            select_challenge = total_actions.select_challenge()
            select_counterattack = total_actions.select_counterattack()

            true_or_false_counter = True

            if select_challenge == 1:
                total_actions.select_the_challenging_player()
                true_or_false_counter = total_actions.start_challenge()
            
            if select_counterattack == 0 and true_or_false_counter == True:
                total_actions.run_action()
                
            
            elif select_counterattack == 2 and true_or_false_counter == True:
                total_actions.select_the_counterattack_player()
                total_actions.start_counterattack()
                select_challenge = total_actions.select_challenge()

                if select_challenge == 1:
                    total_actions.select_the_challenging_player()
                    true_or_false_counter = total_actions.start_challenge()

                    if true_or_false_counter == False:
                        total_actions.run_action()
                        
            else:
                total_actions.run_action()
        
            cls.__Delete_player()
            cls.__player_turn()
            
            if len(cls.__players) == 1:
                Print.winner(cls.__players[0].player)
                break
            

    @classmethod
    def __number_of_players(cls):
        while True:
            number = Console.number_of_players()
            if number == 3 or number == 4:
                cls.NUMBER_PLAYERS= number
                break
            else:
                print("The game only accept 3 or 4 players")

    @classmethod
    def __name_players(cls):
        """#change
        for i in range(1, cls.NUMBER_Players + 1):
            
            name = input("Give the player's %d name: " % i)
            cls.__players.append(Player(name, cls.__card.two_random_cards()))
        """
        cls.__players.append(Player("Amelia", ["Contessa", "Duke"]))  # delete
        cls.__players.append(Player("Bernabé", ["Captain", "Contessa"]))  # delete
        cls.__players.append(Player("Carmen", ["Duke", "Assassin"]))  # delete
        cls.__players.append(Player("Tomas", ["Captain", "Assassin"]))  # delete

    @classmethod
    def __Delete_player(cls):
        delete = []
        for i in range(len(cls.__players)):
            if cls.__card.len_cards(cls.__players[i]) == 0:  
                delete.append(cls.__players[i])
            else:
                continue

        if len(delete) > 0:
            for i in range(len(delete)):
                cls.__losers.append(delete[i].player)
                cls.__players.remove(delete[i])
                cls.NUMBER_PLAYERS -= 1
                cls.__log.player_lost(delete[i].player)

    @classmethod
    def __player_turn(cls):

        if cls.__turn == cls.NUMBER_PLAYERS - 1:
            Console.clean()
            Print.log(cls.__log.log)
            Console.press_to_continue()
            cls.__turn = 0

        elif len(cls.__players)-1 < cls.NUMBER_PLAYERS-1:
            cls.__turn -= 1

        else:
            cls.__turn += 1

    
if __name__ == "__main__":
    Game.play()
