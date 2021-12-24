import math
import random

class Player:

    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        square = random.choice(game.available_move())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(f"{self.letter} \'s Turn. Input move (0-9): ")
            
            try:
                val = int(square)
                if val not in game.available_move():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Ivalid square. Try again")

        return val