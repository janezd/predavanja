

import unittest
import random
import string
import math
import ast


class Test(unittest.TestCase):
    b, j, s = "bukev", "javor", "smreka"

    drevesa = [(s, 4, 6),
               (b, 1, 5), (b, 8, 5),
               (j, -1, 4), (b, 3, 4),
               (j, 7, 3),
               (b, -2, 2), (b, 2, 2), (j, 4, 2),
               (s, -3, -1), (b, 3, -1),
               (j, -1, -2),
               (j, 4, -3)]

    print(drevesa)

class Test06(Test):
    def test_razdalja(self):
        self.assertEqual(5, razdalja(0, 0, 3, 4))
        self.assertEqual(13, razdalja(-12, 0, 0, -5))
        self.assertEqual(5, razdalja(4, 8, 7, 4))

    def test_najblizji(self):
        self.assertEqual("bukev", najblizji(2, 2, self.drevesa))
        self.assertEqual("bukev", najblizji(1, 2, self.drevesa))
        self.assertEqual("javor", najblizji(0, -1, self.drevesa))

    def test_najblizji_enak(self):
        self.assertEqual((2, 2), najblizji_enak(1, 2, "bukev", self.drevesa))
        self.assertEqual((4, 2), najblizji_enak(4, 2, "javor", self.drevesa))
        self.assertEqual((-3, -1), najblizji_enak(0, 2, "smreka", self.drevesa))
        self.assertEqual((4, 6), najblizji_enak(0, 4, "smreka", self.drevesa))

    def test_vse_vrste(self):
        self.assertEqual({"smreka", "javor", "bukev"}, vse_vrste(self.drevesa))

    def test_koordinate_tipov(self):
        self.assertEqual({(-1, 4), (7, 3), (4, 2), (-1, -2), (4, -3)},
                         koordinate_tipov("javor", self.drevesa))
        self.assertEqual(set(), koordinate_tipov("oreh", self.drevesa))
        self.assertEqual({(4, 6), (-3, -1)}, koordinate_tipov("smreka", self.drevesa))

    def test_najblizji_po_vrstah(self):
        self.assertEqual({"bukev": (-2, 2), "javor": (-1, 4), "smreka": (-3, -1)},
                         najblizji_po_vrstah(-1, 2, self.drevesa))
        self.assertEqual({"bukev": (2, 2), "javor": (4, 2), "smreka": (-3, -1)},
                         najblizji_po_vrstah(1, 1, self.drevesa))

    def test_najpogostejsa_vrsta(self):
        self.assertEqual("bukev", najpogostejsa_vrsta(self.drevesa))
        self.assertEqual("javor", najpogostejsa_vrsta(self.drevesa[-4:]))
        self.assertEqual("smreka", najpogostejsa_vrsta(self.drevesa[:1]))

        drevesa = [("".join(random.choice(string.ascii_lowercase) for _ in range(30)),
                    random.randint(-1000000, 1000000),
                    random.randint(-1000000, 1000000))] + [("smreka", 0, 0), ("smreka", 1, 1)]
        # sto tisoč dreves z naključnimi imeni in dve smreki
        self.assertEqual("smreka", najpogostejsa_vrsta(drevesa))


class Test07(Test):
    def test_preberi(self):
        self.assertEqual(set(preberi("drevesa.txt")), set(self.drevesa))


class Test08(Test):
    functions = {elm.name: elm
                 for elm in ast.parse(open(__file__, "r", encoding="utf-8").read()).body
                 if isinstance(elm, ast.FunctionDef)}

    def assert_is_one_line(self, func):
        func
        body = self.functions[func.__code__.co_name].body
        self.assertEqual(len(body), 1, "\nFunkcija ni dolga le eno vrstico")
        self.assertIsInstance(body[0], ast.Return, "\nFunkcija naj bi vsebovala le return")

    def test_nedovoljene_funkcije(self):
        dovoljene_funkcije = {
            "razdalja", "najblizji", "najblizji_enak",
            "vse_vrste", "koordinate_tipov", "najblizji_po_vrstah",
            "najpogostejsa_vrsta", "dolzina_poti",
            "najblizji_par_enakih", "najmanjsi_krog",
            "preberi"}
        for func in self.functions:
            self.assertIn(func, dovoljene_funkcije, f"\nFunkcija {func} ni dovoljena.")

    def test_ena_vrstica(self):
        self.assert_is_one_line(vse_vrste)
        self.assert_is_one_line(koordinate_tipov)
        self.assert_is_one_line(najblizji_po_vrstah)


class Test09(Test):
    def test_dolzina_poti(self):
        self.assertEqual(1, dolzina_poti(1, 2, ["bukev"], self.drevesa))
        self.assertEqual(1, dolzina_poti(1, 2, ["bukev", "bukev"], self.drevesa))
        self.assertEqual(3, dolzina_poti(1, 2, ["bukev", "bukev", "javor"], self.drevesa))
        self.assertEqual(5, dolzina_poti(1, 2, ["bukev", "bukev", "javor", "bukev"], self.drevesa))
        self.assertAlmostEqual(5 + math.sqrt(20), dolzina_poti(1, 2, ["bukev", "bukev", "javor", "bukev", "smreka"], self.drevesa))
        self.assertAlmostEqual(5 + math.sqrt(20) + math.sqrt(5), dolzina_poti(1, 2, ["bukev", "bukev", "javor", "bukev", "smreka", "bukev"], self.drevesa))

def test_najblizji_par_enakih(self):
    self.assertAlmostEqual(math.sqrt(5), najblizji_par_enakih(self.drevesa))

    drevesa = self.drevesa + [("javor", 5, 2)]
    self.assertAlmostEqual(1, najblizji_par_enakih(drevesa))

def test_najmanjsi_krog(self):
    self.assertAlmostEqual(2, najmanjsi_krog(4, 4, self.drevesa))
    self.assertAlmostEqual(5, najmanjsi_krog(0, 3, self.drevesa))
    self.assertAlmostEqual(4, najmanjsi_krog(0, 6, self.drevesa))


if __name__ == "__main__":
    unittest.main()

