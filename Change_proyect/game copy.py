from numpy import random
from cards import Cards
from log import Log
class Game:
 
    actions = ["Income", "Foreign Aid", "Coup", "Duke", "Assassin", "Ambassador", "Captain", "Contessa"]
    NUMBER_Players = None
    card = Cards()
    log = Log()
    
    players = []
    losers = []
    turn = 0

    player_how_have_card = None #number player
    other_player = None #number player

    action_played = None  #name card
    
    select_challenge = None  # counter attack or challenge
    select_counterattack = None

    challenging_players = []  # Player to challenge
    counterattack_players = []  #Player to counter attack
    
    assassinate_or_steal = 0 #number player who lost
    

    @classmethod
    def play(cls): ###
        



        while True:
            
            
            cls.Player_Accion()
            cls.Select_Challenge()
            cls.Select_Counterattack()

            cls.challenge_counterattack_action()

            cls.Delete_player()
            cls.Clean_values()
            cls.player_turn()

            if len(cls.players) == 1:
                break

        Console.winner(cls.players[0].player)
        
    #Create players
    #Prints    
    #Print the players who can be affected
    #Actions

                         
if __name__ == "__main__":
    Game.play()
 
                
