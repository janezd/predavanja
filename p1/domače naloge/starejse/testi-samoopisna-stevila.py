import unittest

class TestObvezna(unittest.TestCase):
    def test_samoopisno(self):
        self.assertTrue(samoopisno(1210))
        self.assertTrue(samoopisno(2020))
        self.assertTrue(samoopisno(3211000))
        self.assertTrue(samoopisno(6210001000))

        self.assertFalse(samoopisno(121))
        self.assertFalse(samoopisno(1211))
        self.assertFalse(samoopisno(202))
        self.assertFalse(samoopisno(20))
        self.assertFalse(samoopisno(123))
        self.assertFalse(samoopisno(1234))
        self.assertFalse(samoopisno(100))
        self.assertFalse(samoopisno(136))

    def test_vsa_samoopisna(self):
        self.assertEqual(vsa_samoopisna(4), [1210, 2020])
        self.assertEqual(vsa_samoopisna(5), [21200])


class TestDodatna(unittest.TestCase):
    def test_pretvori(self):
        self.assertEqual(pretvori(134, 10), "134")
        self.assertEqual(pretvori(22, 2), "10110")
        self.assertEqual(pretvori(22, 3), "211")
        self.assertEqual(pretvori(22, 8), "26")
        self.assertEqual(pretvori(22, 8), "26")
        self.assertEqual(pretvori(0, 8), "0")

        self.assertEqual(pretvori(100, 4), "1210")
        self.assertEqual(pretvori(136, 4), "2020")
        self.assertEqual(pretvori(1425, 5), "21200")
        self.assertEqual(pretvori(225331713, 9), "521001000")

    def test_samoopisno_b(self):
        self.assertTrue(samoopisno_b(100, 4))
        self.assertTrue(samoopisno_b(136, 4))
        self.assertTrue(samoopisno_b(1425, 5))
        self.assertTrue(samoopisno_b(225331713, 9))

        self.assertFalse(samoopisno_b(100, 10))
        self.assertFalse(samoopisno_b(136, 10))


if __name__ == "__main__":
    unittest.main()

