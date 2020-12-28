from math import sqrt


# 5

def dimenzije(gozd):
    return len(gozd[0]), len(gozd)  # to mmorajo v eni vrstici

def je_drevo(x, y, gozd):
    return gozd[y][x] == "#"   # to morajo v eni vrstici


# 6

def vsa_drevesa(gozd):
    sirina, visina = dimenzije(gozd)
    drevesa = set()
    for x in range(sirina):
        for y in range(visina):
            if je_drevo(x, y, gozd):
                drevesa.add((x, y))
    return drevesa


def vsa_drevesa(gozd):
    drevesa = set()
    for y, vrstica in enumerate(gozd):
        for x, c in enumerate(vrstica):
            if c == "#":
                drevesa.add((x, y))
    return drevesa

def vsa_drevesa(gozd):
    sirina, visina = dimenzije(gozd)
    return {(x, y)
            for x in range(sirina) for y in range(visina)
            if je_drevo(x, y, gozd)}



def vsa_drevesa(gozd):
    return {(x, y) for y, vrstica in enumerate(gozd) for x, c in enumerate(vrstica) if c == "#"}

def vsa_drevesa(gozd):
    return {(x, y) for x in range(len(gozd[0])) for y in range(len(gozd)) if je_drevo(x, y, gozd)}



def stevilo_dreves(x0, y0, x1, y1, gozd):
    return sum(je_drevo(x, y, gozd) for x in range(x0, x1) for y in range(y0, y1))

def stevilo_dreves(x0, y0, x1, y1, gozd):
    v = 0
    for x in range(x0, x1):
        for y in range(y0, y1):
            if je_drevo(x, y, gozd):
                v += 1
    return v

def stevilo_dreves(x0, y0, x1, y1, gozd):
    sirina, visina = dimenzije(gozd)
    v = 0
    for x in range(sirina):
        for y in range(visina):
            if x0 <= x < x1 and y0 <= y < y1 and je_drevo(x, y, gozd):
                v += 1
    return v

def stevilo_dreves(x0, y0, x1, y1, gozd):
    v = 0
    for x, y in vsa_drevesa(gozd):
        if x0 <= x < x1 and y0 <= y < y1:
            v += 1
    return v


def stevilo_dreves(x0, y0, x1, y1, gozd):
    return sum(x0 <= x < x1 and y0 <= y < y1 for x, y in vsa_drevesa(gozd))


def ni_dreves(x0, y0, x1, y1, gozd):
    return not stevilo_dreves(x0, y0, x1, y1, gozd)

# 7
def dreves_na_33(x, y, gozd):
    return stevilo_dreves(x, y, x + 3, y + 3, gozd)



def naj_kvadrat(gozd):
    dreves = 0
    sirina, visina = dimenzije(gozd)
    for x in range(sirina - 2):
        for y  in range(visina - 2):
            dreves = max(dreves, dreves_na_33(x, y, gozd))
    return dreves

def naj_kvadrat(gozd):
    return max(
        dreves_na_33(x, y, gozd)
        for x in range(len(gozd[0]) - 2) for y in range(len(gozd) - 2))

# 8

def lovec(x, y, pot, gozd):
    sirina, visina = dimenzije(gozd)
    buske = 0
    for c in pot:
        dx, dy = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}[c]
        nx, ny = x + dx, y + dy
        if not (0 <= nx < sirina and 0 <= ny < visina):
            continue
        elif je_drevo(nx, ny, gozd):
            buske += 1
        else:
            x, y = nx, ny
    return buske



def zajec(drevesa):
    def v_stolpcu(x):
        stolpec = []
        for x0, y0 in drevesa:
            if x0 == x:
                stolpec.append(y0)
        return stolpec

    sirina = max(drevesa)[0] + 1

    naj_koord = None
    naj_dreves = 0
    for x in range(sirina):
        stolpec = v_stolpcu(x)
        if len(stolpec) > naj_dreves:
            naj_dreves = len(stolpec)
            naj_koord = (x, max(stolpec))
    return naj_koord


def zajec(drevesa):
    sirina = max(drevesa)[0] + 1

    naj_koord = None
    naj_dreves = 0
    for x in range(sirina):
        stolpec = []
        for x0, y0 in drevesa:
            if x0 == x:
                stolpec.append(y0)

        if len(stolpec) > naj_dreves:
            naj_dreves = len(stolpec)
            naj_koord = (x, max(stolpec))
    return naj_koord

def zajec(drevesa):
    return max(
        max(({(y, x) for x0, y in drevesa if x0 == x}
             for x in {x for x, y in drevesa}), key=len)
    )[::-1]

# 9

def razdalja(x0, y0, x1, y1):
    return sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2)

def bliznja_drevesa(x, y, r, drevesa):
    return {(x0, y0) for (x0, y0) in drevesa if razdalja(x, y, x0, y0) <= r} - {(x, y)}

def povezana_drevesa(r, drevesa):
    return {(x, y): bliznja_drevesa(x, y, r, drevesa) for (x, y) in drevesa}

def jasa(gozd):
    najni = None
    for x1 in range(len(gozd[0]) + 1):
        for x0 in range(x1):
            for y1 in range(len(gozd) + 1):
                for y0 in range(y1):
                    p = (x1 - x0) * (y1 - y0)
                    if (not najni or p > najni) and ni_dreves(x0, y0, x1, y1, gozd):
                        najni = p
    return najni

def jasa(gozd):
    return max((x1 - x0) * (y1 - y0)
               for x1 in range(len(gozd[0]) + 1)
               for x0 in range(x1)
               for y1 in range(len(gozd) + 1)
               for y0 in range(y1)
               if ni_dreves(x0, y0, x1, y1, gozd))


def jasa(gozd):
    return max([((abs(curik[1]-plac[1])+1)*(abs(curik[0]-plac[0])+1))
                for plac in {(x, y) for x in range(dimenzije(gozd)[0])
                             for y in range(dimenzije(gozd)[1])
                             if not je_drevo(x, y, gozd)}
                for curik in sorted({(x, y) for x in range(dimenzije(gozd)[0])
                                     for y in range(dimenzije(gozd)[1])
                                     if not je_drevo(x, y, gozd)}, reverse=True)
                if ni_dreves(plac[0], plac[1], curik[0]+1, curik[1]+1, gozd) and plac[0] <= curik[0] and plac[1] <= curik[1]])

def jasa(gozd):
    return (lambda free: max([((abs(curik[1]-plac[1])+1)*(abs(curik[0]-plac[0])+1))
                for plac in free
                for curik in reversed(free)
                if ni_dreves(plac[0], plac[1], curik[0]+1, curik[1]+1, gozd) and plac[0] <= curik[0] and plac[1] <= curik[1]]
    ))([(x, y) for x in range(dimenzije(gozd)[0])
                                         for y in range(dimenzije(gozd)[1])
                                         if not je_drevo(x, y, gozd)])
# 10

def opica(x, y, r, drevesa):
    dosegljiva = [(x, y)]
    povezave = povezana_drevesa(r, drevesa)
    for x, y in dosegljiva:
        for x0, y0 in povezave[(x, y)]:
            if (x0, y0) not in dosegljiva:
                dosegljiva.append((x0, y0))
    return set(dosegljiva)

def opica(x, y, r, drevesa):
    dosegljiva = [(x, y)]
    povezave = povezana_drevesa(r, drevesa)
    for drevo in dosegljiva:
        for drevo0 in povezave[drevo]:
            if drevo0 not in dosegljiva:
                dosegljiva.append(drevo0)
    return set(dosegljiva)

def opica(x, y, r, drevesa):
    dosegljiva = [(x, y)]
    povezave = povezana_drevesa(r, drevesa)
    for drevo in dosegljiva:
        dosegljiva += povezave[drevo] - set(dosegljiva)
    return set(dosegljiva)

import unittest
import ast


class TestBase(unittest.TestCase):
    gozd = ["..##.......",
            "#...#...#..",
            ".#..#.#..#.",
            "..#.#...#.#",
            ".#...##..#.",
            "..#.##.....",
            ".#.#.#....#",
            ".#..#.....#",
            "#.###..#...",
            "#....#....#",
            ".#......#.#"]

    mali_gozd = [".#.#.",
                 "...#.",
                 "...#.",
                 "####.",
                 "#....",
                 "#...."]

    functions = {elm.name: elm
                 for elm in ast.parse(open(__file__, "r", encoding="utf-8").read()).body
                 if isinstance(elm, ast.FunctionDef)}

    def assert_is_one_line(self, func):
        func
        name = func.__code__.co_name
        body = self.functions[name].body
        self.assertEqual(len(body), 1, f"\nFunkcija {name} ni dolga le eno vrstico")
        self.assertIsInstance(body[0], ast.Return, "\nFunkcija {name} naj bi vsebovala le return")


class Test05(TestBase):
    def test_nedovoljene_funkcije(self):
        dovoljene_funkcije = {
            "dimenzije", "je_drevo",
            "vsa_drevesa", "stevilo_dreves", "ni_dreves",
            "dreves_na_33", "naj_kvadrat",
            "lovec", "zajec",
            "razdalja", "bliznja_drevesa", "povezana_drevesa", "jasa",
            "opica"}
        for func in self.functions:
            self.assertIn(func, dovoljene_funkcije, f"\nFunkcija {func} ni dovoljena.")

    def test_dimenzije(self):
        self.assert_is_one_line(dimenzije)
        self.assertEqual((11, 11), dimenzije(self.gozd))
        self.assertEqual((5, 6), dimenzije(self.mali_gozd))
        self.assertEqual((3, 2), dimenzije(["...", "..."]))
        self.assertEqual((1, 1), dimenzije(["."]))
        self.assertEqual((2, 3), dimenzije(["..", "..", ".."]))

    def test_je_drevo(self):
        self.assert_is_one_line(je_drevo)

        gozd = self.gozd
        self.assertTrue(je_drevo(2, 0, gozd))
        self.assertTrue(je_drevo(3, 0, gozd))
        self.assertTrue(je_drevo(0, 1, gozd))
        self.assertTrue(je_drevo(1, 4, gozd))

        self.assertFalse(je_drevo(0, 0, gozd))
        self.assertFalse(je_drevo(1, 0, gozd))
        self.assertFalse(je_drevo(4, 0, gozd))
        self.assertFalse(je_drevo(0, 2, gozd))


class Test06(TestBase):
    def test_vsa_drevesa(self):
        self.assertEqual(
            {(1, 0), (3, 0), (3, 1), (3, 2),
             (0, 3), (1, 3), (2, 3), (3, 3),
             (0, 4), (0, 5)},
            vsa_drevesa(self.mali_gozd)
        )
        self.assertEqual(
            {(5, 9), (4, 7), (4, 8), (3, 0), (5, 6), (2, 8), (10, 6), (6, 2),
             (1, 6), (9, 4), (2, 5), (10, 3), (1, 2), (5, 5), (8, 1), (10, 7),
             (8, 10), (3, 6), (1, 10), (4, 1), (10, 9), (6, 4), (5, 4), (4, 5),
             (1, 4), (2, 3), (4, 2), (0, 8), (0, 1), (8, 3), (10, 10), (9, 2),
             (3, 8), (2, 0), (4, 3), (1, 7), (0, 9), (7, 8)},
        vsa_drevesa(self.gozd)
        )
        self.assertEqual({(1, 0)}, vsa_drevesa([".#."]))
        self.assertEqual(set(), vsa_drevesa(["......"]))

    def test_stevilo_dreves(self):
        self.assertEqual(1, stevilo_dreves(0, 0, 2, 3, self.mali_gozd))
        self.assertEqual(3, stevilo_dreves(0, 0, 2, 4, self.mali_gozd))
        self.assertEqual(4, stevilo_dreves(0, 0, 3, 4, self.mali_gozd))
        self.assertEqual(5, stevilo_dreves(0, 3, 3, 6, self.mali_gozd))
        self.assertEqual(0, stevilo_dreves(1, 4, 5, 6, self.mali_gozd))

        self.assertEqual(2, stevilo_dreves(0, 0, 3, 2, self.gozd))
        self.assertEqual(3, stevilo_dreves(0, 0, 4, 2, self.gozd))
        self.assertEqual(6, stevilo_dreves(4, 1, 7, 5, self.gozd))
        self.assertEqual(3, stevilo_dreves(4, 1, 5, 4, self.gozd))
        self.assertEqual(3, stevilo_dreves(4, 1, 5, 5, self.gozd))
        self.assertEqual(4, stevilo_dreves(4, 1, 5, 6, self.gozd))
        self.assertEqual(2, stevilo_dreves(2, 3, 4, 6, self.gozd))

    def test_ni_dreves(self):
        self.assert_is_one_line(ni_dreves)
        self.assertFalse(ni_dreves(0, 3, 3, 6, self.mali_gozd))
        self.assertTrue(ni_dreves(1, 4, 5, 6, self.mali_gozd))


class Test07(TestBase):
    def test_dreves_na_33(self):
        self.assert_is_one_line(dreves_na_33)

        self.assertEqual(3, dreves_na_33(0, 0, self.gozd))
        self.assertEqual(4, dreves_na_33(2, 5, self.gozd))
        self.assertEqual(5, dreves_na_33(3, 5, self.gozd))

        self.assertEqual(5, dreves_na_33(0, 3, self.mali_gozd))
        self.assertEqual(3, dreves_na_33(1, 3, self.mali_gozd))

    def test_naj_kvadrat(self):
        self.assertEqual(5, naj_kvadrat(self.gozd))
        self.assertEqual(5, naj_kvadrat(self.mali_gozd))
        self.assertEqual(9, naj_kvadrat([".....",
                                         "..###",
                                         "..###",
                                         "..###"]))
        self.assertEqual(9, naj_kvadrat(["......",
                                         "..###.",
                                         "..###.",
                                         "..###."]))
        self.assertEqual(4, naj_kvadrat([".....",
                                         ".....",
                                         "...##",
                                         "...##"]))

class Test08(TestBase):
    def test_lovec(self):
        self.assertEqual(3, lovec(1, 0, "v<v>>>v", self.gozd))
        self.assertEqual(5, lovec(1, 0, "vvvvvv", self.gozd))
        self.assertEqual(1, lovec(5, 0, "<<", self.gozd))
        self.assertEqual(2, lovec(5, 0, "<<v", self.gozd))
        self.assertEqual(2, lovec(5, 0, "<<v>vvv", self.gozd))
        self.assertEqual(2, lovec(5, 0, "<<v>vvv>", self.gozd))
        self.assertEqual(3, lovec(5, 0, "<<v>vvv>^", self.gozd))
        self.assertEqual(4, lovec(5, 0, "<<v>vvv>^>>", self.gozd))
        self.assertEqual(4, lovec(5, 0, "<<v>vvv>^>>vvvv", self.gozd))
        self.assertEqual(4, lovec(5, 0, "<<v>vvv>^>>vvvv<<", self.gozd))
        self.assertEqual(5, lovec(5, 0, "<<v>vvv>^>>vvvv<<<", self.gozd))
        self.assertEqual(6, lovec(5, 0, "<<v>vvv>^>>vvvv<<<^", self.gozd))
        self.assertEqual(6, lovec(5, 0, "<<v>vvv>^>>vvvv<<<^v", self.gozd))
        self.assertEqual(7, lovec(5, 0, "<<v>vvv>^>>vvvv<<<^vv", self.gozd))
        self.assertEqual(8, lovec(5, 0, "<<v>vvv>^>>vvvv<<<^vv>>", self.gozd))
        self.assertEqual(8, lovec(5, 0, "<<v>vvv>^>>vvvv<<<^vv>>vv", self.gozd))
        self.assertEqual(8, lovec(5, 0, "<<v>vvv>^>>vvvv<<<^vv>>vvvvv", self.gozd))

        self.assertEqual(8, lovec(5, 0, "^<<v>vvv>^>>vvvv<<<^vv>>vv", self.gozd))

        self.assertEqual(0, lovec(0, 0, "<", self.gozd))
        self.assertEqual(1, lovec(0, 0, "<v", self.gozd))
        self.assertEqual(1, lovec(0, 0, "<^v", self.gozd))

    def test_zajec(self):
        self.assertEqual((4, 8), zajec(vsa_drevesa(self.gozd)))
        self.assertEqual((4, 3), zajec(vsa_drevesa(self.gozd[:4])))
        self.assertEqual((4, 3), zajec(vsa_drevesa(self.gozd[:5])))
        self.assertEqual((3, 3), zajec(vsa_drevesa(self.mali_gozd)))

        x, y0, y1 = 10*51, 10**50, 10**52
        self.assertEqual((x, y0), zajec({(x, y0)}))
        self.assertEqual((x, y1), zajec({(x, y0), (x, y1)}))
        self.assertEqual((x, y1), zajec({(x, y1), (x, y0)}))

class Test09(TestBase):
    def test_izpeljanke(self):
        self.assert_is_one_line(vsa_drevesa)
        self.assert_is_one_line(stevilo_dreves)
        self.assert_is_one_line(naj_kvadrat)
        self.assert_is_one_line(bliznja_drevesa)
        self.assert_is_one_line(povezana_drevesa)

    def test_razdalja(self):
        self.assert_is_one_line(razdalja)
        self.assertAlmostEqual(5, razdalja(1, -5, 4, -1))
        self.assertAlmostEqual(5, razdalja(1, -5, 4, -9))
        self.assertAlmostEqual(5, razdalja(1, -5, -2, -9))

    def test_bliznja_drevesa(self):
        drevesa = vsa_drevesa(self.gozd)
        self.assertEqual({(3, 0), (4, 2), (4, 3)},
                         bliznja_drevesa(4, 1, 2, drevesa))
        self.assertEqual({(0, 1)},
                         bliznja_drevesa(0, 0, 1, drevesa))
        self.assertEqual({(2, 3), (2, 5), (3, 6), (4, 2), (4, 3),
                          (4, 7), (4, 8), (5, 4), (5, 5), (5, 6),
                          (6, 4)},
                         bliznja_drevesa(4, 5, 3, drevesa))
        self.assertEqual(set(),
                         bliznja_drevesa(8, 6, 1, drevesa))
        self.assertEqual({(3, 0), (4, 2)},
                         bliznja_drevesa(4, 1, 1.5, drevesa))

    def test_povezana_drevesa(self):
        drevesa = vsa_drevesa(self.gozd)
        self.assertEqual({(0, 1): {(1, 2)},
                          (0, 8): {(0, 9), (2, 8), (1, 7)},
                          (0, 9): {(1, 10), (0, 8)},
                          (1, 2): {(0, 1), (2, 3), (1, 4)},
                          (1, 4): {(1, 2), (2, 5), (1, 6), (2, 3)},
                          (1, 6): {(2, 5), (3, 6), (1, 4), (1, 7)},
                          (1, 7): {(2, 8), (0, 8), (1, 6)},
                          (1, 10): {(0, 9)},
                          (2, 0): {(3, 0)},
                          (2, 3): {(1, 2), (2, 5), (4, 3), (1, 4)},
                          (2, 5): {(4, 5), (1, 4), (1, 6), (2, 3), (3, 6)},
                          (2, 8): {(3, 8), (1, 7), (0, 8), (4, 8)},
                          (3, 0): {(2, 0), (4, 1)},
                          (3, 6): {(4, 7), (5, 6), (4, 5), (3, 8), (1, 6), (2, 5)},
                          (3, 8): {(2, 8), (4, 7), (3, 6), (4, 8)},
                          (4, 1): {(3, 0), (4, 2), (4, 3)},
                          (4, 2): {(6, 2), (4, 1), (4, 3)},
                          (4, 3): {(5, 4), (4, 5), (2, 3), (4, 2), (4, 1)},
                          (4, 5): {(4, 7), (5, 4), (5, 5), (5, 6), (3, 6), (4, 3), (2, 5)},
                          (4, 7): {(4, 8), (5, 6), (4, 5), (3, 8), (3, 6)},
                          (4, 8): {(3, 8), (5, 9), (4, 7), (2, 8)},
                          (5, 4): {(6, 4), (5, 5), (5, 6), (4, 5), (4, 3)},
                          (5, 5): {(5, 6), (6, 4), (5, 4), (4, 5)},
                          (5, 6): {(5, 4), (4, 7), (5, 5), (4, 5), (3, 6)},
                          (5, 9): {(4, 8)},
                          (6, 2): {(4, 2), (6, 4)},
                          (6, 4): {(5, 4), (6, 2), (5, 5)},
                          (7, 8): set(),
                          (8, 1): {(9, 2), (8, 3)},
                          (8, 3): {(8, 1), (9, 4), (10, 3), (9, 2)},
                          (8, 10): {(10, 10)},
                          (9, 2): {(8, 1), (8, 3), (10, 3), (9, 4)},
                          (9, 4): {(9, 2), (8, 3), (10, 3)},
                          (10, 3): {(9, 2), (8, 3), (9, 4)},
                          (10, 6): {(10, 7)},
                          (10, 7): {(10, 6), (10, 9)},
                          (10, 9): {(10, 7), (10, 10)},
                          (10, 10): {(8, 10), (10, 9)}
                          },
                         povezana_drevesa(2, drevesa))

        self.assertEqual(
            {(0, 1): set(),
             (0, 8): {(0, 9)},
             (0, 9): {(0, 8)},
             (1, 2): set(),
             (1, 4): set(),
             (1, 6): {(1, 7)},
             (1, 7): {(1, 6)},
             (1, 10): set(),
             (2, 0): {(3, 0)},
             (2, 3): set(),
             (2, 5): set(),
             (2, 8): {(3, 8)},
             (3, 0): {(2, 0)},
             (3, 6): set(),
             (3, 8): {(2, 8), (4, 8)},
             (4, 1): {(4, 2)},
             (4, 2): {(4, 1), (4, 3)},
             (4, 3): {(4, 2)},
             (4, 5): {(5, 5)},
             (4, 7): {(4, 8)},
             (4, 8): {(3, 8), (4, 7)},
             (5, 4): {(6, 4), (5, 5)},
             (5, 5): {(5, 6), (5, 4), (4, 5)},
             (5, 6): {(5, 5)},
             (5, 9): set(),
             (6, 2): set(),
             (6, 4): {(5, 4)},
             (7, 8): set(),
             (8, 1): set(),
             (8, 3): set(),
             (8, 10): set(),
             (9, 2): set(),
             (9, 4): set(),
             (10, 3): set(),
             (10, 6): {(10, 7)},
             (10, 7): {(10, 6)},
             (10, 9): {(10, 10)},
             (10, 10): {(10, 9)}},
            povezana_drevesa(1, drevesa))

    def test_jasa(self):
        self.assertEqual(12, jasa(self.gozd))
        self.assertEqual(7, jasa(self.gozd[:6]))
        self.assertEqual(8, jasa(self.mali_gozd))
        gozd2 = self.mali_gozd[:-1] + ["#...#"]
        self.assertEqual(6, jasa(gozd2))


class Test10(TestBase):
    def test_izpeljanke(self):
        self.assert_is_one_line(zajec)
        self.assert_is_one_line(jasa)

    def test_opica(self):
        skupina = {(5, 4), (5, 5), (5, 6), (4, 5), (6, 4)}
        drevesa = vsa_drevesa(self.gozd)
        for x, y in skupina:
            self.assertEqual(skupina, opica(x, y, 1, drevesa))

        skupina = {(x, y) for x, y in drevesa if x <= 5} | {(6, 4)}
        for x, y in skupina:
            self.assertEqual(skupina, opica(x, y, 1.5, drevesa))

        skupina = {(x, y) for x, y in drevesa if x <= 6}
        for x, y in skupina:
            self.assertEqual(skupina, opica(x, y, 2.1, drevesa))

        skupina = {(8, 1), (8, 3), (9, 2), (9, 4), (10, 3)}
        for x, y in skupina:
            self.assertEqual(skupina, opica(x, y, 1.5, drevesa))

        for x, y in drevesa:
            self.assertEqual(drevesa, opica(x, y, 2.5, drevesa))


if __name__ == "__main__":
    unittest.main()
