import unittest
from game.gamepiece import GamePiece, Piece, Color
from game.position import fen_to_pieces

class TestFenToPieces(unittest.TestCase):
    """Tests the fen_to_pieces function"""
    def test_valid_fen(self) -> None:
        """Tests random fen_to_piece with valid fen"""
        test_fen = '7q/2P1b3/6n1/1Q3B2/2N3k1/p3K3/8/6Rr w - - 0 1'
        expected_list = [
            GamePiece((0, 7),Piece.QUEEN,Color.BLACK),
            GamePiece((1, 2),Piece.PAWN,Color.WHITE),
            GamePiece((1, 4),Piece.BISHOP,Color.BLACK),
            GamePiece((2, 6),Piece.KNIGHT,Color.BLACK),
            GamePiece((3, 1),Piece.QUEEN,Color.WHITE),
            GamePiece((3, 5),Piece.BISHOP,Color.WHITE),
            GamePiece((4, 2),Piece.KNIGHT,Color.WHITE),
            GamePiece((4, 6),Piece.KING,Color.BLACK),
            GamePiece((5, 0),Piece.PAWN,Color.BLACK),
            GamePiece((5, 4),Piece.KING,Color.WHITE),
            GamePiece((7, 6),Piece.ROOK,Color.WHITE),
            GamePiece((7, 7),Piece.ROOK,Color.BLACK)
        ]
                        
        output_list = fen_to_pieces(test_fen)
        self.assertCountEqual(expected_list,output_list)

if __name__ == '__main__':
    unittest.main()