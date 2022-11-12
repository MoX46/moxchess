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

Position = tuple[int,int]
Square = str

#columns = files (ABCDEFGH) , rows = ranks (123456789)
# A8 = 00, B8 = 01, C8 = 02...
# A7 = 10, B7 = 11, C7 = 12...

def position_to_square(grid:Position) -> Square:
    """ Converts (row,col) tuple to a chess square name (ex. (4,3) => D4) """
    return FILES[grid[1]] + str(8 - int(grid[0]))

def is_fen_valid(fen:str) -> bool:
    """Tests if fen string is valid. Returns True if valid False if invalid"""
    regex_string = '^((?:(?:[rnbqkpRNBQKP1-8]+\/){7})[rnbqkpRNBQKP1-8]+)\s([b|w])\s(-|[K|Q|k|q]{1,4})\s(-|[a-h][1-8])\s(\d+\s\d+)$'
    fen_parts = re.match(regex_string, fen)
    if not fen_parts:
        return False
    position = fen_parts[1].split('/')
    for rank in position:
        if re.match('[1-8]{2,}',rank):
            return False
        square_counter = 0
        for square in rank:
            if re.match('[1-8]',square):
                square_counter += int(square)
            else:
                square_counter += 1
        if square_counter != 8:
            return False
    return True


class GamePiece():
    """The Piece class represents a chess piece in the game"""
    def __init__(self, position:Position, piece_type:Piece = Piece.EMPTY, color:Color = Color.NONE):
        self.position = position
        self.type = piece_type
        self.color = color
        self.first_move = True
        self._hash = None

    def __str__(self) -> str:
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

    def move(self, position:Position) -> None:
        """Moves the piece to new position"""
        self.position = position
        self.first_move = False

    def get_legal_moves(self) -> list[str]:
        """Returns a list of all legal moves"""
        return []

def fen_to_pieces(fen:str) -> list[GamePiece]:
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
            break
        if c == '/':
            row = row + 1 # skip to next row
            continue
        if re.search('[0-9]',c):
            col = (col + int(c)) % 8 # skip columns when a number is present, loop back to 0 after 7
            continue
        piece, color = fen_entry_to_piece[c]
        piece_list.append(GamePiece((row,col),piece,color))
        col = (col + 1) % 8 # skip columns, loop back to 0 after 7
    return piece_list