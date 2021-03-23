class Filter:
    def izpisi(self, s):
        n = self(s)
        return n, "{}: {} -> {}".format(self.opis(), s, n)

    def __call__(self, s):
        return self.akcija(s)

    def obdelaj(self, s):
        s[:] = self.akcija(s)


###
### Tu dodaj svoje razrede
###




import unittest
class TestFilter(unittest.TestCase):
    def preveri_dedovanje(self, f):
        self.assertIs(f.__call__, Filter.__call__,
            "\nNapaka v {}: filtri ne smejo spreminjati metode __call__"
            .format(f.__name__))

        self.assertIs(f.obdelaj, Filter.obdelaj,
            "\nNapaka v {}: filtri ne smejo spreminjati metode obdelaj"
            .format(f.__name__))

        self.assertIs(f.izpisi, Filter.izpisi,
            "\nNapaka v {}: filtri ne smejo spreminjati metode izpisi"
            .format(f.__name__))

    def preveri_na_mestu(self, f):
        ime = type(f).__name__
        s = [0]
        n = f(s)
        self.assertIsNot(s, n,
             "\nNapaka v {}: filtri morajo vrniti nov seznam, ne pa spreminjati podanega"
             .format(ime))


    def test_Obrni(self):
        f = Obrni()
        self.preveri_dedovanje(Obrni)
        self.preveri_na_mestu(f)
        self.assertEqual(f.opis(), "Obrni")
        self.assertEqual(f([1, 2, 3]), [3, 2, 1])
        self.assertEqual(f([1, 2, 3, 2]), [2, 3, 2, 1])
        self.assertEqual(f([1, 1, 1]), [1, 1, 1])
        self.assertEqual(f([1]), [1])
        self.assertEqual(f([]), [])

    def test_Pristej(self):
        f = Pristej(2)
        self.preveri_dedovanje(Pristej)
        self.preveri_na_mestu(f)
        self.assertEqual(f.opis(), "Pristej 2")
        self.assertEqual(f([1, 2, 3]), [3, 4, 5])
        self.assertEqual(f([1, 2, 3, 2]), [3, 4, 5, 4])
        self.assertEqual(f([1, 1, 1]), [3, 3, 3])
        self.assertEqual(f([1]), [3])
        self.assertEqual(f([]), [])

    def test_Pomnozi(self):
        f = Pomnozi(2)
        self.preveri_dedovanje(Pomnozi)
        self.preveri_na_mestu(f)
        self.assertEqual(f.opis(), "Pomnozi z 2")
        self.assertEqual(f([1, 2, 3]), [2, 4, 6])
        self.assertEqual(f([1, 2, 3, 2]), [2, 4, 6, 4])
        self.assertEqual(f([1, 1, 1]), [2, 2, 2])
        self.assertEqual(f([1]), [2])
        self.assertEqual(f([]), [])

    def test_Pristej3(self):
        f = Pristej(3)
        self.preveri_dedovanje(Pristej)
        self.preveri_na_mestu(f)
        self.assertEqual(f.opis(), "Pristej 3")
        self.assertEqual(f([1, 2, 3]), [4, 5, 6])
        self.assertEqual(f([1, 2, 3, 2]), [4, 5, 6, 5])
        self.assertEqual(f([1, 1, 1]), [4, 4, 4])
        self.assertEqual(f([1]), [4])
        self.assertEqual(f([]), [])

    def test_Pomnozi3(self):
        f = Pomnozi(3)
        self.preveri_dedovanje(Pomnozi)
        self.preveri_na_mestu(f)
        self.assertEqual(f.opis(), "Pomnozi z 3")
        self.assertEqual(f([1, 2, 3]), [3, 6, 9])
        self.assertEqual(f([1, 2, 3, 2]), [3, 6, 9, 6])
        self.assertEqual(f([1, 1, 1]), [3, 3, 3])
        self.assertEqual(f([1]), [3])
        self.assertEqual(f([]), [])

    def test_Normaliziraj(self):
        f = Normaliziraj()
        self.preveri_dedovanje(Normaliziraj)
        self.preveri_na_mestu(f)
        self.assertEqual(f.opis(), "Normaliziraj")
        self.assertEqual(f([1, 2, 4]), [0.25, 0.5, 1])
        self.assertEqual(f([1, 2, 4, 2]), [0.25, 0.5, 1, 0.5])
        self.assertEqual(f([1, 1, 1]), [1, 1, 1])
        self.assertEqual(f([0]), [0])
        self.assertEqual(f([]), [])


    def test_izvedi(self):
        filtri = [Pristej(-2), Pomnozi(2), Obrni(), Pomnozi(0.5)]
        s = [1, 2, 3]
        n = izvedi(filtri, s)
        self.assertEqual(n, [1, 0, -1])
        self.assertIsNot(s, n)

    def test_obdelaj(self):
        filtri = [Pristej(-2), Pomnozi(2), Obrni(), Pomnozi(0.5)]
        s = [1, 2, 3]
        obdelaj(filtri, s)
        self.assertEqual(s, [1, 0, -1])

    def test_preveri(self):
        filtri = [Pristej(-2), Pomnozi(2), Obrni(), Pomnozi(0.5)]
        s = [1, 2, 3]
        n, msg = preveri(filtri, s)
        self.assertEqual(n, [1, 0, -1])
        self.assertEqual(msg.strip(), """Pristej -2: [1, 2, 3] -> [-1, 0, 1]
Pomnozi z 2: [-1, 0, 1] -> [-2, 0, 2]
Obrni: [-2, 0, 2] -> [2, 0, -2]
Pomnozi z 0.5: [2, 0, -2] -> [1.0, 0.0, -1.0]""")
