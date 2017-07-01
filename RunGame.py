import TicTacToe


thisGame = TicTacToe()
while not thisGame.winner:
    thisGame.make_a_move()

