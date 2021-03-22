import unittest

class KraljiceTestCase(unittest.TestCase):
    def test_6stolpec_prost(self):
        if "stolpec_prost" in globals():
            self.assertTrue(stolpec_prost("b", ["a1", "c2", "d4"]))
            self.assertTrue(stolpec_prost("b", []))
            self.assertFalse(stolpec_prost("b", ["b3"]))
            self.assertFalse(stolpec_prost("b", ["a1", "b3"]))
            self.assertFalse(stolpec_prost("b", ["a1", "b3", "c4"]))
            self.assertFalse(stolpec_prost("b", ["b3", "c4"]))

    def test_6prosti_stolpci(self):
        self.assertCountEqual(prosti_stolpci(["a1", "c2", "d4"]), "befgh")
        self.assertCountEqual(prosti_stolpci(["a1"]), "bcdefgh")
        self.assertCountEqual(prosti_stolpci(["h1"]), "abcdefg")
        self.assertCountEqual(prosti_stolpci([]), "abcdefgh")

    def test_6prost_stolpec(self):
        self.assertEqual(prost_stolpec(["a1", "c2", "d4"]), "b")
        self.assertEqual(prost_stolpec(["a1"]), "b")
        self.assertEqual(prost_stolpec(["h1"]), "a")
        self.assertEqual(prost_stolpec([]), "a")

    def test_7napada(self):
        self.assertTrue(napada("a1", "a5"))
        self.assertTrue(napada("a1", "d1"))
        self.assertTrue(napada("c4", "a2"))
        self.assertTrue(napada("c4", "f7"))
        self.assertFalse(napada("c4", "a3"))
        self.assertFalse(napada("c4", "h5"))

    def test_7napadajo(self):
        self.assertCountEqual(napadajo("c2", ["a4", "c7", "d2"]),
            ["a4", "c7", "d2"])
        self.assertCountEqual(napadajo("c6", ["a4", "c7"]), ["a4", "c7"])
        self.assertCountEqual(napadajo("e8", ["a4", "c7", "d2"]), ["a4"])
        self.assertCountEqual(napadajo("a4", ["a4", "c7", "d2"]), ["a4"])
        self.assertCountEqual(napadajo("g8", ["a4", "c7", "d2"]), [])

    def test_7napadeno(self):
        self.assertTrue(napadeno("a7", ["a4", "c7", "d2"]))
        self.assertTrue(napadeno("a6", ["a4", "c7"]))
        self.assertFalse(napadeno("h5", ["a4", "c7", "d2"]))
        self.assertFalse(napadeno("a4", []))

    def test_8prosto_v_stolpcu(self):
        self.assertEqual(prosto_v_stolpcu("a", ["a4", "c7", "d2"]), [])
        self.assertEqual(prosto_v_stolpcu("b", ["a4", "c7", "d2"]), ["b1"])
        self.assertEqual(prosto_v_stolpcu("b", ["a4", "c7", "d1", "d2"]), [])
        self.assertEqual(prosto_v_stolpcu("b", ["a4", "c7", "d1"]), ["b2"])
        self.assertCountEqual(prosto_v_stolpcu("f", ["a4", "c7", "d2"]),
            ["f1", "f3", "f5", "f6", "f8"])
        self.assertCountEqual(prosto_v_stolpcu("f", []),
            ["f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8"])

    def test_8prosto_polje(self):
        self.assertEqual(prosto_polje(["a4", "c7", "d2"]), "b1")
        self.assertEqual(prosto_polje(["a4", "c7", "d1"]), "b2")
        self.assertEqual(prosto_polje(["a3", "c7", "d1"]), "b5")
        self.assertEqual(prosto_polje(["a3", "b3", "c7", "d1"]), "e4")
        self.assertEqual(prosto_polje([]), "a1")
        self.assertEqual(prosto_polje(
            ["f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8"]), None)

    def test_9napadajoce_se(self):
        st = lambda nn: [tuple(sorted(x)) for x in nn]

        self.assertCountEqual(st(napadajoce_se(["a4", "b1", "b7"])),
            [('b1', 'b7')])
        self.assertCountEqual(st(napadajoce_se(["a4", "b1", "e8"])),
            [('a4', 'e8')])
        self.assertCountEqual(st(napadajoce_se(["a4", "b1", "e4"])),
            [('a4', 'e4'), ('b1', 'e4')])
        self.assertCountEqual(st(napadajoce_se(["a4", "b1", "e4", "f2"])),
            [('a4', 'e4'), ('b1', 'e4')])

        self.assertCountEqual(st(napadajoce_se(["a1", "a2", "a3", "a4"])),
            [('a1', 'a2'), ('a1', 'a3'), ('a2', 'a3'),
             ('a1', 'a4'), ('a2', 'a4'), ('a3', 'a4')])

        self.assertEqual(napadajoce_se(["a4", "b1"]), [])
        self.assertEqual(napadajoce_se(
            ["a4", "b1", "c5", "d8", "e2", "f7", "g3", "h6"]), [])

    def test_9legalna(self):
        self.assertTrue(legalna(["a4", "b1", "c5", "d8", "e2", "f7", "g3", "h6"]))
        self.assertFalse(legalna(["a4", "b1", "c5", "d8", "e2", "f7", "g3"]))
        self.assertFalse(legalna(["a4", "b1", "c5", "d8", "e2", "f7", "g3", "h3"]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
