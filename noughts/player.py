import random

import numpy as np
from sklearn.neural_network import MLPRegressor


class Player:
    def __init__(self, smart=False, seed=None):
        if seed:
            self.nn = MLPRegressor(hidden_layer_sizes=(9, 9), random_state=seed)
            self.nn.partial_fit([[0] * 9], [[0] * 9])  # Dummy fit
            self.get_moves = lambda x: np.flip(np.argsort(self.nn.predict([x]))[0], 0)
        elif smart:
            self.get_moves = lambda x: [4] + random.sample([0, 1, 2, 3, 5, 6, 7, 8], k=8)
        else:
            self.get_moves = lambda x: random.sample(range(9), k=9)

if __name__ == '__main__':
    player = Player(seed=11)
    for i in range(100):
        print(player.get_moves([
            0, 1, 1,
            2, 1, 2,
            0, 0, 0
        ]))
