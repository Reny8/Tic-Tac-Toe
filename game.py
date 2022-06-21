
from player import Player
from board import Board
class Game:
    def __init__(self):
        self.x = Player('X')
        self.o = Player('O')
        self.board = Board()          
   
    def check_for_winner(self):
        # check whether a player has won or not 
        # X horizontal wins 
        if self.board.map[0][0] == 'X' and (self.board.map[0][1] == 'X' and self.board.map[0][2] == 'X'):
            print("Player 'X' has won the game!")
            self.x.player_wins = 1
        elif self.board.map[1][0] == 'X' and (self.board.map[1][1] == 'X' and self.board.map[1][2] == 'X'):
            print("Player 'X' has won the game!")
            self.x.player_wins = 1
        elif self.board.map[2][0] == 'X' and (self.board.map[2][1] == 'x' and self.board.map[2][2] == 'X'):
            print("Player 'X' has won the game!")
            self.x.player_wins = 1

        # O horizontal wins 
        if self.board.map[0][0] == 'O' and (self.board.map[0][1] == 'O' and self.board.map[0][2] == 'O'):
            print("Player 'O' has won the game!")
            self.o.player_wins = 1
        elif self.board.map[1][0] == 'O' and (self.board.map[1][1] == 'O' and self.board.map[1][2] == 'O'):
            print("Player 'O' has won the game!")
            self.o.player_wins = 1
        elif self.board.map[2][0] == 'O' and (self.board.map[2][1] == 'O' and self.board.map[2][2] == 'O'):
            print("Player 'O' has won the game!")
            self.o.player_wins = 1

        # X vertical wins 
        if self.board.map[0][0] == 'X' and (self.board.map[1][0] == 'X' and self.board.map[2][0] == 'X'):
            print("Player 'X' has won the game!")
            self.x.player_wins = 1
        elif self.board.map[0][1] == 'X' and (self.board.map[1][1] == 'X' and self.board.map[2][1] == 'X'):
            print("Player 'X' has won the game!")
            self.x.player_wins = 1
        elif self.board.map[0][2] == 'X' and (self.board.map[1][2] == 'X' and self.board.map[2][2] == 'X'):
            print("Player 'X' has won the game!")
            self.x.player_wins = 1

        # O vertical wins 
        if self.board.map[0][0] == 'O' and (self.board.map[1][0] == 'O' and self.board.map[2][0] == 'O'):
            print("Player 'O' has won the game!")
            self.o.player_wins = 1
        elif self.board.map[0][1] == 'O' and (self.board.map[1][1] == 'O' and self.board.map[2][1] == 'O'):
            print("Player 'O' has won the game!")
            self.o.player_wins = 1
        elif self.board.map[0][2] == 'O' and (self.board.map[1][2] == 'O' and self.board.map[2][2] == 'O'):
            print("Player 'O' has won the game!")
            self.o.player_wins = 1

        # X diagonal wins 
        if self.board.map[0][0] == 'X' and (self.board.map[1][1] == 'X' and self.board.map[2][2] == 'X'):
            print("Player X has won the game!")
            self.x.player_wins = 1
        if self.board.map[0][2] == 'X' and (self.board.map[1][1] == 'X' and self.board.map[2][2] == 'X'):
            print("Player 'X' has won the game!")
            self.x.player_wins = 1

        # O diagonal wins 
        if self.board.map[0][0] == 'O' and (self.board.map[1][1] == 'O' and self.board.map[2][2] == 'O'):
            print("Player O has won the game!")
            self.o.player_wins = 1
        if self.board.map[0][2] == 'O' and (self.board.map[1][1] == 'O' and self.board.map[2][2] == 'O'):
            print("Player 'O' has won the game!")
            self.o.player_wins = 1



    def battle(self):
        while self.x.player_wins == 0 and self.o.player_wins == 0:
            self.board.show_board()
            print()
            self.player_x_turn()
            print()
            if self.x.player_wins == 0:
                self.board.show_board()
                print()
                self.player_o_turn()
                
        

    def player_x_turn(self):
        print('Player X')
        row = self.x.row_chosen()
        block = self.x.block_chosen()
        self.board.map[row][block] = 'X'
        self.check_for_winner()
    
    def player_o_turn(self):
        print("PLAYER O")
        row = self.o.row_chosen()
        block = self.o.block_chosen()
        self.board.map[row][block] = 'O'
        self.check_for_winner()

    def display_welcome(self):
        print("Welcome TicTacToe")

    def run_game(self):
        self.display_welcome()
        self.battle()