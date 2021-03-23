import unittest
from random import shuffle, randint


class Test_Ocena6(unittest.TestCase):
    def test_prazna(self):
        cebela = Cebela()
        self.assertEqual(cebela.pot(), [])
        self.assertEqual(cebela.metraza(), 0)

    def test_zbutaj(self):
        cebela = Cebela()
        cebela.premik("R", 10)
        cebela = Cebela()
        self.assertEqual(cebela.pot(), [])
        self.assertEqual(cebela.metraza(), 0)

    def test_premik(self):
        cebela = Cebela()
        cebela.premik("R", 10)
        self.assertEqual(cebela.pot(), [((0, 0), (10, 0))])
        self.assertEqual(cebela.metraza(), 10)

        cebela.premik("D", 20)
        self.assertEqual(cebela.pot(),
                         [((0, 0), (10, 0)), ((10, 0), (10, 20))])
        self.assertEqual(cebela.metraza(), 30)

        cebela.premik("L", 5)
        self.assertEqual(cebela.pot(), [((0, 0), (10, 0)), ((10, 0), (10, 20)),
                                        ((10, 20), (5, 20))])
        self.assertEqual(cebela.metraza(), 35)

        cebela.premik("U", 15)
        self.assertEqual(cebela.pot(), [((0, 0), (10, 0)), ((10, 0), (10, 20)),
                                 ((10, 20), (5, 20)), ((5, 20), (5, 5))])
        self.assertEqual(cebela.metraza(), 50)

    def test_premik_but_premik(self):
        cebela = Cebela()
        cebela.premik("R", 10)
        self.assertEqual(cebela.pot(), [((0, 0), (10, 0))])
        self.assertEqual(cebela.metraza(), 10)

        cebela = Cebela()
        self.assertEqual(cebela.pot(), [])
        self.assertEqual(cebela.metraza(), 0)

        cebela = Cebela()
        cebela.premik("R", 10)
        self.assertEqual(cebela.pot(), [((0, 0), (10, 0))])
        self.assertEqual(cebela.metraza(), 10)

    def test_prezarci(self):
        cebela = Cebela()
        cebela.prezarci(50, 50)
        self.assertEqual(cebela.pot(), [])
        self.assertEqual(cebela.metraza(), 0)

        cebela.premik("D", 10)
        self.assertEqual(cebela.pot(), [((50, 50), (50, 60))])
        self.assertEqual(cebela.metraza(), 10)

        cebela.prezarci(100, 100)
        self.assertEqual(cebela.pot(), [((50, 50), (50, 60))])
        self.assertEqual(cebela.metraza(), 10)

        cebela.premik("R", 42)
        self.assertEqual(cebela.pot(), [((50, 50), (50, 60)),
                                        ((100, 100), (142, 100))])
        self.assertEqual(cebela.metraza(), 52)

    def test_vec_cebel(self):
        cebele = [Cebela() for _ in range(100)]
        for i, cebela in enumerate(cebele):
            cebela.premik("D", i)
        for i, cebela in enumerate(cebele):
            self.assertEqual(cebela.metraza(), i)


class Test_Ocena7(unittest.TestCase):
    def test_leti_do_ld(self):
        cebela = Cebela()
        cebela.premik("R", 100)
        cebela.premik("D", 100)
        cebela.leti_do(60, 130)
        self.assertEqual(cebela.pot(), [((0, 0), (100, 0)),
                                        ((100, 0), (100, 100)),
                                        ((100, 100), (60, 100)),
                                        ((60, 100), (60, 130))])
        self.assertAlmostEqual(cebela.metraza(), 270)

    def test_leti_do_l(self):
        cebela = Cebela()
        cebela.premik("R", 100)
        cebela.premik("D", 100)
        cebela.leti_do(60, 100)
        self.assertEqual(cebela.pot(), [((0, 0), (100, 0)),
                                        ((100, 0), (100, 100)),
                                        ((100, 100), (60, 100))])
        self.assertAlmostEqual(cebela.metraza(), 240)

    def test_leti_do_ru(self):
        cebela = Cebela()
        cebela.premik("R", 100)
        cebela.premik("D", 100)
        cebela.leti_do(130, 60)
        self.assertEqual(cebela.pot(), [((0, 0), (100, 0)),
                                        ((100, 0), (100, 100)),
                                        ((100, 100), (130, 100)),
                                        ((130, 100), (130, 60))])
        self.assertAlmostEqual(cebela.metraza(), 270)

    def test_leti_do_d(self):
        cebela = Cebela()
        cebela.premik("R", 100)
        cebela.premik("D", 100)
        cebela.leti_do(100, 160)
        self.assertEqual(cebela.pot(), [((0, 0), (100, 0)),
                                        ((100, 0), (100, 100)),
                                        ((100, 100), (100, 160))])
        self.assertAlmostEqual(cebela.metraza(), 260)

    def test_let_premik(self):
        cebela = Cebela()
        cebela.leti_do(30, 40)
        self.assertEqual(cebela.pot(), [((0, 0), (30, 0)),
                                        ((30, 0), (30, 40))])
        self.assertAlmostEqual(cebela.metraza(), 70)

        cebela.premik("U", 10)
        self.assertEqual(cebela.pot(), [((0, 0), (30, 0)), ((30, 0), (30, 40)),
                                        ((30, 40), (30, 30))])
        self.assertAlmostEqual(cebela.metraza(), 80)


    def test_sekaj_do_ld(self):
        cebela = Cebela()
        cebela.premik("R", 100)
        cebela.premik("D", 100)
        cebela.sekaj_do(60, 130)
        self.assertEqual(cebela.pot(), [((0, 0), (100, 0)),
                                        ((100, 0), (100, 100)),
                                        ((100, 100), (60, 130))])
        self.assertAlmostEqual(cebela.metraza(), 250)

    def test_sekaj_do_l(self):
        cebela = Cebela()
        cebela.premik("R", 100)
        cebela.premik("D", 100)
        cebela.sekaj_do(60, 100)
        self.assertEqual(cebela.pot(), [((0, 0), (100, 0)),
                                        ((100, 0), (100, 100)),
                                        ((100, 100), (60, 100))])
        self.assertAlmostEqual(cebela.metraza(), 240)

    def test_sekaj_do_ru(self):
        cebela = Cebela()
        cebela.premik("R", 100)
        cebela.premik("D", 100)
        cebela.sekaj_do(130, 60)
        self.assertEqual(cebela.pot(), [((0, 0), (100, 0)),
                                        ((100, 0), (100, 100)),
                                        ((100, 100), (130, 60))])
        self.assertAlmostEqual(cebela.metraza(), 250)

    def test_sekaj_do_d(self):
        cebela = Cebela()
        cebela.premik("R", 100)
        cebela.premik("D", 100)
        cebela.sekaj_do(100, 160)
        self.assertEqual(cebela.pot(), [((0, 0), (100, 0)),
                                        ((100, 0), (100, 100)),
                                        ((100, 100), (100, 160))])
        self.assertAlmostEqual(cebela.metraza(), 260)

    def test_sekaj_premik(self):
        cebela = Cebela()
        cebela.sekaj_do(30, 40)
        self.assertEqual(cebela.pot(), [((0, 0), (30, 40))])
        self.assertAlmostEqual(cebela.metraza(), 50)

        cebela.premik("U", 10)
        self.assertEqual(cebela.pot(), [((0, 0), (30, 40)),
                                        ((30, 40), (30, 30))])
        self.assertAlmostEqual(cebela.metraza(), 60)


class Test_Ocena8(unittest.TestCase):
    def test_ccw(self):
        A = 3, 2
        B = 8, 3
        C = 4, 7
        # Ne vznemirjaj se zaradi spodnje zvezdice - tako pišem, ker je
        # pregledneje v bistvu pa pomeni, da kličemo (3, 2, 8, 3, 4, 7)
        self.assertTrue(ccw(* A + B + C))
        self.assertTrue(ccw(* B + C + A))
        self.assertTrue(ccw(* C + A + B))
        self.assertFalse(ccw(* A + C + B))
        self.assertFalse(ccw(* C + B + A))
        self.assertFalse(ccw(* B + A + C))

        A = 0, 0
        B = 1, -1
        C = 0, 1
        self.assertTrue(ccw(* A + B + C))
        self.assertTrue(ccw(* B + C + A))
        self.assertTrue(ccw(* C + A + B))
        self.assertFalse(ccw(* A + C + B))
        self.assertFalse(ccw(* C + B + A))
        self.assertFalse(ccw(* B + A + C))

    def test_se_sekata_lepi(self):
        A = 4, 2
        B = 9, 6
        C = 3, 5
        D = 10, 3
        self.assertTrue(se_sekata(* A + B + C + D))
        self.assertTrue(se_sekata(* B + A + C + D))
        self.assertTrue(se_sekata(* A + B + D + C))
        self.assertTrue(se_sekata(* B + A + D + C))
        self.assertTrue(se_sekata(* C + D + A + B))
        self.assertTrue(se_sekata(* C + D + B + A))
        self.assertTrue(se_sekata(* D + C + A + B))
        self.assertTrue(se_sekata(* B + A + D + C))

        self.assertFalse(se_sekata(* A + C + B + D))
        self.assertFalse(se_sekata(* C + A + B + D))
        self.assertFalse(se_sekata(* A + C + D + B))
        self.assertFalse(se_sekata(* C + A + D + B))
        self.assertFalse(se_sekata(* B + D + A + C))
        self.assertFalse(se_sekata(* D + B + A + C))
        self.assertFalse(se_sekata(* B + D + C + A))
        self.assertFalse(se_sekata(* D + B + C + A))

        self.assertFalse(se_sekata(* A + D + B + C))
        self.assertFalse(se_sekata(* D + A + B + C))
        self.assertFalse(se_sekata(* A + D + C + B))
        self.assertFalse(se_sekata(* D + A + C + B))
        self.assertFalse(se_sekata(* C + B + D + A))
        self.assertFalse(se_sekata(* B + C + D + A))
        self.assertFalse(se_sekata(* C + B + A + D))
        self.assertFalse(se_sekata(* C + B + D + A))

    def test_se_sekata_ena_vodoravna(self):
        A = 4, 2
        B = 9, 6
        C = 3, 3
        D = 10, 3
        self.assertTrue(se_sekata(* A + B + C + D))
        self.assertTrue(se_sekata(* B + A + C + D))
        self.assertTrue(se_sekata(* A + B + D + C))
        self.assertTrue(se_sekata(* B + A + D + C))
        self.assertTrue(se_sekata(* C + D + A + B))
        self.assertTrue(se_sekata(* C + D + B + A))
        self.assertTrue(se_sekata(* D + C + A + B))
        self.assertTrue(se_sekata(* B + A + D + C))

        self.assertFalse(se_sekata(* A + C + B + D))
        self.assertFalse(se_sekata(* C + A + B + D))
        self.assertFalse(se_sekata(* A + C + D + B))
        self.assertFalse(se_sekata(* C + A + D + B))
        self.assertFalse(se_sekata(* B + D + A + C))
        self.assertFalse(se_sekata(* D + B + A + C))
        self.assertFalse(se_sekata(* B + D + C + A))
        self.assertFalse(se_sekata(* D + B + C + A))

        self.assertFalse(se_sekata(* A + D + B + C))
        self.assertFalse(se_sekata(* D + A + B + C))
        self.assertFalse(se_sekata(* A + D + C + B))
        self.assertFalse(se_sekata(* D + A + C + B))
        self.assertFalse(se_sekata(* C + B + D + A))
        self.assertFalse(se_sekata(* B + C + D + A))
        self.assertFalse(se_sekata(* C + B + A + D))
        self.assertFalse(se_sekata(* C + B + D + A))

    def test_se_sekata_ena_navpicna(self):
        A = 4, 2
        B = 4, 6
        C = 3, 5
        D = 10, 3
        self.assertTrue(se_sekata(* A + B + C + D))
        self.assertTrue(se_sekata(* B + A + C + D))
        self.assertTrue(se_sekata(* A + B + D + C))
        self.assertTrue(se_sekata(* B + A + D + C))
        self.assertTrue(se_sekata(* C + D + A + B))
        self.assertTrue(se_sekata(* C + D + B + A))
        self.assertTrue(se_sekata(* D + C + A + B))
        self.assertTrue(se_sekata(* B + A + D + C))

        self.assertFalse(se_sekata(* A + C + B + D))
        self.assertFalse(se_sekata(* C + A + B + D))
        self.assertFalse(se_sekata(* A + C + D + B))
        self.assertFalse(se_sekata(* C + A + D + B))
        self.assertFalse(se_sekata(* B + D + A + C))
        self.assertFalse(se_sekata(* D + B + A + C))
        self.assertFalse(se_sekata(* B + D + C + A))
        self.assertFalse(se_sekata(* D + B + C + A))

        self.assertFalse(se_sekata(* A + D + B + C))
        self.assertFalse(se_sekata(* D + A + B + C))
        self.assertFalse(se_sekata(* A + D + C + B))
        self.assertFalse(se_sekata(* D + A + C + B))
        self.assertFalse(se_sekata(* C + B + D + A))
        self.assertFalse(se_sekata(* B + C + D + A))
        self.assertFalse(se_sekata(* C + B + A + D))
        self.assertFalse(se_sekata(* C + B + D + A))

    def test_se_sekata_vodoravna_navpicna(self):
        A = 4, 2
        B = 4, 6
        C = 3, 3
        D = 10, 3
        self.assertTrue(se_sekata(* A + B + C + D))
        self.assertTrue(se_sekata(* B + A + C + D))
        self.assertTrue(se_sekata(* A + B + D + C))
        self.assertTrue(se_sekata(* B + A + D + C))
        self.assertTrue(se_sekata(* C + D + A + B))
        self.assertTrue(se_sekata(* C + D + B + A))
        self.assertTrue(se_sekata(* D + C + A + B))
        self.assertTrue(se_sekata(* B + A + D + C))

        self.assertFalse(se_sekata(* A + C + B + D))
        self.assertFalse(se_sekata(* C + A + B + D))
        self.assertFalse(se_sekata(* A + C + D + B))
        self.assertFalse(se_sekata(* C + A + D + B))
        self.assertFalse(se_sekata(* B + D + A + C))
        self.assertFalse(se_sekata(* D + B + A + C))
        self.assertFalse(se_sekata(* B + D + C + A))
        self.assertFalse(se_sekata(* D + B + C + A))

        self.assertFalse(se_sekata(* A + D + B + C))
        self.assertFalse(se_sekata(* D + A + B + C))
        self.assertFalse(se_sekata(* A + D + C + B))
        self.assertFalse(se_sekata(* D + A + C + B))
        self.assertFalse(se_sekata(* C + B + D + A))
        self.assertFalse(se_sekata(* B + C + D + A))
        self.assertFalse(se_sekata(* C + B + A + D))
        self.assertFalse(se_sekata(* C + B + D + A))


class Test_Ocena9(unittest.TestCase):
    def test_previdni_premik(self):
        cebela = Cebela()

        cebela.premik("D", 100)
        cebela.previdni_premik("R", 100)
        cebela.premik("D", 50)
        cebela.previdni_premik("L", 50)
        self.assertAlmostEqual(cebela.metraza(), 300)

        cebela.previdni_premik("U", 100)
        self.assertAlmostEqual(cebela.metraza(), 300)

        cebela.previdni_premik("U", 100)
        self.assertAlmostEqual(cebela.metraza(), 300)

        cebela.previdni_premik("U", 40)
        self.assertAlmostEqual(cebela.metraza(), 340)

        cebela.previdni_premik("R", 100)
        self.assertAlmostEqual(cebela.metraza(), 340)

        cebela.previdni_premik("R", 40)
        self.assertAlmostEqual(cebela.metraza(), 380)

        cebela.prezarci(125, 125)
        cebela.previdni_premik("L", 40)
        self.assertAlmostEqual(cebela.metraza(), 380)

        cebela.previdni_premik("L", 20)
        self.assertAlmostEqual(cebela.metraza(), 400)

    def test_previdni_premik_diag(self):
        cebela = Cebela()
        cebela.premik("D", 100)
        cebela.sekaj_do(100, 200)
        cebela.previdni_premik("L", 50)
        self.assertAlmostEqual(cebela.metraza(), 150 + sqrt(20000))

        cebela.previdni_premik("U", 100)
        self.assertAlmostEqual(cebela.metraza(), 150 + sqrt(20000))

        cebela.previdni_premik("U", 10)
        self.assertAlmostEqual(cebela.metraza(), 160 + sqrt(20000))

        cebela.previdni_premik("R", 100)
        self.assertAlmostEqual(cebela.metraza(), 160 + sqrt(20000))

        cebela.previdni_premik("R", 10)
        self.assertAlmostEqual(cebela.metraza(), 170 + sqrt(20000))

    def test_previdno_sekaj(self):
        cebela = Cebela()
        cebela.premik("D", 100)
        cebela.sekaj_do(100, 200)
        cebela.previdni_premik("L", 50)
        self.assertAlmostEqual(cebela.metraza(), 150 + sqrt(20000))

        cebela.previdno_sekaj(150, 50)
        self.assertAlmostEqual(cebela.metraza(), 150 + sqrt(20000))

        cebela.previdno_sekaj(250, 50)
        self.assertAlmostEqual(cebela.metraza(), 150 + sqrt(20000))

        cebela.premik("U", 100)
        self.assertAlmostEqual(cebela.metraza(), 250 + sqrt(20000))

        cebela.previdno_sekaj(0, 200)
        self.assertAlmostEqual(cebela.metraza(), 250 + sqrt(20000))

        cebela.previdno_sekaj(47, 104)
        self.assertAlmostEqual(cebela.metraza(), 255 + sqrt(20000))


class Test_Ocena10(unittest.TestCase):
    def test_oberi(self):
        vrtovi = [
            [(4, 0), (8, 0), (7, 1), (6, 2), (3, 3), (5, 3), (7, 3), (1, 4),
             (4, 4), (8, 4), (0, 6), (2, 6), (1, 8), (4, 8), (8, 8)],
            [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7),
             (8, 8), (0, 8), (1, 7), (2, 6), (3, 5), (5, 3), (6, 2), (7, 1),
             (8, 0)],
            [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7),
             (8, 8), (0, 8), (1, 7), (2, 6), (3, 5), (5, 3), (6, 2), (7, 1),
             (8, 0), (4, 0), (4, 8), (0, 4), (8, 4)],
            [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7),
             (4, 8), (0, 4), (1, 4), (2, 4), (3, 4), (5, 4), (6, 4), (7, 4),
             (8, 4)],
            [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7),
             (4, 8), (0, 4), (1, 4), (2, 4), (3, 4), (5, 4), (6, 4), (7, 4),
             (8, 4), (0, 0), (0, 8), (8, 0), (8, 8)],
            [(0, 0), (2, 0), (4, 0), (1, 1), (3, 1), (0, 2), (2, 2), (4, 2),
             (1, 3), (3, 3), (0, 4), (2, 4), (4, 4)],
            [(x, y) for x in range(7) for y in range(7)]
        ] + \
        [list(set((randint(0, 8), randint(0, 8)) for _ in range(40)))
            for _ in range(8)]

        # Tole je potrebno zaradi risanja. Ce zelis debugirati in gledati
        # gornje koordinate, zakomentiraj tidve vrstici -- na teste to ne
        # vpliva
        vrtovi = [[(30 + x * 30, 30 + y * 30) for x, y in cvetovi]
                  for cvetovi in vrtovi]

        for cvetovi in vrtovi:
            backup = cvetovi[:]
            for i in range(1):
                print("Razpored:", cvetovi)
                risar.widget.scene.clear()
                cebela = Cebela()
                cebela.oberi(cvetovi)
                segmenti = cebela.pot()
                self.assertEqual(backup, cvetovi,
                                 "Funkcija je spremenila podani argument")
                self.assertEqual(len(cvetovi) - 1, len(segmenti),
                                 "Pot nima prave dolzine")
                self.assertEqual(
                    set(cvetovi),
                    {segmenti[0][0]} | set(seg[1] for seg in segmenti),
                    "Cebela ni obrala vseh cvetov")
                for seg1, seg2 in zip(segmenti, segmenti[1:]):
                    # Segmenti se morajo stikati
                    self.assertEqual(seg1[1], seg2[0],
                                     "Segmenti se ne stikajo: {} in {}"
                                     .format(seg1, seg2))
                    # Vedno zavija desno
                    self.assertTrue(ccw(*seg1[0] + seg1[1] + seg2[1]) ,
                                     "Levi zavoj: {} in {}".format(seg1, seg2))
                shuffle(cvetovi)
