

with open("razpored1.csv", "w", encoding="utf-8") as f:
    f.write("""potnik,voda,sedez
Ana,ne,12A,
Berta,da,8D,
Cilka,ne,8E,
Dani,da,13A,
Ema,ne,5E,
Fanči,da,12B,
Greta,ne,12C,
Helga,da,102E,
Iva,ne,4C,
Jana,da,5C""")

with open("razpored2.csv", "w", encoding="utf-8") as f:
    f.write("""potnik,koda1,koda2,voda,sedez,koda3
Ana,0,14,ne,12A,13
Berta,0,14,da,8D,13
Cilka,0,14,ne,8E,13
Dani,0,14,da,13F,13
Ema,0,14,ne,5E,13
Fanči,0,14,da,12D,13
Greta,0,14,ne,12E,13
Helga,0,14,da,102A,13
Iva,0,14,ne,4F,13
Jana,0,14,da,5D,13""")

import unittest
import warnings


class Test(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)

    def test_01_cena(self):
        zasedenost = np.array([
            [True, False, False, False, False, False],
            [False, True, True, False, False, False],
            [False, False, False, True, True, True],
            [False, False, False, True, True, True],
            [False, True, False, True, True, True],
            [False, False, False, True, True, False],
            [False, False, False, False, True, False]
        ])
        self.assertEqual(2990, cena(zasedenost, [200, 175, 193]))
        self.assertEqual(2815, cena(zasedenost[:-1], [200, 175, 193]))
        self.assertEqual(0, cena(zasedenost[:-1], [0, 0, 0]))
        self.assertEqual(0, cena(np.zeros((80, 6), dtype=bool), [200, 175, 193]))
        self.assertEqual(80 * (200 + 175 + 193) * 2, cena(np.ones((80, 6), dtype=bool), [200, 175, 193]))

    def test_02_stevilo_letov(self):
        leti = [(360, 420), (400, 580), (485, 1300), (490, 600), (600, 800),
                (650, 720), (700, 800), (780, 800), (930, 1380), (950, 1380), (950, 1000), (1100, 1200)]
        self.assertEqual(5, stevilo_letov((360, 420), leti))
        self.assertEqual(3, stevilo_letov((600, 880), leti))
        self.assertEqual(3, stevilo_letov((780, 800), leti))
        self.assertEqual(3, stevilo_letov((700, 800), leti))
        self.assertEqual(2, stevilo_letov((950, 1000), leti))
        self.assertEqual(1, stevilo_letov((950, 1380), leti))

    def test_03_razpored(self):
        zelje = [("Ana", "12A"), ("Berta", "8D"), ("Ema", "5E"), ("Iva", "12C"),
                 ("Cilka", "8D"), ("Fanči", "12A"), ("Dani", "13A"), ("Greta", "12A"),
                 ("Helga", "4E"), ("Jana", "6E"), ("Klara", "5E"),
                 ("Liza", "123E"), ("Micka", "123F"), ("Nina", "123E")]
        self.assertEqual(
            [("Ana", "12A"), ("Berta", "8D"), ("Ema", "5E"), ("Iva", "12C"),
             ("Cilka", "9D"), ("Fanči", "13A"), ("Dani", "14A"), ("Greta", "15A"),
             ("Helga", "4E"), ("Jana", "6E"), ("Klara", "7E"),
             ("Liza", "123E"), ("Micka", "123F"), ("Nina", "124E")],
            razpored(zelje))

    def test_04_ravnotezje(self):
        self.assertEqual(-2, ravnotezje("razpored1.csv"))
        self.assertEqual(6, ravnotezje("razpored2.csv"))

    def test_05_vozni_redi(self):
        vozni_redi([("Ana Argon", "LH2832", (12, 10), (13, 20)),
                    ("Berta Bor", "UO391", (15, 5), (20, 30)),
                    ("Cilka Cankar", "LH192", (7, 0), (12, 30))],
                   "vozni_redi.txt")
        with open("vozni_redi.txt", "r", encoding="utf-8") as f:
            self.assertEqual("""
Ana Argon            LH2832   12:10-13:20
Berta Bor             UO391   15:05-20:30
Cilka Cankar          LH192    7:00-12:30""".lstrip(), f.read().rstrip())


if __name__ == "__main__":
    unittest.main()
