

import unittest

class TestRezalnik(unittest.TestCase):
    def test_rezalnik(self):
        rezalnik1 = Rezalnik()
        rezalnik2 = Rezalnik()
        s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual([[1, 2], [3, 4], [5, 6], [7, 8], [9]],
                         rezalnik1.razrezi(s))
        rezalnik1.nastavi_dolzino(4)
        self.assertEqual([[1, 2, 3, 4], [5, 6, 7, 8], [9]],
                         rezalnik1.razrezi(s))
        self.assertEqual([[1, 2], [3, 4], [5, 6], [7, 8], [9]],
                         rezalnik2.razrezi(s))

if __name__ == "__main__":
    unittest.main()
