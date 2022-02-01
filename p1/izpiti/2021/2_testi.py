
import unittest
import random

visine = dict([("Piran", 23), ("Koper", 4), ("Ilirska Bistrica", 440),
               ("Postojna", 555), ("Gorica", 93), ("Ajdovščina", 106),
               ("Idrija", 340), ("Logatec", 481), ("Cerknica", 559),
               ("Vrhnika", 293), ("Žiri", 481), ("Ljubljana", 295),
               ("Ribnica", 492), ("Kočevje", 465), ("Grosuplje", 338),
               ("Litija", 241), ("Kranj", 386), ("Kamnik", 382),
               ("Škofja Loka", 354), ("Trbovlje", 307), ("Novo mesto", 189),
               ("Krško", 162), ("Celje", 238), ("Maribor", 275),
               ("Velenje", 400), ("Slovenska Bistrica", 271),
               ("Murska Sobota", 189), ("Ptuj", 229), ("Ormož", 216),
               ("Ljutomer", 174), ("Gornja Radgona", 209),
               ("Bled", 507), ("Jesenice", 585)])

povezave = [("Piran", "Koper"),
            ("Koper", "Postojna"),
            ("Ilirska Bistrica", "Postojna"),
            ("Postojna", "Logatec"), ("Postojna", "Cerknica"),
            ("Gorica", "Ajdovščina"), ("Gorica", "Bled"), ("Gorica", "Jesenice"),
            ("Ajdovščina", "Postojna"),
            ("Idrija", "Logatec"), ("Idrija", "Žiri"),
            ("Logatec", "Žiri"), ("Logatec", "Vrhnika"), ("Logatec", "Cerknica"),
            ("Cerknica", "Ribnica"),
            ("Vrhnika", "Ljubljana"),
            ("Žiri", "Škofja Loka"),
            ("Ljubljana", "Škofja Loka"), ("Ljubljana", "Kamnik"),
            ("Ljubljana", "Celje"), ("Ljubljana", "Litija"),
            ("Ljubljana", "Grosuplje"), ("Ljubljana", "Kranj"),
            ("Ribnica", "Grosuplje"), ("Ribnica", "Kočevje"),
            ("Kočevje", "Novo mesto"),
            ("Grosuplje", "Novo mesto"),
            ("Litija", "Trbovlje"),
            ("Kranj", "Bled"), ("Kranj", "Škofja Loka"), ("Kranj", "Kamnik"),
            ("Kamnik", "Velenje"), ("Kamnik", "Celje"), ("Kamnik", "Škofja Loka"),
            ("Trbovlje", "Celje"), ("Trbovlje", "Krško"),
            ("Novo mesto", "Krško"),
            ("Krško", "Ptuj"),
            ("Celje", "Velenje"), ("Celje", "Slovenska Bistrica"),
            ("Maribor", "Slovenska Bistrica"), ("Maribor", "Ptuj"),
            ("Maribor", "Murska Sobota"), ("Maribor", "Ljutomer"),
            ("Velenje", "Slovenska Bistrica"),
            ("Slovenska Bistrica", "Ptuj"),
            ("Murska Sobota", "Gornja Radgona"), ("Murska Sobota", "Ljutomer"),
            ("Ptuj", "Ormož"),
            ("Ljutomer", "Ormož"),
            ("Bled", "Jesenice")]

with open("zemljevid1.txt", "w") as f:
    f.write("""
Piran: 23
Koper: 4
Ilirska Bistrica: 440
Postojna: 555
Nova Gorica: 93
Ribnica: 492
Logatec: 481
Cerknica: 559
""".lstrip())

with open("zemljevid2.txt", "w") as f:
    f.write("""
Piran: 23
Koper: 4
Ilirska Bistrica: 440
Postojna: 555
Nova Gorica: 93
Ribnica: 492
Logatec: 481
Cerknica: 559

Logatec: Cerknica Postojna
Postojna: Cerknica
Ribnica: Cerknica
Koper: Piran Postojna
""".lstrip())

with open("zemljevid3.txt", "w") as f:
    f.write("""
Piran: 23
Koper: 4
Ilirska Bistrica: 440
Postojna: 555
Nova Gorica: 93
Ribnica: 492
Logatec: 481
Cerknica: 559

Logatec: Cerknica
Cerknica: Ribnica Postojna
Koper: Piran Postojna
Postojna: Nova Gorica Logatec Ilirska Bistrica
""".lstrip())

with open("zemljevid4.txt", "w") as f:
    f.write("""
Piran: 23
Nova Gabrovka nad Colom: 12
Gabrovka: 15
Nova Gorica: 55
Gorica zahodno od kraja Nova Gorica: 55
Col: 20
Kanal: 9

Piran: Nova Gabrovka nad Colom Nova Gorica
Gabrovka: Gorica zahodno od kraja Nova Gorica Kanal Nova Gabrovka nad Colom
Nova Gorica: Gabrovka Nova Gabrovka nad Colom
Col: Nova Gabrovka nad Colom Gabrovka 
""".lstrip())


class Test(unittest.TestCase):
    def test_01_ogrozena(self):
        povezave_orig = povezave[:]
        self.assertEqual({"Piran", "Ilirska Bistrica", "Gornja Radgona"},
                         ogrozena(povezave))
        self.assertEqual(povezave_orig, povezave)

        povezave2 = [(f"x{i}", f"x{i + 1}") for i in range(30000)] \
                    + [(f"y{2 * i}", f"y{2 * i + 1}") for i in range(30000)]
        random.shuffle(povezave2)
        self.assertEqual({"x0", "x30000"} | {f"y{i}" for i in range(60000)},
                         ogrozena(povezave2))

    def test_02_mozna_pot(self):
        povezave_orig = povezave[:]
        self.assertTrue(mozna_pot("Jesenice", "Bled", povezave, visine))
        self.assertEqual(povezave_orig, povezave)
        self.assertFalse(mozna_pot("Bled", "Jesenice", povezave, visine))
        self.assertTrue(mozna_pot("Jesenice", "Gorica", povezave, visine))
        self.assertFalse(mozna_pot("Gorica", "Jesenice", povezave, visine))

        self.assertFalse(mozna_pot("Jesenice", "Logatec", povezave, visine))
        self.assertTrue(mozna_pot("Jesenice", "Vrhnika", povezave, visine))

        self.assertFalse(mozna_pot("Bled", "Maribor", povezave, visine))

        self.assertFalse(mozna_pot("Kočevje", "Ljubljana", povezave, visine))
        self.assertFalse(mozna_pot("Kočevje", "Kamnik", povezave, visine))

        self.assertTrue(mozna_pot("Velenje", "Ljutomer", povezave, visine))
        self.assertFalse(mozna_pot("Velenje", "Maribor", povezave, visine))
        self.assertEqual(povezave_orig, povezave)

    def test_03_zasede(self):
        pot1 = ["Postojna", "Logatec", "Idrija", "Bled", "Kranj"]
        pot2 = ["Jesenice", "Bled", "Kranj", "Kamnik"]
        pot3 = ["Celje", "Kamnik", "Kranj", "Ljubljana"]
        pot4 = ["Ljubljana", "Kranj"]

        povezave_orig = povezave[:]
        self.assertEqual(0, zasede([pot1], povezave))  # ni povezave Idrija - Bled
        self.assertEqual(povezave_orig, povezave, "Funkcija naj ne spreminja povezav!")
        self.assertEqual(1, zasede([pot2], povezave))  # uspe
        self.assertEqual(1, zasede([pot3], povezave))  # uspe

        self.assertEqual(1, zasede([pot1, pot2], povezave))  # pot2 uspe; pot1 ne uniči Bled - Kranj
        self.assertEqual(1, zasede([pot2, pot3], povezave))  # pot3 ne uspe, ker pot1 unici Kranj - Kamnik

        self.assertEqual(1, zasede([pot1, pot2, pot3], povezave))  # pot3 ne uspe, ker pot1 unici Kranj - Kamnik
        self.assertEqual(1, zasede([pot3, pot2, pot1], povezave))  # pot1 ne uspe, ker pot3 unici Kranj - Kamnik

        self.assertEqual(2, zasede([pot1, pot2, pot3, pot4], povezave))  # pot1 in pot4
        self.assertEqual(1, zasede([pot3, pot2, pot1, pot4], povezave))  # pot3

        self.assertEqual(povezave_orig, povezave, "Funkcija naj ne spreminja povezav!")

    def test_04_zemljevid(self):
        visine, povezave = zemljevid("zemljevid1.txt")
        self.assertEqual({'Piran': 23,
                          'Koper': 4,
                          'Ilirska Bistrica': 440,
                          'Postojna': 555,
                          'Nova Gorica': 93,
                          'Ribnica': 492,
                          'Logatec': 481,
                          'Cerknica': 559}, visine)
        self.assertEqual([], povezave)

        visine, povezave = zemljevid("zemljevid2.txt")
        self.assertEqual({'Piran': 23,
                          'Koper': 4,
                          'Ilirska Bistrica': 440,
                          'Postojna': 555,
                          'Nova Gorica': 93,
                          'Ribnica': 492,
                          'Logatec': 481,
                          'Cerknica': 559}, visine)
        self.assertEqual([("Logatec", "Cerknica"),
                          ("Logatec", "Postojna"),
                          ("Postojna", "Cerknica"),
                          ("Ribnica", "Cerknica"),
                          ("Koper", "Piran"),
                          ("Koper", "Postojna")], povezave)

        visine, povezave = zemljevid("zemljevid3.txt")
        self.assertEqual({'Piran': 23,
                          'Koper': 4,
                          'Ilirska Bistrica': 440,
                          'Postojna': 555,
                          'Nova Gorica': 93,
                          'Ribnica': 492,
                          'Logatec': 481,
                          'Cerknica': 559}, visine)
        self.assertEqual([('Logatec', 'Cerknica'),
                          ('Cerknica', 'Ribnica'),
                          ('Cerknica', 'Postojna'),
                          ('Koper', 'Piran'),
                          ('Koper', 'Postojna'),
                          ('Postojna', 'Nova Gorica'),
                          ('Postojna', 'Logatec'),
                          ('Postojna', 'Ilirska Bistrica')], povezave)

        visine, povezave = zemljevid("zemljevid4.txt")
        self.assertEqual({'Col': 20,
                          'Gabrovka': 15,
                          'Gorica zahodno od kraja Nova Gorica': 55,
                          'Kanal': 9,
                          'Nova Gabrovka nad Colom': 12,
                          'Nova Gorica': 55,
                          'Piran': 23}, visine)
        self.assertEqual([('Piran', 'Nova Gabrovka nad Colom'),
                          ('Piran', 'Nova Gorica'),
                          ('Gabrovka', 'Gorica zahodno od kraja Nova Gorica'),
                          ('Gabrovka', 'Kanal'),
                          ('Gabrovka', 'Nova Gabrovka nad Colom'),
                          ('Nova Gorica', 'Gabrovka'),
                          ('Nova Gorica', 'Nova Gabrovka nad Colom'),
                          ('Col', 'Nova Gabrovka nad Colom'),
                          ('Col', 'Gabrovka')], povezave)

    def test_5_enota(self):
        a = Enota("Ljubljana", povezave, visine)
        b = Enota("Maribor", povezave, visine)

        self.assertEqual(["Ljubljana"], a.pot())
        self.assertEqual(0, a.vzpon())
        self.assertTrue(a.premik("Kranj"))
        self.assertEqual(["Ljubljana", "Kranj"], a.pot())
        self.assertEqual(91, a.vzpon())

        self.assertFalse(a.premik("Litija"))
        self.assertEqual(["Ljubljana", "Kranj"], a.pot())
        self.assertEqual(91, a.vzpon())

        self.assertTrue(a.premik("Ljubljana"))
        self.assertEqual(["Ljubljana", "Kranj", "Ljubljana"], a.pot())
        self.assertEqual(91, a.vzpon())

        self.assertTrue(a.premik("Litija"))
        self.assertEqual(["Ljubljana", "Kranj", "Ljubljana", "Litija"], a.pot())
        self.assertEqual(91, a.vzpon())

        self.assertTrue(a.premik("Trbovlje"))
        self.assertEqual(["Ljubljana", "Kranj", "Ljubljana", "Litija", "Trbovlje"], a.pot())
        self.assertEqual(91 + 66, a.vzpon())

        self.assertFalse(a.premik("Kranj"))
        self.assertEqual(["Ljubljana", "Kranj", "Ljubljana", "Litija", "Trbovlje"], a.pot())
        self.assertEqual(91 + 66, a.vzpon())

        # b
        self.assertEqual(["Maribor"], b.pot())
        self.assertEqual(0, b.vzpon())

        self.assertFalse(b.premik("Kranj"))
        self.assertEqual(["Maribor"], b.pot())
        self.assertEqual(0, b.vzpon())

        self.assertTrue(b.premik("Slovenska Bistrica"))
        self.assertEqual(["Maribor", "Slovenska Bistrica"], b.pot())
        self.assertEqual(0, b.vzpon())

        self.assertFalse(b.premik("Slovenska Bistrica"))
        self.assertEqual(["Maribor", "Slovenska Bistrica"], b.pot())
        self.assertEqual(0, b.vzpon())

        self.assertTrue(b.premik("Velenje"))
        self.assertEqual(["Maribor", "Slovenska Bistrica", "Velenje"], b.pot())
        self.assertEqual(129, b.vzpon())


if __name__ == "__main__":
    unittest.main()

