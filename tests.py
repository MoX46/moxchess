from re import I
import unittest
import main as m

class TestRankFileToGrid(unittest.TestCase):
    """Test the 'rank_file_to_grid' funciton"""
    def test_first_rank(self):
        """Test first rank 0"""
        self.assertEqual(m.rank_file_to_grid('E1'),(7,4))

    def test_last_rank(self):
        """Test the last rank 8"""
        self.assertEqual(m.rank_file_to_grid('D8'),(0,3))

    def test_first_file(self):
        """Test first file A"""
        self.assertEqual(m.rank_file_to_grid('A3'),(5,0))

    def test_last_file(self):
        """Test last file H"""
        self.assertEqual(m.rank_file_to_grid('H6'),(2,7))

class TestGridToRankFile(unittest.TestCase):
    """Test the grid_to_rank_file function"""
    def test_first_row(self):
        """Test first row, 0"""
        self.assertEqual(m.grid_to_rank_file((0,4)),('E8'))

    def test_last_row(self):
        """Test last row, 7"""
        self.assertEqual(m.grid_to_rank_file((7,7)),('H1'))

    def test_first_col(self):
        """Test first column,  0"""
        self.assertEqual(m.grid_to_rank_file((3,0)),('A5'))

    def test_last_col(self):
        """Test last column, 7"""
        self.assertEqual(m.grid_to_rank_file((5,7)),('H3'))

class TestGamePiece(unittest.TestCase):
    """Tests the game piece class """
    def setUp(self) -> None:
        self.test_piece = m.GamePiece('A4',m.Piece.BISHOP,m.Color.WHITE)

    def test_get_position(self) -> None:
        """Tests the get position method"""
        self.assertEqual(self.test_piece.get_position(), 'A4')

    def test_get_index(self) -> None:
        """Tests the get index method"""
        self.assertEqual(self.test_piece.get_index(),(4,1))

    def get_legal_moves_bishop(self) -> None:
        """Tests legal moves for bishop"""
        test_piece = m.GamePiece('E4',m.Piece.BISHOP,m.Color.WHITE)
        expected = ['F5','G6','H7','F3','G2','H1','D3','C2','D1','D5','C6','B7','A8']
        expected.sort()
        self.assertEqual(test_piece.get_legal_moves(),expected)

if __name__ == '__main__':
    unittest.main()
