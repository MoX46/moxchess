import re
from math import ceil
from game.gamepiece import GamePiece, Piece, Color, Square

def chess_notation_to_square(cn_square:str) -> int:
    for s in Square:
        if s.name == cn_square:
            return s

def fen_to_game_info(fen:str) -> dict:
    return_value = {
        'side_to_move':Color.NONE,
        'castling_ability':{
            Color.WHITE:[],
            Color.BLACK:[]
        },
        'ep_square':Square.NONE,
        'halfmove_clock':int(),
        'fullmove_clock':int()
    }
    fen_array = fen.split(' ')
    side_to_move = fen_array[1]
    castling_ability = fen_array[2]
    ep_square = fen_array[3]
    halfmove_clock = fen_array[4]
    fullmove_clock = fen_array[5]

    if side_to_move == 'w':
        return_value['side_to_move'] = Color.WHITE    
    else:
        return_value['side_to_move'] = Color.BLACK

    if 'K' in castling_ability:
        return_value['castling_ability'][Color.WHITE].append(Square.H1)
    if 'Q' in castling_ability:
        return_value['castling_ability'][Color.WHITE].append(Square.A1)
    if 'k' in castling_ability:
        return_value['castling_ability'][Color.BLACK].append(Square.H8)
    if 'q' in castling_ability:
        return_value['castling_ability'][Color.BLACK].append(Square.A8)

    return_value['ep_square'] = chess_notation_to_square(ep_square.upper())

    return_value['halfmove_clock'] = int(halfmove_clock)
    return_value['fullmove_clock'] = int(fullmove_clock)

    return return_value

def fen_to_pieces(fen:str) -> list[GamePiece]:
    """Converts a FEN string with a list of piece objects which can be added to the board object"""
    piece_list = []
    fen_entry_to_piece = {
        'r':(Piece.ROOK,Color.BLACK), 'n':(Piece.KNIGHT,Color.BLACK),
        'b':(Piece.BISHOP,Color.BLACK), 'q':(Piece.QUEEN,Color.BLACK),
        'k':(Piece.KING,Color.BLACK), 'p':(Piece.PAWN,Color.BLACK),
        'R':(Piece.ROOK,Color.WHITE), 'N':(Piece.KNIGHT,Color.WHITE),
        'B':(Piece.BISHOP,Color.WHITE), 'Q':(Piece.QUEEN,Color.WHITE),
        'K':(Piece.KING,Color.WHITE), 'P':(Piece.PAWN,Color.WHITE)
    }

    counter = 0
    for c in fen:
        if c == ' ':
            break
        if c == '/':
            continue
        if re.search('[0-9]',c):
            counter += int(c)# skip columns when a number is present, loop back to 0 after 7
            continue
        counter += 1
        piece, color = fen_entry_to_piece[c]
        piece_list.append(GamePiece(Square(counter),piece,color))
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

def vertical_squares_visible_to(piece:GamePiece) -> list[Square]:
    visible_squares = []
    if piece.type == Piece.PAWN:
        initial_squares = []
        increment = 0
        if piece.color == Color.WHITE:
            initial_squares = [49,50,51,52,53,54,55,56]
            increment = -8
        if piece.color == Color.BLACK:
            initial_squares = [9,10,11,12,13,14,15,16]
            increment = 8
        if  piece.square.value in initial_squares:
            visible_squares.append(Square(piece.square.value + 2 * increment))
        if (piece.square.value + increment) > 0 and (piece.square.value + increment) <= 64:
            visible_squares.append(Square(piece.square.value + increment))

    if piece.type == Piece.ROOK or piece.type == Piece.QUEEN:
        increment = 8
        next_square = piece.square.value - increment
        while next_square > 0:
            visible_squares.append(Square(next_square))
            next_square -= increment
        next_square = piece.square.value + increment
        while next_square <= 64:
            visible_squares.append(Square(next_square))
            next_square += increment

    return visible_squares

def horizontal_squares_visible_to(piece:GamePiece) -> list[Square]:
    visible_squares = []
    increment = 1
    if piece.type == Piece.ROOK or piece.type == Piece.QUEEN:
        next_square = piece.square.value - increment
        while next_square > (8 * (ceil(piece.square.value/8) - 1)):
            visible_squares.append(Square(next_square))
            next_square -= increment
        next_square = piece.square.value + increment
        while next_square <= (8 * ceil(piece.square.value/8)):
            visible_squares.append(Square(next_square))
            next_square += increment
    
    return visible_squares

def squares_visible_to(piece:GamePiece) -> list[Square]:
    visible_squares = []
    visible_squares += vertical_squares_visible_to(piece) + horizontal_squares_visible_to(piece)
    return visible_squares

class Game():
    def __init__(self, fen:str = ''):
        if not isinstance(fen, str):
            raise TypeError('FEN should be a string')
        if not is_fen_valid(fen):
            raise ValueError('Invalid FEN')
        self.fen = fen
        self.pieces = fen_to_pieces(self.fen)
        self.turn = fen_to_game_info(fen)['side_to_move']
        self.castling_abilty = fen_to_game_info(fen)['castling_ability']
        self.ep_square = fen_to_game_info(fen)['ep_square']
        self.halfmove_clock = fen_to_game_info(fen)['halfmove_clock']
        self.fullmove_clock = fen_to_game_info(fen)['fullmove_clock']
        self._legal_moves = []


    

    
