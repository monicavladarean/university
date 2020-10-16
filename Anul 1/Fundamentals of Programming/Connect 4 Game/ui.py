from Game import *

class Ui:
    def __init__(self,game):
        self._game=game

    def read_move(self):
            column=input("Column for the move: ")
            column=int(column)
            if column<0 or column>6:
                raise ValueError
            return column

    def start(self):
        player_turn=True
        board=self._game.board()

        while board.won()==False and board.tie()==False:
            if player_turn==True:
                print(board)
                try:
                    column=self.read_move()
                    self._game.move_human(column)
                except ValueError:
                    print("Invalid input!")
                    continue

            else:
                self._game.move_computer()

            player_turn = not player_turn

        print("Gsme over!")
        print(board)

        if board.won()==True:
            if player_turn==False:
                print("You won!")
            else:
                print("You lost!")
        else:
            print("Tie!")