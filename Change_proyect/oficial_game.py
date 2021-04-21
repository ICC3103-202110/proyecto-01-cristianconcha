from console import Console
from player import Player
from prints import Print
from cards import Cards
from total_actions import Total_actions #action,challenge and countterattack
from log import Log

class Game:

    NUMBER_PLAYERS = None

    players = []
    player_how_have_card = None
    card = Cards()
    log = Log()
    action_played = None

    losers = []
    turn = 0
    
    @classmethod
    def play(cls):
        Print.wellcome()
        cls.number_of_players()
        cls.name_players()

        #Print.see_players_cards(cls.players) #commit

        while True:
            Console.clean()
            Print.coins(cls.players)
            Print.len_cards(cls.players)
            Print.print_losers(cls.losers)
            Print.cards_lose(cls.card.cards_lose)
            Print.see_player_cards(cls.players) #change

            total_actions = Total_actions(cls.players, cls.players[cls.turn], cls.card, cls.log)
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
        
            cls.Delete_player()
            cls.player_turn()
            
            if len(cls.players) == 1:
                Print.winner(cls.players[0].player)
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
            cls.players.append(Player(name, cls.card.two_random_cards()))
        """
        cls.players.append(Player("Amelia", ["Contessa", "Duke"]))  # delete
        cls.players.append(Player("Bernabé", ["Captain", "Contessa"]))  # delete
        cls.players.append(Player("Carmen", ["Duke", "Assassin"]))  # delete

    @classmethod
    def Delete_player(cls):
        delete = []
        for i in range(len(cls.players)):
            if cls.card.len_cards(cls.players[i]) == 0:  
                delete.append(cls.players[i])
            else:
                continue

        if len(delete) > 0:
            for i in range(len(delete)):
                cls.losers.append(delete[i].player)
                cls.players.remove(delete[i])
                cls.NUMBER_PLAYERS -= 1
                cls.log.player_lost(delete[i].player)

    @classmethod
    def player_turn(cls):

        if cls.turn == cls.NUMBER_PLAYERS - 1:
            Console.clean()
            Print.log(cls.log.log)
            Console.press_to_continue()
            cls.turn = 0

        elif len(cls.players)-1 < cls.NUMBER_PLAYERS-1:
            cls.turn -= 1

        else:
            cls.turn += 1

    
if __name__ == "__main__":
    Game.play()
