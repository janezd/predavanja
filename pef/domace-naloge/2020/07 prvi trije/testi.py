

otroci = {
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

import unittest
import string
import random

class Test(unittest.TestCase):
    def test_prvi(self):
        self.assertEqual("Adam", prvi("Adam"))
        self.assertEqual("Aleksander", prvi("Aleksander"))
        self.assertEqual("Aleksander", prvi("Jožef"))
        self.assertEqual("Aleksander", prvi("Jurij"))
        self.assertEqual("Aleksander", prvi("Elizabeta"))
        self.assertEqual("Erik", prvi("Hans"))
        self.assertEqual("Aleksander", prvi("Daniel"))

        def grozna_rodbina(n):
            jaz = "".join(random.choice(string.ascii_lowercase) for _ in range(10))
            otroci[jaz] = []
            if n:
                for _ in range(2):
                    otroci[jaz].append(grozna_rodbina(n - 1))
            return jaz

        try:
            global otroci
            prejsnji = otroci
            otroci = {}
            koren = grozna_rodbina(17)
            prvi(koren)
        finally:
            otroci = prejsnji

    def test_prvi_trije(self):
        self.assertEqual(["Aleksander", "Alenka", "Jožef"], prvi_trije("Jožef"))
        self.assertEqual(["Franc"], prvi_trije("Franc"))
        self.assertEqual(["Aleksander", "Alenka", "Franc"], prvi_trije("Jurij"))
        self.assertEqual(["Aleksander", "Alenka", "Barbara"], prvi_trije("Elizabeta"))
        self.assertEqual(["Aleksander", "Alenka", "Barbara"], prvi_trije("Daniel"))
        self.assertEqual(["Adam", "Aleksander", "Alenka"], prvi_trije("Adam"))

    def test_NEOBVEZNA_prvi_trije_brez(self):
        self.assertEqual(["Aleksander", "Alenka", "Petra"], prvi_trije_brez("Jožef"))
        self.assertEqual([], prvi_trije_brez("Franc"))
        self.assertEqual(["Aleksander", "Alenka", "Franc"], prvi_trije_brez("Jurij"))
        self.assertEqual(["Aleksander", "Alenka", "Barbara"], prvi_trije_brez("Elizabeta"))
        self.assertEqual(["Aleksander", "Alenka", "Barbara"], prvi_trije_brez("Daniel"))
        self.assertEqual(["Aleksander", "Alenka", "Barbara"], prvi_trije_brez("Adam"))


if __name__ == "__main__":
    unittest.main()

