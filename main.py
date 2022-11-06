"""Main function of moxchess"""
from enum import Enum
import re

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

class GamePiece():
    """The Piece class represents a chess piece in the game"""
    def __init__(self, position:str, piece_type:Piece = Piece.EMPTY, color:Color = Color.NONE):
        self.position = position
        self.type = piece_type
        self.color = color
        self.first_move = True

    def __str__(self):
        if DEBUG:
            return f'I\'m a {self.color.value} {self.type.value}'

        if self.color == Color.WHITE:
            return UNICODE_PIECES[self.type][0]
        if self.color == Color.BLACK:
            return UNICODE_PIECES[self.type][1]
        if self.color == Color.NONE:
            return ''

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

def rank_file_to_grid(square:str) -> tuple[int,int]:
    """ Converts a chess square name to a (row,col) tuple (ex.E4 => (4,3)) """
    return (FILES.index(square[0]),RANKS.index(int(square[1]))) 

def grid_to_rank_file(index:tuple[int,int]) -> str:
    """ Converts (row,col) tuple to a chess square name (ex. (4,3) => E4) """
    return (FILES[index[0]] + str(RANKS[index[1]]))

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
    current_pieces = []
    fen_entry_to_piece = {
        'r':(PieceTypes.ROOK,Colors.BLACK),
        'n':(PieceTypes.KNIGHT,Colors.BLACK),
        'b':(PieceTypes.BISHOP,Colors.BLACK),
        'q':(PieceTypes.QUEEN,Colors.BLACK),
        'k':(PieceTypes.KING,Colors.BLACK),
        'p':(PieceTypes.PAWN,Colors.BLACK),
        'R':(PieceTypes.ROOK,Colors.WHITE),
        'N':(PieceTypes.KNIGHT,Colors.WHITE),
        'B':(PieceTypes.BISHOP,Colors.WHITE),
        'Q':(PieceTypes.QUEEN,Colors.WHITE),
        'K':(PieceTypes.KING,Colors.WHITE),
        'P':(PieceTypes.PAWN,Colors.WHITE),
    }
    rank_id = 7
    file_id = 0

    for i in fen:
        if i == ' ':
            break
        if i == '/':
            rank_id = (rank_id - 1) % 7 
            continue
        if re.search('[0-9]',i):
            file_id = (file_id + int(i)) % 8 
            continue
        file_id = (file_id + 1) % 8
        piece_type, color = fen_entry_to_piece[i]
        current_pieces.append(Piece(piece_type, color))
    for piece in current_pieces:
        print(piece.type, piece.color)

    return current_pieces

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
    white_queen = GamePiece('E4',Piece.QUEEN,Color.WHITE)
    pos = white_queen.get_position()
    idx = white_queen.get_index()
    white_queen.move('C6')
    new_pos = white_queen.get_position()
    new_idx = white_queen.get_index()
    print(f'Origiona position: {pos} | Original index: {idx}')
    print(f'New position: {new_pos} | New index: {new_idx}')
    print(white_queen)

if __name__ == "__main__":
    main()
