
import unittest
import warnings
import random

class Test(unittest.TestCase):
    @staticmethod
    def setUpClass():
        warnings.simplefilter("ignore", ResourceWarning)

    def test_01_valovi(self):
        self.assertEqual([1 / 2, 1 / 3, 1, 0], vrhovi([1, 6, 5, 0, 0, 0, 2, 8, 5, 3, 0, 5, 8, 0, 0, 0, 5, 1, 1, 0, 0]))
        self.assertEqual([1 / 2, 1 / 3, 1, 0], vrhovi([1, 6, 5, 0, 0, 0, 2, 8, 5, 3, 0, 5, 8, 0, 0, 0, 5, 1, 1, 0]))
        self.assertEqual([1 / 2, 1 / 3, 1, 0], vrhovi([1, 6, 5, 0, 0, 0, 2, 8, 5, 3, 0, 5, 8, 0, 0, 0, 5, 1, 1]))
        self.assertEqual([1 / 2, 1 / 3, 1, 0], vrhovi([0, 1, 6, 5, 0, 0, 0, 2, 8, 5, 3, 0, 5, 8, 0, 0, 0, 5, 1, 1]))
        self.assertEqual([1 / 2, 1 / 3, 1, 0], vrhovi([0, 0, 1, 6, 5, 0, 0, 0, 2, 8, 5, 3, 0, 5, 8, 0, 0, 0, 5, 1, 1]))
        self.assertEqual([1, 1], vrhovi([0, 0, 5, 6, 0, 5, 6]))
        self.assertEqual([0, 1], vrhovi([0, 0, 5, 0, 5, 6]))
        self.assertEqual([0], vrhovi([0, 0, 5, 0,]))
        self.assertEqual([0], vrhovi([5, 0,]))
        self.assertEqual([0], vrhovi([5]))
        self.assertEqual([0], vrhovi([5, 3, 4]))

    def test_02_najpodobonejsi(self):
        markerji =                         {"ATTA", "GGT", "TTG", "TCCCTC"}
        vzorec = "GCGCATTAGCGGTCCCTCAAAGGT"  #  1     1      0       1
        sev1 = "GCATTAGGTCCCTCTTG"           #  1     1      1       1   => 3
        sev2 = "CGCGGCGCGCGATTA"             #  1     0      0       0   => 2
        sev3 = "ATTAGGTTTG"                  #  1     1      1       0   => 2
        sev4 = "ATTAATTAATTAATTA"            #  1     0      0       0   => 2
        sev5 = "ATTAATTAATTAATTATTG"         #  1     0      1       0   => 1
        sev6 = "AAAAAAATTGAAAAAAA"           #  0     0      1       0   => 0
        sev7 = "ATTAATTAATTAATTAATTATTG"     #  1     0      0       0   => 1
        vsi = {sev1, sev2, sev3, sev4, sev5, sev6, sev7}
        self.assertEqual(sev1, najpodobnejsi(vzorec, vsi, markerji))
        self.assertIn(najpodobnejsi(vzorec, vsi - {sev1}, markerji), {sev2, sev3, sev4, sev7})
        self.assertEqual(sev2, najpodobnejsi(vzorec, {sev2, sev5, sev6, sev7}, markerji))
        self.assertEqual(sev3, najpodobnejsi(vzorec, {sev3, sev5, sev6, sev7}, markerji))
        self.assertEqual(sev4, najpodobnejsi(vzorec, {sev4, sev5, sev6, sev7}, markerji))
        self.assertEqual(sev5, najpodobnejsi(vzorec, {sev5, sev6}, markerji))
        self.assertEqual(sev7, najpodobnejsi(vzorec, {sev7, sev6}, markerji))
        self.assertEqual(sev6, najpodobnejsi(vzorec, {sev6}, markerji))

    def test_03_stanje_regij(self):
        rx = str(random.randint(1000, 2000))
        ox = str(random.randint(1000, 2000))
        open("obcine.txt", "wt").write(f"""Moravce, 5354, Osrednjeslovenska
Ljubljana, 288832, Osrednjeslovenska
Koper, 51828, Primorska
Kocevje ob gozdu, 16549, Juznoslovenska
Piran, 17613, Primorska
{ox}, 50000, {rx}
Kamnik, 13768, Osrednjeslovenska""")

        open("okuzbe.txt", "wt").write(f"""Kamnik: 80
Kocevje ob gozdu: 50
{ox}: 100
Ljubljana: 90""")
        okuzenost = stanje_regij()
        self.assertAlmostEqual((80 + 90) / (5354 + 288832 + 13768), okuzenost["Osrednjeslovenska"])
        self.assertAlmostEqual(50 / 16549, okuzenost["Juznoslovenska"])
        self.assertAlmostEqual(0, okuzenost["Primorska"])
        self.assertAlmostEqual(100 / 50000, okuzenost[rx])

    def test_04_argmax(self):
        self.assertEqual((3, 8), argmax([5, 4, 7, 8, 5, 1]))
        self.assertEqual((3, 8), argmax([5, 4, 7, 8, 5, 8, 1]))
        self.assertEqual((0, 8), argmax([8, 5, 1]))
        self.assertEqual((0, 8), argmax([8]))

    def test_05_sledilnik(self):
        for cls in (Sledilnik, Sledilnik2):
            s = cls()
            t = cls()

            self.assertEqual(0, s.naj_brez_okuzb)
            self.assertEqual(0, s.naj_dnevnih)
            self.assertEqual(0, s.tekoce_brez_okuzb)
            if cls is Sledilnik2:
                self.assertEqual(0, s.skupno_okuzenih)

            s.nov_dan(15)
            self.assertEqual(0, s.naj_brez_okuzb)
            self.assertEqual(15, s.naj_dnevnih)
            self.assertEqual(0, s.tekoce_brez_okuzb)
            if cls is Sledilnik2:
                self.assertEqual(15, s.skupno_okuzenih)

            self.assertEqual(0, t.naj_dnevnih)

            s.nov_dan(10)
            self.assertEqual(0, s.naj_brez_okuzb)
            self.assertEqual(15, s.naj_dnevnih)
            self.assertEqual(0, s.tekoce_brez_okuzb)
            if cls is Sledilnik2:
                self.assertEqual(25, s.skupno_okuzenih)

            s.nov_dan(20)
            self.assertEqual(0, s.naj_brez_okuzb)
            self.assertEqual(20, s.naj_dnevnih)
            self.assertEqual(0, s.tekoce_brez_okuzb)
            if cls is Sledilnik2:
                self.assertEqual(45, s.skupno_okuzenih)

            s.nov_dan(0)
            self.assertEqual(1, s.naj_brez_okuzb)
            self.assertEqual(20, s.naj_dnevnih)
            self.assertEqual(1, s.tekoce_brez_okuzb)
            if cls is Sledilnik2:
                self.assertEqual(45, s.skupno_okuzenih)

            s.nov_dan(0)
            self.assertEqual(2, s.naj_brez_okuzb)
            self.assertEqual(20, s.naj_dnevnih)
            self.assertEqual(2, s.tekoce_brez_okuzb)
            if cls is Sledilnik2:
                self.assertEqual(45, s.skupno_okuzenih)

            s.nov_dan(5)
            self.assertEqual(2, s.naj_brez_okuzb)
            self.assertEqual(20, s.naj_dnevnih)
            self.assertEqual(0, s.tekoce_brez_okuzb)
            if cls is Sledilnik2:
                self.assertEqual(50, s.skupno_okuzenih)

            s.nov_dan(0)
            self.assertEqual(2, s.naj_brez_okuzb)
            self.assertEqual(20, s.naj_dnevnih)
            self.assertEqual(1, s.tekoce_brez_okuzb)

            s.nov_dan(0)
            s.nov_dan(0)
            s.nov_dan(0)
            s.nov_dan(0)
            self.assertEqual(5, s.naj_brez_okuzb)
            self.assertEqual(20, s.naj_dnevnih)
            self.assertEqual(5, s.tekoce_brez_okuzb)

            s.nov_dan(3)
            self.assertEqual(5, s.naj_brez_okuzb)
            self.assertEqual(20, s.naj_dnevnih)
            self.assertEqual(0, s.tekoce_brez_okuzb)

            s.nov_dan(0)
            s.nov_dan(0)
            self.assertEqual(5, s.naj_brez_okuzb)
            self.assertEqual(20, s.naj_dnevnih)
            self.assertEqual(2, s.tekoce_brez_okuzb)


if __name__ == "__main__":
    unittest.main()
