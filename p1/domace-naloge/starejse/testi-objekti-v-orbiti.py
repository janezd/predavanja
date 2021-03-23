
import unittest
from unittest.mock import patch
import random


class Test01Obvezna(unittest.TestCase):
    def test01_luna(self):
        a = Luna()
        self.assertIsNone(a.pripni("b"), "Metoda `pripni` ne sme vračati ničesar")
        a.pripni("c")
        a.pripni("d")

        b = Luna()
        b.pripni("xyz")

        c = Luna()

        self.assertEqual({"b", "c", "d"}, a.lune())
        self.assertEqual({"xyz"}, b.lune())
        self.assertEqual(set(), c.lune())

        self.assertTrue(a.ima_luno("b"))
        self.assertFalse(a.ima_luno("xyz"))

        self.assertFalse(b.ima_luno("b"))
        self.assertTrue(b.ima_luno("xyz"))

        self.assertFalse(c.ima_luno("b"))
        self.assertFalse(c.ima_luno("xyz"))

        self.assertEqual(3, a.stevilo_lun())
        self.assertEqual(1, b.stevilo_lun())
        self.assertEqual(0, c.stevilo_lun())

    def test02_ekskluzivna_luna_pripni(self):
        imena = ["asd", "asdf", "aoij", "ivuiv", "asdjnf", "oija"]
        for _ in range(10):
            random.shuffle(imena)
            a = EkskluzivnaLuna()
            a.pripni(imena[0])
            self.assertEqual(1, a.stevilo_lun())
            a.pripni(imena[1])
            self.assertEqual(2, a.stevilo_lun())
            for i in range(2, len(imena)):
                a.pripni(imena[i])
                self.assertEqual(3, a.stevilo_lun())
                self.assertEqual(a.lune(), set(imena[i - 2:i + 1]),
                                 f"ko dodajam v tem vrstnem redu: {imena},\n"
                                 f"pride do napake, ko dodam {imena[i]}")

    def test02_ekskluzivna_luna_struktura(self):
        self.assertEqual((Luna,), EkskluzivnaLuna.__bases__,
                         "Razred EkskluzivnaLuna mora biti izpeljan iz razreda Luna")
        self.assertEqual(["pripni"],
                         [name for name in EkskluzivnaLuna.__dict__ if name[:2] != "__"],
                         "Razred EkskluzivnaLuna naj doda/spremeni samo metodo `pripni`")
        with patch.object(Luna, "pripni") as mock_pripni:
            a = EkskluzivnaLuna()
            a.pripni("b")
            self.assertTrue(mock_pripni.called, "Metoda pripni mora klicati podedovano metodo")


class Test02Dodatna(unittest.TestCase):
    def setUp(self):
        pari = [p.split(")")
                for p in "COM)B B)C C)D D)E E)F B)G G)H D)I E)J J)K K)L K)YOU I)SAN".split()]
        self.lune = {ime: Luna() for ime, _ in pari}
        self.lune.update({ime: Luna() for _, ime in pari})
        for center, luna in pari:
            self.lune[center].pripni(self.lune[luna])

    def test_ima_odvisnika(self):
        for kdo, koga in [("COM", "I"), ("COM", "E"), ("G", "H")]:
            self.assertTrue(self.lune[kdo].ima_odvisnika(self.lune[koga]),
                            f"Luna {kdo} ima odvisnika {koga}, "
                            "funkcija pa je vrnila False namesto True")

        for kdo, koga in [("C", "H"), ("SAN", "G"), ("G", "SAN")]:
            self.assertFalse(self.lune[kdo].ima_odvisnika(self.lune[koga]),
                             f"Luna {kdo} nima odvisnika {koga}, "
                             "funkcija pa je vrnila True namesto False")

    def test_n_odvisnikov(self):
        self.assertEqual(8, self.lune["D"].n_odvisnikov())
        self.assertEqual(0, self.lune["F"].n_odvisnikov())
        self.assertEqual(13, self.lune["COM"].n_odvisnikov())

    def test_sirina_orbite(self):
        d = self.lune["D"]
        self.assertEqual(3, d.sirina_orbite(2))

        com = self.lune["COM"]
        self.assertEqual(1, com.sirina_orbite(0))
        self.assertEqual(1, com.sirina_orbite(1))
        self.assertEqual(2, com.sirina_orbite(2))
        self.assertEqual(2, com.sirina_orbite(3))
        self.assertEqual(2, com.sirina_orbite(4))
        self.assertEqual(3, com.sirina_orbite(5))
        self.assertEqual(1, com.sirina_orbite(6))
        self.assertEqual(2, com.sirina_orbite(7))
        self.assertEqual(0, com.sirina_orbite(8))
        self.assertEqual(0, com.sirina_orbite(20))

        c = self.lune["C"]
        self.assertEqual(1, c.sirina_orbite(0))
        self.assertEqual(1, c.sirina_orbite(1))
        self.assertEqual(2, c.sirina_orbite(2))
        self.assertEqual(3, c.sirina_orbite(3))
        self.assertEqual(1, c.sirina_orbite(4))
        self.assertEqual(2, c.sirina_orbite(5))

        self.assertEqual(1, self.lune["YOU"].sirina_orbite(0))


class TestKudos(unittest.TestCase):
    def test_struktura(self):
        com = BiLuna("com", None)
        b = BiLuna("b", com)
        g = BiLuna("g", b)
        h = BiLuna("h", g)
        c = BiLuna("c", b)
        d = BiLuna("d", c)
        i = BiLuna("i", d)
        san = BiLuna("san", i)
        e = BiLuna("e", d)
        f = BiLuna("f", e)
        j = BiLuna("j", e)
        k = BiLuna("k", j)
        l = BiLuna("l", k)
        you = BiLuna("you", k)

        self.assertIs(d.center(), c)
        self.assertEqual({e, i}, d.lune())

        self.assertIs(k.center(), j)
        self.assertEqual({k}, j.lune())
        self.assertEqual({e, j, k, l, f, you}, e.poddrevo())

        k.zamenjaj_center(d)
        self.assertIs(k.center(), d)

        self.assertEqual(j.lune(), set())
        self.assertEqual({e, i, k}, d.lune())

        self.assertEqual({e, j, f}, e.poddrevo())
        self.assertEqual({d, i, san, e, j, k, l, f, you}, d.poddrevo())

        i.zamenjaj_center(None)
        self.assertIsNone(i.center())
        self.assertEqual({e, k}, d.lune())
        self.assertEqual({san}, i.lune())
        self.assertEqual({d, e, j, k, l, f, you}, d.poddrevo())

        i.zamenjaj_center(g)
        self.assertIs(i.center(), g)
        self.assertEqual({i, h}, g.lune())
        self.assertEqual({h, g, i, san}, g.poddrevo())

        i.zamenjaj_center(g)
        self.assertIs(i.center(), g)
        self.assertEqual({i, h}, g.lune())
        self.assertEqual({h, g, i, san}, g.poddrevo())

        i.zamenjaj_center(k)
        self.assertIs(i.center(), k)
        self.assertEqual({h}, g.lune())
        self.assertEqual({h, g}, g.poddrevo())

    def test_dosegljivo(self):
        # Malo drugače kot v prejšnjem testu:
        com = BiLuna("com", None)
        b = BiLuna("b", com)
        g = BiLuna("g", b)
        h = BiLuna("h", g)
        c = BiLuna("c", b)

        dom = BiLuna("dom", None)
        i = BiLuna("i", dom)
        san = BiLuna("san", i)
        e = BiLuna("e", dom)
        f = BiLuna("f", e)
        j = BiLuna("j", e)
        k = BiLuna("k", j)
        l = BiLuna("l", k)
        you = BiLuna("you", k)

        self.assertTrue(com.dosegljivo(h))
        self.assertTrue(h.dosegljivo(com))
        self.assertTrue(com.dosegljivo(c))
        self.assertTrue(c.dosegljivo(com))
        self.assertTrue(h.dosegljivo(c))
        self.assertTrue(c.dosegljivo(h))

        self.assertTrue(j.dosegljivo(f))
        self.assertTrue(f.dosegljivo(j))
        self.assertTrue(you.dosegljivo(san))
        self.assertTrue(san.dosegljivo(you))

        self.assertFalse(com.dosegljivo(dom))
        self.assertFalse(dom.dosegljivo(com))
        self.assertFalse(e.dosegljivo(g))
        self.assertFalse(g.dosegljivo(e))
        self.assertFalse(g.dosegljivo(l))
        self.assertFalse(l.dosegljivo(g))

        k.zamenjaj_center(c)
        self.assertTrue(g.dosegljivo(l))
        self.assertTrue(l.dosegljivo(g))
        self.assertFalse(com.dosegljivo(dom))
        self.assertFalse(dom.dosegljivo(com))
        self.assertFalse(e.dosegljivo(g))
        self.assertFalse(g.dosegljivo(e))


if __name__ == "__main__":
    unittest.main()
