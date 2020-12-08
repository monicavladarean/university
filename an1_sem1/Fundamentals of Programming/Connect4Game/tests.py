import unittest
from Board import *

class Tests(unittest.TestCase):
    def __init__(self):
        self.board=Board()

    def Test_add_move(self):
        self.board.add_move("X",0)
        self.assertEqual(self.board[35],"X")
        self.board.add_move("X", 0)
        self.assertEqual(self.board[28], "X")

