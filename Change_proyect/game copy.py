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

        
    

 
    
    @classmethod
    def Action(cls):  #actions

        if cls.action_played == "Income":  
            cls.players[cls.player_how_have_card].add_one_coin()
            cls.log.income(cls.players[cls.player_how_have_card].player)
        
        elif cls.action_played == "Foreign Aid":  
            cls.players[cls.player_how_have_card].add_two_coins(2)
            cls.log.foreign_aid(cls.players[cls.player_how_have_card].player)
        
        elif cls.action_played == "Coup":
            Console.pass_next_player(cls.players[cls.assassinate_or_steal].player)
            cls.players[cls.assassinate_or_steal].delete_one_card()
            cls.log.coup(cls.players[cls.player_how_have_card].player,
                         cls.players[cls.assassinate_or_steal].player)
              
        elif cls.action_played == "Duke":  #(tax)
            cls.players[cls.player_how_have_card].add_three_coins()
            cls.log.tax(cls.players[cls.player_how_have_card].player)
        
        elif cls.action_played == "Assassin":  # (assassinate)
            Console.pass_next_player(cls.players[cls.assassinate_or_steal].player)
            cls.players[cls.assassinate_or_steal].delete_one_card()
            cls.log.assassinate(cls.players[cls.player_how_have_card].player,
            cls.players[cls.assassinate_or_steal].player)
                
        elif cls.action_played == "Ambassador":  # (Exhange)
            cards = cls.card.randomCards()
            cls.players[cls.player_how_have_card].add_two_cards(cards)
            cards = cls.players[cls.player_how_have_card].delete_two_cards()
            cls.card.add_two_cards(cards)
            cls.log.exchange(cls.players[cls.player_how_have_card].player)
            
        elif cls.action_played == "Captain":  # (Steal)
            total_coins = cls.players[cls.ssassinate_or_steal].delete_two_coins()
            cls.players[cls.player_how_have_card].add_two_coins(total_coins)
            cls.log.steal(cls.players[cls.player_how_have_card].player,
                          cls.players[cls.assassinate_or_steal].player,
                          total_coins)

    @classmethod
    def Clean_values(cls):
        cls.player_how_have_card = None
        cls.other_player = None
        cls.action_played = None  
        cls.select_challenge = None  
        cls.select_counterattack = None
        cls.challenging_player = [] 
        cls.counterattack_player = []  
      
    @classmethod
    def Delete_player(cls): 
        delete = []
        for i in range(len(cls.players)):
            if cls.players[i].len_cards() == 0: #contar cartas
                delete.append(cls.players[i])
            else:
                continue

        if len(delete) > 0:
            for i in range(len(delete)):
                cls.losers.append(delete[i].player)
                cls.players.remove(delete[i])
                cls.NUMBER_Players -= 1
                cls.log.player_lost(delete[i].player)


    @classmethod
    def player_turn(cls):
        
        if cls.turn == cls.NUMBER_Players - 1:
            Console.clean()
            cls.log.print_log()
            Console.press_to_continue()
            cls.turn = 0

        elif len(cls.players)-1 < cls.NUMBER_Players-1:
            cls.turn -= 1

        else:
            cls.turn += 1
        
                  
if __name__ == "__main__":
    Game.play()
 
                
