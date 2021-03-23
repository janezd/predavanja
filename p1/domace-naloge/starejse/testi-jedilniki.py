import unittest

jedi = {"palacinke": {"jajce": 1, "mleko": 0.3, "moka": 0.2},
        "smorn": {"jajce": 1, "mleko": 0.3, "moka": 0.2},
        "krompirjev golaz": {"krompir": 2, "paprika": 1, "cebula": 1},
        "sataras": {"paradiznik": 1, "paprika": 1, "jajce": 1, "cebula": 1,
                    "kruh": 0.2},
        "hrenovke": {"hrenovka": 1, "kruh": 0.2},
        "makaroni": {"makaroni": 0.2, "paradiznik": 0.5, "meso": 0.2,
                     "cebula": 0.3},
        "marmelada": {"marmelada": 0.1, "kruh": 0.3},
        "piškot": {"piškot": 2},
        "nic": {}}


class TestJedilniki(unittest.TestCase):
    def test_ena_jed(self):
        import copy
        jedi2 = copy.deepcopy(jedi)
        self.assertDictEqual(
            ena_jed("krompirjev golaz", 2),
            {"krompir": 4, "paprika": 2, "cebula": 2})
        self.assertEqual(jedi, jedi2, "Ne spreminjajte slovarja jedi!")
        self.assertDictEqual(
            ena_jed("hrenovke", 0), {"hrenovka": 0, "kruh": 0})
        self.assertDictEqual(ena_jed("nic", 10), {})

    def test_nakup(self):
        self.assertDictEqual(
            nakup([("makaroni", 20), ("krompirjev golaz", 25),
                   ("hrenovke", 18), ("sataras", 18)]),
            {'meso': 4.0, 'cebula': 49.0, 'kruh': 7.2, 'jajce': 18.0,
             'hrenovka': 18.0, 'paprika': 43.0, 'paradiznik': 28.0,
             'makaroni': 4.0, 'krompir': 50.0})
        self.assertDictEqual(nakup([]), {})
        self.assertDictEqual(
            nakup([("hrenovke", 20)]),
            {"hrenovka": 20, "kruh": 4})

    def test_obrokov(self):
        zaloga = {"jajce": 10, "mleko": 2, "moka": 2, "marmelada": 2, "kruh": 1}
        self.assertAlmostEqual(obrokov("palacinke", zaloga), 6)
        self.assertAlmostEqual(obrokov("marmelada", zaloga), 3)
        self.assertAlmostEqual(obrokov("makaroni", zaloga), 0)
        self.assertAlmostEqual(obrokov("palacinke", {}), 0)

    def test_prazni(self):
        zaloga = {"jajce": 10, "mleko": 2, "moka": 2, "marmelada": 2, "kruh": 1}
        self.assertIsNone(
            prazni([("palacinke", 3), ("marmelada", 2), ("palacinke", 1)],
                   zaloga))
        self.assertDictEqual(
            zaloga,
            {'kruh': 0.4, 'moka': 1.2, 'marmelada': 1.8, 'mleko': 0.8,
             'jajce': 6.0})
        self.assertIsNone(prazni([("palacinke", 1)], zaloga))
        self.assertDictEqual(
            zaloga,
            {'kruh': 0.4, 'moka': 1, 'marmelada': 1.8, 'mleko': 0.5,
             'jajce': 5.0})
        self.assertIsNone(prazni([], zaloga))
        self.assertDictEqual(
            zaloga,
            {'kruh': 0.4, 'moka': 1, 'marmelada': 1.8, 'mleko': 0.5,
             'jajce': 5.0})


if __name__ == "__main__":
    unittest.main()
