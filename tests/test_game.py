import unittest
from game.game import Game
from game.gamepiece import GamePiece, Piece, Color, Square

class TestGamePiece(unittest.TestCase):
    """Tests the game piece class """
    def setUp(self) -> None:
        self.game1 = Game('7q/2P1b3/6n1/1Q3B2/2N3k1/p3K3/8/6Rr w K e3 0 1')
        self.game2 = Game('2n2b2/r1pK4/P2P1P2/q7/4pNB1/1bk5/5p2/7N b Qq c6 0 1')

    def test_pieces(self) -> None:
        """Tests piece identity method"""
        expected_list = [
            GamePiece(Square.H8,Piece.QUEEN,Color.BLACK),
            GamePiece(Square.C7,Piece.PAWN,Color.WHITE),
            GamePiece(Square.E7,Piece.BISHOP,Color.BLACK),
            GamePiece(Square.G6,Piece.KNIGHT,Color.BLACK),
            GamePiece(Square.B5,Piece.QUEEN,Color.WHITE),
            GamePiece(Square.F5,Piece.BISHOP,Color.WHITE),
            GamePiece(Square.C4,Piece.KNIGHT,Color.WHITE),
            GamePiece(Square.G4,Piece.KING,Color.BLACK),
            GamePiece(Square.A3,Piece.PAWN,Color.BLACK),
            GamePiece(Square.E3,Piece.KING,Color.WHITE),
            GamePiece(Square.G1,Piece.ROOK,Color.WHITE),
            GamePiece(Square.H1,Piece.ROOK,Color.BLACK)
        ]
        self.assertEqual(expected_list,self.game1.pieces)

    def test_turn(self) -> None:
        """Test if game returns correct turn"""
        self.assertEqual(Color.WHITE,self.game1.turn)
        self.assertEqual(Color.BLACK,self.game2.turn)

    def test_castling_ability(self) -> None:
        """Tests if game returns correct casttling rights"""
        self.assertIn(Square.H1, self.game1.castling_abilty[Color.WHITE])
        self.assertIn(Square.A1, self.game2.castling_abilty[Color.WHITE])
        self.assertIn(Square.A8, self.game2.castling_abilty[Color.BLACK])


    def test_ep_square(self) -> None:
        """Test if game returns correct en passant squarer"""
        self.assertEqual(Square.E3,self.game1.ep_square)
        self.assertEqual(Square.C6,self.game2.ep_square)


if __name__ == '__main__':
    unittest.main()