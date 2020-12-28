def prestej(darila):
    stevila = {}
    for darilo in darila:
        if darilo in stevila:
            stevila[darilo] += 1
        else:
            stevila[darilo] = 1
    return stevila

def prestej(darila):
    stevci = {}
    for dar in darila:
        stevci[dar] = darila.count(dar)
    return stevci


def prestej(darila):
    return {dar: darila.count(dar) for dar in darila}



def sestej(darila):
    stevila = {}
    for darilo, kolicina in darila:
        if darilo in stevila:
            stevila[darilo] += kolicina
        else:
            stevila[darilo] = kolicina
    return stevila

def cena(stevila, cene):
    vsota = 0
    for darilo, kosov in stevila.items():
        vsota += kosov * cene[darilo]
    return vsota


def cena(stevila, cene):
    return sum([kosov * cene[darilo] for darilo, kosov in stevila.items()])


def stevilo_daril(stevila):
    return sum(stevila.values())

def razlicnih_daril(stevila):
    return len(stevila)

def napredek(lani, letos):
    razlika = letos.copy()
    for darilo, kosov in lani.items():
        if darilo in razlika:
            razlika[darilo] -= kosov
            if not razlika[darilo]:
                del razlika[darilo]
        else:
            razlika[darilo] = -kosov
    return razlika



import unittest
class Test01Ogrevalna(unittest.TestCase):
    def test_prestej(self):
        self.assertDictEqual({"avto": 3, "lok": 2, "bomboni": 1}, prestej(["avto", "lok", "avto", "avto", "bomboni", "lok"]))
        self.assertDictEqual({"avto": 4}, prestej(["avto", "avto", "avto", "avto"]))
        self.assertDictEqual({}, prestej([]))


class Test02Obvezna(unittest.TestCase):
    def test_sestej(self):
        self.assertDictEqual(
            {"avto": 7, "lok": 5, "bomboni": 42},
            sestej([("avto", 2), ("lok", 2), ("avto", 4), ("avto", 1),
                    ("bomboni", 42), ("lok", 3)]))
        self.assertDictEqual({"avto": 8}, sestej([("avto", 1), ("avto", 4), ("avto", 2), ("avto", 1)]))
        self.assertDictEqual({"avto": 1}, sestej([("avto", 1)]))
        self.assertDictEqual({"avto": 2}, sestej([("avto", 2)]))
        self.assertDictEqual({}, sestej([]))

    def test_cena(self):
        self.assertEqual(
                88,
                cena({"avto": 7, "lok": 5, "bomboni": 42},
                     {"avto": 3, "lok": 5, "bomboni": 1, "dron": 10}))
        self.assertEqual(
                95,
                cena({"avto": 7, "lok": 5, "bomboni": 42},
                     {"avto": 4, "lok": 5, "bomboni": 1, "dron": 10}))
        self.assertEqual(
                21,
                cena({"avto": 7},
                     {"avto": 3, "lok": 5, "bomboni": 1, "dron": 10}))
        self.assertEqual(0, cena({}, {"avto": 3, "lok": 5, "bomboni": 1, "dron": 10}))
        self.assertEqual(
                20,
                cena({"dron": 2}, {"avto": 3, "lok": 5, "bomboni": 1, "dron": 10}))

    def test_stevilo_daril(self):
        self.assertEqual(54, stevilo_daril({"avto": 7, "lok": 5, "bomboni": 42}))
        self.assertEqual(7, stevilo_daril({"avto": 7}))
        self.assertEqual(0, stevilo_daril({}))

    def test_razlicnih_daril(self):
        self.assertEqual(3, razlicnih_daril({"avto": 7, "lok": 5, "bomboni": 42}))
        self.assertEqual(1, razlicnih_daril({"avto": 7}))
        self.assertEqual(0, razlicnih_daril({}))


class Test03Dodatna(unittest.TestCase):
    def test_napredek(self):
        self.assertDictEqual(
                {"avto": 5, "lok": 2, "bomboni": 2, "dron": 4},
                napredek({"avto": 3, "lok": 5, "bomboni": 1, "dron": 10},
                         {"avto": 8, "lok": 7, "bomboni": 3, "dron": 14}))
        self.assertDictEqual(
                {"avto": 5, "bomboni": 2, "dron": 4},
                napredek({"avto": 3, "lok": 5, "bomboni": 1, "dron": 10},
                         {"avto": 8, "lok": 5, "bomboni": 3, "dron": 14}))
        self.assertDictEqual(
                {"avto": 5, "lok": -2, "bomboni": 2, "dron": 4},
                napredek({"avto": 3, "lok": 5, "bomboni": 1, "dron": 10},
                         {"avto": 8, "lok": 3, "bomboni": 3, "dron": 14}))
        self.assertDictEqual(
                {"avto": 5, "lok": 3, "bomboni": 3, "dron": 4},
                napredek({"avto": 3, "dron": 10},
                         {"avto": 8, "lok": 3, "bomboni": 3, "dron": 14}))
        self.assertDictEqual(
                {"avto": 5, "lok": -5, "bomboni": -1, "dron": 4},
                napredek({"avto": 3, "lok": 5, "bomboni": 1, "dron": 10},
                         {"avto": 8, "dron": 14}))
        self.assertDictEqual(
                {"avto": 8, "dron": 14},
                napredek({}, {"avto": 8, "dron": 14}))
        self.assertDictEqual(
                {"avto": 8, "dron": 14, "lizika": -4},
                napredek({"lizika": 4}, {"avto": 8, "dron": 14}))
        self.assertDictEqual(
                {"lizika": -4},
                napredek({"lizika": 4}, {}))
        self.assertDictEqual({}, napredek({}, {}))


if __name__ == "__main__":
    unittest.main()
