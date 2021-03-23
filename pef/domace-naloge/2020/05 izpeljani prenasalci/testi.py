


import unittest
import ast

class Test(unittest.TestCase):
    functions = {elm.name: elm
                 for elm in ast.parse(open(__file__, "r", encoding="utf-8").read()).body
                 if isinstance(elm, ast.FunctionDef)}

    def setUp(self):
        self.obiski = [
            ("Ana", "kava"), ("Berta", "kava"), ("Cilka", "telovadba"),
            ("Dani", "zdravnik"), ("Ana", "zdravnik"), ("Cilka", "kava"),
            ("Ema", "telovadba")]

    def assert_is_one_line(self, func):
        func
        body = self.functions[func.__code__.co_name].body
        self.assertEqual(len(body), 1, "\nFunkcija ni dolga le eno vrstico")
        self.assertIsInstance(body[0], ast.Return, "\nFunkcija naj bi vsebovala le return")

    def test_nedovoljene_funkcije(self):
        dovoljene_funkcije = {
            "osebe", "dejavnosti", "dejavnosti_osebe",
            "udelezenci", "v_stiku", "v_karanteno"}
        for func in self.functions:
            self.assertIn(func, dovoljene_funkcije, f"\nFunkcija {func} ni dovoljena.")

    def test_osebe(self):
        self.assert_is_one_line(osebe)
        self.assertEqual({"Ana", "Berta", "Cilka", "Dani", "Ema"}, osebe(self.obiski))

    def test_aktivnosti(self):
        self.assert_is_one_line(dejavnosti)
        self.assertEqual({"kava", "telovadba", "zdravnik"}, dejavnosti(self.obiski))

    def test_dejavnosti_osebe(self):
        self.assert_is_one_line(dejavnosti_osebe)
        self.assertEqual({"kava", "zdravnik"}, dejavnosti_osebe("Ana", self.obiski))
        obiski = self.obiski + [("Ana", "kava")]
        self.assertEqual({"kava", "zdravnik", "kava"}, dejavnosti_osebe("Ana", obiski))
        self.assertEqual({"telovadba", "kava"}, dejavnosti_osebe("Cilka", self.obiski))

    def test_udelezenci(self):
        self.assert_is_one_line(udelezenci)
        self.assertEqual({"Ana", "Berta", "Cilka"}, udelezenci("kava", self.obiski))
        self.assertEqual({"Ema", "Cilka"}, udelezenci("telovadba", self.obiski))

    def test_v_stiku(self):
        self.assert_is_one_line(v_stiku)
        self.assertTrue(v_stiku("Ana", "Berta", self.obiski))
        self.assertTrue(v_stiku("Ema", "Cilka", self.obiski))
        self.assertFalse(v_stiku("Ema", "Ana", self.obiski))

    def test_v_karanteno(self):
        self.assert_is_one_line(v_karanteno)
        self.assertEqual({"Berta", "Cilka", "Dani"}, v_karanteno("Ana", self.obiski))
        self.assertEqual({"Cilka"}, v_karanteno("Ema", self.obiski))


if __name__ == "__main__":
    unittest.main()
