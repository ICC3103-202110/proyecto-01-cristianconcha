from numpy import random
from player import Player
from cards import Cards
from console import Console
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
    def play(cls):
        Console.wellcome()
        cls.number_of_players()
        cls.name_players()
        #cls.see_player_cards()

        while True:
            Console.clean()
            
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
    @classmethod
    def number_of_players(cls):
        
        while True:
            number = Console.number_of_players()
            if number == 3 or number == 4:
                cls.NUMBER_Players = number
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
        cls.players.append(Player("Amelia", ["Contessa", "Duke"]))#delete
        cls.players.append(Player("Bernabé", ["Captain", "Contessa"]))#delete
        cls.players.append(Player("Carmen", ["Duke", "Assassin"]))#delete

    #Prints
    @classmethod 
    def print_Coins(cls):
        print("Coins    ", end="| ")
        for i in range(len(cls.players)):
            cls.players[i].printCoins()
        print("")
    
    @classmethod  # Delete
    def print_cards(cls):
        print("Cards:")
        for i in range(len(cls.players)):
            cls.players[i].printCard()
        
    @classmethod
    def print_losers(cls):
        print("Losers: ")
        for i in range(len(cls.losers)):
            Console.print_losers(cls.losers[i])
        print("")

    @classmethod
    def print_players_cards(cls):
        print("Influence", end="| ")
        for i in range(len(cls.players)):
            cls.players[i].print_len_cards()
        print("\n")
    
    @classmethod
    def see_player_cards(cls):
        Console.clean()
        for i in range(len(cls.players)):
            Console.pass_next_player_cards(cls.players[i].player)
            cls.players[i].printCard()
            Console.press_to_continue()

    #Print the players who can be affected
    @classmethod
    def Coup_choose(cls):
        while True:
            print("Choose the player to lose Influence \n")
            for i in range(len(cls.players)):
                if i == cls.player_how_have_card:
                    continue
                else:
                    print(i, cls.players[i].player)

            select = Console.select_player()
            if select != cls.turn and select < len(cls.players):
                return select
            else:
                Console.clean()
                print("The number is invalid\n")

        
    @classmethod 
    def Assassin_choose(cls): 
        print("Choose the player to lose Influence \n")

        for i in range(len(cls.players)):
            if i == cls.player_how_have_card:
                continue

            elif cls.players[i].len_cards() == 0:
                continue

            else:
                print(i, cls.players[i].player)
    
    @classmethod
    def Captain_choose(cls):
        while True:
            print("Choose the player to lose 2 coins \n")
            for i in range(len(cls.players)):
                if i == cls.player_how_have_card:
                    continue
                else:
                    print(i, " = ", cls.players[i].player, "have", cls.players[i].coin, "coins")

            select = Console.select_player()
            if select != cls.turn and select < len(cls.players):
                return select
            else:
                Console.clean()
                print("The number is invalid\n")

    #Actions
    @classmethod
    def Player_Accion(cls):
        cls.log.turn(cls.players[cls.turn].player)
        
        while True:
            cls.player_how_have_card = int(cls.turn)
            
            print("\nTurn: ",cls.turn) #delete ###########
            Console.player_turn(cls.players[cls.player_how_have_card].player)
            cls.print_Coins()
            cls.print_players_cards()
            cls.print_losers()
            cls.card.print_cards_lose()
            cls.print_cards()  #delete ##############
            print("")

            if cls.players[cls.player_how_have_card].coin >= 10:
                print("You have more than 10 coins, \nso you must use the coup action\n")
                Console.press_to_continue()
                cls.action_played = "Coup"
                cls.players[cls.player_how_have_card].pay_seven_coins()
                cls.log.more_coins(cls.players[cls.player_how_have_card].player)
                break
                
            else:
                print("Actions:\n")
                for i in range(len(cls.actions)):
                    print(i, "=" , cls.actions[i])

                cls.players[cls.player_how_have_card].printCard()
                action = Console.select_action()

                if action >= 0 and action < 7:
                    cls.action_played = str(cls.actions[action])
                    Console.clean()

                    if cls.action_played == "Coup" and cls.players[cls.player_how_have_card].coin < 7:
                        print("You don`t have 7 coins\n")

                    elif cls.action_played == "Assassin" and cls.players[cls.player_how_have_card].coin < 3:
                        print("You don`t have 3 coins\n")

                    else:
                        cls.log.action_selected(cls.action_played,
                        cls.players[cls.player_how_have_card].player,
                        cls.players[cls.assassinate_or_steal].player)

                        if cls.action_played == "Coup":
                            cls.players[cls.player_how_have_card].pay_seven_coins()
                            cls.assassinate_or_steal = cls.Coup_choose()
                            cls.log.pay_coup(cls.players[cls.player_how_have_card].player)
                            Console.clean()
                            Console.coup(cls.players[cls.player_how_have_card].player,
                                        cls.players[cls.assassinate_or_steal].player)
   
                        elif cls.action_played == "Assassin":
                            cls.players[cls.player_how_have_card].pay_three_coins()
                            cls.Assassin_choose()

                            cls.assassinate_or_steal = Console.select_player()

                            cls.log.pay_assassinate(cls.players[cls.player_how_have_card].player)
                            Console.clean()
                            Console.assassinate(cls.players[cls.player_how_have_card].player,
                                                cls.players[cls.assassinate_or_steal].player)

                        elif cls.action_played == "Captain":
                            cls.players[cls.player_how_have_card].pay_seven_coins()
                            cls.assassinate_or_steal = cls.Captain_choose()
                            
                            Console.clean()
                            Console.steal(cls.players[cls.player_how_have_card].player,
                                            cls.players[cls.assassinate_or_steal].player)
                        
                        break

                else:
                    Console.invalid_action()
        
    @classmethod
    def Select_Challenge(cls):

        if cls.action_played == "Income":
            Console.player_select(cls.players[cls.player_how_have_card].player, cls.action_played)
            Console.press_to_continue()
            
        elif cls.action_played == "Coup":
            Console.player_select(cls.players[cls.player_how_have_card].player, cls.action_played)
            Console.pass_next_player(cls.players[cls.player_how_have_card].player)
            
        elif cls.action_played == "Foreign Aid":
            pass
                    
        else:
            while True:
                Console.player_select(
                    cls.players[cls.player_how_have_card].player, cls.action_played)
                print("Some player wants to challenge: \n")
                
                print("\nPlayers:")
                for i in range(len(cls.players)):

                    if i == cls.player_how_have_card:
                        continue
                    else:
                        print("", i, "=", cls.players[i].player)
                
                select = Console.select_player_number()
                
                if select == "c":
                    break
                
                else:
                    cls.select_challenge = 1
                    cls.challenging_players.append(int(select))
    
    @classmethod
    def Select_Counterattack(cls):
        if cls.action_played == "Income":
            pass

        elif cls.action_played == "Coup":
            pass

        else:
            while True:
                Console.player_select(
                    cls.players[cls.player_how_have_card].player, cls.action_played)

                print("Some player wants to counterattack: \n")
                print("Players:")

                for i in range(len(cls.players)):
                    if i == cls.player_how_have_card:
                        continue
                    else:
                        print("", i, "=", cls.players[i].player)

                select = Console.select_player_number()

                if select == "c":
                    break
                else:
                    cls.select_counterattack = 2
                    cls.counterattack_players.append(int(select))
    
    @classmethod
    def challenge_counterattack_action(cls):
        if cls.select_challenge == 1 or cls.select_challenge == 3:
            #1 for challenge the first action and 3 for challenge the countterattack
            cls.select_the_challenging_player()
            cls.Challenge()

        elif cls.select_counterattack == 2:
            cls.select_the_counterattack_player()
            cls.Counterattack()

        else:
            cls.Action()

    @classmethod
    def Challenge(cls):
        true_or_false = cls.players[cls.player_how_have_card].compare_cards(cls.action_played)
        
        if true_or_false == False:  #Player turn Dont have the card
            print("The player %s dont`t have the card\n" % cls.players[cls.player_how_have_card].player)
            Console.pass_next_player(cls.players[cls.player_how_have_card].player)
            card_lose = cls.players[cls.player_how_have_card].delete_one_card()
            cls.card.card_lose(card_lose)
            cls.log.dont_have_card(cls.players[cls.player_how_have_card].player, cls.action_played)
            cls.log.player_lose_card(cls.players[cls.player_how_have_card].player, card_lose)


        elif true_or_false == True:  #Player turn Have the car
            
            print("The player %s" % cls.players[cls.player_how_have_card].player, 
            "have the %s" % cls.action_played)
            cls.log.have_card(cls.players[cls.player_how_have_card].player, cls.action_played)
            
            print("\nThe player %s lose one card" % cls.players[cls.other_player].player)
            Console.pass_next_player(cls.players[cls.other_player].player)

            card_lose = cls.players[cls.other_player].delete_one_card()
            cls.card.card_lose(card_lose)
            cls.log.player_lose_card(cls.players[cls.other_player].player, card_lose)
            Console.clean()
            
            print("The player %s change the card" % cls.players[cls.player_how_have_card].player)
            Console.pass_next_player(cls.players[cls.player_how_have_card].player)

            cls.players[cls.player_how_have_card].delete_card_played(cls.action_played)
            cls.card.add_card(cls.action_played)
            cls.log.change_card(cls.players[cls.player_how_have_card].player, cls.action_played)

            card = cls.card.One_random_Card() 
            cls.players[cls.player_how_have_card].add_one_card(card)

            if cls.select_challenge == 1:
                cls.Action()
            
            Console.press_to_continue()

    @classmethod
    def Counterattack(cls):
        Console.pass_next_player(cls.players[cls.player_how_have_card].player)

        if cls.action_played == "Foreign Aid":  
            select = Console.counterattack_foreign_aid()

        elif cls.action_played == "Captain":
            select = Console.counterattack_captain()

        elif cls.action_played == "Assassin":  
            select =Console.counterattack_assassin()
        
        cls.action_played = cls.actions[select]
        Console.clean()

        print(cls.players[cls.player_how_have_card].player, 
        "say that he have the %s\n" % cls.action_played)
        cls.log.said_that_have(cls.players[cls.player_how_have_card].player,  cls.action_played)
        Console.press_to_continue()

        cls.challenge_the_counterattack()
        
    @classmethod
    def challenge_the_counterattack(cls):
        cls.select_challenge = 0
        cls.challenging_players = []
        cls.Select_Challenge()

        if cls.select_challenge == 1:
            cls.select_challenge = 3 #challenge the counterattack
            cls.challenge_counterattack_action()

    @classmethod
    def select_the_challenging_player(cls):
        for i in range(len(cls.challenging_players)-1):
            number = random.randint(0, len(cls.challenging_players)-1)
            cls.challenging_players.pop(number)

        cls.other_player = int(cls.challenging_players[0])
        cls.log.challenge(cls.players[cls.other_player].player,
                          cls.players[cls.player_how_have_card].player)
        Console.clean()
        print("%s was selected to challenge\n" %cls.players[cls.other_player].player)

    @classmethod
    def select_the_counterattack_player(cls):
        for i in range(len(cls.counterattack_players)-1):
            number = random.randint(0, len(cls.counterattack_players)-1)
            cls.counterattack_player.pop(number)

        cls.player_how_have_card = int(cls.counterattack_players[0])
        cls.log.counterattack(cls.players[cls.player_how_have_card].player,
                          cls.players[cls.turn].player)
        Console.clean()
        print("%s was selected to Counterattack\n" %cls.players[cls.player_how_have_card].player)
    
    @classmethod
    def Action(cls):  #corroborate inputs numbers

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
 
                
