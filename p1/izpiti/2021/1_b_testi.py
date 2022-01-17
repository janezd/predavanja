

import unittest
from random import randint
import os

class Test(unittest.TestCase):
    def test_01_uravnotezena(self):
        self.assertTrue(uravnotezena([3, 7, 5, 1, 3, 5]))
        self.assertTrue(uravnotezena([3, 17, 5, 1, 3, 5, 2]))
        self.assertFalse(uravnotezena([3, 17, 5, 1, 3, 5, 1]))
        self.assertFalse(uravnotezena([11]))
        self.assertTrue(uravnotezena([10]))
        self.assertTrue(uravnotezena([]))

    def test_02_deli(self):
        paketi = [
            6,  # 0:6:0, ker ne more na 0
            4,  # 4:6:0
            2,  # 4:6:2 (na ladji 2 je najmanj)
            1,  # 4:6:3
            5,  # 4:11:3 (na 0 in 1 ne more)
            1,  # 4:11:4 (na ladji 2 je najmanj)
            15,  # 4:11:4 (ne more nikamor)
            1,  # 5:11:4 na ladjo 0 (ker je na 0 in 2 najmanj in 2 je prej)
        ]
        self.assertEqual([5, 11, 4], deli(paketi, [5, 20, 7]))
        self.assertEqual([6, 4, 2, 1, 5, 1, 1, 0, 0],
                         deli(paketi, [10] * 9))

    def test_03_kontrola(self):
        kontrola
        fname = f"nacrt{randint(0, 9999):04}.txt"
        with open(fname, "wt", encoding="utf-8") as f:
            f.write("""Orgum: 15: 3, 5, 7
Gubgat: 20: 10, 5, 6
Thrombaq: 5: 1
Thrombaq 2: 5: 1, 4
Humwat Bolwat: 10: 2, 2, 2, 2, 2, 2
Askeg 8: 13: 14""")
        self.assertEqual(
            {"Gubgat", "Askeg 8", "Humwat Bolwat"}, kontrola(fname)
        )
        os.remove(fname)

    def test_04_pravilna(self):
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
        antene = {
            "Adam": 111, "Matjaž": 90, "Cilka": 88, "Daniel": 85, "Erik": 83,
            "Viljem": 58, "Tadeja": 20, "Elizabeta": 68, "Hans": 64, "Ludvik": 50,
            "Jurij": 49, "Barbara": 45, "Herman": 39, "Mihael": 32, "Franc": 30,
            "Jožef": 29, "Margareta": 3, "Alenka": 9, "Aleksander": 5, "Petra": 7}

        self.assertFalse(pravilna("Adam", hierarhija, antene))
        self.assertTrue(pravilna("Elizabeta", hierarhija, antene))
        antene["Erik"] = 5
        self.assertTrue(pravilna("Adam", hierarhija, antene))
        antene["Franc"] = 50
        self.assertFalse(pravilna("Elizabeta", hierarhija, antene))
        self.assertFalse(pravilna("Adam", hierarhija, antene))

    def test_05_ladja(self):
        ladja = Ladja()
        ladja.nalozi("Paradižnik v grozdu", 5)
        ladja.nalozi("Paradižnik v grozdu", 15)
        ladja.nalozi("Prha", 4)
        ladja.nalozi("Španski zeleni", 2)
        ladja.nalozi("Prha", 8)
        ladja.nalozi("Nizozemski kockasti", 8)
        self.assertEqual(20, ladja.kolicina("Paradižnik v grozdu"))
        self.assertEqual(12, ladja.kolicina("Prha"))
        self.assertEqual(0, ladja.kolicina("Nizozemski kockasti"))
        ladja.nalozi("Nizozemski kockasti", 8)
        self.assertEqual(0, ladja.kolicina("Nizozemski kockasti"))


if __name__ == "__main__":
    unittest.main()

