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

    def test_get_index(self) -> None:
        """Tests the get index method"""
        self.assertEqual(self.test_piece.index,(4,0))

    # def get_legal_moves_bishop(self) -> None:
    #     """Tests legal moves for bishop"""
    #     bishop_piece = m.GamePiece('E4',m.Piece.BISHOP,m.Color.WHITE)
    #     expected = ['F5','G6','H7','F3','G2','H1','D3','C2','D1','D5','C6','B7','A8']
    #     expected.sort()
    #     self.assertEqual(bishop_piece.get_legal_moves(),expected)

class TestFenToPieces(unittest.TestCase):
    """Tests the fen_to_pieces function"""
    def test_valid_fen(self) -> None:
        """Tests random fen_to_piece with valid fen"""
        test_fen = '7q/2P1b3/6n1/1Q3B2/2N3k1/p3K3/8/6Rr w - - 0 1'
        expected_list = [
                            m.GamePiece('H8',m.Piece.QUEEN,m.Color.BLACK),
                            m.GamePiece('C7',m.Piece.PAWN,m.Color.WHITE),
                            m.GamePiece('E7',m.Piece.BISHOP,m.Color.BLACK),
                            m.GamePiece('G6',m.Piece.KNIGHT,m.Color.BLACK),
                            m.GamePiece('B5',m.Piece.QUEEN,m.Color.WHITE),
                            m.GamePiece('F5',m.Piece.BISHOP,m.Color.WHITE),
                            m.GamePiece('C4',m.Piece.KNIGHT,m.Color.WHITE),
                            m.GamePiece('G4',m.Piece.KING,m.Color.BLACK),
                            m.GamePiece('A3',m.Piece.PAWN,m.Color.BLACK),
                            m.GamePiece('E3',m.Piece.KING,m.Color.WHITE),
                            m.GamePiece('G1',m.Piece.ROOK,m.Color.WHITE),
                            m.GamePiece('H1',m.Piece.ROOK,m.Color.BLACK)
                        ]
        output_list = m.fen_to_pieces(test_fen)
        self.assertCountEqual(expected_list,output_list)

class TestIsFenValid(unittest.TestCase):
    """Tests is_fen_valid function"""
    def test_valid_fens(self) -> None:
        """Tests valid fens"""
        res = True
        fen_strings = [
            '5n2/2k3p1/8/2p3Pn/6pK/2N2P2/q2rb1R1/1R3Q2 w - - 0 1',
            '5b2/1n2p3/4p3/3pP1Pp/4N3/p3K1n1/1R2Q3/3r3k w - - 0 1',
            '6K1/prB1Q3/8/3P4/Np1R1P2/7p/RP1p4/3kn3 w - - 0 1',
            '8/1Pp5/np4N1/4P1KB/2N2pp1/8/p1prPk2/8 w - - 0 1',
            '6K1/4P3/P2npB2/2Pk4/6pQ/1P1r2p1/R2N1r2/8 w - - 0 1'
        ]
        for fen in fen_strings:
            if not m.is_fen_valid(fen):
                res = False
        self.assertTrue(res,True)

    def test_invalid_fens(self) -> None:
        """Tests invalid fens"""
        res = True
        fen_strings = [
            '1q4p1/4P3/PQ1Q1rBb/4p2p/7K/P2p1p2/8 w - - 0 1',
            '3B4/1Kp2q7/4nPPP/2Pr4/7b/N1P5/7p/N2k4 w - - 0 1',
            'n1K5/2p5/1p1bP3/p7/p3k3/1N3q1Q/1P2r1P1/2B5 z - - 0 1',
            'nRB2n1r/8/pQ5p/2K3P1/3Q1P2/2P5/3r3B/4k3 w wwf - 0 1',
            'Q6K/Pp6/2k1P3/P1b3p1/6np/P5pB/7p/n7 w - z0  0 1',
            'nRB2n1r/8/pQ5p/2K3P1/3Q1P2/2P5/3r3B/4k3 w - - - 1',
            '1r6/R2p3P/4b1BN/3p1PP1/5bp1/K3k3/1p6/2q5 w - - 0 -',

        ]
        for fen in fen_strings:
            if m.is_fen_valid(fen):
                res = False
        self.assertTrue(res,True)
      
if __name__ == '__main__':
    unittest.main()
