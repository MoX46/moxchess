import unittest
from game.game import squares_visible_to
from game.gamepiece import GamePiece, Piece, Color, Square

class TestSquaresVisibleTo(unittest.TestCase):
    """Tests the if up visible square are returned"""
    def setUp(self) -> None:
        self.white_pawn_c2 = GamePiece(Square.C2,Piece.PAWN,Color.WHITE)
        self.white_pawn_f4 = GamePiece(Square.F4,Piece.PAWN,Color.WHITE)
        self.white_pawn_a1 = GamePiece(Square.A1,Piece.PAWN,Color.WHITE)
        self.black_pawn_d7 = GamePiece(Square.D7,Piece.PAWN,Color.BLACK)
        self.black_pawn_e3 = GamePiece(Square.E3,Piece.PAWN,Color.BLACK)
        self.black_pawn_g8 = GamePiece(Square.G8,Piece.PAWN,Color.BLACK)
        self.queen = GamePiece(Square.F6,Piece.QUEEN,Color.BLACK)

    def test_up_square(self) -> None:
        self.assertCountEqual([Square.C4, Square.C3], squares_visible_to(self.white_pawn_c2)) 
