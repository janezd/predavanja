otroci = {
    "Adam":	["Matjaž", "Cilka", "Daniel", "Erik"],
    "Aleksander": [],
    "Alenka": [],
    "Barbara": [],
    "Cilka": [],
    "Daniel": ["Elizabeta", "Hans"],
    "Erik": [],
    "Elizabeta": ["Ludvik", "Jurij", "Barbara", "Herman", "Mihael"],
    "Franc": [],
    "Herman": ["Margareta"],
    "Hans": [],
    "Jožef": ["Alenka", "Aleksander", "Petra"],
    "Jurij": ["Franc", "Jožef"],
    "Ludvik": [],
    "Margareta": [],
    "Matjaž": ["Viljem"],
    "Mihael": [],
    "Petra": [],
    "Tadeja": [],
    "Viljem": ["Tadeja"],
}

starost = {
    "Adam": 111, "Matjaž": 90, "Cilka": 88, "Daniel": 85, "Erik": 83,
    "Viljem": 58, "Tadeja": 20, "Elizabeta": 68, "Hans": 64, "Ludvik": 50,
    "Jurij": 49, "Barbara": 45, "Herman": 39, "Mihael": 32, "Franc": 30,
    "Jožef": 29, "Margareta": 3, "Alenka": 9, "Aleksander": 5, "Petra": 7}



import unittest
class TestNovakovi(unittest.TestCase):
    def test_starost_najmlajsega(self):
        self.assertEqual(najmlajsi_clan("Adam"), (3, "Margareta"))
        self.assertEqual(najmlajsi_clan("Daniel"), (3, "Margareta"))
        self.assertEqual(najmlajsi_clan("Jurij"), (5, "Aleksander"))
        self.assertEqual(najmlajsi_clan("Matjaž"), (20, "Tadeja"))
        self.assertEqual(najmlajsi_clan("Tadeja"), (20, "Tadeja"))

    def test_mlajsi_od(self):
        self.assertSetEqual(mlajsi_od("Adam", 10), {"Alenka", "Petra", "Aleksander", "Margareta"})
        self.assertSetEqual(mlajsi_od("Elizabeta", 10), {"Alenka", "Petra", "Aleksander","Margareta"})
        self.assertSetEqual(mlajsi_od("Elizabeta", 7), {"Aleksander","Margareta"})
        self.assertSetEqual(mlajsi_od("Jurij", 10), {"Alenka", "Petra", "Aleksander"})
        self.assertSetEqual(mlajsi_od("Matjaž", 10), set())
        self.assertSetEqual(mlajsi_od("Tadeja", 21), {"Tadeja"})
        self.assertSetEqual(mlajsi_od("Tadeja", 20), set())

    def test_naj_izmenicna_starost(self):
        global starost
        k_starost = starost.copy()
        try:
            self.assertEqual(naj_izmenicna_starost("Adam"), 2)
            self.assertEqual(naj_izmenicna_starost("Franc"), 1)
            self.assertEqual(naj_izmenicna_starost("Jurij"), 2)
            self.assertEqual(naj_izmenicna_starost("Elizabeta"), 3)
            self.assertEqual(naj_izmenicna_starost("Daniel"), 4)
            self.assertEqual(naj_izmenicna_starost("Herman"), 1)
            self.assertEqual(naj_izmenicna_starost("Mihael"), 1)

            starost["Daniel"] = 86
            starost["Elizabeta"] = 67
            self.assertEqual(naj_izmenicna_starost("Adam"), 4)

            for k in starost:
                starost[k] = 42
            self.assertEqual(naj_izmenicna_starost("Adam"), 1)

            starost["Matjaž"] = starost["Daniel"] = 41
            self.assertEqual(naj_izmenicna_starost("Adam"), 3)

            starost["Tadeja"] = 39
            self.assertEqual(naj_izmenicna_starost("Adam"), 4)

            starost["Jurij"] = 39
            self.assertEqual(naj_izmenicna_starost("Adam"), 5)
        finally:
            starost = k_starost
