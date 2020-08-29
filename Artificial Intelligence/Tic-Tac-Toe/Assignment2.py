#Name : Kartik Gupta
#PRN : 1032170673
#Subject : Artificial Intelligance
#Assignment 2
#Roll No. : PB-40

from time import time

class Game:
    def __init__(self):
        #initialized the empty tic tac toe board
        self.current_state = [
            ['.', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.']
        ]
        self.result = None
        self.player_turn = 'X'

    #this functions prints the current state of the board/game
    def print_board(self):
        for i in range(3):
            for j in range(3):
                print(self.current_state[i][j], end="\t")
            print(end="\n\n")

    def winner_is(self):
        #for loop returns player if any player won either horizontally or vertically
        for i in range(3):
            if self.current_state[i] == ['X', 'X', 'X']:
                return 'X'
            elif self.current_state[i] == ['O', 'O', 'O']:
                return 'O'
            elif self.current_state[0][i] != '.' and self.current_state[0][i] == self.current_state[1][i] == self.current_state[2][i]:
                return self.current_state[0][i]

        #this if condition returns the player if that player won diagonally
        if self.current_state[1][1] != '.':
            if self.current_state[0][0] == self.current_state[1][1] == self.current_state[2][2] or self.current_state[0][2] == self.current_state[1][1] == self.current_state[2][0]:
                return self.current_state[1][1]

        #this for loop returns None if game is not over yet (i.e if there are still empty places on board)
        for i in range(3):
            for j in range(3):
                if self.current_state[i][j] == '.':
                    return None

        #if no one wins and board is also full, then we return T for Tie
        return 'T'

    def max(self):
        max_value = -10
        move_x = None
        move_y = None

        winner = self.winner_is()
        if winner == 'X':
            return -10, 0, 0
        elif winner == 'O':
            return 10, 0, 0
        elif winner == 'T':
            return 0, 0, 0
        elif winner == None:
            for i in range(3):
                for j in range(3):
                    if self.current_state[i][j] == '.':
                        self.current_state[i][j] = 'O'
                        m, min_i, min_j = self.min()
                        if m > max_value:
                            max_value, move_x, move_y = m, i, j
                        self.current_state[i][j] = '.'
            return max_value, move_x, move_y

    def min(self):
        min_value = 10
        move_x = None
        move_y = None

        winner = self.winner_is()
        if winner == 'X':
            return -10, 0, 0
        elif winner == 'O':
            return 10, 0, 0
        elif winner == 'T':
            return 0, 0, 0
        elif winner == None:
            for i in range(3):
                for j in range(3):
                    if self.current_state[i][j] == '.':
                        self.current_state[i][j] = 'X'
                        m, max_i, max_j = self.max()
                        if m < min_value:
                            min_value, move_x, move_y = m, i, j
                        self.current_state[i][j] = '.'
            return min_value, move_x, move_y

    def play(self):
        while True:
            self.print_board()
            self.result = self.winner_is()
            if self.result != None:
                if self.result == 'T':
                    print('\n***  Game Tied ***\n')
                elif self.result == 'X':
                    print('\n***  You Won... :(  ***\n')
                elif self.result == 'O':
                    print('***  I won... Now you have to take me to park :)  ***')
                return

            if self.player_turn == 'X':
                start_time = time()
                m, move_x, move_y = self.min()
                print(f'Your Turn Hooman.. Don\'t boop\nRecommended move : X = {move_x}, Y = {move_y}\t(Calculated in {round(time()-start_time, 10)} seconds)')
                while True:
                    user_move_x = int(input('Enter X : '))
                    user_move_y = int(input('Enter y : '))
                    if self.current_state[user_move_x][user_move_y] == '.':
                        self.current_state[user_move_x][user_move_y] = 'X'
                        self.player_turn = 'O'
                        break
                    else:
                        print('Invalid Move... Use your eyes hooman')
            else:
                print('My turn now... let\'s think beep beep boop boop')
                m, move_x, move_y = self.max()
                self.current_state[move_x][move_y] = 'O'
                print(f'I put my O on ({move_x}, {move_y})')
                self.player_turn = 'X'
                
def main():
    print('\nhey... hey hooman... let\'s play tic tac toe...')
    print('You are X\n')
    game = Game()
    game.play()

main()


#Sample Input/Output


#hey... hey hooman... let's play tic tac toe...
#You are X
#
#.	.	.	
#
#.	.	.	
#
#.	.	.	
#
#Your Turn Hooman.. Don't boop
#Recommended move : X = 0, Y = 0	(Calculated in 5.0717909336 seconds)
#Enter X : 1
#Enter y : 1
#.	.	.	
#
#.	X	.	
#
#.	.	.	
#
#My turn now... let's think beep beep boop boop
#I put my O on (0, 0)
#O	.	.	
#
#.	X	.	
#
#.	.	.	
#
#Your Turn Hooman.. Don't boop
#Recommended move : X = 0, Y = 1	(Calculated in 0.0569653511 seconds)
#Enter X : 0
#Enter y : 2
#O	.	X	
#
#.	X	.	
#
#.	.	.	
#
#My turn now... let's think beep beep boop boop
#I put my O on (2, 0)
#O	.	X	
#
#.	X	.	
#
#O	.	.	
#
#Your Turn Hooman.. Don't boop
#Recommended move : X = 1, Y = 0	(Calculated in 0.0010316372 seconds)
#Enter X : 1
#Enter y : 0
#O	.	X	
#
#X	X	.	
#
#O	.	.	
#
#My turn now... let's think beep beep boop boop
#I put my O on (1, 2)
#O	.	X	
#
#X	X	O	
#
#O	.	.	
#
#Your Turn Hooman.. Don't boop
#Recommended move : X = 0, Y = 1	(Calculated in 0.0 seconds)
#Enter X : 0
#Enter y : 1
#O	X	X	
#
#X	X	O	
#
#O	.	.	
#
#My turn now... let's think beep beep boop boop
#I put my O on (2, 1)
#O	X	X	
#
#X	X	O	
#
#O	O	.	
#
#Your Turn Hooman.. Don't boop
#Recommended move : X = 2, Y = 2	(Calculated in 0.0 seconds)
#Enter X : 2
#Enter y : 2
#O	X	X	
#
#X	X	O	
#
#O	O	X	
#
#
#***  Game Tied ***
