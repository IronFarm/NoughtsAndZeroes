import random


class Player:
    def __init__(self):
        self.get_moves = lambda x: random.sample(range(9), k=9)
