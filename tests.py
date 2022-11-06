import unittest
import main as m

class TestRankFileToGrid(unittest.TestCase):
    def test_first_rank(self):
        self.assertEqual(m.rank_file_to_grid('E1'),(4,0))

    def test_last_rank(self):
        self.assertEqual(m.rank_file_to_grid('E8'),(4,7))

    def test_first_file(self):
        self.assertEqual(m.rank_file_to_grid('A3'),(0,2))

    def test_last_file(self):
        self.assertEqual(m.rank_file_to_grid('H7'),(7,6))

if __name__ == '__main__':
    unittest.main()