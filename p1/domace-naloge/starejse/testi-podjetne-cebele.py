from random import randint
import copy
import unittest
class TestCebela(unittest.TestCase):
    vrt = [
        [1,3,3,8,5,4,2,1,5,6],
        [2,4,3,3,6,8,1,3,5,6],
        [4,5,6,4,7,4,3,6,4,7],
        [2,8,7,0,0,7,4,7,8,0],
        [2,3,4,7,0,8,7,6,3,8],
        [3,7,9,0,8,5,3,2,3,4],
        [1,5,7,7,6,4,2,3,5,6],
        [0,6,3,3,6,8,0,6,7,7],
        [0,1,3,2,8,0,0,0,0,0],
        [3,1,0,3,6,7,0,5,3,1],
        [1,3,5,7,0,8,6,5,3,1],
        [3,6,3,1,3,5,8,7,5,1],
        [4,3,6,0,0,8,4,7,5,3],
        [3,5,6,8,6,3,1,3,5,2]]

    vrt0 = [[42]]
    vrt_x = [[1, 2, 3, 5, 4]]
    vrt_y = [[1], [2], [3], [5], [4]]


    def test_05_naj_koordinate(self):
        self.assertTupleEqual(naj_koordinate(self.vrt), (2, 5))
        vrt = copy.deepcopy(self.vrt)
        vrt[3][0] = 9
        self.assertTupleEqual(naj_koordinate(vrt), (0, 3))
        vrt[0][3] = 9
        self.assertTupleEqual(naj_koordinate(vrt), (3, 0))
        vrt[0][0] = 9
        self.assertTupleEqual(naj_koordinate(vrt), (0, 0))

        self.assertTupleEqual(naj_koordinate(self.vrt0), (0, 0))
        self.assertTupleEqual(naj_koordinate(self.vrt_x), (3, 0))
        self.assertTupleEqual(naj_koordinate(self.vrt_y), (0, 3))
        for i in range(5):
            s, v = randint(5, 15), randint(5, 15)
            vrt = [[randint(1, 99) for _ in range(s)] for _ in range(v)]
            nx, ny = randint(4, s - 1), randint(4, v - 1)
            vrt[ny][nx] = 100
            self.assertTupleEqual(naj_koordinate(vrt), (nx, ny))
            vrt[ny][nx - 1] = 100
            self.assertTupleEqual(naj_koordinate(vrt), (nx - 1, ny))
            vrt[ny - 1][nx] = 100
            self.assertTupleEqual(naj_koordinate(vrt), (nx, ny - 1))
            vrt[ny - 1][nx - 1] = 100
            self.assertTupleEqual(naj_koordinate(vrt), (nx - 1, ny - 1))

    def test_06_pravilna_pot(self):
        vrt = self.vrt
        self.assertTrue(pravilna_pot("", vrt))
        self.assertTrue(pravilna_pot("R", vrt))
        self.assertTrue(pravilna_pot("RRRLLRRR", vrt))
        self.assertTrue(pravilna_pot("RRRLLLRR", vrt))
        self.assertTrue(pravilna_pot("D", vrt))
        self.assertTrue(pravilna_pot("DUDUDU", vrt))
        self.assertTrue(pravilna_pot("D"*(len(vrt) - 1), vrt))
        self.assertTrue(pravilna_pot("R"*(len(vrt[0]) - 1), vrt))
        self.assertTrue(pravilna_pot("R"*(len(vrt[0]) - 1) + "LLLRRR", vrt))

        self.assertFalse(pravilna_pot("L", vrt))
        self.assertFalse(pravilna_pot("RLL", vrt))
        self.assertFalse(pravilna_pot("DDUDLRR", vrt))
        self.assertFalse(pravilna_pot("R"*len(vrt[0]), vrt))
        self.assertFalse(pravilna_pot("R"*(len(vrt[0]) - 1) + "LRRLLLL", vrt))
        self.assertFalse(pravilna_pot("D"*len(vrt), vrt))
        self.assertFalse(pravilna_pot("D"*(len(vrt) - 1) + "UDDUUUU", vrt))

        self.assertTrue(pravilna_pot("RRLLR", self.vrt_x))
        self.assertTrue(pravilna_pot("DDUUD", self.vrt_y))
        self.assertFalse(pravilna_pot("RRLDLLR", self.vrt_x))
        self.assertFalse(pravilna_pot("DDURUUD", self.vrt_y))

    def test_07_dobicek_na_poti(self):
        vrt = self.vrt
        self.assertEqual(dobicek_na_poti("", vrt), 1)
        self.assertEqual(dobicek_na_poti("R", vrt), 4)
        self.assertEqual(dobicek_na_poti("RR", vrt), 7)
        self.assertEqual(dobicek_na_poti("RD", vrt), 8)
        self.assertEqual(dobicek_na_poti("RDDD", vrt), 21)
        self.assertEqual(dobicek_na_poti("RDDDL", vrt), 23)
        self.assertEqual(dobicek_na_poti("R"*(len(vrt[0]) - 1), vrt), 38)

    def test_08_brez_ponovitve(self):
        self.assertTrue(brez_ponovitve(""))
        self.assertTrue(brez_ponovitve("RRR"))
        self.assertTrue(brez_ponovitve("RRRD"))
        self.assertTrue(brez_ponovitve("RRRDL"))
        self.assertTrue(brez_ponovitve("RRRDDLDRR"))
        self.assertTrue(brez_ponovitve("RRRDDDLUUL"))
        self.assertTrue(brez_ponovitve("RRRDDRRRULL"))

        self.assertFalse(brez_ponovitve("DRUL"))
        self.assertFalse(brez_ponovitve("RRRLRRRD"))
        self.assertFalse(brez_ponovitve("RRRDDRRULL"))

    def test_09_najboljsa_pot(self):
        self.assertEqual(najboljsa_pot(self.vrt), 136)
        self.assertEqual(najboljsa_pot(self.vrt0), 42)
        self.assertEqual(najboljsa_pot(self.vrt_x), 15)
        self.assertEqual(najboljsa_pot(self.vrt_y), 15)
        for s, v, d in [(6, 8, 75), (5, 8, 67), (4, 8, 58),
                        (2, 8, 42), (5, 3, 33)]:
            kos = [x[:s] for x in self.vrt[:v]]
            self.assertEqual(najboljsa_pot(kos), d)
        hudobna = [[0, 0, 9, 9, 9]] + [[0]*5]*4
        hudobna[1][0] = 1
        self.assertEqual(najboljsa_pot(hudobna), 27)
        hudobna = list(zip(*hudobna))
        self.assertEqual(najboljsa_pot(hudobna), 27)


    def test_10_naj_narascajoca(self):
        pot = naj_narascajoca(self.vrt)
        self.assertTrue(pot in ["RDDRDL", "DRDRDL", "DDRRDL"],
                        'Pravilne poti so "RDDRDL", "DRDRDL" in "DDRRDL", ne {}'
                        .format(pot))
        self.assertEqual(naj_narascajoca([list(range(5))*2]), "R"*4)
        self.assertEqual(naj_narascajoca([[x] for x in range(5)]*2), "D"*4)
        self.assertEqual(naj_narascajoca([[0]*4]*4), "")
        self.assertEqual(naj_narascajoca([[ 0,  1,  2,  3,  0],
                                          [10,  0,  0,  0,  0],
                                          [11, 12, 13, 14, 15]]), "DDRRRR")

    def test_11_naj_nepadajoca(self):
        pot = naj_nepadajoca(self.vrt)
        self.assertTrue(pot in ["RRDLDRDL", "RRDRDLDL"],
                        'Pravilni poti sta "RRDLDRDL" in "RRDRDLDL", ne {}'
                        .format(pot))
        self.assertEqual(naj_nepadajoca([list(range(5))*2]), "R"*4)
        self.assertEqual(naj_nepadajoca([[x] for x in range(5)]*2), "D"*4)
        pot = naj_nepadajoca([[0]*4]*4)
        self.assertEqual(len(pot), 15)
        self.assertTrue(brez_ponovitve(pot))

if __name__ == "__main__":
    unittest.main()
