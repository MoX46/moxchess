import unittest
from game.gamepiece import position_to_square

class TestPositionToSquare(unittest.TestCase):
    """Test the grid_to_rank_file function"""
    def test_first_rowo(self):
        """Test first row, 0"""
        self.assertEqual(position_to_square((0,4)),('E8'))

    def test_last_row(self):
        """Test last row, 7"""
        self.assertEqual(position_to_square((7,7)),('H1'))

    def test_first_col(self):
        """Test first column,  0"""
        self.assertEqual(position_to_square((3,0)),('A5'))

    def test_last_col(self):
        """Test last column, 7"""
        self.assertEqual(position_to_square((5,7)),('H3'))

if __name__ == '__main__':
    unittest.main()