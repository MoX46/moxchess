import unittest
import main as m

class TestRankFileToGrid(unittest.TestCase):
    """Test the 'rank_file_to_grid' funciton"""
    def test_first_rank(self):
        """Test first rank 0"""
        self.assertEqual(m.rank_file_to_grid('E1'),(7,4))

    def test_last_rank(self):
        """Test the last rank 8"""
        self.assertEqual(m.rank_file_to_grid('D8'),(7,3))

    def test_first_file(self):
        """Test first file A"""
        self.assertEqual(m.rank_file_to_grid('A3'),(0,0))

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


if __name__ == '__main__':
    unittest.main()
