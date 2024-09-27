
class Game():
    
    def __init__(self):
        self.board = {1 : " ", 2 : " ", 3 : " ", 
                      4 : " ", 5 : " ", 6 : " ",
                      7 : " ", 8 : " ", 9 : " "}

    def display_board(self):
        print(self.board[1] + "_|_" + self.board[2] + "_|_" + self.board[3])
        print(self.board[4] + "_|_" + self.board[5] + "_|_" + self.board[6])
        print(self.board[7] + " | " + self.board[8] + " | " + self.board[9])

    def player_input(self, player):

        print(f"It's {player}'s turn")

        turn_over = False

        while(turn_over is False):

            number = input()

            if number != '1' and '2' and '3' and '4' and '5' and '6' and '7' and '8' and '9':
                print("Please enter a number")

            if self.board[int(number)] == ' ':
                self.board[int(number)] = player
                turn_over = True
            else:
                print("This position has been taken")
                print("Enter a different number")

    def check_winner(self, player):

        if self.board[1] == self.board[2] and self.board[1] == self.board[3] and self.board[1] == player:
            return True
        elif self.board[4] == self.board[5] and self.board[4] == self.board[6] and self.board[4] == player:
            return True
        elif self.board[7] == self.board[8] and self.board[7] == self.board[9] and self.board[7] == player:
            return True
        elif self.board[1] == self.board[4] and self.board[1] == self.board[7] and self.board[1] == player:
            return True
        elif self.board[2] == self.board[5] and self.board[2] == self.board[8] and self.board[2] == player:
            return True
        elif self.board[3] == self.board[6] and self.board[3] == self.board[9] and self.board[3] == player:
            return True
        elif self.board[1] == self.board[5] and self.board[1] == self.board[9] and self.board[1] == player:
            return True
        elif self.board[3] == self.board[5] and self.board[3] == self.board[7] and self.board[3] == player:
            return True
        
        return False

    def check_tie(self, turns):
   
        if turns == 9:
            return True
        else:
            return False


    def reset_board(self):
        
        for space in self.board:
            self.board[space] = ' '



game = Game()

turn = 0

def end_game():
    pass

while True:

    game.display_board()

    game.player_input('X')

    if game.check_winner('X'):
        print("X wins!")
        print("Would you like to play again?")
        print("Type y for yes or n for no")
        new_game = input()
        if new_game == 'y':
            print("New Game!")
            game.reset_board()
            continue
        else:
            break

    game.display_board()
    turn += 1

    if game.check_tie(turn):
        print("Draw!")
        print("Would you like to play again?")
        print("Type y for yes or n for no")
        new_game = input()
        if new_game == 'y':
            print("New Game!")
            game.reset_board()
            continue
        else:
            break

    print(f"Turns: {turn}")

    game.player_input('O')

    if game.check_winner('O'):
        print("O wins!")
        print("Would you like to play again?")
        print("Type y for yes or n for no")
        new_game = input()
        if new_game == 'y':
            print("New Game!")
            game.reset_board()
            continue
        else:
            break

    if game.check_tie(turn):
        print("Draw!")
        print("Would you like to play again?")
        print("Type y for yes or n for no")
        new_game = input()
        if new_game == 'y':
            print("New Game!")
            game.reset_board()
            continue
        else:
            break

    turn += 1
    print(f"Turns: {turn}")




print("Thanks for playing!")