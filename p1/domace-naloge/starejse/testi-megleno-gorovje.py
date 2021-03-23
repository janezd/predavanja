import unittest
import random


class TestMeglenoGorovje(unittest.TestCase):
    zemljevid = {0: [6, 3], 6: [5, 81], 3: [8, 24], 5: [2, 18], 81: [None, None],
                 8: [42, None], 24: [63, 13], 2: [7, 27], 18: [None, 35],
                 42: [None, 66], 63: [61, None], 13: [4, 12], 7: [None, None],
                 27: [None, None], 35: [None, None], 66: [None, None],
                 61: [None, None], 4:[None, None], 12: [None, None]}

    zemljevid2 = {}
    for k, v in zemljevid.items():
        zemljevid2[k] = v[::-1]

    def sestavi_zemljevid(self):
        red = list(range(1, 600))
        random.shuffle(red)
        sobe = [(0, 0)]
        zemljevid = {}
        globina = None
        for soba, glob in sobe:
            if soba == 42:
                globina = glob
            spodaj = [red and random.random() < 20 / (1 + len(zemljevid))
                      and red.pop() or None for _ in "  "]
            zemljevid[soba] = spodaj
            sobe += zip(filter(None, spodaj), [glob + 1] * 2)
        if not globina:
            cilj, globina = random.choice(sobe[1:])
            zemljevid[42] = zemljevid[cilj]
            del zemljevid[cilj]
            for spodaj in zemljevid.values():
                spodaj[:] = [42 if i == cilj else i for i in spodaj]
        return zemljevid, globina

    def test_prehodi_pot(self):
        for pot, soba in [("", 0), ("L", 6), ("D", 3),
                          ("LL", 5), ("LD", 81), ("DL", 8), ("DD", 24),
                          ("LLL", 2), ("LLD", 18), ("DLL", 42), ("DDL", 63),
                          ("DDD", 13), ("LLLL", 7), ("LLLD", 27), ("LLDD", 35),
                          ("DLLD", 66), ("DDLL", 61), ("DDDL", 4),
                          ("DDDD", 12)]:
            s = prehodi_pot(self.zemljevid, 0, pot)
            self.assertEqual(s, soba, "Pot {} vodi v {}, ne {}".format(
                pot or '""', soba, s))

    def test_globina_prstana(self):
        nn = [None, None]
        self.assertEqual(globina_prstana({0: [42, 3], 42: nn, 3: nn}, 0), 1)
        self.assertEqual(globina_prstana({0: [42, 3], 42: [1, 2], 3: nn,
                                          1: nn, 2: nn}, 0), 1)
        self.assertEqual(globina_prstana({0: [3, 42], 3: nn, 42: nn}, 0), 1)
        self.assertEqual(globina_prstana({0: [3, 42], 3: nn, 42: [1, 2],
                                          1: nn, 2: nn}, 0), 1)
        self.assertEqual(globina_prstana({0: [1, 3], 1: [42, None],
                                          3: nn, 42: nn}, 0), 2)
        self.assertEqual(globina_prstana({0: [3, 1], 1: [42, None],
                                          3: nn, 42: nn}, 0), 2)
        self.assertEqual(globina_prstana(self.zemljevid, 0), 3)
        self.assertEqual(globina_prstana(self.zemljevid2, 0), 3)
        for i in range(20):
            z, g = self.sestavi_zemljevid()
            self.assertEqual(globina_prstana(z, 0), g)

    def test_pot_do_prstana(self):
        def pp(zemljevid):
            pot = pot_do_prstana(zemljevid, 0)
            soba = prehodi_pot(zemljevid, 0, pot)
            self.assertEqual(soba, 42,
                             "Pot {} ne vodi v sobo 42 temveč {}\n"
                             "Zemljevid: {}".format(pot, soba, zemljevid))

        nn = [None, None]
        pp({0: [42, 3], 42: nn, 3: nn})
        pp({0: [42, 3], 42: [1, 2], 3: nn, 1: nn, 2: nn})
        pp({0: [3, 42], 3: nn, 42: nn})
        pp({0: [3, 42], 3: nn, 42: [1, 2], 1: nn, 2: nn})
        pp({0: [1, 3], 1: [42, None], 3: nn, 42: nn})
        pp({0: [3, 1], 1: [42, None], 3: nn, 42: nn})
        pp(self.zemljevid)
        pp(self.zemljevid2)
        for i in range(20):
            pp(self.sestavi_zemljevid()[0])

if __name__ == "__main__":
    unittest.main()