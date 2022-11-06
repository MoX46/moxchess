from enum import Enum, auto

# reset board 
# board from FEN
# get all valid moves
# get piece valid moves
# history of all moves
# castling rights (black/white, king/queensid)

class PieceTypes(Enum):
    KING = auto()
    QUEEN = auto()
    ROOK = auto()
    BISHOP = auto()
    KNIGHT = auto()
    PAWN = auto()

class Colors(Enum):
    BLACK = auto()
    WHITE = auto()

def square_to_index(square:str):
    letters = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7}
    i = letters[square[0]]



class Board():
    def new_board(self,size: int):
        self.board = [[],[],[],[],[],[],[],[]]

class Piece():
    def __init__(self, type:PieceTypes, color:Colors):
        self.type = type
        self.color = color
        self.first_move = True