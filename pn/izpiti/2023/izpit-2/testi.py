# Svojo rešitev pišite sem.
# Najboljše je, da pustite teste v datoteki z rašitvijo, da ne bi ponesreči pobrisali preveč.





with open("sporocilo1.txt", "w", encoding="utf-8") as f:
    f.write("""Spoštovani,
    
potrjujemo nakup vozovnice. Detajli so zapisani spodaj.

Posebne želje: nima posebnih želja.
Ime potnika: Janez Tone Novak
Starost: 34
Cena: 184E

Dodelili smo vam sedež 12A, kot ste želeli.
""")

with open("sporocilo2.txt", "w", encoding="utf-8") as f:
    f.write("""Spoštovani potnik
    
z naslednjim lepim imenom: Joze Ivanovic Merzel Hartmansgruber
ima dodeljen želje: 8D. Prosim, da se obrnete na našo pomoč strankam, če imate kakšne posebne želje.

Github Copilot tu dodaja še nekaj besedila, ki ga ne potrebujemo. Konkretno, tole je popolnoma nepotrebno.
Zdaj bom nehal ponavljati, da je to nepotrebno, ker je to že postalo nepotrebno. Torej,  
""")


with open("sporocilo3.txt", "w", encoding="utf-8") as f:
    f.write("""Tole nima zveze z letalskimi kartami (192A), pač pa
    nekdo gleda film v 3D.
    In zdaj (194A).
    
Podpis: ni podpisa  
""")

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

    def test_02_preberi_sporocilo(self):
        self.assertEqual(("Janez Tone Novak", "12A"), preberi_sporocilo("sporocilo1.txt"))
        self.assertEqual(("Joze Ivanovic Merzel Hartmansgruber", "8D"), preberi_sporocilo("sporocilo2.txt"))
        self.assertEqual((None, "3D"), preberi_sporocilo("sporocilo3.txt"))

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
