import unittest
class TestKraji(unittest.TestCase):
    class CountCalls:
        def __init__(self, f):
            self.f = f
            self.call_count = 0

        def __call__(self, *args, **kwargs):
            self.call_count += 1
            return self.f(*args, **kwargs)

    @classmethod
    def setUpClass(cls):
        global koordinate, razdalja
        try:
            koordinate = cls.CountCalls(koordinate)
        except:
            pass
        try:
            razdalja = cls.CountCalls(razdalja)
        except:
            pass

    def test_1_razdalja(self):
        self.assertEqual(razdalja(0, 0, 1, 0), 1)
        self.assertEqual(razdalja(0, 0, 0, 1), 1)
        self.assertEqual(razdalja(0, 0, -1, 0), 1)
        self.assertEqual(razdalja(0, 0, 0, -1), 1)
        self.assertEqual(razdalja(1, 0, 0, 0), 1)
        self.assertEqual(razdalja(0, 1, 0, 0), 1)
        self.assertEqual(razdalja(-1, 0, 0, 0), 1)
        self.assertEqual(razdalja(0, -1, 0, 0), 1)

        self.assertEqual(razdalja(1, 2, 4, 6), 5)
        self.assertEqual(razdalja(1, 2, -2, 6), 5)
        self.assertEqual(razdalja(1, 2, 4, -2), 5)
        self.assertEqual(razdalja(1, 2, -2, -2), 5)

        from math import sqrt
        self.assertAlmostEqual(razdalja(1, 2, 0, 1), sqrt(2))

    def test_2_koordinate(self):
        kraji = [
            ('Brežice', 68.66, 7.04),
            ('Lenart', 85.20, 78.75),
            ('Rateče', -65.04, 70.04),
            ('Ljutomer', 111.26, 71.82)
        ]

        self.assertEqual(koordinate("Brežice", kraji), (68.66, 7.04))
        self.assertEqual(koordinate("Lenart", kraji), (85.20, 78.75))
        self.assertEqual(koordinate("Rateče", kraji), (-65.04, 70.04))
        self.assertEqual(koordinate("Ljutomer", kraji), (111.26, 71.82))
        self.assertIsNone(koordinate("Ljubljana", kraji))

        kraji = [('Brežice', 68.66, 7.04)]
        self.assertEqual(koordinate("Brežice", kraji), (68.66, 7.04))
        self.assertIsNone(koordinate("Lenart", kraji))

        kraji = []
        self.assertIsNone(koordinate("Brežice", kraji))

    def test_2_range_len(self):
        class NoGetItem(list):
            def __getitem__(*x):
                raise IndexError("Nauči se (pravilno) uporabljati zanko for!")

        kraji = NoGetItem([('Brežice', 68.66, 7.04), ('Lenart', 85.20, 78.75),
                           ('Rateče', -65.04, 70.04)])
        self.assertEqual(koordinate("Brežice", kraji), (68.66, 7.04))
        self.assertEqual(koordinate("Lenart", kraji), (85.20, 78.75))
        self.assertEqual(koordinate("Rateče", kraji), (-65.04, 70.04))
        self.assertIsNone(koordinate("Ljubljana", kraji))

    def test_3_razdalja_krajev(self):
        kraji = [
            ('Brežice', 10, 20),
            ('Lenart', 13, 24),
            ('Rateče', 17, 20),
            ('Ljutomer', 8, 36)
        ]

        from math import sqrt
        self.assertEqual(oddaljenost("Brežice", "Lenart", kraji), 5)
        self.assertEqual(oddaljenost("Lenart", "Brežice", kraji), 5)
        self.assertEqual(oddaljenost("Brežice", "Rateče", kraji), 7)
        self.assertAlmostEqual(oddaljenost("Lenart", "Rateče", kraji), sqrt(32))
        self.assertEqual(oddaljenost("Lenart", "Ljutomer", kraji), 13)

        koordinate.call_count = razdalja.call_count = 0
        oddaljenost("Brežice", "Lenart", kraji)
        self.assertEqual(
            koordinate.call_count, 2,
            "Funkcija `razdalja_krajev` mora dvakrat poklicati `koordinate`")
        self.assertEqual(
            razdalja.call_count, 1,
            "Funkcija `razdalja_krajev` mora enkrat poklicati `razdalja`")

    def test_4_najblizji(self):
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
            ('Kanal', -71.00, 26.25)]
        self.assertEqual(najblizji("Brežice", kraji), "Rogaška Slatina")
        self.assertEqual(najblizji("Kanal", kraji), "Lokve")
        self.assertEqual(najblizji("Ljutomer", kraji), "Lenart")

        razdalja.call_count = 0
        najblizji("Ljutomer", kraji)
        self.assertGreaterEqual(
            razdalja.call_count, len(kraji) - 1,
            "Funkcija `najblizji` mora vsaj {}-krat poklicati funkcijo "
            "`razdalja`".format(len(kraji) - 1))

        kraji = [
            ('Brežice', 68.66, 7.04),
            ('Lenart', 85.20, 78.75)]
        self.assertEqual(najblizji("Brežice", kraji), "Lenart")


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

    def test_5_veriga(self):
        self.assertEqual(
            veriga("Brežice", self.kraji),
            ['Brežice', 'Krško', 'Brestanica', 'Radeče', 'Laško', 'Celje',
             'Žalec', 'Velenje', 'Šoštanj', 'Slovenj Gradec', 'Dravograd',
             'Muta', 'Radlje ob Dravi', 'Mislinja', 'Vitanje', 'Šentjur',
             'Rogaška Slatina', 'Pragersko', 'Slovenska Bistrica', 'Maribor',
             'Pesnica', 'Lenart', 'Gornja Radgona', 'Radenci', 'Murska Sobota',
             'Beltinci', 'Ljutomer', 'Ormož', 'Ptuj', 'Hodoš', 'Črna',
             'Gornji Grad', 'Kamnik', 'Domžale', 'Ljubljana', 'Vrhnika',
             'Cerknica', 'Postojna', 'Vipava', 'Ajdovščina', 'Dutovlje',
             'Sežana', 'Škofije', 'Koper', 'Izola', 'Portorož', 'Piran',
             'Savudrija', 'Brtonigla', 'Motovun', 'Ilirska Bistrica',
             'Sodražica', 'Velike Lašče', 'Ribnica', 'Kočevje', 'Žužemberk',
             'Novo mesto', 'Metlika', 'Črnomelj', 'Vinica', 'Litija',
             'Trbovlje', 'Kranj', 'Škofja Loka', 'Radovljica', 'Bled',
             'Jesenice', 'Mojstrana', 'Kranjska Gora', 'Podkoren', 'Rateče',
             'Na Logu', 'Soča', 'Bovec', 'Žaga', 'Kobarid', 'Tolmin',
             'Most na Soči', 'Kanal', 'Anhovo', 'Plave', 'Nova Gorica',
             'Miren', 'Komen', 'Lokve', 'Čepovan', 'Idrija',
             'Bohinjska Bistrica', 'Stara Fužina', 'Log pod Mangartom',
             'Tržič'])

    def test_6_vojska(self):
        resitev = {
            ('Brežice', 'Krško'), ('Krško', 'Brestanica'),
            ('Brestanica', 'Radeče'), ('Radeče', 'Laško'), ('Laško', 'Celje'),
            ('Celje', 'Žalec'), ('Celje', 'Šentjur'), ('Žalec', 'Velenje'),
            ('Velenje', 'Šoštanj'), ('Žalec', 'Trbovlje'),
            ('Šoštanj', 'Slovenj Gradec'), ('Slovenj Gradec', 'Dravograd'),
            ('Dravograd', 'Muta'), ('Muta', 'Radlje ob Dravi'),
            ('Slovenj Gradec', 'Mislinja'), ('Mislinja', 'Vitanje'),
            ('Šentjur', 'Rogaška Slatina'), ('Rogaška Slatina', 'Pragersko'),
            ('Pragersko', 'Slovenska Bistrica'), ('Pragersko', 'Ptuj'),
            ('Šoštanj', 'Črna'), ('Pragersko', 'Maribor'), ('Maribor', 'Pesnica'),
            ('Pesnica', 'Lenart'), ('Lenart', 'Gornja Radgona'),
            ('Gornja Radgona', 'Radenci'), ('Radenci', 'Murska Sobota'),
            ('Murska Sobota', 'Beltinci'), ('Beltinci', 'Ljutomer'),
            ('Ljutomer', 'Ormož'), ('Črna', 'Gornji Grad'),
            ('Gornji Grad', 'Kamnik'), ('Kamnik', 'Domžale'),
            ('Domžale', 'Ljubljana'), ('Ljubljana', 'Vrhnika'),
            ('Vrhnika', 'Cerknica'), ('Cerknica', 'Postojna'),
            ('Domžale', 'Litija'), ('Postojna', 'Vipava'),
            ('Vipava', 'Ajdovščina'), ('Ajdovščina', 'Dutovlje'),
            ('Dutovlje', 'Sežana'), ('Dutovlje', 'Komen'), ('Komen', 'Miren'),
            ('Miren', 'Nova Gorica'), ('Nova Gorica', 'Plave'),
            ('Plave', 'Anhovo'), ('Anhovo', 'Kanal'), ('Kanal', 'Most na Soči'),
            ('Most na Soči', 'Tolmin'), ('Most na Soči', 'Čepovan'),
            ('Čepovan', 'Lokve'), ('Tolmin', 'Kobarid'), ('Kobarid', 'Žaga'),
            ('Žaga', 'Bovec'), ('Bovec', 'Soča'), ('Bovec', 'Log pod Mangartom'),
            ('Soča', 'Na Logu'), ('Na Logu', 'Kranjska Gora'),
            ('Kranjska Gora', 'Podkoren'), ('Podkoren', 'Rateče'),
            ('Kranjska Gora', 'Mojstrana'), ('Mojstrana', 'Jesenice'),
            ('Jesenice', 'Bled'), ('Bled', 'Radovljica'), ('Radovljica', 'Tržič'),
            ('Tržič', 'Kranj'), ('Kranj', 'Škofja Loka'),
            ('Bled', 'Bohinjska Bistrica'), ('Bohinjska Bistrica', 'Stara Fužina'),
            ('Lokve', 'Idrija'), ('Sežana', 'Škofije'), ('Škofije', 'Koper'),
            ('Koper', 'Izola'), ('Izola', 'Portorož'), ('Portorož', 'Piran'),
            ('Piran', 'Savudrija'), ('Portorož', 'Brtonigla'),
            ('Brtonigla', 'Motovun'), ('Cerknica', 'Sodražica'),
            ('Sodražica', 'Velike Lašče'), ('Sodražica', 'Ribnica'),
            ('Ribnica', 'Kočevje'), ('Ribnica', 'Žužemberk'),
            ('Žužemberk', 'Novo mesto'), ('Novo mesto', 'Metlika'),
            ('Metlika', 'Črnomelj'), ('Črnomelj', 'Vinica'),
            ('Murska Sobota', 'Hodoš'), ('Postojna', 'Ilirska Bistrica')}

        self.assertSetEqual(
            set(vojska(self.kraji)), resitev,
            "Če ta test ne uspe, to še ne pomeni nujno, da je rešitev napačna")

if __name__ == "__main__":
    unittest.main()
