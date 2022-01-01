class TicTacToe:

    def __init__(self, starting_player="Human"):
        self.board = []
        self.current_player = starting_player
        self.human_symbol = "X"
        self.computer_symbol = "O"

    def __generate_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                col = "-"
                row.append(col)
            self.board.append(row)

    def __check_for_winner(self):
        # Check for horizontal winner
        for row in self.board:
            if row[0] != "-" and row[0] == row[1] and row[1] == row[2]:
                return self.__assign_winner(row[0])

        # Check for vertical winner
        for col in range(3):
            if self.board[0][col] != "-" and self.board[0][col] == self.board[1][col] == self.board[2][col]:
                return self.__assign_winner(self.board[0][col])
        # Check for diagonal winners
        if self.board[1][1] != "-" and self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
            return self.__assign_winner(self.board[1][1])
        if self.board[1][1] != "-" and self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.__assign_winner(self.board[1][1])
        return "None"

    def __is_board_filled(self):
        for row in self.board:
            for col in row:
                if col == "-":
                    return False
        return True

    def __assign_winner(self, winning_tile):
        if winning_tile == self.human_symbol:
            return "Human"
        elif winning_tile == self.computer_symbol:
            return "Computer"
        else:
            return "None"

    def __swap_current_player(self):
        if self.current_player == "Human":
            self.current_player = "Computer"
        elif self.current_player == "Computer":
            self.current_player = "Human"

    def __play_turn(self, position):
        # Adjust position to account for 0-based indexing
        position -= 1
        # Translate position into a row and column
        row = position // 3
        col = position - (3 * row)
        if self.current_player == "Human":
            self.board[row][col] = self.human_symbol
        elif self.current_player == "Computer":
            self.board[row][col] = self.computer_symbol
        self.__swap_current_player()

    def __print_board(self):
        for row in self.board:
            print(row, "\n")

    def start_game(self):
        game_result = "None"
        self.__generate_board()

        while self.__check_for_winner() == "None" and self.__is_board_filled() is False:
            position = int(input("Enter position value: "))
            self.__play_turn(position)
            self.__print_board()

        game_result = self.__check_for_winner()
        print("The winner is:", game_result)


if __name__ == '__main__':
    tictactoe = TicTacToe("Human")
    tictactoe.start_game()
