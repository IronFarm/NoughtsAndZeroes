import logging

from noughts.player import Player

logging.basicConfig(level=logging.INFO)


class InvalidMove(Exception):
    pass


class NoMoreMoves(Exception):
    pass


class Game:
    def __init__(self, players, current_player=0):
        self.board = [0] * 9
        self.players = players
        self.current_player = current_player

    def play(self):
        while True:
            try:
                winner = self.next_move()
                return winner
            except NoMoreMoves:
                continue

    def next_move(self):
        logging.debug('Player {}\'s move'.format(self.current_player + 1))
        player = self.players[self.current_player]

        for move in player.get_moves(self.board):
            try:
                logging.debug('Playing square {}'.format(move))
                self.make_move(move)
                self.print_board()
                game_over, winner = self.game_over()
                if game_over:
                    if winner:
                        logging.info('The winner is player {}!'.format(self.current_player + 1))
                    else:
                        logging.info('It\'s a tie!')
                    return winner

                break  # Valid move but no winner
            except InvalidMove:
                logging.debug('Bad move')
                continue

        self.current_player = 1 - self.current_player
        raise NoMoreMoves()

    def make_move(self, move):
        if self.board[move]:
            raise InvalidMove()
        else:
            self.board[move] = self.current_player + 1

    def game_over(self):
        for triplet in (
                [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
                [0, 3, 6], [1, 4, 7], [2, 4, 8],  # Columns
                [0, 4, 8], [2, 4, 6]  # Diagonals
        ):
            if self.winner(triplet):
                return True, self.winner(triplet)

        if self.board.count(0) == 0:
            return True, 0
        else:
            return False, 0

    def winner(self, triplet):
        if not (self.board[triplet[0]] and self.board[triplet[1]] and self.board[triplet[2]]):
            return 0

        if self.board[triplet[0]] == self.board[triplet[1]] and self.board[triplet[0]] == self.board[triplet[2]]:
            return self.board[triplet[0]]

    def print_board(self):
        logging.debug(
            '\n{}|{}|{}'
            '\n{}|{}|{}'
            '\n{}|{}|{}'.format(*self.board))


if __name__ == '__main__':
    results = {0: 0, 1: 0, 2: 0}

    for i in range(10000):
        game = Game([Player(True), Player()], i % 2)
        results[game.play()] += 1

    logging.info(results)
