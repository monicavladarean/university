from texttable import Texttable

class Board:
    def __init__(self):
        self._board=[" "]*42

    def __str__(self):
        table=Texttable()
        for i in range(6):
            row=self._board[7*i:7*i+7]
            table.add_row(row)
        return table.draw()

    def empty_place(self):
        columns=[]
        for column in range(6):
            times=7
            while times<=35 and times >=0:
                if self._board[times+column]==" ":
                    columns.append(column)
                    break
                times-=7
        return columns

    def add_move(self,symbol, column):
        '''adds a move on the board (X for the player, Y for the computer)'''
        if self._board[column]!=" ":
            raise ValueError("Full column!")
        times=7*5
        while self._board[times+column]!=" ":
            times=times-7
        self._board[times+column]=symbol

    def won(self):
        '''marks if the game is won by somebody, or not'''
        board=self._board

        for i in range(6):
            if board[i]==board[i+7]==board[i+14]==board[i+21]!=" ":
                return True
            if board[i+7]==board[i+14]==board[i+21]==board[i+28]!=" ":
                return True
            if board[i+14]==board[i+21]==board[i+28]==board[i+35]!=" ":
                return  True

        for i in [0,7,14,21,28,35]:
            if board[i]==board[i+1]==board[i+2]==board[i+3]!=" ":
                return True
            if board[i+1]==board[i+2]==board[i+3]==board[i+4]!=" ":
                return True
            if board[i+2]==board[i+3]==board[i+4]==board[i+5]!=" ":
                return  True
            if board[i+3]==board[i+4]==board[i+5]==board[i+6]!=" ":
                return  True

        for i in [3,4,5,6,13,20]:
            if board[i]==board[i+6]==board[i+12]==board[i+18]!=" ":
                return True

        for i in [4,5,6,13]:
            if board[i+6]==board[i+12]==board[i+18]==board[i+24]!=" ":
                return True

        for i in [5,6]:
            if board[i+12]==board[i+18]==board[i+24]==board[i+30]!=" ":
                return True

        for i in [0 , 1 , 2 , 3 , 7 , 14]:
            if board[i] == board[i + 8] == board[i + 16] == board[i + 24] != " ":
                return True

        for i in [0,1,2,7]:
            if board[i + 8] == board[i + 16] == board[i + 24] == board[i + 32] != " ":
                return True

        for i in [0,1]:
            if board[i + 16] == board[i + 24] == board[i + 32] == board[i + 40] != " ":
                return True

        return False

    def tie(self):
        '''marks if the game is finished with a tie, or not'''
        if self.won()==False and len(self.empty_place())==0:
            return True
        return False