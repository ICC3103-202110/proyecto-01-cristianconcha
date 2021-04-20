from player import Player

class Coins:

    #add
    @staticmethod
    def add_one_coin(player):
        player.coin += 1
    
    @staticmethod
    def add_two_coins(player):
        player.coin += 2

    @staticmethod
    def add_three_coins(player):
        player.coin += 3
    
    @staticmethod
    def add_coins(player, total_coins):
        player.coin += total_coins
    
    #delete
    @staticmethod
    def pay_three_coins(player):
        player.coin -= 3

    @staticmethod
    def pay_seven_coins(player):
        player.coin -= 7
    
    @staticmethod
    def select_the_coins_to_delete(player):
        total_coins = 0
        if player.coin == 1:
            player.coin -= 1
            total_coins += 1
            
        elif player.coin >= 2:
            player.coin -= 2
            total_coins += 2
        return total_coins
        
    

    
    

    
