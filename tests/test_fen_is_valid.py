import unittest
from game.game import is_fen_valid

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
            if not is_fen_valid(fen):
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
            '1rBN4/PNK5/Pp2pn2/111p1P2/5R2/2n5/1k6/8 w - - 0 1',
        ]
        for fen in fen_strings:
            if is_fen_valid(fen):
                res = False
        self.assertTrue(res,True)

if __name__ == '__main__':
    unittest.main()