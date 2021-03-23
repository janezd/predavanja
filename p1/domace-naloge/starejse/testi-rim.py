

import unittest

class TestObvezna(unittest.TestCase):
    def test_vsota(self):
        with self.assertRaises(RecursionError, msg="Funkcija ni rekurzivna."):
            vsota([0] * 2000)
        self.assertEqual(vsota([5, 1, 2, 5]), 13)
        self.assertEqual(vsota([5, 1, 2, 5] + [42] * 100), 4213)
        self.assertEqual(vsota([]), 0)

    def test_vsebuje(self):
        with self.assertRaises(RecursionError, msg="Funkcija ni rekurzivna."):
            vsebuje([1] * 2000, 0)
        self.assertTrue(vsebuje([4, 1, 5, 2, 8], 4))
        self.assertTrue(vsebuje([4, 1, 5, 2, 8], 1))
        self.assertTrue(vsebuje([4, 1, 5, 2, 8], 5))
        self.assertTrue(vsebuje([4, 1, 5, 2, 8], 2))
        self.assertTrue(vsebuje([4, 1, 5, 2, 8], 8))
        self.assertTrue(vsebuje([4], 4))
        self.assertTrue(vsebuje([4, 0, 1], 0))
        self.assertTrue(vsebuje([0], 0))

        self.assertFalse(vsebuje([4, 1, 5, 2, 8], 42))
        self.assertFalse(vsebuje([], 42))
        self.assertFalse(vsebuje([], 0))

    def test_najvecja_potenca(self):
        with self.assertRaises(RecursionError, msg="Funkcija ni rekurzivna."):
            najvecja_potenca(2 ** 2000)
        self.assertEqual(najvecja_potenca(20), 16)
        self.assertEqual(najvecja_potenca(16), 16)
        self.assertEqual(najvecja_potenca(5), 4)
        self.assertEqual(najvecja_potenca(30), 16)
        self.assertEqual(najvecja_potenca(31), 16)
        self.assertEqual(najvecja_potenca(32), 32)
        self.assertEqual(najvecja_potenca(33), 32)
        self.assertEqual(najvecja_potenca(1), 1)


class TestDodatna(unittest.TestCase):
    @staticmethod
    def najvecja_potenca(n):
        p = 1
        while p <= n:
            p *= 2
        return p // 2

    def test_razbij(self):
        global najvecja_potenca
        naj_pot = najvecja_potenca
        najvecja_potenca = self.najvecja_potenca
        try:
            with self.assertRaises(RecursionError, msg="Funkcija ni rekurzivna."):
                razbij(2 ** 2000 - 1)
        finally:
            najvecja_potenca = naj_pot
        self.assertEqual(razbij(22), [16, 4, 2])
        self.assertEqual(razbij(23), [16, 4, 2, 1])
        self.assertEqual(razbij(56), [32, 16, 8])
        self.assertEqual(razbij(1), [1])
        self.assertEqual(razbij(0), [])

    def test_brez(self):
        with self.assertRaises(RecursionError, msg="Funkcija ni rekurzivna."):
            brez([0, 1] * 2000, 1)
        self.assertEqual(brez([5, 1, 2, 3, 1, 5], 1), [5, 2, 3, 5])
        self.assertEqual(brez([5, 1, 2, 3, 1, 5], 4), [5, 1, 2, 3, 1, 5])


class TestZaLastnoVeselje(unittest.TestCase):
    def test_razlika(self):
        with self.assertRaises(RecursionError, msg="Funkcija ni rekurzivna."):
            razlika([0] * 2000, [1] * 2000)
        self.assertEqual(sorted(razlika([1, 2, 4], [1, 4, 8])), [2, 8])
        self.assertEqual(sorted(razlika([4, 1, 16], [1, 8, 2])), [2, 4, 8, 16])
        self.assertEqual(sorted(razlika([1, 2, 5, 13, 7], [13, 7, 1, 2])), [5])
        self.assertEqual(sorted(razlika([1, 2, 5, 13, 7], [13, 7, 1, 2, 5])), [])
        self.assertEqual(sorted(razlika([1, 2, 5, 13, 7], [])), [1, 2, 5, 7, 13])
        self.assertEqual(sorted(razlika([], [42])), [42])
        self.assertEqual(sorted(razlika([42], [42])), [])
        self.assertEqual(sorted(razlika([], [])), [])

    def test_razbij_seznam(self):
        with self.assertRaises(RecursionError, msg="Funkcija ni rekurzivna."):
            razbij_seznam([1] * 2000)
        self.assertEqual(razbij_seznam([22, 56, 7]), [[16, 4, 2], [32, 16, 8], [4, 2, 1]])
        self.assertEqual(razbij_seznam([22]), [[16, 4, 2]])
        self.assertEqual(razbij_seznam([]), [])

    def test_zdruzi_sezname(self):
        with self.assertRaises(RecursionError, msg="Funkcija ni rekurzivna."):
            zdruzi_sezname([[1]] * 2000)
        self.assertEqual(sorted(zdruzi_sezname([[16, 4, 2], [32, 16, 8], [4, 2, 1]])), [1, 8, 32])
        self.assertEqual(zdruzi_sezname([[1, 2, 3]]), [1, 2, 3])
        self.assertEqual(zdruzi_sezname([]), [])


if __name__ == "__main__":
    unittest.main()
