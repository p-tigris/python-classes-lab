class Game():
    wins_X = 0
    wins_O = 0

    def __init__(self, turn='X', tie=False, winner=None, play=True):
        self.turn = turn
        self.tie = tie
        self.winner = winner
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }
        self.play = play

    def play_game(self):
        print("Welcome to Tic-Tac-Toe!")
        while self.play:
            self.render()
            if not self.winner and not self.tie:
                self.get_move()
                self.check_for_winner()
                self.check_for_tie()
                self.switch_turn()
            else:
                self.check_score()
                self.play_again()

    def play_again(self):
        play_again = input("Would you like to play again? (y/n) ").lower()

        if play_again == 'y':
            self.play = True
            self.turn = 'X'
            self.winner = None
            self.tie = False
            for key in self.board.keys():
                self.board[key] = None
        else:
            self.play = False

    def check_score(self):
        if self.winner == 'X':
            Game.wins_X += 1
        elif self.winner == 'O':
            Game.wins_O += 1

        print(f"Wins for X: {Game.wins_X}, Wins for O: {Game.wins_O}")
    
    def print_board(self):
        b = self.board
        print(f"""
                A   B   C
            1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
                ----------
            2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
                ----------
            3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)

    def print_message(self):
        if self.tie:
            print("Tie game!")
        elif self.winner:
            print(f"{self.winner} wins the game!")
        else:
            print(f"It's player {self.turn}'s turn!")

    def render(self):
        self.print_board()
        self.print_message()

    def get_move(self):
        while True:
            move = input(f"Enter a valid move (example: A1): ").lower()
            if move in self.board.keys() and not self.board[move]:
                self.board[move] = self.turn
                break
            else:
                print("Invalid input")

    def check_for_winner(self):
        if ((self.board['a1'] and (self.board['a1'] == self.board['b1'] == self.board['c1'])) or
           (self.board['a2'] and (self.board['a2'] == self.board['b2'] == self.board['c2'])) or
           (self.board['a3'] and (self.board['a3'] == self.board['b3'] == self.board['c3'])) or
           (self.board['a1'] and (self.board['a1'] == self.board['a2'] == self.board['a3'])) or
           (self.board['b1'] and (self.board['b1'] == self.board['b2'] == self.board['b3'])) or
           (self.board['c1'] and (self.board['c1'] == self.board['c2'] == self.board['c3'])) or
           (self.board['a1'] and (self.board['a1'] == self.board['b2'] == self.board['c3'])) or
           (self.board['a3'] and (self.board['a3'] == self.board['b2'] == self.board['c1']))):
           self.winner = self.turn

    def check_for_tie(self):
        if None not in self.board.values() and not self.winner:
            self.tie = True

    def switch_turn(self):
        if self.turn == 'X':
            self.turn = 'O'
        elif self.turn == 'O':
            self.turn = 'X'


game_instance = Game()
game_instance.play_game()