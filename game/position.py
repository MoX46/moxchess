import re
from game.gamepiece import GamePiece, Piece, Color

def fen_to_pieces(fen:str) -> list[GamePiece]:
    """Converts a FEN string with a list of piece objects which can be added to the board object"""
    piece_list = []
    fen_entry_to_piece = {
        'r':(Piece.ROOK,Color.BLACK), 'n':(Piece.KNIGHT,Color.BLACK), 'b':(Piece.BISHOP,Color.BLACK),
        'q':(Piece.QUEEN,Color.BLACK), 'k':(Piece.KING,Color.BLACK), 'p':(Piece.PAWN,Color.BLACK),
        'R':(Piece.ROOK,Color.WHITE), 'N':(Piece.KNIGHT,Color.WHITE), 'B':(Piece.BISHOP,Color.WHITE),
        'Q':(Piece.QUEEN,Color.WHITE), 'K':(Piece.KING,Color.WHITE), 'P':(Piece.PAWN,Color.WHITE),
    }
    row, col = 0, 0
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

class Position():
    def __init__(self):
        raise NotImplementedError
