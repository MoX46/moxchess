import unittest
from game.gamepiece import GamePiece, Piece, Color, Square
from game.game import fen_to_pieces

class TestFenToPieces(unittest.TestCase):
    """Tests the fen_to_pieces function"""
    def test_valid_fen(self) -> None:
        """Tests random fen_to_piece with valid fen"""
        test_fen = '7q/2P1b3/6n1/1Q3B2/2N3k1/p3K3/8/6Rr w - - 0 1'
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
        output_list = fen_to_pieces(test_fen)
        self.assertCountEqual(expected_list,output_list)

if __name__ == '__main__':
    unittest.main()