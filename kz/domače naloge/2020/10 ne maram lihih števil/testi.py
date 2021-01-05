

import unittest

class Test00_Ogrevanje(unittest.TestCase):
    def test_vsebuje_samo_soda(self):
        self.assertTrue(vsebuje_sama_soda([]))
        self.assertTrue(vsebuje_sama_soda([2]))
        self.assertTrue(vsebuje_sama_soda([4, 2]))
        self.assertTrue(vsebuje_sama_soda([8, 4, 0, 6]))
        self.assertFalse(vsebuje_sama_soda([3, 8, 4, 0, 6]))
        self.assertFalse(vsebuje_sama_soda([8, 3, 4, 0, 6]))
        self.assertFalse(vsebuje_sama_soda([8, 4, 0, 6, 3]))
        self.assertFalse(vsebuje_sama_soda([3]))

        with self.assertRaises(RecursionError, msg="Funkcija ni rekurzivna"):
            vsebuje_sama_soda([0] * 1010)

    def test_obrni(self):
        self.assertEqual([], obrni([]))
        self.assertEqual([2], obrni([2]))
        self.assertEqual([2, 4], obrni([4, 2]))
        self.assertEqual([1, 2, 4], obrni([4, 2, 1]))
        self.assertEqual([1, 8, 2, 4], obrni([4, 2, 8, 1]))

    def test_samo_soda(self):
        self.assertEqual([], samo_soda([]))
        self.assertEqual([2], samo_soda([2]))
        self.assertEqual([], samo_soda([1]))
        self.assertEqual([2], samo_soda([1, 2]))
        self.assertEqual([2, 4], samo_soda([1, 2, 4]))
        self.assertEqual([2, 6, 2, 4], samo_soda([1, 2, 3, 6, 2, 1, 4]))


class Test01Obvezna(unittest.TestCase):
    def test_prestej_liha(self):
        self.assertEqual(0, prestej_liha([]))
        self.assertEqual(0, prestej_liha([2]))
        self.assertEqual(1, prestej_liha([5]))
        self.assertEqual(1, prestej_liha([2, 5]))
        self.assertEqual(2, prestej_liha([5, 4, 3]))
        self.assertEqual(2, prestej_liha([5, 4, 3]))
        self.assertEqual(3, prestej_liha([1, 2, 3, 6, 2, 1, 4]))

    def test_ena_vec(self):
        self.assertEqual([], ena_vec([]))
        self.assertEqual([3], ena_vec([2]))
        self.assertEqual([3, 7], ena_vec([2, 6]))
        self.assertEqual([3, 7, 1], ena_vec([2, 6, 0]))
        self.assertEqual([3, 7, 1, 8], ena_vec([2, 6, 0, 7]))

    def test_zbij_liha(self):
        self.assertEqual([], zbij_liha([]))
        self.assertEqual([4], zbij_liha([4]))
        self.assertEqual([2], zbij_liha([3]))
        self.assertEqual([2, 6, 0, 4, 6], zbij_liha([3, 6, 1, 5, 6]))


class Test02Dodatno(unittest.TestCase):
    def test_zadnje_liho(self):
        self.assertFalse(zadnje_liho([]))
        self.assertFalse(zadnje_liho([4]))
        self.assertFalse(zadnje_liho([4, 6, 2, 42]))
        self.assertEqual(5, zadnje_liho([5, 4, 6, 2, 42]))
        self.assertEqual(5, zadnje_liho([4, 6, 5, 2, 42]))
        self.assertEqual(5, zadnje_liho([4, 6, 2, 42, 5]))
        self.assertEqual(5, zadnje_liho([4, 6, 3, 2, 42, 5]))
        self.assertEqual(5, zadnje_liho([11, 4, 6, 3, 2, 42, 5]))


if __name__ == "__main__":
    unittest.main()

