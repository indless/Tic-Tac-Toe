from IPython.display import clear_output
import random


class TicTacToe(object):
    def __init__(self):
        self.board = []
        self.board.append(['*', '1', '2', '3'])
        self.board.append(['1', ' ', ' ', ' '])
        self.board.append(['2', ' ', ' ', ' '])
        self.board.append(['3', ' ', ' ', ' '])

        self.mark = ' '
        self.player1mark = 'X'
        self.player2mark = 'O'
        self.playerSelectedMarker = ' '
        self.marker_choices = {'x': ('X', 'O'), 'o': ('O', 'X')}
        self.player = 0
        self.row = 0
        self.col = 0
        self.rowStr = ' '
        self.colStr = ' '
        self.move_counter = 0
        self.player1won = False
        self.player2won = False
        self.winner = False

        print('Welcome to Tic-Tac-Toe!')

    def show_board(self):
        clear_output()
        print(self.board[0])
        print(self.board[1])
        print(self.board[2])
        print(self.board[3])

    def board_is_blank(self):
        for r in range(1,4):
            for c in range(1,4):
                if self.board[r][c] != ' ':
                    return False
        return True

    def chose_player(self):
        return random.randint(0, 1)

    def chose_marker(self):
        self.playerSelectedMarker = ' '
        while not (self.playerSelectedMarker in 'X O'.lower().split()):
            self.playerSelectedMarker = \
                input('Player {x} was randomly chosen to go first! '
                      '\nWould you like to be X\'s or O\'s? (X/O) '.format(x=self.player+1)).lower()

    def set_marker(self):
        if self.player == 0:
            self.player1mark = self.marker_choices[self.playerSelectedMarker][0]
            self.player2mark = self.marker_choices[self.playerSelectedMarker][1]
        else:
            self.player2mark = self.marker_choices[self.playerSelectedMarker][0]
            self.player1mark = self.marker_choices[self.playerSelectedMarker][1]

    def make_a_move(self):
        if self.board_is_blank():
            self.show_board()
            self.player = self.chose_player()
            self.chose_marker()
            self.set_marker()
        self.get_player_move()
        self.mark_player_move()
        self.show_board()
        if self.is_game_over():
            self.game_is_over()

    def get_player_move(self):
        # determine player for turn
        if self.player == 0:
            print('Player 1\'s move!')
        else:
            print('Player 2\'s move!')
        # get row and col selection from user
        self.rowStr = ' '
        # while self.rowStr not in '1 2 3'.split():
        while not (self.rowStr == '1' or self.rowStr == '2' or self.rowStr == '3'):
            self.rowStr = input('What row would you like to choose for your move?: ')
        self.colStr = ' '
        while not (self.colStr == '1' or self.colStr == '2' or self.colStr == '3'):
            self.colStr = input('What column would you like to choose for your move?: ')
        # set row and col integers
        self.row = int(self.rowStr)
        self.col = int(self.colStr)
        # verify user selection is blank
        if self.board[self.row][self.col] != ' ' or (1 > self.row or self.row > 3) or (1 > self.col or self.col > 3):
            print('Invalid Move! That space is not available, please choose another space')
            self.get_player_move()

    def mark_player_move(self):
        if self.player == 0:
            self.mark = self.player1mark
            self.player = 1
        else:
            self.mark = self.player2mark
            self.player = 0
        self.board[self.row][self.col] = self.mark

    def is_game_over(self):
        # 3 in a row
        for r in range(1, 4):
            if self.board[r][1] == self.board[r][2] == self.board[r][3] != ' ':
                if self.board[r][1] == self.player1mark:
                    self.player1won = True
                else:
                    self.player2won = True
                self.winner = True
        # 3 in a column
        for c in range(1, 4):
            if self.board[1][c] == self.board[2][c] == self.board[3][c] != ' ':
                if self.board[1][c] == self.player1mark:
                    self.player1won = True
                else:
                    self.player2won = True
                self.winner = True
        # 3 diagonal
        if (self.board[1][1] == self.board[2][2] == self.board[3][3] != ' ') or (
                    self.board[1][3] == self.board[2][2] == self.board[3][1] != ' '):
            if self.board[2][2] == self.player1mark:
                self.player1won = True
            else:
                self.player2won = True
            self.winner = True
        # max moves reached
        self.move_counter += 1
        if self.move_counter >= 9 and not self.winner:
            self.game_is_tie()

        return self.winner

    def game_is_over(self):
        print('3 in a row! \nThe game is over')
        if self.player1won:
            print('Player 1 ({m}) wins!'.format(m=self.player1mark))
            self.player1won = False
        elif self.player2won:
            print('Player 2 ({m}) wins!'.format(m=self.player2mark))
            self.player2won = False
        self.play_again()

    def game_is_tie(self):
        print('It\'s a draw!')
        if not self.play_again():
            self.winner = True

    def play_again(self):
        if input('Play again? (yes/no) ').lower().startswith('y'):
            self.clear_board()
            self.move_counter = 0
            return True
        else:
            return False

    def clear_board(self):
            clear_output()
            self.board = []
            self.board.append(['*', '1', '2', '3'])
            self.board.append(['1', ' ', ' ', ' '])
            self.board.append(['2', ' ', ' ', ' '])
            self.board.append(['3', ' ', ' ', ' '])
            self.winner = False

thisGame = TicTacToe()
while not thisGame.winner:
    thisGame.make_a_move()
