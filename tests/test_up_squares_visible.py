import unittest
from game.game import squares_visible_to
from game.gamepiece import GamePiece, Piece, Color, Square

class TestSquaresVisibleTo(unittest.TestCase):
    """Tests the if up visible square are returned"""
    def setUp(self) -> None:
        self.white_pawn_c2 = GamePiece(Square.C2,Piece.PAWN,Color.WHITE)
        self.white_pawn_f4 = GamePiece(Square.F4,Piece.PAWN,Color.WHITE)
        self.white_pawn_a1 = GamePiece(Square.A8,Piece.PAWN,Color.WHITE)
        self.black_pawn_d7 = GamePiece(Square.D7,Piece.PAWN,Color.BLACK)
        self.black_pawn_e3 = GamePiece(Square.E3,Piece.PAWN,Color.BLACK)
        self.black_pawn_g8 = GamePiece(Square.G1,Piece.PAWN,Color.BLACK)

        self.queen_f6 = GamePiece(Square.F6,Piece.QUEEN,Color.BLACK)
        self.rook_c1 = GamePiece(Square.C1, Piece.ROOK, Color.WHITE)
        self.rook_h8 = GamePiece(Square.H8, Piece.ROOK, Color.BLACK)

    def test_pawn(self) -> None:
        self.assertCountEqual([Square.C4, Square.C3], squares_visible_to(self.white_pawn_c2))
        self.assertCountEqual([Square.F5], squares_visible_to(self.white_pawn_f4))
        self.assertCountEqual([], squares_visible_to(self.white_pawn_a1))
        self.assertCountEqual([Square.D6, Square.D5], squares_visible_to(self.black_pawn_d7))
        self.assertCountEqual([Square.E2], squares_visible_to(self.black_pawn_e3))
        self.assertCountEqual([], squares_visible_to(self.black_pawn_g8))

    def test_queen(self) -> None:
        self.assertCountEqual([
            Square.F7, Square.F8, Square.F5, Square.F4, Square.F3, Square.F2,
            Square.F1, Square.A6, Square.B6, Square.C6, Square.D6, Square.E6,
            Square.G6, Square.H6], squares_visible_to(self.queen_f6))

    def test_rook(self) -> None:
        self.assertCountEqual([
            Square.C2, Square.C3, Square.C4, Square.C5, Square.C6, Square.C7,
            Square.C8, Square.A1, Square.B1, Square.D1, Square.E1, Square.F1,
            Square.G1, Square.H1], squares_visible_to(self.rook_c1))
        self.assertCountEqual([
            Square.H7, Square.H6, Square.H5, Square.H4, Square.H3, Square.H2,
            Square.H1, Square.G8, Square.F8, Square.E8, Square.D8, Square.C8,
            Square.B8, Square.A8], squares_visible_to(self.rook_h8))
        