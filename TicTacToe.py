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
        square = random.choice(game.available_moves())
        return square
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(f'Giliran {self.letter}. Masukkan nomor kotak (0-8): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Input tidak valid. Coba Lagi.')
        return val
class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + '  | '.join(row) + ' |')
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    def empty_squares(self):
        return ' ' in self.board
    def num_empty_squares(self):
        return self.board.count(' ')
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    def winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in column]):
            return True
        col_ind = square % 3
        column = [self.board[i][col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        if square % 2 == 0:
           diagonal1 = [self.board[i] for i in [0, 4, 8]]
           if all([spot == letter for spot in diagonal1]):
              return True
           diagonal2 = [self.board[i] for i in [2, 4, 6]]
           if all([spot == letter for spot in diagonal]):
              return True
        return False
def play(game, player1, player2, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'x'
    while game