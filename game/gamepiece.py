from enum import Enum
from typing_extensions import Self

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

FILES = ['A','B','C','D','E','F','G','H']

Coordinates = tuple[int,int]
Square = str

def position_to_square(grid:Coordinates) -> Square:
    """ Converts (row,col) tuple to a chess square name (ex. (4,3) => D4) """
    return FILES[grid[1]] + str(8 - int(grid[0]))

class GamePiece():
    """The Piece class represents a chess piece in the game"""
    def __init__(self, position:Coordinates, piece_type:Piece = Piece.EMPTY, color:Color = Color.NONE):
        self.position = position
        self.type = piece_type
        self.color = color
        self.first_move = True
        self._hash = None

    def __str__(self) -> str:
        return self.identity

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
        return f'I\'m a {self.color.value} {self.type.value} on {position_to_square(self.position)}'

    def move(self, position:Coordinates) -> None:
        """Moves the piece to new position"""
        self.position = position
        self.first_move = False

    def get_legal_moves(self) -> list[str]:
        """Returns a list of all legal moves"""
        return []