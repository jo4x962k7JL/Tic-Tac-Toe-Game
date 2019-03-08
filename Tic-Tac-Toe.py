# coding=utf-8
"""
2019.03.08
"""

from random import randrange

class TicTacToe():
    def new_board_gen(self):
        board = []
        board = [' '] * 9
        return board

    def show(self, board):
        print()
        print('0 | 1 | 2', ' ' * 10, board[0], '|', board[1], '|', board[2])
        print('---------', ' ' * 9, '-' * 11)
        print('3 | 4 | 5', ' ' * 10, board[3], '|', board[4], '|', board[5])
        print('---------', ' ' * 9, '-' * 11)
        print('6 | 7 | 8', ' ' * 10, board[6], '|', board[7], '|', board[8])
        print()

    def check_line(self, char, board, pos1, pos2, pos3):
        if board[pos1] == board[pos2] == board[pos3] == char:
            return True
        else:
            return False

    def check_all(self, char, board):
        if (self.check_line(char, board, 0, 1, 2) or
            self.check_line(char, board, 3, 4, 5) or
            self.check_line(char, board, 6, 7, 8) or
            self.check_line(char, board, 0, 3, 6) or
            self.check_line(char, board, 1, 4, 7) or
            self.check_line(char, board, 2, 5, 8) or
            self.check_line(char, board, 0, 4, 8) or
            self.check_line(char, board, 2, 4, 6)):
            return True
        else:
            return False

    def user_choose(self, board):
        while board.count('x') + board.count('o') < 9:
            user_input = int(input('You are "x", Select a spot(0~9): '))
            if board[user_input] not in ('x', 'o'):
                board[user_input] = 'x'
                break
            else:
                print('This spot is taken!')
        while board.count('x') + board.count('o') < 9:
            ai_choose = randrange(9)
            if board[ai_choose] not in ('x', 'o'):
                board[ai_choose] = 'o'
                break

if __name__ == '__main__':
    t1 = TicTacToe()
    board = t1.new_board_gen()
    t1.show(board)
    while board.count('x') + board.count('o') < 9:
        if not (t1.check_all('x', board) or t1.check_all('o', board)):
            t1.user_choose(board)
            t1.show(board)
        if t1.check_all('x', board):
            print('You Win!')
            break
        if t1.check_all('o', board):
            print('You Lose!')
            break
    if (board.count('x') + board.count('o') == 9 and
        not (t1.check_all('x', board) or t1.check_all('o', board))):
        print('No one wins!')
