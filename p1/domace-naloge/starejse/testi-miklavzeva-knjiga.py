import unittest

tockovalnik = {
    'pometanje stopnic': 3,
    'kuhanje kosila': 5,
    'pomivanje posode': 3,
    'brisanje mize': 1,
    'pretep z bratom': -3,
    'pretep s sestro': -3,
    'prepir z mamo': -5,
    'nenarejena naloga': -4,
    'prepisana naloga': -7,
    'jezikanje': -4
}

cena = {
    'sanke': 20,
    'zvezek': 5,
    'lok za violino': 30,
    'barvice': 7,
    'bomboni': 3
}


class TestMiklavzevaKnjiga(unittest.TestCase):
    knjiga = {
        "Ana": ["pometanje stopnic", "jezikanje", "kuhanje kosila",
                "pretep z bratom", "pometanje stopnic", "kuhanje kosila"],
        "Benjamin": ["brisanje mize", "jezikanje", "prepisana naloga",
                     "pretep s sestro"],
        "Cilka": [],
        "Dani": ["prepir z mamo", "kuhanje kosila", "kuhanje kosila"],
        "Eva": ["pretep z bratom", "nenarejena naloga"],
        "Franc": ["pomivanje posode", "brisanje mize", "pometanje stopnic",
                  "kuhanje kosila", "kuhanje kosila", "pometanje stopnic"],
        "Greta": ["pometanje stopnic", "jezikanje"],
        "Helga": ["pometanje stopnic", "jezikanje", "kuhanje kosila",
                  "prepir z mamo", "pometanje stopnic", "kuhanje kosila"],
    }

    def test_oceni(self):
        self.assertEqual(oceni(["pometanje stopnic"]), 3)
        self.assertEqual(oceni(["pometanje stopnic", "pometanje stopnic"]), 6)
        self.assertEqual(oceni(["pometanje stopnic", "kuhanje kosila"]), 8)
        self.assertEqual(oceni(["prepir z mamo"]), -5)
        self.assertEqual(oceni(["prepir z mamo", "kuhanje kosila"]), 0)
        self.assertEqual(oceni([]), 0)

        self.assertEqual(oceni(self.knjiga["Ana"]), 9)
        self.assertEqual(oceni(self.knjiga["Benjamin"]), -13)
        self.assertEqual(oceni(self.knjiga["Cilka"]), 0)

    def test_povzetek_knjige(self):
        self.assertDictEqual(
            povzetek_knjige(self.knjiga),
            {'Franc': 20, 'Dani': 5, 'Benjamin': -13, 'Eva': -7, 'Helga': 7,
             'Ana': 9, 'Cilka': 0, 'Greta': -1})
        self.assertDictEqual(povzetek_knjige({
            "Ana": ["pometanje stopnic", "jezikanje", "kuhanje kosila",
                    "pretep z bratom", "pometanje stopnic", "kuhanje kosila"],
            "Benjamin": ["brisanje mize", "jezikanje", "prepisana naloga",
                         "pretep s sestro"],
            "Cilka": []}),
            {'Ana': 9, 'Benjamin': -13, 'Cilka': 0})

        self.assertDictEqual(povzetek_knjige({}), {})

    def test_izberi(self):
        self.assertSetEqual(
            izberi(["pometanje stopnic", "pomivanje posode", "kuhanje kosila",
                    "pretep s sestro"],
                   {"zvezek", "lok za violino", "barvice", "bomboni"}),
            {"zvezek", "barvice", "bomboni"}
        )
        self.assertSetEqual(
            izberi(["pometanje stopnic", "pomivanje posode", "kuhanje kosila",
                    "pretep s sestro"],
                   set()),
            set()
        )
        self.assertSetEqual(
            izberi(["pometanje stopnic", "pomivanje posode", "kuhanje kosila",
                    "pretep s sestro"],
                   {"zvezek"}),
            {"zvezek"}
        )
        self.assertSetEqual(
            izberi(["pometanje stopnic", "pomivanje posode", "kuhanje kosila",
                    "pretep s sestro"],
                   {"sanke"}),
            set()
        )
        self.assertSetEqual(izberi([], {"zvezek"}), set())


    def test_strosek(self):
        self.assertEqual(
            strosek(["pometanje stopnic", "pomivanje posode", "kuhanje kosila", "pretep s sestro"],
                    {"zvezek", "lok za violino", "barvice", "bomboni"}),
            15
        )
        self.assertEqual(
            strosek(["pometanje stopnic", "pomivanje posode", "kuhanje kosila", "pretep s sestro"],
                    set()),
            0
        )
        self.assertEqual(
            strosek(["pometanje stopnic", "pomivanje posode", "kuhanje kosila", "pretep s sestro"],
                    {"zvezek"}),
            5
        )
        self.assertEqual(
            strosek(["pometanje stopnic", "pomivanje posode", "kuhanje kosila", "pretep s sestro"],
                   {"sanke"}),
            0
        )
        self.assertEqual(strosek([], {"zvezek"}), 0)

    def test_najpridnejsi_otrok(self):
        self.assertEqual(najpridnejsi_otrok(self.knjiga), "Franc")

        self.assertEqual(
            najpridnejsi_otrok({
                "Ana": ["pometanje stopnic", "jezikanje", "kuhanje kosila",
                        "pretep z bratom", "pometanje stopnic", "kuhanje kosila"],
                "Eva": ["pretep z bratom", "nenarejena naloga"],
                "Helga": ["pometanje stopnic", "jezikanje", "kuhanje kosila",
                          "prepir z mamo", "pometanje stopnic", "kuhanje kosila"]
            }), "Ana")
        self.assertEqual(
            najpridnejsi_otrok({"Eva": ["pretep z bratom", "nenarejena naloga"]}), "Eva")
        self.assertEqual(
            najpridnejsi_otrok({
                "Eva": ["pretep z bratom", "nenarejena naloga"],
                "Greta": ["pometanje stopnic", "jezikanje"]}),
            "Greta")

    def test_poreden(self):
        self.assertFalse(poreden(
            ["pometanje stopnic", "pomivanje posode", "kuhanje kosila",
             "pretep s sestro"]))
        self.assertFalse(poreden([]))

        self.assertTrue(poreden(
            ["pometanje stopnic", "prepir z mamo", "pomivanje posode",
             "kuhanje kosila", "pretep s sestro"]))
        self.assertTrue(poreden(
            ["pometanje stopnic"] * 10 + ["prepisana naloga",
            "pomivanje posode", "kuhanje kosila", "pretep s sestro"]))
        self.assertTrue(poreden(["prepir z mamo"]))

    def test_obdarovani(self):
        self.assertSetEqual(
            obdarovani(self.knjiga), {'Eva', 'Franc', 'Cilka', 'Greta', 'Ana'})

        self.assertSetEqual(
            obdarovani({
                "Ana": ["pometanje stopnic", "jezikanje", "kuhanje kosila",
                        "pretep z bratom", "pometanje stopnic",
                        "kuhanje kosila"],
                "Eva": ["pretep z bratom", "nenarejena naloga"],
                "Helga": ["pometanje stopnic", "jezikanje",
                          "kuhanje kosila",
                          "prepir z mamo", "pometanje stopnic",
                          "kuhanje kosila"]
            }), {"Ana", "Eva"})
        self.assertSetEqual(
            obdarovani(
                {"Eva": ["pretep z bratom", "nenarejena naloga"]}), {"Eva"})
        self.assertSetEqual(
            obdarovani({
                "Benjamin": ["brisanje mize", "jezikanje", "prepisana naloga",
                             "pretep s sestro"],
                "Cilka": [],
                "Dani": ["prepir z mamo", "kuhanje kosila", "kuhanje kosila"]
            }),
            {"Cilka"})
        self.assertSetEqual(
            obdarovani({
                "Benjamin": ["brisanje mize", "jezikanje", "prepisana naloga",
                             "pretep s sestro"],
                "Dani": ["prepir z mamo", "kuhanje kosila", "kuhanje kosila"]
            }),
            set())

if __name__ == "__main__":
    unittest.main()
