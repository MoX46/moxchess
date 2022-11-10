"""Main function of moxchess"""
from enum import Enum
import re
from typing_extensions import Self

DEBUG = True
STARTING_FEN_STRING = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
RANKS = [1,2,3,4,5,6,7,8]
FILES = ['A','B','C','D','E','F','G','H']

class Piece(Enum):
    """Enumerated piece type. Usage: PieceTypes.KING, PieceTypes.QUEEN"""
    KING = 'king'
    QUEEN = 'queen'
    ROOK = 'rook'
    BISHOP = 'bishop'
    KNIGHT = 'knight'
    PAWN = 'pawn'
    EMPTY = ''

class Color(Enum):
    """Enumerated colors. Usage. Colors.BLACK, Colors.WHITE"""
    BLACK = 'black'
    WHITE = 'white'
    NONE = ''

UNICODE_PIECES = {
    Piece.KING: ('♔', '♚'),
    Piece.QUEEN: ('♕','♛'),
    Piece.ROOK: ('♖','♜'),
    Piece.BISHOP: ('♗','♝'),
    Piece.KNIGHT: ('♘','♞'),
    Piece.PAWN: ('♙','♟︎')
}

#columns = files (ABCDEFGH) , rows = ranks (123456789)
# A8 = 00, B8 = 01, C8 = 02...
# A7 = 10, B7 = 11, C7 = 12...

def rank_file_to_grid(square:str) -> tuple[int,int]:
    """ Converts a chess square name to a (row,col) tuple (ex. A8 => (0,0)) """
    return(abs(int(square[1]) - 8), FILES.index(square[0]))

def grid_to_rank_file(grid:tuple[int,int]) -> str:
    """ Converts (row,col) tuple to a chess square name (ex. (4,3) => D4) """
    return FILES[grid[1]] + str(8 - int(grid[0])) 

class GamePiece():
    """The Piece class represents a chess piece in the game"""
    def __init__(self, position:str, piece_type:Piece = Piece.EMPTY, color:Color = Color.NONE):
        self.position = position
        self.type = piece_type
        self.color = color
        self.first_move = True
        self._hash = None

    def __str__(self):
        if DEBUG:
            return f'I\'m a {self.color.value} {self.type.value}'
        if self.color == Color.WHITE:
            return UNICODE_PIECES[self.type][0]
        if self.color == Color.BLACK:
            return UNICODE_PIECES[self.type][1]
        if self.color == Color.NONE:
            return ''

    def __eq__(self, other:Self) -> bool:
        if (self.position == other.position and
            self.type == other.type and 
            self.color == other.color):
            return True
        return False

    def __hash__(self) -> int:
        return hash(self.identity)

    @property
    def identity(self) -> str:
        """Returns a string which identifies the piece (ex. I'm a white rook)"""
        return f'I\'m a {self.color.value} {self.type.value}'

    def move(self, position:str) -> None:
        """Moves the piece to new position"""
        self.position = position
        self.first_move = False

    def get_position(self) -> str:
        """Returns the position of the piece"""
        return self.position

    def get_index(self) -> tuple[int,int]:
        """Returns the index of the piece"""
        return rank_file_to_grid(self.position)

    def get_legal_moves(self) -> list[str]:
        """Returns a list of all legal moves"""
        return []

class Board():
    """The Board class represents a chess board"""
    def __init__(self,size = 8):
        self.board = []
        self.size = size
        for i in range(size):
            for j in range(size):
                square = str(FILES[i])+str(RANKS[j])
                self.place_piece(Piece(),square)
    
    def place_piece(self,piece:Piece,square:str):
        """"Places a piece on the board"""
        row, col = square_to_index(square)
        self.board[row][col] = piece

    def __str__(self):
        board_string = ''
        for i in range(self.size):
            for j in range(self.size):
                print(board[i][j])
                

def fen_to_pieces(fen:str) -> list:
    """Converts a FEN string with a list of piece objects which can be added to the board object"""
    piece_list = []
    fen_entry_to_piece = {
        'r':(Piece.ROOK,Color.BLACK),
        'n':(Piece.KNIGHT,Color.BLACK),
        'b':(Piece.BISHOP,Color.BLACK),
        'q':(Piece.QUEEN,Color.BLACK),
        'k':(Piece.KING,Color.BLACK),
        'p':(Piece.PAWN,Color.BLACK),
        'R':(Piece.ROOK,Color.WHITE),
        'N':(Piece.KNIGHT,Color.WHITE),
        'B':(Piece.BISHOP,Color.WHITE),
        'Q':(Piece.QUEEN,Color.WHITE),
        'K':(Piece.KING,Color.WHITE),
        'P':(Piece.PAWN,Color.WHITE),
    }
    row = 0
    col = 0
    for c in fen:
        if c == ' ':
            return piece_list
        if c == '/':
            row = row + 1 # skip to next row
            continue
        if re.search('[0-9]',c):
            col = (col + int(c)) % 8 # skip columns when a number is present, loop back to 0 after 7
            continue

        piece, color = fen_entry_to_piece[c]
        pos = grid_to_rank_file((row,col))
        piece_list.append(GamePiece(pos,piece,color))
        col = (col + 1) % 8 # skip columns, loop back to 0 after 7


class Game():
    """The Game class holds the board, the pieces, and all the game states"""
    def __init__(self,processor = fen_to_pieces, data = STARTING_FEN_STRING):
        self.board = Board()
        self.pieces = processor(data)
        for piece in self.pieces:
            self.board.place_piece(piece,square)
        self.move = 0

def fen_to_game(fen:str):
    """Returns a board game object which includes a Board and all the Pieces from a fen string"""
    print('hello')

def main():
    print('Welcome to MoxChess!')

if __name__ == "__main__":
    main()
