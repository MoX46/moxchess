import unittest
from game.gamepiece import GamePiece, Piece, Color

class TestGamePiece(unittest.TestCase):
    """Tests the game piece class """
    def setUp(self) -> None:
        self.test_piece = GamePiece((4,0),Piece.BISHOP,Color.WHITE)

    def test_identity(self) -> None:
        """Tests piece identity method"""
        self.assertTrue(self.test_piece.identity,'I\'m a white bishop on A4')

    # def get_legal_moves_bishop(self) -> None:
    #     """Tests legal moves for bishop"""
    #     bishop_piece = GamePiece('E4',m.Piece.BISHOP,m.Color.WHITE)
    #     expected = ['F5','G6','H7','F3','G2','H1','D3','C2','D1','D5','C6','B7','A8']
    #     expected.sort()
    #     self.assertEqual(bishop_piece.get_legal_moves(),expected)

if __name__ == '__main__':
    unittest.main()