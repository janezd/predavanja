import unittest
from math import sqrt

class TestDistribucija(unittest.TestCase):
    def test_05_razdalja(self):
        self.assertAlmostEqual(razdalja((0, 0), (3, 4)), 5)
        self.assertAlmostEqual(razdalja((0, 0), (-3, 4)), 5)
        self.assertAlmostEqual(razdalja((12, 11), (12, 10)), 1)
        self.assertAlmostEqual(razdalja((12, 11), (13, 11)), 1)
        self.assertAlmostEqual(razdalja((12, 11), (12, 11)), 0)
        self.assertAlmostEqual(razdalja((5, 8), (2, 12)), 5)
        self.assertAlmostEqual(razdalja((0, 0), (-1, -1)), sqrt(2))

        self.assertAlmostEqual(razdalja((0,), (1,)), 1)
        self.assertAlmostEqual(razdalja((3,), (-7,)), 10)
        self.assertAlmostEqual(razdalja((1, 1, 1, 1, 1, 1, 1),
                                        (2, 2, 0, 2, 0, 1, 1)), sqrt(5))

    def test_06_najblizji(self):
        pts = {(0, 0), (10, 0), (10, 10)}
        self.assertTupleEqual(najblizji((0, 0), pts), (0, 0))
        self.assertTupleEqual(najblizji((0, 1), pts), (0, 0))
        self.assertTupleEqual(najblizji((0, -1), pts), (0, 0))
        self.assertTupleEqual(najblizji((0, 7), pts), (0, 0))
        self.assertTupleEqual(najblizji((10, 7), pts), (10, 10))
        self.assertTupleEqual(najblizji((10, 2), pts), (10, 0))

        self.assertTupleEqual(najblizji((10, 10), {(0, 0)}), (0, 0))

        self.assertTupleEqual(najblizji((1, ) * 8,
                                        {(0, ) * 8, (10, ) * 8}),
                              (0, ) * 8)


    def test_07_pop_razdalja(self):
        self.assertAlmostEqual(pop_razdalja((1, 1),
                                            {(0, 0), (10, 0), (10, 10)}),
                               (sqrt(2) + sqrt(82) + sqrt(162)) / 3)
        self.assertAlmostEqual(pop_razdalja((1, 1), {(0, 0)}), sqrt(2))
        self.assertAlmostEqual(pop_razdalja((1,), {(0, )}), 1)

    def test_07_center(self):
        self.assertTupleEqual(
            center({(0, 0), (10, 0), (0, 10), (10, 10), (5, 5)}),
            (5, 5))
        self.assertTupleEqual(
            center({(0, 0), (10, 0), (0, 10), (10, 10), (4, 5)}),
            (4, 5))
        self.assertTupleEqual(
            center({(0, 0), (4, 5), (10, 0), (0, 10), (10, 10)}),
            (4, 5))
        self.assertTupleEqual(
            center({(0, 0), (10, 0), (10, 10)}),
            (10, 0))
        self.assertTupleEqual(
            center({(1, ), (2, ), (3, ), (4, ), (5, ), }),
            (3, ))

    def test_08_tezisce(self):
        t = tezisce({(0, 0), (10, 0), (10, 10)})
        self.assertIsInstance(t, tuple)
        self.assertAlmostEqual(t[0], 20 / 3)
        self.assertAlmostEqual(t[1], 10 / 3)

        self.assertEqual(tezisce({(1, 2, 3, 4, 5, 6, 7, 8),
                                  (3, 4, 5, 6, 7, 8, 9, 10)}),
                                  (2, 3, 4, 5, 6, 7, 8, 9))

        t = tezisce({(0, ), (1, ), (2, ), (3, ), })
        self.assertIsInstance(t, tuple)
        self.assertEqual(t[0], 1.5)

    def test_09_razdeli(self):
        self.assertDictEqual(razdeli({(5, 5), (5, 10), (15, 5), (40, 50)},
            {(5, 5), (4, 5), (5, 9), (6, 11), (-20, -20), (16, 5)}),
            {(5, 5): {(5, 5), (4, 5), (-20, -20)},
             (5, 10): {(5, 9), (6, 11)},
             (15, 5): {(16, 5)},
             (40, 50): set()})

    def test_09_poisci_centre(self):
        self.assertSetEqual(poisci_centre(
            [{(0, 0), (10, 0), (0, 10), (10, 10), (5, 5)},
             {(0, 0), (4, 5), (10, 0), (0, 10), (10, 10)},
             {(0, 0), (10, 0), (10, 10)},
             {(42, 42)}]),
            {(5, 5), (4, 5), (10, 0), (42, 42)})

    def test_10_nacrtuj(self):
        otroci = [
            (0, 0), (1, 0), (0, 1),
            (0, 5), (0, 6), (0, 7),
            (5, 0), (5, 1), (5, 2)]
        self.assertDictEqual(nacrtuj(otroci, 3),
                             {(0, 0): {(0, 0), (1, 0), (0, 1)},
                              (0, 6): {(0, 5), (0, 6), (0, 7)},
                              (5, 1): {(5, 0), (5, 1), (5, 2)}})
        self.assertDictEqual(nacrtuj(otroci, len(otroci)),
                             {x: {x} for x in otroci})
