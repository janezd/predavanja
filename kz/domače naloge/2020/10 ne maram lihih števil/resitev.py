# ogrevanje

# Seznam vsebuje sama soda števila, če je prazen pa je prvo število sodo
# in vsebuje preostanek sama soda števila.
def vsebuje_sama_soda(s):
    return not s or s[0] % 2 == 0 and vsebuje_sama_soda(s[1:])

# Seznam obrnemo tako, da k obrnjenim ostalim elementom dodamo prvi element
# Točneje: vrnemo vsoto seznama, ki vsebuje ostale elemente v obratnem
# vrstnem redu, in seznama, ki vsebuje le prvi element.
def obrni(s):
    return s and obrni(s[1:]) + [s[0]]

# Da vrnemo vsa soda števila, vrnemo vsoto seznama, ki vsebuje prvi element
# in seznama, ki vsebuje samo_soda števila iz ostanka
def samo_soda(s):
    return s and s[:s[0] % 2 == 0] + samo_soda(s[1:])


# obvezna

def prestej_liha(s):
    return len(s) and (s[0] % 2 + prestej_liha(s[1:]))

def ena_vec(s):
    return s and [s[0] + 1] + ena_vec(s[1:])

def zbij_liha(s):
    return s and [s[0] - s[0] % 2] + zbij_liha(s[1:])

# dodatna
def zadnje_liho(s):
    if s == []:
        return False
    zadnje = zadnje_liho(s[1:])
    if zadnje:
        return zadnje
    if s[0] % 2 == 1:
        return s[0]
    return False

def zadnje_liho(s):
    return s != [] and (zadnje_liho(s[1:]) or s[0] % 2 == 1 and s[0])



import unittest

class Test00_Ogrevanje(unittest.TestCase):
    def test_vsebuje_samo_soda(self):
        self.assertTrue(vsebuje_sama_soda([]))
        self.assertTrue(vsebuje_sama_soda([2]))
        self.assertTrue(vsebuje_sama_soda([4, 2]))
        self.assertTrue(vsebuje_sama_soda([8, 4, 0, 6]))
        self.assertFalse(vsebuje_sama_soda([3, 8, 4, 0, 6]))
        self.assertFalse(vsebuje_sama_soda([8, 3, 4, 0, 6]))
        self.assertFalse(vsebuje_sama_soda([8, 4, 0, 6, 3]))
        self.assertFalse(vsebuje_sama_soda([3]))

        with self.assertRaises(RecursionError, msg="Funkcija ni rekurzivna"):
            vsebuje_sama_soda([0] * 1010)

    def test_obrni(self):
        self.assertEqual([], obrni([]))
        self.assertEqual([2], obrni([2]))
        self.assertEqual([2, 4], obrni([4, 2]))
        self.assertEqual([1, 2, 4], obrni([4, 2, 1]))
        self.assertEqual([1, 8, 2, 4], obrni([4, 2, 8, 1]))

    def test_samo_soda(self):
        self.assertEqual([], samo_soda([]))
        self.assertEqual([2], samo_soda([2]))
        self.assertEqual([], samo_soda([1]))
        self.assertEqual([2], samo_soda([1, 2]))
        self.assertEqual([2, 4], samo_soda([1, 2, 4]))
        self.assertEqual([2, 6, 2, 4], samo_soda([1, 2, 3, 6, 2, 1, 4]))


class Test01Obvezna(unittest.TestCase):
    def test_prestej_liha(self):
        self.assertEqual(0, prestej_liha([]))
        self.assertEqual(0, prestej_liha([2]))
        self.assertEqual(1, prestej_liha([5]))
        self.assertEqual(1, prestej_liha([2, 5]))
        self.assertEqual(2, prestej_liha([5, 4, 3]))
        self.assertEqual(2, prestej_liha([5, 4, 3]))
        self.assertEqual(3, prestej_liha([1, 2, 3, 6, 2, 1, 4]))

    def test_ena_vec(self):
        self.assertEqual([], ena_vec([]))
        self.assertEqual([3], ena_vec([2]))
        self.assertEqual([3, 7], ena_vec([2, 6]))
        self.assertEqual([3, 7, 1], ena_vec([2, 6, 0]))
        self.assertEqual([3, 7, 1, 8], ena_vec([2, 6, 0, 7]))

    def test_zbij_liha(self):
        self.assertEqual([], zbij_liha([]))
        self.assertEqual([4], zbij_liha([4]))
        self.assertEqual([2], zbij_liha([3]))
        self.assertEqual([2, 6, 0, 4, 6], zbij_liha([3, 6, 1, 5, 6]))


class Test02Dodatno(unittest.TestCase):
    def test_zadnje_liho(self):
        self.assertFalse(zadnje_liho([]))
        self.assertFalse(zadnje_liho([4]))
        self.assertFalse(zadnje_liho([4, 6, 2, 42]))
        self.assertEqual(5, zadnje_liho([5, 4, 6, 2, 42]))
        self.assertEqual(5, zadnje_liho([4, 6, 5, 2, 42]))
        self.assertEqual(5, zadnje_liho([4, 6, 2, 42, 5]))
        self.assertEqual(5, zadnje_liho([4, 6, 3, 2, 42, 5]))
        self.assertEqual(5, zadnje_liho([11, 4, 6, 3, 2, 42, 5]))


if __name__ == "__main__":
    unittest.main()
