import random


class Player:
    def __init__(self, smart=False):
        if smart:
            self.get_moves = lambda x: [4] + random.sample([0, 1, 2, 3, 5, 6, 7, 8], k=8)
        else:
            self.get_moves = lambda x: random.sample(range(9), k=9)
