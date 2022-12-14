from enum import Enum

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

class Square(Enum):
    A8 = 1
    B8 = 2
    C8 = 3
    D8 = 4
    E8 = 5
    F8 = 6
    G8 = 7
    H8 = 8
    A7 = 9
    B7 = 10
    C7 = 11
    D7 = 12
    E7 = 13
    F7 = 14
    G7 = 15
    H7 = 16
    A6 = 17
    B6 = 18
    C6 = 19
    D6 = 20
    E6 = 21
    F6 = 22
    G6 = 23
    H6 = 24
    A5 = 25
    B5 = 26
    C5 = 27
    D5 = 28
    E5 = 29
    F5 = 30
    G5 = 31
    H5 = 32
    A4 = 33
    B4 = 34
    C4 = 35
    D4 = 36
    E4 = 37
    F4 = 38
    G4 = 39
    H4 = 40
    A3 = 41
    B3 = 42
    C3 = 43
    D3 = 44
    E3 = 45
    F3 = 46
    G3 = 47
    H3 = 48
    A2 = 49
    B2 = 50
    C2 = 51
    D2 = 52
    E2 = 53
    F2 = 54
    G2 = 55
    H2 = 56
    A1 = 57
    B1 = 58
    C1 = 59
    D1 = 60
    E1 = 61
    F1 = 62
    G1 = 63
    H1 = 64
    NONE = None

