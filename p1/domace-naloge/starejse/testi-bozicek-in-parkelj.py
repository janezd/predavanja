import unittest

class TestMesto(unittest.TestCase):
    def test_mesto(self):
        a = Mesto()
        b = Mesto()

        self.assertSetEqual(a.vse_obdarovane(), set())
        self.assertSetEqual(b.vse_obdarovane(), set())
        self.assertFalse(a.je_obdarovana(1, 3))
        self.assertFalse(b.je_obdarovana(1, 3))

        a.obdaruj(1, 3)
        self.assertSetEqual(a.vse_obdarovane(), {(1, 3)})
        self.assertSetEqual(b.vse_obdarovane(), set())
        self.assertTrue(a.je_obdarovana(1, 3))
        self.assertFalse(b.je_obdarovana(1, 3))

        a.obdaruj(1, 3)
        self.assertSetEqual(a.vse_obdarovane(), {(1, 3)})
        self.assertSetEqual(b.vse_obdarovane(), set())
        self.assertTrue(a.je_obdarovana(1, 3))
        self.assertFalse(a.je_obdarovana(-2, -3))
        self.assertFalse(b.je_obdarovana(1, 3))

        a.obdaruj(-2, -3)
        self.assertSetEqual(a.vse_obdarovane(), {(1, 3), (-2, -3)})
        self.assertSetEqual(b.vse_obdarovane(), set())
        self.assertTrue(a.je_obdarovana(1, 3))
        self.assertTrue(a.je_obdarovana(-2, -3))
        self.assertFalse(b.je_obdarovana(1, 3))

        b.obdaruj(0, 0)
        self.assertSetEqual(a.vse_obdarovane(), {(1, 3), (-2, -3)})
        self.assertSetEqual(b.vse_obdarovane(), {(0, 0)})
        self.assertTrue(a.je_obdarovana(1, 3))
        self.assertTrue(a.je_obdarovana(-2, -3))
        self.assertFalse(b.je_obdarovana(1, 3))
        self.assertTrue(b.je_obdarovana(0, 0))
        self.assertFalse(a.je_obdarovana(0, 0))


class TestBozicek(unittest.TestCase):
    def test_obdaruj(self):
        m = Mesto()
        n = Mesto()
        b = Bozicek(m)
        b.obdaruj()
        self.assertSetEqual(m.vse_obdarovane(), {(0, 0)})
        self.assertSetEqual(n.vse_obdarovane(), set())

    def test_premik(self):
        m = Mesto()
        n = Mesto()
        b = Bozicek(m)
        c = Bozicek(m)
        b.obdaruj()
        self.assertSetEqual(m.vse_obdarovane(), {(0, 0)})
        self.assertSetEqual(n.vse_obdarovane(), set())
        b.premik("^")
        b.premik("<")
        b.premik("<")
        b.obdaruj()
        b.premik("v")
        self.assertSetEqual(m.vse_obdarovane(), {(0, 0), (-2, 1)})
        self.assertSetEqual(n.vse_obdarovane(), set())
        c.obdaruj()
        self.assertSetEqual(m.vse_obdarovane(), {(0, 0), (-2, 1)})
        b.obdaruj()
        self.assertSetEqual(m.vse_obdarovane(), {(0, 0), (-2, 1), (-2, 0)})
        b.premik(">")
        self.assertSetEqual(m.vse_obdarovane(), {(0, 0), (-2, 1), (-2, 0)})
        b.obdaruj()
        self.assertSetEqual(m.vse_obdarovane(), {(0, 0), (-2, 1), (-2, 0), (-1, 0)})
        c.premik("v")
        self.assertSetEqual(m.vse_obdarovane(), {(0, 0), (-2, 1), (-2, 0), (-1, 0)})
        c.obdaruj()
        self.assertSetEqual(m.vse_obdarovane(), {(0, 0), (-2, 1), (-2, 0), (-1, 0), (0, -1)})
        self.assertSetEqual(n.vse_obdarovane(), set())


    def test_premiki(self):
        m = Mesto()
        b = Bozicek(m)
        b.premiki("v<<^^^>>>>>")
        b.obdaruj()
        self.assertSetEqual(m.vse_obdarovane(), {(3, 2)})

        cc = ""
        def p(c):
            nonlocal cc
            cc += c
        b.premik = p
        b.premiki("v<<^^^>>>>>")
        self.assertEqual(
            cc, "v<<^^^>>>>>",
            "Napiši metodo `premiki` tako, da bo uporabljala metodo `premik`")

    def test_hitri_bozicek(self):
        m = Mesto()
        b = HitriBozicek(m, 2)
        c = HitriBozicek(m, 3)
        b.obdaruj()
        self.assertSetEqual(m.vse_obdarovane(), {(0, 0)})
        b.premik("^")
        b.obdaruj()
        self.assertSetEqual(m.vse_obdarovane(), {(0, 0), (0, 2)})
        b.premik("<")
        b.obdaruj()
        self.assertSetEqual(m.vse_obdarovane(), {(0, 0), (0, 2), (-2, 2)})
        c.premik("<")
        c.obdaruj()
        self.assertSetEqual(m.vse_obdarovane(), {(0, 0), (0, 2), (-2, 2), (-3, 0)})

    def test_metode(self):
        self.assertIs(HitriBozicek.premiki, Bozicek.premiki,
                      "HitriBozicek naj podeduje metodo premiki")
        self.assertIs(HitriBozicek.obdaruj, Bozicek.obdaruj,
                      "HitriBozicek naj podeduje metodo obdaruj")


class TestParkelj(unittest.TestCase):
    def test_parkelj(self):
        self.assertEqual(parkelj(0, 0, [(4, 0)]), ">>>>")
        self.assertEqual(parkelj(0, 0, [(-2, 0)]), "<<")
        self.assertEqual(parkelj(5, 0, [(5, 3)]), "^^^")
        self.assertEqual(parkelj(12, 10, [(12, 8)]), "vv")

        self.assertEqual(sorted(parkelj(0, 0, [(4, 2)])), sorted(">>>>^^"))

        pot = parkelj(50, 6, [(46, 2), (52, 2), (41, 0)])
        self.assertEqual(sorted(pot[:8]), sorted("<<<<vvvv"))
        self.assertEqual(pot[8:14], ">>>>>>")
        self.assertEqual(sorted(pot[-13:]), sorted("<" * 11 + "vv"))

        self.assertEqual(parkelj(0, 0, [(0, 0)]), "")
        self.assertEqual(parkelj(0, 0, [(0, 0), (2, 0)]), ">>")

    def test_hitri_parkelj(self):
        m = Mesto()
        for i in range(3):
            m.obdaruj(i, 0)
            m.obdaruj(i, 1)
        self.assertTrue(hitri_parkelj(0, 0, m) in (">>^<<", "^>>v<", "^>v>^"))

        n = Mesto()
        n.obdaruj(2, 0)
        n.obdaruj(0, 1)
        n.obdaruj(0, 10)
        pot = hitri_parkelj(0, 0, n)
        self.assertTrue(pot[:2], ">>")


if __name__ == "__main__":
    unittest.main()

