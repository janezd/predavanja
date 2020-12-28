def ime(s):
    return s.split()[1]

def datum(s):
    mes, dan, let = s.split()[0].split("/")
    return int(let), int(mes), int(dan)

def dolzina(s):
    return int(s.split()[-1])

def podatki(s):
    return datum(s), ime(s), dolzina(s)

def je_novejsa(dat1, dat2):
    return datum(dat1) > datum(dat2)

def najnovejsa(ime, arhiv):
    naj_pod = None
    naj_dat = None
    for vrstica in arhiv:
        pod = dat, ime2, _2 = podatki(vrstica)
        if ime == ime2 and (naj_dat == None or dat > naj_dat):
            naj_pod = pod
            naj_dat = dat
    return naj_pod


def datumi(ime, arhiv):
    dats = []
    for vrstica in arhiv:
        dat, im, _ = podatki(vrstica)
        if im == ime:
            dats.append(dat)
    return sorted(dats, reverse=True)

def brez(im, arhiv):
    filtriran = []
    for vrstica in arhiv:
        if ime(vrstica) != im:
            filtriran.append(vrstica)
    return filtriran


import unittest
from random import shuffle


class TestObvezna(unittest.TestCase):
    def test_ime(self):
        self.assertEqual("ime_datoteke.md", ime("11/16/2020 ime_datoteke.md 314236"))
        self.assertEqual("foo.txt", ime("1/1/1971 foo.txt 42"))

    def test_dolzina(self):
        self.assertEqual(314236, dolzina("11/16/2020 ime_datoteke.md 314236"))
        self.assertEqual(42, dolzina("1/1/1971 foo.txt 42"))

    def test_datum(self):
        self.assertEqual((2020, 11, 16), datum("11/16/2020 ime_datoteke.md 314236"))
        self.assertEqual((1971, 1, 1), datum("1/1/1971 foo.txt 42"))

    def test_podatki(self):
        self.assertEqual(((2020, 11, 16), "ime_datoteke.md", 314236), podatki("11/16/2020 ime_datoteke.md 314236"))
        self.assertEqual(((1971, 1, 1), "foo.txt", 42), podatki("1/1/1971 foo.txt 42"))

    def test_je_novejsa(self):
        self.assertIs(True, je_novejsa("11/16/2020 ime 314236", "10/16/2020 ime 314236"))
        self.assertIs(True, je_novejsa("11/16/2020 ime 314236", "11/5/2020 ime 314236"))
        self.assertIs(True, je_novejsa("11/16/2020 ime 314236", "11/15/2015 ime 314236"))
        self.assertIs(True, je_novejsa("11/16/2020 ime 314236", "5/16/2020 ime 314236"))
        self.assertIs(True, je_novejsa("5/16/2020 ime 314236", "4/16/2020 ime 314236"))

        self.assertIs(False, je_novejsa("10/16/2020 ime 314236", "11/16/2020 ime 314236"))
        self.assertIs(False, je_novejsa("11/5/2020 ime 314236", "11/16/2020 ime 314236"))
        self.assertIs(False, je_novejsa("11/5/2020 ime 314236", "11/5/2020 ime 314236"))
        self.assertIs(False, je_novejsa("11/15/2020 ime 314236", "11/16/2020 ime 314236"))
        self.assertIs(False, je_novejsa("5/16/2015 ime 314236", "11/16/2020 ime 314236"))
        self.assertIs(False, je_novejsa("4/16/2020 ime 314236", "5/16/2020 ime 314236"))

        self.assertIs(True, je_novejsa("4/16/2020   i   m e 314236", "12/31/2018   i  m e 314236"))
        self.assertIs(True, je_novejsa("4/16/2020   i   m e 314236", "1/1/2018   i  m e 314236"))

    def test_najnovejsa(self):
        vrstice = [
            "10/16/2020 ime_dat.avi 314236",
            "10/14/2020 ime_dat.avi 312353",
            "5/16/2020 ime_dat.avi 21532",
            "10/16/2020 some_other.avi 314236",
            "10/18/2020 another_file.avi 351352",
            "10/18/2018 another_file.avi 314236",
        ]
        for i in range(10):
            shuffle(vrstice)
            self.assertEqual(((2020, 10, 16), "ime_dat.avi", 314236), najnovejsa("ime_dat.avi", vrstice))
            self.assertEqual(((2020, 10, 18), "another_file.avi", 351352), najnovejsa("another_file.avi", vrstice))
            self.assertEqual(((2020, 10, 16), "some_other.avi", 314236), najnovejsa("some_other.avi", vrstice))


class TestDodatna(unittest.TestCase):
    def test_datumi(self):
        vrstice = [
            "10/16/2020 ime_dat.avi 314236",
            "10/14/2020 ime_dat.avi 312353",
            "5/16/2020 ime_dat.avi 21532",
            "12/31/2018 ime_dat.avi 21532",
            "10/16/2020 some_other.avi 314236",
            "10/18/2020 another_file.avi 351352",
            "10/18/2018 another_file.avi 314236",
        ]
        for i in range(10):
            shuffle(vrstice)
            self.assertEqual([(2020, 10, 16), (2020, 10, 14), (2020, 5, 16), (2018, 12, 31)], datumi("ime_dat.avi", vrstice))
            self.assertEqual([(2020, 10, 16)], datumi("some_other.avi", vrstice))
            self.assertEqual([], datumi("no_such_file.avi", vrstice))

    def test_brez(self):
        from random import shuffle

        f1 = ["10/18/2018 another_file.avi 314236"]
        f2 = ["10/18/2020 ime_dat.avi 314236"]
        f3 = ["10/18/2020 some_other.avi 314236"]
        vrstice = 10 * f1 + 2 * f2 + f3

        for i in range(10):
            kopija = vrstice[:]
            shuffle(kopija)
            self.assertEqual(2 * f2 + f3, sorted(brez("another_file.avi", kopija)))


if __name__ == "__main__":
    unittest.main()
