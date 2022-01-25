def preblizu(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2 < 1.5 ** 2

def koordinate(ime, osebe):
    for ime1, x, y in osebe:
        if ime == ime1:
            return x, y
    return None


def krsitelji(osebe):
    imena = set()
    for ime, x1, y1 in osebe:
        for ime2, x2, y2 in osebe:
            if ime1 != ime2 and preblizu(x1, y1, x2, y2):
                imena.add(ime1)
                break
    return imena

def krsitelji(osebe):
    imena = set()
    for ime, x1, y1 in osebe:
        if any(ime != druga and preblizu(x1, y1, x2, y2) for druga, x2, y2 in osebe):
            imena.add(ime)
    return imena

def krsitelji(osebe):
    return {ime for ime, x1, y1 in osebe
            if any(ime != druga and preblizu(x1, y1, x2, y2) for druga, x2, y2 in osebe)}


def kazni(osebe):
    izrecene = {}
    for ime, x1, y1 in osebe:
        kazen = -1
        for druga, x2, y2 in osebe:
            if preblizu(x1, y1, x2, y2):
                kazen += 1
        if kazen:
            izrecene[ime] = kazen
    return izrecene

def kazni(osebe):
    izrecene = {}
    for ime, x1, y1 in osebe:
        kazen = sum(preblizu(x1, y1, x2, y2) for _, x2, y2 in osebe) - 1
        if kazen:
            izrecene[ime] = kazen
    return izrecene


def kazni(osebe):
    return {ime: kazen for ime, x1, y1 in osebe
            if (kazen := sum(preblizu(x1, y1, x2, y2) for _, x2, y2 in osebe) - 1) > 0}


def krsitelji(osebe):
    return set(kazni(osebe))

def okuzeni(ime, osebe):
    imena = {ime}
    x1, y1 = koordinate(ime, osebe)
    for drugi, x2, y2 in osebe:
        if y1 > y2 and preblizu(x1, y1, x2, y2):
            imena |= okuzeni(drugi, osebe)
    return imena

def kihanje(imena, osebe):
    osebe = osebe.copy()
    for ime in imena:
        koord = koordinate(ime, osebe)
        if koord is None:
            continue
        x1, y1 = koord
        i = 0
        while i < len(osebe):
            _, x2, y2 = osebe[i]
            if preblizu(x1, y1, x2, y2):
                del osebe[i]
            else:
                i += 1
    return {ime for ime, x, y in osebe}

def kihanje(imena, osebe):
    for ime in imena:
        koord = koordinate(ime, osebe)
        if koord is None:
            continue
        x1, y1 = koord
        preostali = []
        for ime2, x2, y2 in osebe:
            if not preblizu(x1, y1, x2, y2):
                preostali.append((ime2, x2, y2))
        osebe = preostali
    return {ime for ime, x, y in osebe}

def kihanje(imena, osebe):
    prisotne = {ime for ime, x, y in osebe}
    for ime in imena:
        if ime not in prisotne:
            continue
        x1, y1 = koordinate(ime, osebe)
        for ime2, x2, y2 in osebe:
            if preblizu(x1, y1, x2, y2):
                prisotne.discard(ime2)
    return prisotne


class Prireditev:
    def __init__(self, min_razdalja):
        self.min_razdalja = min_razdalja
        self.osebe = []

    def prihod(self, ime, x, y):
        if all((x - x2) ** 2 + (y - y2) ** 2 >= self.min_razdalja ** 2
               for _, x2, y2 in self.osebe):
            self.osebe.append((ime, x, y))

    def udelezenci(self):
        return {ime for ime, x, y in self.osebe}

class Prireditev:
    def __init__(self, min_razdalja):
        self.min_razdalja = min_razdalja
        self.koordinate = []
        self.osebe = set()

    def prihod(self, ime, x, y):
        if all((x - x2) ** 2 + (y - y2) ** 2 >= self.min_razdalja ** 2
               for x2, y2 in self.koordinate):
            self.osebe.add(ime)
            self.koordinate.append((x, y))

    def udelezenci(self):
        return self.osebe


import unittest

class Test(unittest.TestCase):
    osebe = [("Ana", 2, 4.5),
             ("Berta", 1, 3),
             ("Cilka", 1, 4),
             ("Dani", -1, 2),
             ("Ema", 1, 1),
             ("Fanči", 2, 0.5),
             ("Greta", -1, -1.5),
             ("Helga", 0, -1),
             ("Iva", 2, 0),
             ("Jana", 0, 0),
             ("Klara", 5, 1)
             ]

    def test_0_preblizu(self):
        self.assertTrue(preblizu(5, 3, 6, 2))
        self.assertTrue(preblizu(5, 2, 5, 2))
        self.assertTrue(preblizu(6, 2, 5, 3))
        self.assertTrue(preblizu(0, 0, 1.4, 0))
        self.assertFalse(preblizu(5, 3, 6, 1))

    def test_0_koordinate(self):
        self.assertEqual((-1, 2), koordinate("Dani", self.osebe))

    def test_1_krsitelji(self):
        self.assertEqual(
            set("Ana Berta Cilka Ema Fanči Greta Helga Iva Jana".split()),
            krsitelji(self.osebe)
        )
        self.assertEqual(
            set("Ana Berta Cilka Ema Fanči Greta Helga Iva Jana".split()),
            krsitelji(self.osebe[:-1])
        )
        self.assertEqual(
            set("Greta Helga Jana".split()),
            krsitelji(self.osebe[-5:])
        )
        self.assertEqual(
            set(),
            krsitelji(self.osebe[:2])
        )

    def test_2_kazni(self):
        self.assertEqual(
            {"Ana": 1, "Berta": 1, "Cilka": 2, "Ema": 3,
             "Fanči": 2, "Greta": 1, "Helga": 2, "Iva": 2, "Jana": 2},
            kazni(self.osebe)
        )

    def test_3_okuzenih(self):
        self.assertEqual(
            {"Ema", "Fanči", "Iva", "Jana", "Greta", "Helga"},
            okuzeni("Ema", self.osebe))
        self.assertEqual(
            {"Jana", "Greta", "Helga"},
            okuzeni("Jana", self.osebe))
        self.assertEqual(
            {"Ana", "Berta", "Cilka"},
            okuzeni("Ana", self.osebe))
        self.assertEqual(
            {"Berta"},
            okuzeni("Berta", self.osebe))
        self.assertEqual(
            {"Klara"},
            okuzeni("Klara", self.osebe))

    def test_4_kihanje(self):
        self.assertEqual(
            set("Ana Berta Cilka Dani Ema Fanči Greta Helga Iva Jana Klara".split()),
            kihanje([], self.osebe)
        )
        self.assertEqual(
            set("Ana Berta Cilka Dani Greta Helga Jana Klara".split()),
            kihanje(["Fanči"], self.osebe)
        )
        self.assertEqual(
            set("Ana Berta Cilka Dani Greta Helga Klara".split()),
            kihanje(["Ema"], self.osebe)
        )
        self.assertEqual(
            set("Ana Berta Cilka Dani Greta Helga Klara".split()),
            kihanje(["Ema", "Jana"], self.osebe)
        )
        self.assertEqual(
            set("Ana Berta Cilka Dani Greta Helga Klara".split()),
            kihanje(["Ema", "Fanči"], self.osebe)
        )
        self.assertEqual(
            set("Ana Berta Cilka Dani Greta Helga".split()),
            kihanje(["Ema", "Fanči", "Klara"], self.osebe)
        )
        self.assertEqual(
            set("Dani Greta Helga".split()),
            kihanje(["Ema", "Fanči", "Klara", "Cilka"], self.osebe)
        )
        self.assertEqual(
            set("Ana Berta Cilka Dani Fanči Greta Iva Klara".split()),
            kihanje(["Jana", "Helga", "Ema"], self.osebe)
        )
        self.assertEqual(
            set("Ana Berta Cilka Dani Klara".split()),
            kihanje(["Helga", "Ema", "Jana"], self.osebe)
        )

    def test_5_prireditev(self):
        g = Prireditev(1.5)
        for ime, x, y in self.osebe:
            g.prihod(ime, x, y)
        self.assertEqual(
            {"Ana", "Berta", "Dani", "Ema", "Greta", "Klara"},
            g.udelezenci()
        )

        g = Prireditev(1.5)
        for ime, x, y in self.osebe:
            if ime != "Ema":
                g.prihod(ime, x, y)
        self.assertEqual(
            {"Ana", "Berta", "Dani", "Fanči", "Greta", "Jana", "Klara"},
            g.udelezenci()
        )

        g = Prireditev(3)
        for ime, x, y in self.osebe:
            g.prihod(ime, x, y)
        self.assertEqual(
            {"Ana", "Dani", "Fanči", "Greta", "Klara"},
            g.udelezenci()
        )


if __name__ == "__main__":
    unittest.main()

