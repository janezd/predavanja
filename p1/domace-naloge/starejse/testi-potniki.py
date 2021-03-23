
import unittest
from unittest.mock import Mock


class TestBase(unittest.TestCase):
    kraji = [
        ('Brežice', 68.66, 7.04),
        ('Lenart', 85.20, 78.75),
        ('Rateče', -65.04, 70.04),
        ('Ljutomer', 111.26, 71.82),
        ('Rogaška Slatina', 71.00, 42.00),
        ('Ribnica', 7.10, -10.50),
        ('Dutovlje', -56.80, -6.93),
        ('Lokve', -57.94, 19.32),
        ('Vinica', 43.81, -38.43),
        ('Brtonigla', -71.00, -47.25),
        ('Kanal', -71.00, 26.25),
        ('Črnomelj', 39.05, -27.93),
        ('Trbovlje', 29.61, 35.07),
        ('Beltinci', 114.81, 80.54),
        ('Domžale', -2.34, 31.50),
        ('Hodoš', 120.70, 105.00),
        ('Škofja Loka', -23.64, 35.07),
        ('Velike Lašče', 0.00, 0.00),
        ('Velenje', 33.16, 54.29),
        ('Šoštanj', 29.61, 57.75),
        ('Laško', 42.60, 33.29),
        ('Postojna', -29.54, -5.25),
        ('Ilirska Bistrica', -27.19, -27.93),
        ('Radenci', 100.61, 84.00),
        ('Črna', 15.41, 66.57),
        ('Radeče', 39.05, 24.57),
        ('Vitanje', 47.36, 57.75),
        ('Bled', -37.84, 56.07),
        ('Tolmin', -63.90, 36.75),
        ('Miren', -72.14, 7.04),
        ('Ptuj', 87.61, 61.32),
        ('Gornja Radgona', 97.06, 89.25),
        ('Plave', -73.34, 21.00),
        ('Novo mesto', 37.91, -3.47),
        ('Bovec', -76.89, 52.50),
        ('Nova Gorica', -69.79, 12.29),
        ('Krško', 60.35, 14.07),
        ('Cerknica', -18.89, -3.47),
        ('Slovenska Bistrica', 66.31, 57.75),
        ('Anhovo', -72.14, 22.78),
        ('Ormož', 107.71, 61.32),
        ('Škofije', -59.14, -27.93),
        ('Čepovan', -60.35, 22.78),
        ('Murska Sobota', 108.91, 87.57),
        ('Ljubljana', -8.24, 22.78),
        ('Idrija', -43.74, 17.54),
        ('Radlje ob Dravi', 41.46, 82.32),
        ('Žalec', 37.91, 43.79),
        ('Mojstrana', -49.70, 64.79),
        ('Log pod Mangartom', -73.34, 59.54),
        ('Podkoren', -62.69, 70.04),
        ('Kočevje', 16.61, -21.00),
        ('Soča', -69.79, 52.50),
        ('Ajdovščina', -53.25, 5.25),
        ('Bohinjska Bistrica', -48.49, 47.25),
        ('Tržič', -22.44, 56.07),
        ('Piran', -75.69, -31.50),
        ('Kranj', -20.09, 43.79),
        ('Kranjska Gora', -60.35, 68.25),
        ('Izola', -68.59, -31.50),
        ('Radovljica', -31.95, 54.29),
        ('Gornji Grad', 13.06, 49.03),
        ('Šentjur', 54.46, 40.32),
        ('Koper', -63.90, -29.72),
        ('Celje', 45.01, 42.00),
        ('Mislinja', 42.60, 66.57),
        ('Metlika', 48.56, -19.21),
        ('Žaga', -81.65, 49.03),
        ('Komen', -63.90, -1.68),
        ('Žužemberk', 21.30, 0.00),
        ('Pesnica', 74.55, 80.54),
        ('Vrhnika', -23.64, 14.07),
        ('Dravograd', 28.40, 78.75),
        ('Kamnik', -1.14, 40.32),
        ('Jesenice', -40.19, 64.79),
        ('Kobarid', -74.55, 43.79),
        ('Portorož', -73.34, -33.18),
        ('Muta', 37.91, 82.32),
        ('Sežana', -54.39, -13.96),
        ('Vipava', -47.29, 1.79),
        ('Maribor', 72.21, 75.28),
        ('Slovenj Gradec', 31.95, 71.82),
        ('Litija', 14.20, 22.78),
        ('Na Logu', -62.69, 57.75),
        ('Stara Fužina', -52.04, 47.25),
        ('Motovun', -56.80, -52.50),
        ('Pragersko', 73.41, 57.75),
        ('Most na Soči', -63.90, 33.29),
        ('Brestanica', 60.35, 15.75),
        ('Savudrija', -80.44, -34.96),
        ('Sodražica', 0.00, -6.93),
    ]

    kraji6 = [
        ('Brežice', 68.66, 7.04),
        ('Lenart', 85.20, 78.75),
        ('Rateče', -65.04, 70.04),
        ('Ljutomer', 111.26, 71.82),
        ('Rogaška Slatina', 71.00, 42.00),
        ('Ribnica', 7.10, -10.50),
    ]

    try:
        povezave5 = dvosmerno(povezave(5, kraji))
    except:
        pass


class Test06(TestBase):
    def test_koordict(self):
        self.assertEqual(
            koordict(self.kraji6),
            {'Brežice': (68.66, 7.04),
             'Lenart': (85.20, 78.75),
             'Rateče': (-65.04, 70.04),
             'Ljutomer': (111.26, 71.82),
             'Rogaška Slatina': (71.00, 42.00),
             'Ribnica': (7.10, -10.50)
            }
        )

    def test_razdalje(self):
        razdalja = {k: r for r, k in razdalje("Lenart", self.kraji6)}
        self.assertAlmostEqual(razdalja["Brežice"], 5415.895699999999)
        self.assertAlmostEqual(razdalja["Rogaška Slatina"], 1552.2025)
        self.assertAlmostEqual(razdalja["Ljutomer"], 727.1485000000002)
        self.assertAlmostEqual(razdalja["Ribnica"], 14065.1725)
        self.assertAlmostEqual(razdalja["Rateče"], 22647.921700000003)

        razdalja = razdalje("Brežice", self.kraji6[:2]).pop()
        self.assertAlmostEqual(razdalja[0], 5415.895699999999)
        self.assertAlmostEqual(razdalja[1], "Lenart")

        self.assertEqual(razdalje("Brežice", self.kraji6[:1]), set())

    def test_sosedi(self):
        self.assertEqual(
            sosedi(1, "Maribor", self.kraji), {'Pesnica'}
        )
        self.assertEqual(
            sosedi(2, "Maribor", self.kraji), {'Lenart', 'Pesnica'}
        )
        self.assertEqual(
            sosedi(3, "Maribor", self.kraji), {'Lenart', 'Pragersko', 'Pesnica'}
        )
        self.assertEqual(
            sosedi(0, "Maribor", self.kraji), set()
        )
        self.assertEqual(
            sosedi(10, "Ljubljana", self.kraji),
            {'Cerknica', 'Domžale', 'Gornji Grad', 'Kamnik', 'Kranj', 'Litija',
             'Sodražica', 'Velike Lašče', 'Vrhnika', 'Škofja Loka'}
        )

    def test_povezave(self):
        self.assertEqual(
            povezave(2, self.kraji6),
            {'Brežice': {'Rogaška Slatina', 'Ribnica'},
             'Lenart': {'Rogaška Slatina', 'Ljutomer'},
             'Ljutomer': {'Lenart', 'Rogaška Slatina'},
             'Rateče': {'Rogaška Slatina', 'Ribnica'},
             'Ribnica': {'Rogaška Slatina', 'Brežice'},
             'Rogaška Slatina': {'Lenart', 'Brežice'}}
        )
        self.assertEqual(
            povezave(3, self.kraji6),
            {'Brežice': {'Ribnica', 'Lenart', 'Rogaška Slatina'},
             'Lenart': {'Brežice', 'Ljutomer', 'Rogaška Slatina'},
             'Ljutomer': {'Brežice', 'Lenart', 'Rogaška Slatina'},
             'Rateče': {'Ribnica', 'Brežice', 'Rogaška Slatina'},
             'Ribnica': {'Brežice', 'Rateče', 'Rogaška Slatina'},
             'Rogaška Slatina': {'Brežice', 'Lenart', 'Ljutomer'}}
        )

    def test_dvosmerno(self):
        d = {"a": {"b", "c"},
             "b": {"a", "d"},
             "c": {"a", "b"},
             "d": {"c", "b"}
            }
        c = d.copy()
        self.assertEqual(
            dvosmerno(d),
            {"a": {"b", "c"},
             "b": {"a", "c", "d"},
             "c": {"a", "b", "d"},
             "d": {"c", "b"}}
        )
        self.assertEqual(
            c, d, "Funkcija 'dvosmerno' ne sme spreminjati podanega slovarja")
        self.assertEqual(d["b"], {"a", "d"})


class Test07(TestBase):
    def test_veljavna_pot(self):
        self.assertTrue(
            veljavna_pot(["Ljubljana", "Litija", "Žužemberk", "Novo mesto",
                          "Metlika", "Črnomelj", "Kočevje"], self.povezave5))
        self.assertTrue(
            veljavna_pot(
            ["Ljubljana", "Litija", "Žužemberk", "Novo mesto",
             "Metlika", "Črnomelj", "Kočevje"][::-1],
            self.povezave5))
        self.assertTrue(
            veljavna_pot(["Ljubljana", "Litija", "Žužemberk"], self.povezave5))
        self.assertTrue(veljavna_pot(["Ljubljana", "Litija"], self.povezave5))
        self.assertTrue(veljavna_pot(["Ljubljana"], self.povezave5))
        self.assertTrue(veljavna_pot([], self.povezave5))

        self.assertTrue(
            veljavna_pot(["Ljubljana", "Litija", "Žužemberk", "Velike Lašče",
                          "Ljubljana", "Litija", "Žužemberk"], self.povezave5))
        self.assertTrue(
            veljavna_pot(
                ["Vrhnika", "Cerknica", "Postojna", "Vrhnika", "Cerknica"],
                self.povezave5))
        self.assertTrue(
            veljavna_pot(
                ["Ljubljana", "Litija", "Kamnik", "Domžale", "Škofja Loka"] * 5
                + ["Vrhnika", "Postojna"],
                self.povezave5))

        self.assertFalse(
            veljavna_pot(
                ["Ljubljana", "Idrija", "Vrhnika", "Postojna"],
                self.povezave5
            )
        )
        self.assertFalse(
            veljavna_pot(
                ["Kamnik", "Ljubljana", "Idrija", "Vrhnika", "Postojna"],
                self.povezave5
            )
        )
        self.assertFalse(
            veljavna_pot(
                ["Kranj", "Kamnik", "Ljubljana", "Idrija"],
                self.povezave5
            )
        )
        self.assertFalse(
            veljavna_pot(
                ["Ljubljana", "Domžale", "Ljubljana", "Kamnik", "Kranj"],
                self.povezave5
            )
        )
        self.assertFalse(
            veljavna_pot(
                ["Kamnik", "Ljubljana", "Vrhnika", "Ljubljana", "Litija",
                 "Žužemberk"],
                self.povezave5
            )
        )
        self.assertFalse(
            veljavna_pot(["Ljubljana", "Ljubljana", "Vrhnika"], self.povezave5))
        self.assertFalse(
            veljavna_pot(["a", "b", "c"], {"a": {"b"}, "b": {"a"}, "c": {"b"}}))

    def test_izberi(self):
        d = ["a", "b", "c", "d"]
        nabrano = set()
        for i in range(100):
            i = izberi(d, "a")
            self.assertIn(i, {"b", "c", "d"})
            nabrano.add(i)
        self.assertEqual(nabrano, {"b", "c", "d"})

        d = {"a", "b", "c", "d"}
        nabrano = set()
        for i in range(100):
            i = izberi(d, "a")
            self.assertIn(i, {"b", "c", "d"})
            nabrano.add(i)
        self.assertEqual(nabrano, {"b", "c", "d"})

    def test_potnik(self):
        zacetek = "Kočevje"
        pot = potnik(zacetek, 1000, self.povezave5)
        self.assertEqual(pot[0], zacetek)
        self.assertEqual(len(pot), 1001)
        self.assertTrue(veljavna_pot(pot, self.povezave5))
        self.assertGreater(len(set(pot)), 10)


class Test08(TestBase):
    def test_prestej(self):
        self.assertEqual(
            prestej(["ana", "berta", "ana", "cilka", "berta", "ana"]),
            {"ana": 3, "berta": 2, "cilka": 1}
        )
        self.assertEqual(
            prestej("aaabbcadda"),
            {"a": 5, "b": 2, "c": 1, "d": 2})

    def test_pristej_slovar(self):
        a, b, c, d = "abcd"
        s = {a: 5, b: 6, d: 4}
        t = {b: 3, c: 8}
        self.assertIsNone(pristej_slovar(s, t))
        self.assertDictEqual({a: 5, b: 9, c: 8, d: 4}, s)
        self.assertDictEqual({b: 3, c: 8}, t)

        e = {}
        self.assertIsNone(pristej_slovar(s, e))
        self.assertDictEqual({a: 5, b: 9, c: 8, d: 4}, s)
        self.assertDictEqual({}, e)

        self.assertIsNone(pristej_slovar(e, t))
        self.assertDictEqual({b: 3, c: 8}, e)

    def test_pomembnost(self):
        global potnik
        stari_potnik = potnik
        try:
            pot = ["Metlika", "Novo mesto", "Brežice", "Radeče", "Novo mesto",
                   "Žužemberk", "Kočevje", "Novo mesto", "Brežice"]
            potnik = Mock(return_value=pot)
            p = pomembnost(5, 8, self.povezave5, False)
            self.assertEqual(potnik.call_count, 5)
            self.assertEqual(
                p,
                {"Metlika": 5, "Novo mesto": 15, "Brežice": 10, "Radeče": 5,
                 "Žužemberk": 5, "Kočevje": 5})

            p = pomembnost(5, 8, self.povezave5, False)
            self.assertEqual(potnik.call_count, 10)
            self.assertEqual(
                p,
                {"Metlika": 5, "Novo mesto": 15, "Brežice": 10, "Radeče": 5,
                 "Žužemberk": 5, "Kočevje": 5})

            p = pomembnost(5, 8, self.povezave5, True)
            self.assertEqual(potnik.call_count, 15)
            self.assertAlmostEqual(p["Metlika"], 5 / 45)
            self.assertAlmostEqual(p["Novo mesto"], 15 / 45)
            self.assertAlmostEqual(p["Brežice"], 10 / 45)
            self.assertEqual(
                set(p),
                {"Metlika", "Novo mesto", "Brežice", "Radeče",
                 "Žužemberk", "Kočevje"})
        finally:
            potnik = stari_potnik


class Test09(TestBase):
    def test_razsiri(self):
        self.assertEqual(
            razsiri({"Ljubljana"}, self.povezave5),
            {"Vrhnika", "Škofja Loka", "Domžale", "Litija", "Velike Lašče", "Kamnik"}
        )
        self.assertEqual(
            razsiri({"Ljubljana", "Domžale"}, self.povezave5),
            {"Vrhnika", "Škofja Loka", "Litija", "Velike Lašče", "Kamnik",
             "Kranj"}
        )
        self.assertEqual(
            razsiri({"Ljubljana", "Vrhnika"}, self.povezave5),
            {"Škofja Loka", "Domžale", "Litija", "Velike Lašče", "Kamnik",
             "Idrija", "Postojna", "Cerknica"}
        )
        self.assertEqual(
            razsiri({"Ljubljana", "Hodoš", "Ilirska Bistrica"}, self.povezave5),
            {"Vrhnika", "Škofja Loka", "Domžale", "Litija", "Velike Lašče", "Kamnik",
             "Ljutomer", "Gornja Radgona", "Radenci", "Murska Sobota", "Beltinci",
             "Škofije", "Sežana", "Postojna", "Cerknica", "Sodražica"}
        )

    def test_razdalja(self):
        self.assertEqual(razdalja("Metlika", "Kočevje", self.povezave5), 1)
        self.assertEqual(razdalja("Metlika", "Žužemberk", self.povezave5), 2)
        self.assertEqual(razdalja("Žužemberk", "Metlika", self.povezave5), 2)
        self.assertEqual(razdalja("Žužemberk", "Trbovlje", self.povezave5), 2)
        self.assertEqual(razdalja("Žužemberk", "Radeče", self.povezave5), 2)
        self.assertEqual(razdalja("Radeče", "Žužemberk", self.povezave5), 2)
        self.assertEqual(razdalja("Trbovlje", "Žužemberk", self.povezave5), 2)
        self.assertEqual(razdalja("Vinica", "Kobarid", self.povezave5), 8)
        self.assertEqual(razdalja("Savudrija", "Hodoš", self.povezave5), 13)


class Test10(TestBase):
    def test_razsiri2(self):
        self.assertEqual(
            razsiri2({"Ljubljana", "Hodoš", "Ilirska Bistrica"}, self.povezave5),
            {"Vrhnika": "Ljubljana",
              "Škofja Loka": "Ljubljana",
              "Domžale": "Ljubljana",
              "Litija": "Ljubljana",
              "Velike Lašče": "Ljubljana",
              "Kamnik": "Ljubljana",
              "Ljutomer": "Hodoš",
              "Gornja Radgona": "Hodoš",
              "Radenci": "Hodoš",
              "Murska Sobota": "Hodoš",
              "Beltinci": "Hodoš",
              "Škofije": "Ilirska Bistrica",
              "Sežana": "Ilirska Bistrica",
              "Postojna": "Ilirska Bistrica",
              "Cerknica": "Ilirska Bistrica",
              "Sodražica": "Ilirska Bistrica"}
        )

    def test_najkrajsa_pot(self):
        self.assertEqual(
            najkrajsa_pot("Trbovlje", "Žužemberk", self.povezave5),
            ["Trbovlje", "Litija", "Žužemberk"])

        pot = najkrajsa_pot("Vinica", "Kobarid", self.povezave5)
        self.assertEqual(len(pot), 9)
        self.assertEqual(pot[0], "Vinica")
        self.assertEqual(pot[8], "Kobarid")
        self.assertTrue(veljavna_pot(pot, self.povezave5))

        pot = najkrajsa_pot("Savudrija", "Hodoš", self.povezave5)
        self.assertEqual(len(pot), 14)
        self.assertEqual(pot[0], "Savudrija")
        self.assertEqual(pot[13], "Hodoš")

try:
    import risar
except:
    pass

def tx(x):
    return (125 + x) * 5

def ty(y):
    return (115 - y) * 5

def narisi_kraje(kraji):
    oznake = {}
    for ime, x, y in kraji:
        risar.krog(tx(x), ty(y), 2)
        b = oznake[ime] = risar.besedilo(tx(x), ty(y), ime, velikost=12)
        r = b.boundingRect()
        b.setPos(b.x() - r.width() / 2, b.y() - r.height())
    return oznake

def narisi_povezave(kraji, enosmerne=False):
    koord = koordict(kraji)
    pov = povezave(5, kraji)
    if not enosmerne:
        pov = dvosmerno(pov)
    for kraj, sosedi in pov.items():
        for sosed in sosedi:
            x1, y1 = koord[kraj]
            x2, y2 = koord[sosed]
            if enosmerne:
                x2 = .6 * x1 + .4 * x2
                y2 = .6 * y1 + .4 * y2
            risar.crta(tx(x1), ty(y1), tx(x2), ty(y2), barva=risar.barva(48, 48, 48), sirina=4)
            risar.crta(tx(x1), ty(y1), tx(x2), ty(y2), barva=risar.barva(96, 96, 96), sirina=1)

def naloga6_povezave(eno=True, nestoj=False):
    risar.obnavljaj = False
    narisi_povezave(TestBase.kraji, eno)
    krogi = narisi_kraje(TestBase.kraji)
    risar.obnavljaj = True
    if nestoj:
        return krogi
    risar.stoj()

def naloga6_dvosmerno():
    naloga6_povezave(False)

def naloga7_potnik():
    naloga6_povezave(False, True)
    pov = dvosmerno(povezave(5, TestBase.kraji))
    kraji = TestBase.kraji
    koord = koordict(kraji)
    pot = potnik(random.choice(kraji)[0], 1000, pov)
    krog = risar.krog(0, 0, 5, sirina=4, barva=risar.zelena)
    for kraj0, kraj1 in zip(pot, pot[1:]):
        x0, y0 = koord[kraj0]
        x1, y1 = koord[kraj1]
        for i in [0.1, 0.3, 0.6, 0.9, 1]:
            krog.setPos(tx(x0 * (1 - i) + x1 * i), ty(y0 * (1 - i) + y1 * i))
            risar.cakaj(0.005)

def naloga8_pomembnost():
    from collections import defaultdict

    oznake = naloga6_povezave(False, True)
    kraji = TestBase.kraji
    pov = dvosmerno(povezave(5, kraji))
    koord = koordict(kraji)
    barve = [risar.modra, risar.zelena, risar.rumena, risar.rdeca, risar.rjava]
    zacetki = [random.choice(kraji)[0] for _ in range(5)]
    poti = list(zip(*(potnik(zacetek, 1000, pov) for zacetek in zacetki)))
    krogi = [risar.krog(tx(koord[zacetek][0]), ty(koord[zacetek][1]),
                        5, sirina=4, barva=barva)
             for zacetek, barva in zip(zacetki, barve)]

    obiski = defaultdict(int)
    for kraji0, kraji1 in zip(poti, poti[1:]):
        for kraj in kraji0:
            obiski[kraj] += 1
            oznake[kraj].setPlainText(f"{kraj}: {obiski[kraj]}")
        xy0 = [koord[kraj] for kraj in kraji0]
        xy1 = [koord[kraj] for kraj in kraji1]
        for i in [0.1, 0.3, 0.6, 0.9, 1]:
            for (x0, y0), (x1, y1), krog in zip(xy0, xy1, krogi):
                krog.setPos(tx(x0 * (1 - i) + x1 * i), ty(y0 * (1 - i) + y1 * i))
            risar.cakaj(0.005)
    risar.stoj()

def naloga9_razsiri():
    oznake = naloga6_povezave(False, True)
    zacetek = {"Ljubljana", "Lenart", "Žužemberk"}
    razsirjen = razsiri(zacetek, Test09.povezave5)
    for kraj, oznaka in oznake.items():
        if kraj in zacetek:
            barva = risar.rumena
        elif kraj in razsirjen:
            barva = risar.bela
        else:
            barva = risar.barva(48, 48, 48)
        oznaka.setDefaultTextColor(barva)
    risar.stoj()

def naloga9_razdalja():
    from PyQt5.QtGui import QColor
    from collections import defaultdict

    na_razdalji = defaultdict(set)
    for kraj, _, _ in TestBase.kraji:
        na_razdalji[razdalja("Vrhnika", kraj, Test09.povezave5)].add(kraj)
    oznake = naloga6_povezave(False, True)
    for r, kraji in na_razdalji.items():
        barva = QColor.fromHsl(r * 36, 255, 128)
        for kraj in kraji:
            oznake[kraj].setDefaultTextColor(barva)
            oznake[kraj].setPlainText(f"{kraj}: {r}")
    risar.stoj()

def naloga10_pot():
    kraji = TestBase.kraji
    pov = dvosmerno(povezave(5, kraji))
    koord = koordict(kraji)
    pot = najkrajsa_pot("Škofije", "Lenart", pov)

    risar.obnavljaj = False
    narisi_povezave(kraji)
    for kraj1, kraj2 in zip(pot, pot[1:]):
        x1, y1 = koord[kraj1]
        x2, y2 = koord[kraj2]
        risar.crta(tx(x1), ty(y1), tx(x2), ty(y2), barva=risar.zelena, sirina=3)
    narisi_kraje(TestBase.kraji)
    risar.obnavljaj = True
    risar.obnovi()
    risar.stoj()


#naloga6_povezave()
#naloga6_dvosmerno()
#naloga7_potnik()
#naloga8_pomembnost()
#naloga9_razsiri()
#naloga9_razdalja()
#naloga10_pot()

if __name__ == "__main__":
    unittest.main()
