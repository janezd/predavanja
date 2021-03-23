import unittest

prevodi = [("v_slovar", "to_dict"),
           ("v_pare", "to_pairs"),
           ("n_znancev", "n_friends"),
           ("osamljeni", "lonely"),
           ("najbolj_znan", "most_known"),
           ("skupni_znanci", "common_friends"),
           ("po_znancih", "by_n_friends"),
           ("priporocila", "suggestions"),
           ("klika", "clique"),
           ("najvec_skupnih", "most_commons"),
           ("neznanci", "strangers"),
           ("je_pokritje", "is_cover"),
           ("trikotniki", "triangles"),
           ("najmanjse_pokritje", "minimal_cover")]
globals().update({slov: globals()[angl]
                  for slov, angl in prevodi if angl in globals()})

class Testi(unittest.TestCase):
    def setUp(self):
        A, B, C, D = "ABCD"
        self.mali_pari = {(A, B), (A, C), (B, C), (C, D)}
        self.mala_mreza = {A: {B, C}, B: {A, C}, C: {A, B, D}, D: {C}}

        self.pari = {("Ana", "Berta"), ("Ana", "Greta"), ("Ana", "Helga"),
                     ("Berta", "Cilka"), ("Berta", "Helga"),
                     ("Cilka", "Dani"),
                     ("Dani", "Ema"), ("Dani", "Greta"), ("Dani", "Helga"),
                     ("Ema", "Fanči"), ("Ema", "Greta"), ("Ema", "Helga"),
                     ("Fanči", "Iva"), ("Fanči", "Jana"), ("Fanči", "Klavdija"),
                     ("Greta", "Helga")}

        self.mreza = {"Ana": {"Berta", "Greta", "Helga"},
                      "Berta": {"Ana", "Helga", "Cilka"},
                      "Cilka": {"Berta", "Dani"},
                      "Dani": {"Cilka", "Ema", "Greta", "Helga"},
                      "Ema": {"Dani", "Fanči", "Greta", "Helga"},
                      "Fanči": {"Ema", "Iva", "Jana", "Klavdija"},
                      "Greta": {"Ana", "Dani", "Ema", "Helga"},
                      "Helga": {"Ana", "Berta", "Dani", "Ema", "Greta"},
                      "Iva": {"Fanči"},
                      "Jana": {"Fanči"},
                      "Klavdija": {"Fanči"}
                      }

class Test06(Testi):
    def test_v_slovar(self):
        self.assertEqual(v_slovar({("A", "B")}), {"A": {"B"}, "B": {"A"}})
        self.assertEqual(v_slovar(self.mali_pari), self.mala_mreza)
        self.assertEqual(v_slovar(self.pari), self.mreza)

    def test_v_pare(self):
        self.assertEqual(v_pare({"A": {"B"}, "B": {"A"}}), {("A", "B")})
        self.assertEqual(v_pare(self.mala_mreza), self.mali_pari)
        self.assertEqual(v_pare(self.mreza), self.pari)

    def test_n_znancev(self):
        self.assertEqual(n_znancev(self.mala_mreza, 1), {"D"})
        self.assertEqual(n_znancev(self.mala_mreza, 2), {"A", "B"})
        self.assertEqual(n_znancev(self.mala_mreza, 3), {"C"})
        self.assertEqual(n_znancev(self.mala_mreza, 4), set())
        self.assertEqual(n_znancev(self.mala_mreza, 5), set())
        self.assertEqual(n_znancev(self.mala_mreza, 42), set())

        self.assertEqual(n_znancev(self.mreza, 2), {"Cilka"})
        self.assertEqual(n_znancev(self.mreza, 3), {"Ana", "Berta"})
        self.assertEqual(n_znancev(self.mreza, 6), set())
        self.assertEqual(n_znancev(self.mreza, 6), set())

    def test_osamljeni(self):
        self.assertEqual(osamljeni({"A": {"B"}, "B": {"A"}}), {"A", "B"})
        self.assertEqual(osamljeni(self.mala_mreza), {"D"})
        self.assertEqual(osamljeni(self.mreza), {"Klavdija", "Iva", "Jana"})

    def test_najbolj_znan(self):
        self.assertEqual(najbolj_znan(self.mala_mreza), "C")
        self.assertEqual(najbolj_znan(self.mreza), "Helga")

    def test_skupni_znanci(self):
        self.assertEqual(skupni_znanci(self.mreza, "Iva", "Jana"), {"Fanči"})
        self.assertEqual(skupni_znanci(self.mreza, "Fanči", "Dani"), {"Ema"})
        self.assertEqual(skupni_znanci(self.mreza, "Greta", "Helga"), {"Ana", "Dani", "Ema"})
        self.assertEqual(skupni_znanci(self.mreza, "Greta", "Ana"), {"Helga"})
        self.assertEqual(skupni_znanci(self.mreza, "Fanči", "Berta"), set())

class Test07(Testi):
    def test_po_znancih(self):
        self.assertEqual(po_znancih(self.mala_mreza),
                         {1: {"D"}, 2: {"A", "B"}, 3: {"C"}})
        self.assertEqual(po_znancih(self.mreza),
                         {1: {"Iva", "Klavdija", "Jana"},
                          2: {"Cilka"},
                          3: {"Ana", "Berta"},
                          4: {"Dani", "Ema", "Fanči", "Greta"},
                          5: {"Helga"},
                          6: set(),
                          7: set(),
                          8: set(),
                          9: set(),
                          10: set()
                          })

    def test_priporocila(self):
        self.assertEqual(priporocila(self.mala_mreza), {("A", "D"), ("B", "D")})
        self.assertEqual(priporocila(self.mreza),
                         {('Ana', 'Cilka'),
                          ('Ana', 'Dani'),
                          ('Ana', 'Ema'),
                          ('Berta', 'Dani'),
                          ('Berta', 'Ema'),
                          ('Berta', 'Greta'),
                          ('Cilka', 'Ema'),
                          ('Cilka', 'Greta'),
                          ('Cilka', 'Helga'),
                          ('Dani', 'Fanči'),
                          ('Ema', 'Iva'),
                          ('Ema', 'Jana'),
                          ('Ema', 'Klavdija'),
                          ('Fanči', 'Greta'),
                          ('Fanči', 'Helga'),
                          ('Iva', 'Jana'),
                          ('Iva', 'Klavdija'),
                          ('Jana', 'Klavdija')})

    def test_klika(self):
        self.assertTrue(klika(self.mala_mreza, {"A", "B", "C"}))
        self.assertTrue(klika(self.mala_mreza, {"A", "B"}))
        self.assertTrue(klika(self.mala_mreza, {"A"}))
        self.assertTrue(klika(self.mala_mreza, set()))
        self.assertFalse(klika(self.mala_mreza, {"A", "C", "D"}))
        self.assertFalse(klika(self.mala_mreza, {"A", "D"}))

        self.assertTrue(klika(self.mreza, {"Greta", "Helga", "Ema", "Dani"}))
        self.assertTrue(klika(self.mreza, {"Greta", "Helga", "Ana"}))
        self.assertFalse(klika(self.mreza, {"Greta", "Helga", "Ana", "Berta"}))

    def test_najvec_skupnih(self):
        self.assertEqual(najvec_skupnih(self.mreza), ("Greta", "Helga"))

class Test08(Testi):
    def test_neznanci(self):
        self.assertTrue(neznanci(self.mala_mreza, {"A", "D"}))
        self.assertFalse(neznanci(self.mala_mreza, {"A", "B", "D"}))

        self.assertTrue(
            neznanci(self.mreza, {"Ana", "Cilka", "Ema", "Iva", "Klavdija", "Jana"}))
        self.assertFalse(
            neznanci(self.mreza, {"Ana", "Berta", "Cilka", "Ema", "Iva", "Klavdija", "Jana"}))

    def test_je_pokritje(self):
        self.assertTrue(je_pokritje(self.mala_mreza, {"C"}))
        self.assertTrue(je_pokritje(self.mala_mreza, {"A", "C", "D"}))
        self.assertTrue(je_pokritje(self.mala_mreza, {"A", "B", "D"}))
        self.assertTrue(je_pokritje(self.mala_mreza, {"B", "C"}))
        self.assertTrue(je_pokritje(self.mala_mreza, {"A", "B", "C", "D"}))

        self.assertFalse(je_pokritje(self.mala_mreza, {"A"}))
        self.assertFalse(je_pokritje(self.mala_mreza, {"A", "B"}))

        self.assertTrue(je_pokritje(self.mreza, {"Fanči", "Helga", "Cilka"}))
        self.assertTrue(je_pokritje(self.mreza, {"Fanči", "Greta", "Cilka"}))
        self.assertTrue(je_pokritje(self.mreza, {"Fanči", "Ema", "Berta"}))
        self.assertTrue(je_pokritje(self.mreza, {"Fanči", "Ema", "Ana", "Cilka"}))

        self.assertFalse(je_pokritje(self.mreza, {"Fanči", "Ema", "Ana"}))

    def test_trikotniki(self):
        self.assertEqual(trikotniki(self.mala_mreza), 1)
        self.assertEqual(trikotniki(self.mreza), 6)

class Test09(Testi):
    def test_najmanjse_pokritje(self):
        self.assertEqual(najmanjse_pokritje(self.mala_mreza), {"C"})
        self.assertIn(najmanjse_pokritje(self.mreza),
                      [{'Fanči', 'Ema', 'Berta'},
                       {'Fanči', 'Dani', 'Ana'},
                       {'Fanči', 'Dani', 'Berta'},
                       {'Fanči', 'Dani', 'Helga'},
                       {'Fanči', 'Ana', 'Cilka'},
                       {'Fanči', 'Berta', 'Greta'},
                       {'Fanči', 'Greta', 'Cilka'},
                       {'Fanči', 'Helga', 'Berta'},
                       {'Fanči', 'Helga', 'Cilka'}])

if __name__ == "__main__":
    unittest.main()

