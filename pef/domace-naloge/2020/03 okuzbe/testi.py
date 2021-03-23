import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.obiski = [
            ("Ana", "kava"), ("Berta", "kava"), ("Cilka", "telovadba"),
            ("Dani", "zdravnik"), ("Ana", "zdravnik"), ("Cilka", "kava"),
            ("Ema", "telovadba")]


    def test_osebe(self):
        self.assertEqual({"Ana", "Berta", "Cilka", "Dani", "Ema"}, osebe(self.obiski))

    def test_aktivnosti(self):
        self.assertEqual({"kava", "telovadba", "zdravnik"}, dejavnosti(self.obiski))

    def test_dejavnosti_osebe(self):
        self.assertEqual({"kava", "zdravnik"}, dejavnosti_osebe("Ana", self.obiski))
        obiski = self.obiski + [("Ana", "kava")]
        self.assertEqual({"kava", "zdravnik", "kava"}, dejavnosti_osebe("Ana", obiski))
        self.assertEqual({"telovadba", "kava"}, dejavnosti_osebe("Cilka", self.obiski))

    def test_udelezenci(self):
        self.assertEqual({"Ana", "Berta", "Cilka"}, udelezenci("kava", self.obiski))
        self.assertEqual({"Ema", "Cilka"}, udelezenci("telovadba", self.obiski))

    def test_v_stiku(self):
        self.assertTrue(v_stiku("Ana", "Berta", self.obiski))
        self.assertTrue(v_stiku("Ema", "Cilka", self.obiski))
        self.assertFalse(v_stiku("Ema", "Ana", self.obiski))

    def test_v_karanteno(self):
        self.assertEqual({"Berta", "Cilka", "Dani"}, v_karanteno("Ana", self.obiski))
        self.assertEqual({"Cilka"}, v_karanteno("Ema", self.obiski))

    def test_zlatko(self):
        self.assertIn(zlatko(self.obiski), {"Cilka", "Ana"})
        obiski = [("a", "1"), ("a", "2"),
                  ("b", "1"), ("b", "3"), ("b", "4"),
                  ("c", "2"), ("c", "5"), ("c", "6"),
                  ]
        self.assertEqual("a", zlatko(obiski))

    def test_osumljenci(self):
        self.assertEqual({"Dani"}, osumljenci("Ana", {"Berta"}, self.obiski))
        self.assertEqual({"Berta", "Cilka"}, osumljenci("Ana", {"Dani"}, self.obiski))
        self.assertEqual({"Berta", "Cilka", "Dani"}, osumljenci("Ana", set(), self.obiski))
        self.assertEqual({"Ana"}, osumljenci("Dani", set(), self.obiski))
        self.assertEqual(set(), osumljenci("Dani", {"Berta"}, self.obiski))


if __name__ == "__main__":
    unittest.main()
