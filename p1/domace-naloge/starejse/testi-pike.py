import unittest
from functools import reduce
from operator import iadd
from copy import deepcopy


class TestStevilcnica(unittest.TestCase):
    def test_5_dopolni(self):
        polje = [[] for i in range(5)]
        dopolni(polje, 10)
        self.assertEqual(len(polje), 5)
        self.assertTrue(all(len(stolpec) == 10 for stolpec in polje))
        vse_stevilke = reduce(iadd, polje, [])
        for i in range(1, 6):
            self.assertGreaterEqual(
                vse_stevilke.count(i), 2,
                "Med 50 številkami bi pričakoval vsaj dve številki {}".format(i)
            )

        zacetek = [[1], [4, 1], [2, 1, 4], [], [1, 2, 3, 4]]
        polje = zacetek.copy()
        dopolni(polje, 4)
        for stolpec, zstolpec in zip(polje, zacetek):
            self.assertEqual(stolpec[:len(zstolpec)], zstolpec,
                             "'dopolni' ne sme spreminjati obstoječih številk")
            self.assertEqual(len(zstolpec), 4)

    def test_6_izpis(self):
        polje = [[1, 2, 4, 4],
                 [4, 1, 4, 2],
                 [2, 1, 4, 3],
                 [2, 4, 2, 3],
                 [1, 2, 3, 4]]
        self.assertEqual(izpisi(polje).strip(), "42334\n44423\n21142\n14221")

        polje = [[1], [4], [2], [2], [1]]
        self.assertEqual(izpisi(polje).strip(), "14221")

        polje = [[1, 4, 2, 2, 1]]
        self.assertEqual(izpisi(polje).strip(), "1\n2\n2\n4\n1")

    def test_7_pobrisi_pot(self):
        polje = [[1, 2, 4, 4],
                 [4, 1, 4, 2],
                 [2, 1, 4, 3],
                 [2, 4, 2, 3],
                 [1, 2, 3, 4]]

        pobrisi_pot([(0, 1), (1, 1), (2, 1)], polje)
        self.assertEqual(polje, [[1, 4, 4],
                                 [4, 4, 2],
                                 [2, 4, 3],
                                 [2, 4, 2, 3],
                                 [1, 2, 3, 4]])

        polje = [[0, 1, 2, 3, 4],
                 [4, 4, 2, 2, 2]]
        pobrisi_pot([(0, 1), (0, 2)], polje)
        self.assertEqual(polje, [[0, 3, 4],
                                 [4, 4, 2, 2, 2]])

        polje = [[0, 1, 2, 3, 4],
                 [4, 4, 2, 2, 2]]
        pobrisi_pot([(0, 2), (0, 1)], polje)
        self.assertEqual(polje, [[0, 3, 4],
                                 [4, 4, 2, 2, 2]])

        polje = [[0, 1, 2, 3, 4],
                 [4, 4, 2, 2, 2]]
        pobrisi_pot([(0, 2), (0, 4), (0, 0), (0, 3), (0, 1)], polje)
        self.assertEqual(polje, [[],
                                 [4, 4, 2, 2, 2]])


    def test_7_pobrisi_barvo(self):
        polje = [[1, 2, 4, 4],
                 [4, 1, 4, 2],
                 [2, 1, 4, 3],
                 [2, 4, 2, 3],
                 [1, 2, 3, 4]]

        polje2 = deepcopy(polje)
        pobrisi_barvo(1, polje2)
        self.assertEqual(polje2, [[2, 4, 4],
                                  [4, 4, 2],
                                  [2, 4, 3],
                                  [2, 4, 2, 3],
                                  [2, 3, 4]])

        polje2 = deepcopy(polje)
        pobrisi_barvo(2, polje2)
        self.assertEqual(polje2, [[1, 4, 4],
                                  [4, 1, 4],
                                  [1, 4, 3],
                                  [4, 3],
                                  [1, 3, 4]])

        polje2 = deepcopy(polje)
        pobrisi_barvo(3, polje2)
        self.assertEqual(polje2, [[1, 2, 4, 4],
                                  [4, 1, 4, 2],
                                  [2, 1, 4],
                                  [2, 4, 2],
                                  [1, 2, 4]])

        polje2 = deepcopy(polje)
        pobrisi_barvo(4, polje2)
        self.assertEqual(polje2, [[1, 2],
                                  [1, 2],
                                  [2, 1, 3],
                                  [2, 2, 3],
                                  [1, 2, 3]])

        polje2 = deepcopy(polje)
        pobrisi_barvo(5, polje2)
        self.assertEqual(polje2, [[1, 2, 4, 4],
                                  [4, 1, 4, 2],
                                  [2, 1, 4, 3],
                                  [2, 4, 2, 3],
                                  [1, 2, 3, 4]])

    def test_8_preveri_pot(self):
        polje = [[1, 2, 4, 4],
                 [4, 1, 4, 2],
                 [2, 1, 4, 3],
                 [2, 4, 2, 3],
                 [1, 2, 3, 4]]

        polje4 = [[4] * 4] * 5

        self.assertTrue(preveri_pot([(1, 1), (2, 1)], polje))
        self.assertTrue(preveri_pot([(0, 2), (0, 3)], polje))
        self.assertTrue(preveri_pot([(0, 2), (1, 2), (2, 2)], polje))
        self.assertTrue(preveri_pot([(2, 2), (1, 2), (0, 2), (0, 3)], polje))

        self.assertTrue(preveri_pot([(2, 2), (1, 2), (1, 1), (2, 1), (2, 2)],
                                    polje4))
        self.assertTrue(preveri_pot([(1, 1), (1, 2), (1, 3), (2, 3), (3, 3),
                                     (3, 2), (2, 2), (2, 1), (1, 1)],
                                    polje4))

        self.assertFalse(preveri_pot([(1, 1)], polje))
        self.assertFalse(preveri_pot([(1, 1), (2, 2)], polje4),
                         "Diagonale so prepovedane")
        self.assertFalse(preveri_pot([(0, 2), (2, 2)], polje4),
                         "Dovoljeni so le premiki za eno polje")
        self.assertFalse(preveri_pot([(1, 2), (0, 2), (2, 2)], polje4),
                         "Dovoljeni so le premiki za eno polje")
        self.assertFalse(preveri_pot([(0, 2), (2, 2), (1, 2)], polje4),
                         "Dovoljeni so le premiki za eno polje")
        self.assertFalse(preveri_pot([(2, 2), (0, 2)], polje4),
                         "Dovoljeni so le premiki za eno polje")
        self.assertFalse(preveri_pot([(1, 0), (1, 2)], polje4),
                         "Dovoljeni so le premiki za eno polje")
        self.assertFalse(preveri_pot([(1, 2), (1, 0)], polje4),
                         "Dovoljeni so le premiki za eno polje")
        self.assertFalse(preveri_pot([(1, 0), (4, 3)], polje4),
                         "Dovoljeni so le premiki za eno polje")
        self.assertFalse(preveri_pot([(0, 0), (1, 0), (2, 0), (3, 0), (3, 1),
                                      (3, 2), (5, 2), (5, 3), (5, 4)], polje4),
                         "Dovoljeni so le premiki za eno polje")

        self.assertFalse(preveri_pot([(1, 3), (1, 2), (2, 2), (1, 2)], polje4),
                         "Polja se ne smejo ponavljati")
        self.assertFalse(preveri_pot([(2, 2), (2, 1), (2, 0), (2, 1), (2, 2)],
                                     polje4),
                         "Polja se ne smejo ponavljati")

        self.assertFalse(preveri_pot([(0, 2), (1, 2), (2, 2), (2, 3)], polje),
                         "Vsa polja na poti morajo biti enake barve")
        self.assertFalse(preveri_pot([(0, 2), (1, 2), (2, 2), (2, 3), (3, 3)],
                                     polje),
                         "Vsa polja na poti morajo biti enake barve")
        self.assertFalse(preveri_pot([(1, 2), (2, 2), (2, 3), (3, 3)], polje),
                         "Vsa polja na poti morajo biti enake barve")
        self.assertFalse(preveri_pot([(2, 2), (2, 3), (3, 3)], polje),
                         "Vsa polja na poti morajo biti enake barve")
        self.assertFalse(preveri_pot([(2, 2), (2, 3), (2, 2)], polje),
                         "Vsa polja na poti morajo biti enake barve")

        self.assertFalse(preveri_pot([(0, 0), (-1, 0), (-1, 1)], polje4),
                         "Pot ne sme zapustiti polja")
        self.assertFalse(preveri_pot([(-1, 0), (-1, 1)], polje4),
                         "Pot ne sme zapustiti polja")
        self.assertFalse(preveri_pot([(-1, 0)], polje4),
                         "Pot ne sme zapustiti polja")
        self.assertFalse(preveri_pot([(0, 0), (0, -1), (1, -1)], polje4),
                         "Pot ne sme zapustiti polja")
        self.assertFalse(preveri_pot([(0, 2), (0, 3), (0, 4)], polje4),
                         "Pot ne sme zapustiti polja")
        self.assertFalse(preveri_pot([(4, 2), (4, 3), (5, 3)], polje4),
                         "Pot ne sme zapustiti polja")
        self.assertFalse(preveri_pot([(5, 3), (4, 3)], polje4),
                         "Pot ne sme zapustiti polja")
        self.assertFalse(preveri_pot([(5, 3), (4, 3), (5, 3)], polje4),
                         "Pot ne sme zapustiti polja")
        self.assertFalse(preveri_pot([(1, 2), (1, 1), (1, 0), (1, -1),
                                      (1, 0), (1, 1), (1, 2)], polje4),
                         "Pot ne sme zapustiti polja")

    def test_9_pot_iz_koordinat(self):
        self.assertEqual(pot_iz_koordinat("53"), [(5, 3)])
        self.assertEqual(pot_iz_koordinat("53R"), [(5, 3), (6, 3)])
        self.assertEqual(pot_iz_koordinat("53UDLR"),
                         [(5, 3), (5, 4), (5, 3), (4, 3), (5, 3)])
        self.assertEqual(pot_iz_koordinat("53DDDDD"),
                         [(5, 3), (5, 2), (5, 1), (5, 0), (5, -1), (5, -2)])

    def test_A_ni_sosednjih(self):
        self.assertFalse(ni_sosednjih([[1, 2, 3], [4, 4, 6], [7, 8, 9]]))
        self.assertFalse(ni_sosednjih([[1, 2, 3], [4, 5, 5], [7, 8, 9]]))
        self.assertFalse(ni_sosednjih([[1, 2, 3], [4, 5, 6], [7, 8, 6]]))
        self.assertFalse(ni_sosednjih([[1, 2, 3], [4, 5, 3], [7, 8, 9]]))
        self.assertFalse(ni_sosednjih([[1, 2, 3], [4, 5, 6], [4, 8, 9]]))
        self.assertFalse(ni_sosednjih([[1, 2, 3], [4, 5, 6], [7, 5, 9]]))
        self.assertFalse(ni_sosednjih([[1, 5, 3], [4, 5, 6], [7, 8, 9]]))
        self.assertFalse(ni_sosednjih([[1, 2, 3], [1, 5, 6], [7, 8, 9]]))
        self.assertFalse(ni_sosednjih([[1, 2, 3], [4, 5, 3], [7, 8, 9]]))

        self.assertTrue(ni_sosednjih([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

        self.assertTrue(ni_sosednjih([[1, 2, 3, 4, 5, 6]]))
        self.assertFalse(ni_sosednjih([[2, 2, 3, 4, 5, 6]]))
        self.assertFalse(ni_sosednjih([[1, 2, 3, 3, 5, 6]]))
        self.assertFalse(ni_sosednjih([[1, 2, 3, 4, 5, 5]]))

        self.assertTrue(ni_sosednjih([[1, 2, 3], [4, 5, 6], [7, 8, 7]]))
        self.assertTrue(ni_sosednjih([[1, 2, 3], [4, 5, 4], [7, 8, 9]]))
        self.assertTrue(ni_sosednjih([[1, 2, 3], [4, 5, 6], [1, 8, 9]]))
        self.assertTrue(ni_sosednjih([[1, 2, 3], [4, 5, 6], [7, 8, 3]]))

if __name__ == "__main__":
    unittest.main()
