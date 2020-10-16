from Board import *
from random import choice

class Game:
    def __init__(self):
        self._board=Board()

    def board(self):
        return self._board

    def move_human(self,column):
        '''makes the human's move, when is his turn'''
        self._board.add_move("X",column)

    def move_computer(self):
        '''makes a move, for the computer's turn'''
        columns=self._board.empty_place()
        self._board.add_move("Y",choice(columns))