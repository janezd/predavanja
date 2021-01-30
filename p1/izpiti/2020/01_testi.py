
import unittest

class Test(unittest.TestCase):
    def test_01_valovi(self):
        self.assertEqual([12, 5, 13], valovi([1, 5, 6, 0, 0, 0, 2, 3, 0, 5, 8, 0]))
        self.assertEqual([12, 5, 13], valovi([1, 5, 6, 0, 0, 0, 2, 3, 0, 5, 8]))
        self.assertEqual([12, 5, 13], valovi([0, 0, 1, 5, 6, 0, 0, 0, 2, 3, 0, 5, 8]))
        self.assertEqual([11, 11], valovi([0, 0, 5, 6, 0, 5, 6]))
        self.assertEqual([5, 11], valovi([0, 0, 5, 0, 5, 6]))
        self.assertEqual([5], valovi([0, 0, 5, 0,]))
        self.assertEqual([5], valovi([5, 0,]))
        self.assertEqual([5], valovi([5]))
        self.assertEqual([12], valovi([5, 3, 4]))

    def test_02_sledilnik(self):
        dnevi = [
            (["gledališča", "smučišča"], []),
            (["šole", "frizer", "muzeji"], ["smučišča"]),
            (["knjižnice"], ["muzeji", "smučišča"]),
            (["smučišča", "knjižnice", "gledališča"], ["šole"]),
            (["šole"], ["frizer", "smučišča"]),
            (["smučišča"], []),
            ([], []),
            ([], ["smučišča"])
        ]
        self.assertEqual(4, sledilnik(dnevi))

    def test_03_okuzeni(self):
        druzenja = {
            "Ana": [("Berta", 7), ("Cilka", 10), ("Dani", 4), ("Fanči", 3)],
            "Berta": [("Ana", 7), ("Cilka", 3)],
            "Cilka": [("Ana", 10), ("Berta", 3), ("Dani", 5)],
            "Dani": [("Ana", 4), ("Cilka", 5), ("Ema", 1), ("Fanči", 2)],
            "Ema": [("Dani", 1), ("Fanči", 8), ("Greta", 3)],
            "Fanči": [("Ana", 3), ("Dani", 2), ("Ema", 8), ("Greta", 2)],
            "Greta": [("Ema", 3), ("Fanči", 2)]
        }
        # Najprej samo test testa; ignoriraj
        for oseba1, d in druzenja.items():
            for oseba2, kdaj in d:
                self.assertIn((oseba1, kdaj), druzenja[oseba2])

        self.assertEqual({"Ana"}, okuzeni("Ana", 10, druzenja))
        self.assertEqual({"Ana", "Berta", "Cilka"}, okuzeni("Ana", 5, druzenja))
        self.assertEqual({"Ana", "Berta", "Cilka", "Dani"}, okuzeni("Ana", 3, druzenja))
        self.assertEqual({"Ana", "Berta", "Cilka", "Dani", "Ema", "Fanči"}, okuzeni("Ana", 2, druzenja))
        self.assertEqual({"Ana", "Berta", "Cilka", "Dani"}, okuzeni("Cilka", 1, druzenja))
        self.assertEqual({"Ana", "Cilka", "Dani"}, okuzeni("Cilka", 3, druzenja))
        self.assertEqual({"Ana", "Berta", "Cilka", "Dani", "Ema", "Fanči"}, okuzeni("Dani", 1, druzenja))
        self.assertEqual({"Ana", "Berta", "Cilka", "Dani", "Ema", "Fanči", "Greta"}, okuzeni("Ema", 0, druzenja))

    def test_04_identifikator(self):
        self.assertEqual(
            "GGU",
            identifikator(['GGGUGCCCCA', 'CCCAUAGGGU', 'CAGCUCGGUU'],
                          ['ACCUCAGGAG', 'UCGACCGAAG', 'GUCACUCGCA', 'CGCUUCCCGC', 'GGACCCCGCU'],
                          ["AUC", "GGU", "CAG", "CCC", "GGG", "UCA", "UGC"]))
        self.assertEqual(
            "GGU",
            identifikator(['GGGUGCCCCA', 'CCCAUAGGGU', 'CAGCUCGGUU'],
                          ['ACCUCAGGAG', 'UCGACCGAAG', 'GUCACUCGCA', 'CGCUUCCCGC'],
                          ["AUC", "GGU", "CAG", "CCC", "GGG", "UCA", "UGC"]))
        self.assertIn(
            identifikator(['GGGUGCCCCA', 'CCCAUAGGGU', 'CAGCUCGGUU'],
                          ['ACCUCAGGAG', 'UCGACCGAAG', 'GUCACUCGCA', 'CGCUUCCCGC'],
                          ["AUC", "CAG", "CCC", "UCA", "UGC"]),
            ("CCC", "UGC"))
        self.assertEqual(
            "GGG",
            identifikator(['GGGUGCCCCA', 'CCCAUAGGGU', 'CAGCUCGGUU'],
                          ['ACCUCAGGAG', 'UCGACCGAAG', 'GUCACUCGCA', 'CGCUUCCCGC', 'GGACCCCGCU'],
                          ["AUC", "CAG", "CCC", "GGG", "UCA", "UGC"]))
        self.assertEqual(
            "GGGGGG",
            identifikator(["UGGGGGGGA", "GGGGGGGGGGGGGGGG"],
                          ['ACCUCAGGAG', 'UCGACCGAAG', 'GGGGGGGGGGGG'],
                          ["GGGGGG", "AGG", "U"]))

    def test_05_virus(self):
        virus = Virus("ACCUTCCUUGUACUUTAA")
        self.assertFalse(virus.mrtev())
        self.assertIsNone(virus.izbij("CUU"))
        self.assertEqual("ACCUTCGUATAA", virus.ostanek())
        self.assertFalse(virus.mrtev())

        self.assertIsNone(virus.izbij("A"))
        self.assertEqual("CCUTCGUT", virus.ostanek())
        self.assertFalse(virus.mrtev())

        self.assertIsNone(virus.izbij("UT"))
        self.assertEqual("CCCG", virus.ostanek())
        self.assertFalse(virus.mrtev())

        self.assertIsNone(virus.izbij("CC"))
        self.assertEqual("CG", virus.ostanek())
        self.assertFalse(virus.mrtev())

        self.assertIsNone(virus.izbij("CG"))
        self.assertEqual("", virus.ostanek())
        self.assertTrue(virus.mrtev())

        virus = Virus("AAAAAAAAAAA")
        virus.izbij("AA")
        self.assertEqual("A", virus.ostanek())
        self.assertFalse(virus.mrtev())

        virus = Virus("AAAAAAAAAA")
        virus.izbij("AA")
        self.assertEqual("", virus.ostanek())
        self.assertTrue(virus.mrtev())


if __name__ == "__main__":
    unittest.main()
