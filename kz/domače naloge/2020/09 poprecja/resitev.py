from math import ceil

def redovalnica(ime_datoteke):
    red = {}
    for vrstica in open(ime_datoteke):
        polja = vrstica.split()
        red[polja[0]] = [int(x) for x in polja[1:]]
    return red


def poprecne_ocene(ime_datoteke):
    return {k: int(ceil(sum(v) / len(v)))
            for k, v in redovalnica(ime_datoteke).items()}


def zapisi_poprecja(vhod, izhod):
    f = open(izhod, "wt")
    for ime, popr in poprecne_ocene(vhod).items():
        f.write(ime + " " + str(popr) + "\n")


import unittest
import random
import os
import warnings

from string import ascii_letters

class Test(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)

    @staticmethod
    def rands():
        return "".join(random.choice(ascii_letters) for _ in range(25))

    def test_redovalnica(self):
        self.assertEqual({
            "Ana": [4, 2, 3, 4, 5],
            "Berta": [4, 3],
            "Cilka": [5, 5, 3, 5],
            "Dani": [4, 3, 5],
            "Ema": [3]},
            redovalnica("ocene.txt")
        )

        fname = self.rands()
        try:
            ime = self.rands()
            with open(fname, "w") as f:
                f.write(f"{ime} 3 4 5\n")
            self.assertEqual({ime: [3, 4, 5]}, redovalnica(fname))
        finally:
            os.remove(fname)

    def test_poprecne_ocene(self):
        self.assertEqual(
            {'Ana': 4, 'Berta': 4, 'Cilka': 5, 'Dani': 4, 'Ema': 3},
            poprecne_ocene("ocene.txt"))

    def test_zapisi_poprecja(self):
        fname = self.rands() + ".txt"
        zapisi_poprecja("ocene.txt", fname)
        self.assertEqual(
            {'Ana': [4], 'Berta': [4], 'Cilka': [5], 'Dani': [4], 'Ema': [3]},
            redovalnica(fname)
        )
        os.remove(fname)


if __name__ == "__main__":
    unittest.main()
