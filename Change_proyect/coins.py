from player import Player

class Coins:

    
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
    
