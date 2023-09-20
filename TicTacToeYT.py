class TicTacToe:
    def __init__(self):
        self.board = ["-", "-", "-",
                      "-", "-", "-",
                      "-", "-", "-"]
        self.currentPlayer = "X"
        self.winner = None
        self.gameRunning = True

    def print_board(self):
        print(self.board[0] + " | " + self.board[1] + " | " + self.board[2])
        print("---------")
        print(self.board[3] + " | " + self.board[4] + " | " + self.board[5])
        print("---------")
        print(self.board[6] + " | " + self.board[7] + " | " + self.board[8])

    def player_input(self):
        inp = int(input("Select a spot 1-9: "))
        if self.board[inp - 1] == "-":
            self.board[inp - 1] = self.currentPlayer
        else:
            print("Oops, a player is already at that spot.")

    def check_horizontal(self):
        if self.board[0] == self.board[1] == self.board[2] and self.board[0] != "-":
            self.winner = self.board[0]
            return True
        elif self.board[3] == self.board[4] == self.board[5] and self.board[3] != "-":
            self.winner = self.board[3]
            return True
        elif self.board[6] == self.board[7] == self.board[8] and self.board[6] != "-":
            self.winner = self.board[6]
            return True
        return False

    def check_row(self):
        if self.board[0] == self.board[3] == self.board[6] and self.board[0] != "-":
            self.winner = self.board[0]
            return True
        elif self.board[1] == self.board[4] == self.board[7] and self.board[1] != "-":
            self.winner = self.board[1]
            return True
        elif self.board[2] == self.board[5] == self.board[8] and self.board[2] != "-":
            self.winner = self.board[2]
            return True
        return False

    def check_diag(self):
        if self.board[0] == self.board[4] == self.board[8] and self.board[0] != "-":
            self.winner = self.board[0]
            return True
        elif self.board[2] == self.board[4] == self.board[6] and self.board[4] != "-":
            self.winner = self.board[2]
            return True
        return False

    def check_if_win(self):
        if self.check_horizontal() or self.check_row() or self.check_diag():
            self.print_board()
            print(f"The winner is {self.winner}!")
            self.gameRunning = False
            exit()

    def check_if_tie(self):
        if "-" not in self.board:
            self.print_board()
            print("It's a tie!")
            self.gameRunning = False

    def switch_player(self):
        if self.currentPlayer == "X":
            self.currentPlayer = "O"
        else:
            self.currentPlayer = "X"

    def play_game(self):
        while self.gameRunning:
            self.print_board()
            self.player_input()
            self.check_if_win()
            self.check_if_tie()
            self.switch_player()
            self.check_if_win()
            self.check_if_tie()


if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
