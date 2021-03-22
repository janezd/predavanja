import unittest

class TestKonj(unittest.TestCase):
    def test_pretvorba(self):
        for r, x in enumerate("ABCDEFGH"):
            for y in range(1, 9):
                self.assertEqual((r+1, y), polje_v_koord(x+str(y)))
                self.assertEqual(x+str(y), koord_v_polje(r+1, y))

    def test_legalne(self):
        for y in range(1, 9):
            for x in range(1, 9):
                self.assertTrue(legalne_koord(x, y))
        self.assertFalse(legalne_koord(0, 1))
        self.assertFalse(legalne_koord(1, 0))
        self.assertFalse(legalne_koord(0, 0))
        self.assertFalse(legalne_koord(-5, 5))
        self.assertFalse(legalne_koord(9, 2))
        self.assertFalse(legalne_koord(2, 9))
        self.assertFalse(legalne_koord(9, 9))

    def test_moznosti(self):
        self.assertEqual(moznosti("A1"), ["B3", "C2"])
        self.assertEqual(moznosti("A2"), ["B4", "C1", "C3"])
        self.assertEqual(moznosti("A3"), ["B1", "B5", "C2", "C4"])
        self.assertEqual(moznosti("A4"), ["B2", "B6", "C3", "C5"])
        self.assertEqual(moznosti("A8"), ["B6", "C7"])
        self.assertEqual(moznosti("B2"), ["A4", "C4", "D1", "D3"])
        self.assertEqual(moznosti("B5"), ["A3", "A7", "C3", "C7", "D4", "D6"])
        self.assertEqual(moznosti("D1"), ["B2", "C3", "E3", "F2"])
        self.assertEqual(moznosti("D2"), ["B1", "B3", "C4", "E4", "F1", "F3"])
        self.assertEqual(moznosti("D3"), ["B2", "B4", "C1", "C5", "E1", "E5", "F2", "F4"])
        self.assertEqual(moznosti("G1"), ["E2", "F3", "H3"])
        self.assertEqual(moznosti("G2"), ["E1", "E3", "F4", "H4"])
        self.assertEqual(moznosti("G3"), ["E2", "E4", "F1", "F5", "H1", "H5"])
        self.assertEqual(moznosti("H1"), ["F2", "G3"])
        self.assertEqual(moznosti("H2"), ["F1", "F3", "G4"])
        self.assertEqual(moznosti("H3"), ["F2", "F4", "G1", "G5"])
        self.assertEqual(moznosti("H7"), ["F6", "F8", "G5"])
        self.assertEqual(moznosti("H8"), ["F7", "G6"])
        self.assertEqual(moznosti("D8"), ["B7", "C6", "E6", "F7"])
        self.assertEqual(moznosti("D7"), ["B6", "B8", "C5", "E5", "F6", "F8"])
        self.assertEqual(moznosti("D6"), ["B5", "B7", "C4", "C8", "E4", "E8", "F5", "F7"])

    def test_legalna(self):
        self.assertTrue(legalna("A1", "C2"))
        self.assertTrue(legalna("A3", "C2"))
        self.assertTrue(legalna("C2", "A1"))
        self.assertTrue(legalna("C2", "A3"))

        self.assertTrue(legalna("D4", "B3"))
        self.assertTrue(legalna("D4", "B5"))
        self.assertTrue(legalna("D4", "C2"))
        self.assertTrue(legalna("D4", "C6"))
        self.assertTrue(legalna("D4", "E2"))
        self.assertTrue(legalna("D4", "E6"))
        self.assertTrue(legalna("D4", "F3"))
        self.assertTrue(legalna("D4", "F5"))

        self.assertFalse(legalna("D4", "D4"))

        self.assertFalse(legalna("D4", "D6"))
        self.assertFalse(legalna("D4", "D2"))
        self.assertFalse(legalna("D4", "B4"))
        self.assertFalse(legalna("D4", "B6"))
        self.assertFalse(legalna("D4", "E5"))
        self.assertFalse(legalna("D4", "E7"))
        self.assertFalse(legalna("D4", "C5"))
        self.assertFalse(legalna("D4", "C7"))
        self.assertFalse(legalna("D4", "F6"))
        self.assertFalse(legalna("D4", "B6"))
        self.assertFalse(legalna("D4", "B2"))
        self.assertFalse(legalna("D4", "F2"))

    def test_legalna_pot(self):
        self.assertTrue(legalna_pot("A2 B4 A2 C3 D5 B6 D5 B4 D3 F2 G4".split()))

        self.assertFalse(legalna_pot("A2 B5 A2 C3 D5 B6 D5 B4 E3 G2 G4".split()))
        self.assertFalse(legalna_pot("A2 B4 A2 C3 D5 B6 D5 B4 D3 F2 F2".split()))

    def test_obhod(self):
        self.assertTrue(obhod("D4 F5 D6 E8 C7 A8 B6 A4 B2 D1 F2 H1 G3 H5 G7 E6 F8 D7 B8 A6 B4 A2 C1 E2 G1 H3 F4 D3 C5 E4 C3 D5 E3 C4 E5 C6 D8 B7 A5 B3 A1 C2 E1 G2 H4 G6 H8 F7 H6 G4 H2 F1 D2 B1 A3 B5 A7 C8 E7 G8 F6 H7 G5 F3 D4".split()))
        self.assertTrue(obhod("F3 D4 F5 D6 E8 C7 A8 B6 A4 B2 D1 F2 H1 G3 H5 G7 E6 F8 D7 B8 A6 B4 A2 C1 E2 G1 H3 F4 D3 C5 E4 C3 D5 E3 C4 E5 C6 D8 B7 A5 B3 A1 C2 E1 G2 H4 G6 H8 F7 H6 G4 H2 F1 D2 B1 A3 B5 A7 C8 E7 G8 F6 H7 G5 F3".split()))

        # Ne ponovi zadnjega polja
        self.assertFalse(obhod("D4 F5 D6 E8 C7 A8 B6 A4 B2 D1 F2 H1 G3 H5 G7 E6 F8 D7 B8 A6 B4 A2 C1 E2 G1 H3 F4 D3 C5 E4 C3 D5 E3 C4 E5 C6 D8 B7 A5 B3 A1 C2 E1 G2 H4 G6 H8 F7 H6 G4 H2 F1 D2 B1 A3 B5 A7 C8 E7 G8 F6 H7 G5 F3".split()))

        # Prekratko
        self.assertFalse(obhod("D4 F5 D6 E8 C7 A8 B6 A4 B2 D1 F2 H1 G3 H5 G7 E6 F8 D7 B8 A6 B4 A2 C1 E2 G1 H3 F4 D3 C5 E4 C3 D5 E3 C4 E5 C6 D8 B7 A5 B3 A1 C2 E1 G2 H4 G6 H8 F7 H6 G4 H2 F1 D2 B1 A3 B5 A7 C8 E7 G8 F6".split()))

        # Samo štiri polja
        self.assertFalse(obhod("D4 E6 G5 F3 D4".split()))

        # Samo štiri polja
        self.assertFalse(obhod("D4 E6 G5 F3 D4 E6 G5 F3 D4 E6 G5 F3 D4 E6 G5 F3 D4 E6 G5 F3 D4 E6 G5 F3 D4 E6 G5 F3 D4 E6 G5 F3 D4 E6 G5 F3 D4 E6 G5 F3 D4 E6 G5 F3 D4 E6 G5 F3 D4 E6 G5 F3 D4 E6 G5 F3 D4 E6 G5 F3 D4 E6 G5 F3 D4".split()))

        # Še bolj prekratko
        self.assertFalse(obhod(["D4"]))

        # Ponovi polje G4
        self.assertFalse(obhod("D4 F5 D6 E8 C7 A8 B6 A4 B2 D1 F2 H1 G3 H5 G7 E6 F8 D7 B8 A6 B4 A2 C1 E2 G1 H3 F4 D3 C5 E4 C3 D5 E3 G4 E5 C6 D8 B7 A5 B3 A1 C2 E1 G2 H4 G6 H8 F7 H6 G4 H2 F1 D2 B1 A3 B5 A7 C8 E7 G8 F6 H7 G5 F3 D4".split()))

    def test_razdalje(self):
        self.assertEqual(razdalje().strip(),
            "03232345\n34123434\n21432345\n32323434\n23234345\n34343454\n43434545\n54545456")

if __name__ == '__main__':
    unittest.main(verbosity=2)
