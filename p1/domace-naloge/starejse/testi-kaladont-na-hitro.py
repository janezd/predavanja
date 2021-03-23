
def kvaliteta_besede(beseda):
    return (-len(beseda), beseda)


import unittest
import ast


class TestBase(unittest.TestCase):
    functions = {elm.name: elm
                 for elm in ast.parse(open(__file__).read()).body
                 if isinstance(elm, ast.FunctionDef)}

    def assert_is_one_line(self, func):
        func
        body = self.functions[func.__code__.co_name].body
        self.assertEqual(len(body), 1, "\nFunkcija ni dolga le eno vrstico")
        self.assertIsInstance(body[0], ast.Return, "\nFunkcija naj bi vsebovala le return")

    def test_nedovoljene_funkcije(self):
        dovoljene_funkcije = {
            "lahko_sledi", "ni_ponavljanj", "preveri_zaporedje",
            "mozne_naslednje",
            "kvaliteta_besede", "izberi_besedo", "pogostosti_zacetnic"}
        for func in self.functions:
            self.assertIn(func, dovoljene_funkcije, f"\nFunkcija {func} ni dovoljena.")

class Obvezna(TestBase):
    def test_lahko_sledi(self):
        self.assert_is_one_line(lahko_sledi)
        self.assertTrue(lahko_sledi("OMARA", "ASPARAGUS"))
        self.assertTrue(lahko_sledi("PETER", "REBEKA"))
        self.assertFalse(lahko_sledi("PETER", "ASPARAGUS"))
        self.assertFalse(lahko_sledi("PRETEP", "PRETEP"))

    def test_ni_ponavljanj(self):
        self.assert_is_one_line(ni_ponavljanj)
        self.assertTrue(ni_ponavljanj(["PETER", "ŽOGA", "METLA", "JOŽE"]))
        self.assertTrue(ni_ponavljanj(["PETER"]))
        self.assertTrue(ni_ponavljanj([]))

        self.assertFalse(ni_ponavljanj(["PETER", "PETER"]))
        self.assertFalse(ni_ponavljanj(["PETER", "ŽOGA", "JOŽE", "JOŽE"]))
        self.assertFalse(ni_ponavljanj(["PETER", "ŽOGA", "JOŽE", "ŽOGA"]))
        self.assertFalse(ni_ponavljanj(["PETER", "ŽOGA", "JOŽE", "PETER"]))
        self.assertFalse(ni_ponavljanj(["PETER", "ŽOGA", "PETER", "JOŽE"]))

    def test_preveri_zaporedje(self):
        self.assert_is_one_line(preveri_zaporedje)
        self.assertTrue(preveri_zaporedje(
            ["PETER", "RAZBOJNIK", "KLEMEN", "NEPRIDIPRAV", "VINKO",
             "OROŽNIK"]))
        self.assertTrue(preveri_zaporedje(["PETER", "RAZBOJNIK"]))
        self.assertTrue(preveri_zaporedje(["VINKO"]))

        self.assertFalse(
            preveri_zaporedje(["PETER", "ZABOJNIK", "KLEMEN", "NEPRIDIPRAV"]))
        self.assertFalse(
            preveri_zaporedje(["PETER", "RAZBOJNIK", "ALEŠ", "NEPRIDIPRAV"]))
        self.assertFalse(
            preveri_zaporedje(["PETER", "RAZBOJNIK", "KLEMEN", "TAT"]))
        self.assertFalse(
            preveri_zaporedje(["PETER", "RAZBOJNIK", "KLEP", "PETER", "RIBA"]))

    def test_mozne_naslednje(self):
        self.assert_is_one_line(mozne_naslednje)
        mali_slovar = ["ABRAHAM", "ANGLIJA", "BOTER", "ČEŠNJA"]
        self.assertEqual(["ABRAHAM", "ANGLIJA"],
                         mozne_naslednje("ROŽA", mali_slovar))
        self.assertEqual(["BOTER"], mozne_naslednje("ROB", mali_slovar))
        self.assertEqual([], mozne_naslednje("ROBNIK", mali_slovar))



class TestDodatna(TestBase):
    slovar = ["ABRAHAM", "MELODIJA", "ASTEROID", "DREVO", "MEČ", "OBLAK",
              "KLEPTOMAN", "KAČA", ]

    def test_pogostosti_zacetnic(self):
        self.assert_is_one_line(pogostosti_zacetnic)
        self.assertEqual([2, 1, 0, 1] + [0] * 21, pogostosti_zacetnic(
            ["ABRAHAM", "ANGLIJA", "BOTER", "ČEŠNJA"]))
        self.assertEqual(
            [2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0,
             0, 0, 0], pogostosti_zacetnic(self.slovar))

    def test_izberi_besedo(self):
        self.assert_is_one_line(izberi_besedo)
        self.assertEqual(
            "RAZBOJNIK", izberi_besedo("PETER",
                                       ["RAZBOJNIK", "ROPAR", "RAVBAR", "TAT",
                                        "ŽEPAR", "OTORINOLARINGOLOGIJA"]))
        self.assertEqual(
            "RAZBOJNIK", izberi_besedo("PETER",
                                       ["ROPAR", "RAVBAR", "RAZBOJNIK", "TAT",
                                        "ŽEPAR", "OTORINOLARINGOLOGIJA"]))
        self.assertEqual(
            "RAVBAR", izberi_besedo("PETER",
                                    ["ROPAR", "RAVBAR", "TAT", "ROLAND",
                                     "ŽEPAR", "OTORINOLARINGOLOGIJA"]))
        self.assertEqual(
            "RAVBAR", izberi_besedo("PETER", ["ROPAR", "ROLAND", "TAT",
                                              "OTORINOLARINGOLOGIJA", "RAVBAR",
                                              "ŽEPAR"]))
        self.assertEqual(
            "PETER", izberi_besedo("PRETEP",
                                   ["PETER", "OTORINOLARINGOLOGIJA", "PRETEP",
                                    "PERO", "MAFIJA"]))


if __name__ == "__main__":
    unittest.main()

