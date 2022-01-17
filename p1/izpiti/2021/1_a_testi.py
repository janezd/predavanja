
import unittest
from random import randint
import os

class Test(unittest.TestCase):
    def test_01_paketov(self):
        self.assertEqual(2, paketov([5, 3, 8, 1, 2, 6], 9))
        self.assertEqual(2, paketov([5, 3, 8, 1, 2, 6], 8))
        self.assertEqual(2, paketov([5, 3, 8, 1, 2, 6], 15))
        self.assertEqual(3, paketov([5, 3, 8, 1, 2, 6], 16))
        self.assertEqual(1, paketov([5, 3, 8, 1, 2, 6], 5))
        self.assertEqual(1, paketov([5, 3, 8, 1, 2, 6], 6))
        self.assertEqual(0, paketov([5, 3, 8, 1, 2, 6], 4))
        self.assertEqual(6, paketov([5, 3, 8, 1, 2, 6], 25))
        self.assertEqual(6, paketov([5, 3, 8, 1, 2, 6], 30))
        self.assertEqual(6, paketov([5, 3, 8, 1, 2, 6], 50))
        self.assertEqual(2, paketov([5, 3], 50))
        self.assertEqual(1, paketov([5], 50))
        self.assertEqual(0, paketov([], 50))

    def test_02_razporedi(self):
        paketi = [5, 3, 8, 1, 2, 3, 5, 4, 2, 4]
        self.assertEqual([[5, 3, 1], [8], [2, 3, 4], [5, 2], [4]],
                         razporedi(paketi, 9))
        self.assertEqual(paketi, [5, 3, 8, 1, 2, 3, 5, 4, 2, 4])

    def test_03_popis(self):
        popis  # če funkcije ni, ne sestavljaj datoteke
        fname = f"inventar{randint(0, 9999):04}.txt"
        kraj = f"Kraj{randint(100, 200)}"
        with open(fname, "wt", encoding="utf-8") as f:
            f.write(f"""Ljubljana: paradižnik 18
Maribor: rumena koleraba 5
Ljubljana: rdeča pesa 13
Ljubljana: paradižnik 5
{kraj}: paradižnik 3
Škofja Loka: buče 5
Škofja Loka: paradižnik 1
""")
        self.assertEqual(
            {"Ljubljana": 23, kraj: 3, "Škofja Loka": 1},
            popis(fname))
        # Če test pade, naj datoteka ostane ...
        os.remove(fname)

    def test_04_skladiscniki(self):
        hierarhija = {
            "Adam": ["Matjaž", "Cilka", "Daniel"],
            "Aleksander": [],
            "Alenka": [],
            "Barbara": [],
            "Cilka": [],
            "Daniel": ["Elizabeta", "Hans"],
            "Erik": [],
            "Elizabeta": ["Ludvik", "Jurij", "Barbara"],
            "Franc": [],
            "Herman": ["Margareta"],
            "Hans": ["Herman", "Erik"],
            "Jožef": ["Alenka", "Aleksander", "Petra"],
            "Jurij": ["Franc", "Jožef"],
            "Ludvik": [],
            "Margareta": [],
            "Matjaž": ["Viljem"],
            "Petra": [],
            "Tadeja": [],
            "Viljem": ["Tadeja"],
        }
        self.assertEqual(10, skladiscniki("Adam", hierarhija))
        self.assertEqual(6, skladiscniki("Elizabeta", hierarhija))
        self.assertEqual(3, skladiscniki("Jožef", hierarhija))
        self.assertEqual(1, skladiscniki("Petra", hierarhija))
        self.assertEqual(2, skladiscniki("Hans", hierarhija))

    def test_05_ladja(self):
        ladja = Ladja()
        self.assertFalse(ladja.nalozi(12)) #  ne gre -- [12 : 0]
        self.assertEqual(0, ladja.obremenitev())
        self.assertTrue(ladja.nalozi(8))  # 8 : 0
        self.assertEqual(8, ladja.obremenitev())
        self.assertTrue(ladja.nalozi(12)) # 8 : 12
        self.assertEqual(20, ladja.obremenitev())
        self.assertTrue(ladja.nalozi(12)) # 20 : 12
        self.assertEqual(32, ladja.obremenitev())
        self.assertFalse(ladja.nalozi(19)) #  ne gre -- [20 : 31]
        self.assertEqual(32, ladja.obremenitev())
        self.assertFalse(ladja.nalozi(21)) #  ne gre -- [20 : 33]
        self.assertEqual(32, ladja.obremenitev())
        self.assertFalse(ladja.nalozi(19)) #  ne gre -- [20 : 33]
        self.assertEqual(32, ladja.obremenitev())
        self.assertTrue(ladja.nalozi(5)) # 20 : 17
        self.assertEqual(37, ladja.obremenitev())
        self.assertFalse(ladja.nalozi(8)) #    [28 : 17]
        self.assertEqual(37, ladja.obremenitev())
        self.assertTrue(ladja.nalozi(3)) # 23 : 17
        self.assertEqual(40, ladja.obremenitev())


if __name__ == "__main__":
    unittest.main()

