import unittest
import random


class TestMenjave(unittest.TestCase):
    def test_zamenjaj(self):
        s = ["Ana", "Berta", "Cilka", "Dani", "Ema"]
        zamenjaj(s, 2, 3)
        self.assertEqual(s, ["Ana", "Berta", "Dani", "Cilka", "Ema"])
        zamenjaj(s, 0, 3)
        self.assertEqual(s, ["Cilka", "Berta", "Dani", "Ana", "Ema"])
        zamenjaj(s, 0, 1)
        self.assertEqual(s, ["Berta", "Cilka", "Dani", "Ana", "Ema"])

    def test_preuredi(self):
        s = ["Ana", "Berta", "Cilka", "Dani", "Ema"]
        menjave = [(2, 3), (0, 3), (0, 1)]
        preuredi(s, menjave)
        self.assertEqual(s, ["Berta", "Cilka", "Dani", "Ana", "Ema"])

    def test_urejen(self):
        self.assertTrue(urejen([1, 2, 3, 4]))
        self.assertTrue(urejen([1, 2, 3]))
        self.assertTrue(urejen([1, 2]))
        self.assertTrue(urejen([1]))
        self.assertTrue(urejen([]))
        self.assertTrue(urejen(list(range(100))))

        self.assertFalse(urejen([2, 1, 3, 4]))
        self.assertFalse(urejen([1, 3, 2, 4]))
        self.assertFalse(urejen([1, 2, 4, 3]))
        self.assertFalse(urejen([2, 1, 3]))
        self.assertFalse(urejen([1, 3, 2]))
        self.assertFalse(urejen([3, 1]))

    def test_ureja(self):
        s = ["Berta", "Cilka", "Dani", "Ana", "Ema"]
        self.assertTrue(ureja(s[:], [(0, 1), (0, 3), (2, 3)]))
        self.assertFalse(ureja(s[:], [(0, 1), (0, 3)]))

    def test_nacrt(self):
        for i in range(200):
            t = [random.randint(1, 100) for _ in range(10)]
            v = t[:]
            n = nacrt(t)
            self.assertEqual(t, v)
            self.assertTrue(ureja(t, n), "Nacrt ne deluje za seznam " + str(t))

        t = [3, 4, 4, 2, 1, 5, 2, 3, 2, 2]
        n = nacrt(t)
        self.assertTrue(ureja(t, n), "Nacrt ne deluje za seznam " + str(t))

if __name__ == '__main__':
    unittest.main()

