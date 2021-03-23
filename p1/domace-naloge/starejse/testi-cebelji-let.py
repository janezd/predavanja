import unittest

class Test_Risanje(unittest.TestCase):
    def setUp(self):
        def zavita_crta(*args, **kwargs):
            self.klici.append(sorted([args[:2], args[2:4]]))
            return stara_crta(*args, **kwargs)
        stara_crta = risar.crta
        risar.crta = zavita_crta
        self.klici = []

    def assert_risi(self, first, second):
        risi_pot(first)
        super().assertEqual(self.klici, second)
        self.klici = []

    def assert_risi_prosto(self, first, second):
        risi_prosto_pot(first)
        super().assertEqual(self.klici, second)
        self.klici = []

    def test_risi_pot(self):
        self.assert_risi("", [])
        self.assert_risi("R", [[(0, 0), (10, 0)]])
        self.assert_risi("RR", [[(0, 0), (10, 0)], [(10, 0), (20, 0)]])
        self.assert_risi("RRDLU", [[(0, 0), (10, 0)],
                                  [(10, 0), (20, 0)],
                                  [(20, 0), (20, 10)],
                                  [(10, 10), (20, 10)],
                                  [(10, 0), (10, 10)]])
        self.assert_risi("RRDRDLLUL", [[(0, 0), (10, 0)],
                                      [(10, 0), (20, 0)],
                                      [(20, 0), (20, 10)],
                                      [(20, 10), (30, 10)],
                                      [(30, 10), (30, 20)],
                                      [(20, 20), (30, 20)],
                                      [(10, 20), (20, 20)],
                                      [(10, 10), (10, 20)],
                                      [(0, 10), (10, 10)]])

    def test_risi_prosto_pot(self):
        self.assert_risi_prosto("", [])
        self.assert_risi_prosto("R1", [[(0, 0), (1, 0)]])
        self.assert_risi_prosto("R12", [[(0, 0), (12, 0)]])
        self.assert_risi_prosto("R105", [[(0, 0), (105, 0)]])
        self.assert_risi_prosto("R1D13", [[(0, 0), (1, 0)], [(1, 0), (1, 13)]])
        self.assert_risi_prosto("R12D5", [[(0, 0), (12, 0)], [(12, 0), (12, 5)]])
        self.assert_risi_prosto("R105D1", [[(0, 0), (105, 0)], [(105, 0), (105, 1)]])
        self.assert_risi_prosto("R105U1", [[(0, 0), (105, 0)], [(105, -1), (105, 0)]])
        self.assert_risi_prosto("R15R123D246L123U246",
                                [[(0, 0), (15, 0)],
                                 [(15, 0), (138, 0)],
                                 [(138, 0), (138, 246)],
                                 [(15, 246), (138, 246)],
                                 [(15, 0), (15, 246)]])
        self.assert_risi_prosto("R1R12D8R4D50L2L12U5R42",
                                [[(0, 0), (1, 0)],
                                      [(1, 0), (13, 0)],
                                      [(13, 0), (13, 8)],
                                      [(13, 8), (17, 8)],
                                      [(17, 8), (17, 58)],
                                      [(15, 58), (17, 58)],
                                      [(3, 58), (15, 58)],
                                      [(3, 53), (3, 58)],
                                      [(3, 53), (45, 53)]])

if __name__ == "__main__":
    unittest.main()
