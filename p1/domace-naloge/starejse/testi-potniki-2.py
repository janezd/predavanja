class Potnik:
    def __init__(self, energija):
        self.x = self.y = 0
        self.__energija = energija

    def pojdi(self, smer, razdalja):
        x0, y0 = self.x, self.y
        self.premik(smer, razdalja)
        self.__energija += 5 * ((x0 * self.x < 0) + (y0 * self.y < 0))

    def porabi(self, energija):
        if self.__energija < energija:
            return False
        self.__energija -= energija
        return True


class Potnik2:
    def __init__(self, energija):
        self.x = self.y = 0
        self.__energija = energija

    def pojdi(self, smer, razdalja):
        dx, dy = self.premik(smer, razdalja)
        if not self.porabi(sqrt(dx ** 2 + dy ** 2)):
            return
        x0, y0 = self.x, self.y
        self.x += dx
        self.y += dy
        self.__energija += 5 * ((x0 * self.x < 0) + (y0 * self.y < 0))

    def porabi(self, energija):
        if self.__energija < energija:
            return False
        self.__energija -= energija
        return True


import unittest
class TestPotnik(unittest.TestCase):
    def test_orto(self):
        Potnik = Orto.__base__
        self.assertFalse(hasattr(Potnik, "premik"),
                         "Ne spreminjajte razreda Potnik")
        self.assertEqual(Potnik.__name__, "Potnik",
                         "Ne spreminjajte razreda Potnik")
        self.assertRaises(AttributeError, Potnik(20).pojdi, ("S", 2),
                          "Ne spreminjajte razreda Potnik")

        potnik1 = Orto(20)
        potnik2 = Orto(10)

        potnik1.pojdi("S", 5)
        self.assertEqual(potnik1.x, 0)
        self.assertEqual(potnik1.y, 5)
        self.assertEqual(potnik1._Potnik__energija, 15)
        self.assertEqual(potnik2.x, 0)
        self.assertEqual(potnik2.y, 0)
        self.assertEqual(potnik2._Potnik__energija, 10)

        potnik1.pojdi("J", 3)
        potnik1.pojdi("V", 4)
        potnik1.pojdi("Z", 5)
        self.assertEqual(potnik1.x, -1)
        self.assertEqual(potnik1.y, 2)
        # 15 - 3 - 4 - 5 = 3, vendar dobi +5 za sekanje osi y.
        self.assertEqual(potnik1._Potnik__energija, 8)

        for smer in "SJVZ":
            potnik1.pojdi(smer, 9)
            self.assertEqual(potnik1.x, -1)
            self.assertEqual(potnik1.y, 2)
            self.assertEqual(potnik1._Potnik__energija, 8)

        potnik2.pojdi("J", 9)
        self.assertEqual(potnik2.x, 0)
        self.assertEqual(potnik2.y, -9)
        self.assertEqual(potnik2._Potnik__energija, 1)

    def test_orto_plus(self):
        Potnik = OrtoPlus.__base__
        self.assertFalse(hasattr(Potnik, "premik"),
                         "Ne spreminjajte razreda Potnik")
        self.assertEqual(Potnik.__name__, "Potnik",
                         "Ne spreminjajte razreda Potnik")
        self.assertRaises(AttributeError, Potnik(20).pojdi, ("S", 2),
                          "Ne spreminjajte razreda Potnik")

        from math import sqrt
        potnik1 = OrtoPlus(4)
        potnik1.pojdi("SV", 1)
        self.assertEqual(potnik1.x, 1)
        self.assertEqual(potnik1.y, 1)
        self.assertAlmostEqual(potnik1._Potnik__energija, 4 - sqrt(2))
        # Te poti ne more narediti, ker nima dovolj energije!
        potnik1.pojdi("JZ", 2)
        self.assertEqual(potnik1.x, 1)
        self.assertEqual(potnik1.y, 1)
        self.assertAlmostEqual(potnik1._Potnik__energija, 4 - sqrt(2))


    def test_liberalec(self):
        Potnik = Liberalec.__base__
        self.assertFalse(hasattr(Potnik, "premik"),
                         "Ne spreminjajte razreda Potnik")
        self.assertEqual(Potnik.__name__, "Potnik",
                         "Ne spreminjajte razreda Potnik")
        self.assertRaises(AttributeError, Potnik(20).pojdi, (0, 2),
                          "Ne spreminjajte razreda Potnik")

        from math import sqrt, pi
        potnik1 = Liberalec(10)
        potnik1.pojdi(0, 2)
        self.assertAlmostEqual(potnik1.x, 2)
        self.assertAlmostEqual(potnik1.y, 0)
        self.assertAlmostEqual(potnik1._Potnik__energija, 8)
        potnik1.pojdi(8 * pi / 6, 2)
        self.assertAlmostEqual(potnik1.x, 1)
        self.assertAlmostEqual(potnik1.y, -sqrt(3))
        self.assertAlmostEqual(potnik1._Potnik__energija, 6)
        potnik1.pojdi(-pi / 2, 4)
        self.assertAlmostEqual(potnik1.x, 1)
        self.assertAlmostEqual(potnik1.y, -4 - sqrt(3))
        self.assertAlmostEqual(potnik1._Potnik__energija, 2)
        potnik1.pojdi(-pi / 2, 4)
        self.assertAlmostEqual(potnik1.x, 1)
        self.assertAlmostEqual(potnik1.y, -4 - sqrt(3))


import unittest
class TestPotnik2(unittest.TestCase):
    def test_orto2(self):
        Potnik2 = Orto2.__base__
        self.assertFalse(hasattr(Potnik2, "premik"),
                         "Ne spreminjajte razreda Potnik2")
        self.assertEqual(Potnik2.__name__, "Potnik2",
                         "Ne spreminjajte razreda Potnik2")
        self.assertRaises(AttributeError, Potnik2(20).pojdi, ("S", 2),
                          "Ne spreminjajte razreda Potnik2")

        potnik1 = Orto2(20)
        potnik2 = Orto2(10)

        potnik1.pojdi("S", 5)
        self.assertEqual(potnik1.x, 0)
        self.assertEqual(potnik1.y, 5)
        self.assertEqual(potnik1._Potnik2__energija, 15)
        self.assertEqual(potnik2.x, 0)
        self.assertEqual(potnik2.y, 0)
        self.assertEqual(potnik2._Potnik2__energija, 10)

        potnik1.pojdi("J", 3)
        potnik1.pojdi("V", 4)
        potnik1.pojdi("Z", 5)
        self.assertEqual(potnik1.x, -1)
        self.assertEqual(potnik1.y, 2)
        # 15 - 3 - 4 - 5 = 3, vendar dobi +5 za sekanje osi y.
        self.assertEqual(potnik1._Potnik2__energija, 8)

        for smer in "SJVZ":
            potnik1.pojdi(smer, 9)
            self.assertEqual(potnik1.x, -1)
            self.assertEqual(potnik1.y, 2)
            self.assertEqual(potnik1._Potnik2__energija, 8)

        potnik2.pojdi("J", 9)
        self.assertEqual(potnik2.x, 0)
        self.assertEqual(potnik2.y, -9)
        self.assertEqual(potnik2._Potnik2__energija, 1)

    def test_orto_plus2(self):
        Potnik2 = OrtoPlus2.__base__
        self.assertFalse(hasattr(Potnik2, "premik"),
                         "Ne spreminjajte razreda Potnik2")
        self.assertEqual(Potnik2.__name__, "Potnik2",
                         "Ne spreminjajte razreda Potnik2")
        self.assertRaises(AttributeError, Potnik2(20).pojdi, ("S", 2),
                          "Ne spreminjajte razreda Potnik2")

        from math import sqrt
        potnik1 = OrtoPlus2(4)
        potnik1.pojdi("SV", 1)
        self.assertEqual(potnik1.x, 1)
        self.assertEqual(potnik1.y, 1)
        self.assertAlmostEqual(potnik1._Potnik2__energija, 4 - sqrt(2))
        # Te poti ne more narediti, ker nima dovolj energije!
        potnik1.pojdi("JZ", 2)
        self.assertEqual(potnik1.x, 1)
        self.assertEqual(potnik1.y, 1)
        self.assertAlmostEqual(potnik1._Potnik2__energija, 4 - sqrt(2))


    def test_liberalec(self):
        Potnik2 = Liberalec2.__base__
        self.assertFalse(hasattr(Potnik2, "premik"),
                         "Ne spreminjajte razreda Potnik2")
        self.assertEqual(Potnik2.__name__, "Potnik2",
                         "Ne spreminjajte razreda Potnik2")
        self.assertRaises(AttributeError, Potnik2(20).pojdi, ("S", 2),
                          "Ne spreminjajte razreda Potnik2")

        from math import sqrt, pi
        potnik1 = Liberalec2(10)
        potnik1.pojdi(0, 2)
        self.assertAlmostEqual(potnik1.x, 2)
        self.assertAlmostEqual(potnik1.y, 0)
        self.assertAlmostEqual(potnik1._Potnik2__energija, 8)
        potnik1.pojdi(8 * pi / 6, 2)
        self.assertAlmostEqual(potnik1.x, 1)
        self.assertAlmostEqual(potnik1.y, -sqrt(3))
        self.assertAlmostEqual(potnik1._Potnik2__energija, 6)
        potnik1.pojdi(-pi / 2, 4)
        self.assertAlmostEqual(potnik1.x, 1)
        self.assertAlmostEqual(potnik1.y, -4 - sqrt(3))
        self.assertAlmostEqual(potnik1._Potnik2__energija, 2)
        potnik1.pojdi(-pi / 2, 4)
        self.assertAlmostEqual(potnik1.x, 1)
        self.assertAlmostEqual(potnik1.y, -4 - sqrt(3))

if __name__ == "__main__":
    unittest.main()
