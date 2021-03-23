import unittest
class TestTekaci(unittest.TestCase):
    def test_tekac(self):
        self.assertEqual(tekac(1, "ROMAN SONJA", 1979, 1, 15, 2),
                         "   1. ROMAN SONJA          01:15:02")
        self.assertEqual(tekac(1234, "ROMAN SONJA", 1979, 0, 1, 23),
                         "1234. ROMAN SONJA          00:01:23")
        self.assertEqual(tekac(1, "JAN HUS", 1979, 1, 15, 2),
                         '   1. JAN HUS              01:15:02')
    def test_tekac_star(self):
        self.assertEqual(tekac_star(1, "ROMAN SONJA", 1979, 1, 15, 2),
                         "   1. ROMAN SONJA (1979)         01:15:02")
        self.assertEqual(tekac_star(1234, "ROMAN SONJA", 1979, 0, 1, 23),
                         "1234. ROMAN SONJA (1979)         00:01:23")
        self.assertEqual(tekac_star(1234, "JAN HUS", 1979, 0, 1, 23),
                         '1234. JAN HUS (1979)             00:01:23')

if __name__ == "__main__":
    unittest.main()
