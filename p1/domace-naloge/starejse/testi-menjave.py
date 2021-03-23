

import unittest


class TestObvezna(unittest.TestCase):
    def test_zamenjaj(self):
        s = ["Ana", "Berta", "Cilka", "Dani"]
        self.assertIsNone(zamenjaj(s, 1, 2))
        self.assertEqual(s, ["Ana", "Cilka", "Berta", "Dani"])
        self.assertIsNone(zamenjaj(s, 3, 0))
        self.assertEqual(s, ["Dani", "Cilka", "Berta", "Ana"])
        self.assertIsNone(zamenjaj(s, 3, 3))
        self.assertEqual(s, ["Dani", "Cilka", "Berta", "Ana"])

    def test_zamenjan(self):
        s = ["Ana", "Berta", "Cilka", "Dani"]
        self.assertListEqual(["Ana", "Berta", "Dani", "Cilka"], zamenjan(s, 3, 2))
        self.assertListEqual(["Ana", "Berta", "Cilka", "Dani"], s)

        self.assertListEqual(["Ana", "Berta", "Cilka", "Dani"], zamenjan(s, 3, 3))
        self.assertListEqual(["Ana", "Berta", "Cilka", "Dani"], s)


class TestDodatna(unittest.TestCase):
    def test_uredi(self):
        s = [5, 1, 2, 8]
        m = uredi(s)
        self.assertEqual([5, 1, 2, 8], s, "Pusti s pri miru!")
        for e, f in m:
            zamenjaj(s, e, f)
        self.assertTrue(all(e <= f for e, f in zip(s, s[1:])))

        s = [5, 1, 2, 8, 3, 42, 13]
        m = uredi(s)
        self.assertEqual([5, 1, 2, 8, 3, 42, 13], s, "Pusti s pri miru!")
        for e, f in m:
            zamenjaj(s, e, f)
        self.assertTrue(all(e <= f for e, f in zip(s, s[1:])))

        s = [5, 1, 2, 4, 5, 5, 5, 1, 4, 2, 5]
        m = uredi(s)
        self.assertEqual([5, 1, 2, 4, 5, 5, 5, 1, 4, 2, 5], s, "Pusti s pri miru!")
        for e, f in m:
            zamenjaj(s, e, f)
        self.assertTrue(all(e <= f for e, f in zip(s, s[1:])))


if __name__ == "__main__":
    if __name__ == '__main__':
        unittest.main()
