


import unittest
from random import shuffle


class TestObvezna(unittest.TestCase):
    def test_ime(self):
        self.assertEqual("ime_datoteke.md", ime("11/16/2020 ime_datoteke.md 314236"))
        self.assertEqual("ime datoteke s presledki.md", ime("11/6/2015 ime datoteke s presledki.md 123"))
        self.assertEqual("ime  s     presledki.md", ime("11/16/2020 ime  s     presledki.md 436"))
        self.assertEqual("ime  s     presledki.md", ime("1/6/2020     ime  s     presledki.md   0"))

    def test_dolzina(self):
        self.assertEqual(314236, dolzina("11/16/2020 ime_datoteke.md 314236"))
        self.assertEqual(123, dolzina("11/6/2015 ime datoteke s presledki.md 123"))
        self.assertEqual(436, dolzina("11/16/2020 ime  s     presledki.md 436"))
        self.assertEqual(0, dolzina("1/6/2020     ime  s     presledki.md   0"))

    def test_datum(self):
        self.assertEqual((2020, 11, 16), datum("11/16/2020 ime_datoteke.md 314236"))
        self.assertEqual((2015, 11, 6), datum("11/6/2015 ime datoteke s presledki.md 123"))
        self.assertEqual((2020, 11, 16), datum("11/16/2020 ime  s     presledki.md 436"))
        self.assertEqual((2020, 1, 6), datum("1/6/2020     ime  s     presledki.md   0"))

    def test_podatki(self):
        self.assertEqual(((2020, 11, 16), "ime_datoteke.md", 314236), podatki("11/16/2020 ime_datoteke.md 314236"))
        self.assertEqual(((2015, 11, 6), "ime datoteke s presledki.md", 123), podatki("11/6/2015 ime datoteke s presledki.md 123"))
        self.assertEqual(((2020, 11, 16), "ime  s     presledki.md", 436), podatki("11/16/2020 ime  s     presledki.md 436"))
        self.assertEqual(((2020, 1, 6), "ime  s     presledki.md", 0), podatki("1/6/2020     ime  s     presledki.md   0"))

    def test_je_novejsa(self):
        self.assertIs(True, je_novejsa("11/16/2020   i   m e 314236", "10/16/2020   i  m e 314236"))
        self.assertIs(True, je_novejsa("11/16/2020   i   m e 314236", "11/5/2020   i  m e 314236"))
        self.assertIs(True, je_novejsa("11/16/2020   i   m e 314236", "11/15/2015   i  m e 314236"))
        self.assertIs(True, je_novejsa("11/16/2020   i   m e 314236", "5/16/2020   i  m e 314236"))
        self.assertIs(True, je_novejsa("5/16/2020   i   m e 314236", "4/16/2020   i  m e 314236"))

        self.assertIs(False, je_novejsa("10/16/2020   i   m e 314236", "11/16/2020   i  m e 314236"))
        self.assertIs(False, je_novejsa("11/5/2020   i   m e 314236", "11/16/2020   i  m e 314236"))
        self.assertIs(False, je_novejsa("11/5/2020   i   m e 314236", "11/5/2020   i  m e 314236"))
        self.assertIs(False, je_novejsa("11/15/2020   i   m e 314236", "11/16/2020   i  m e 314236"))
        self.assertIs(False, je_novejsa("5/16/2015   i   m e 314236", "11/16/2020   i  m e 314236"))
        self.assertIs(False, je_novejsa("4/16/2020   i   m e 314236", "5/16/2020   i  m e 314236"))

    def test_datumi(self):
        vrstice = [
            "10/16/2020 ime dat.avi 314236",
            "10/14/2020 ime dat.avi   312353",
            "5/16/2020   ime dat.avi 21532",
            "12/31/2018   ime dat.avi 21532",
            "10/16/2020 some other.avi 314236",
            "10/18/2020 another file.avi 351352",
            "10/18/2018 another file.avi 314236",
        ]
        for i in range(10):
            shuffle(vrstice)
            self.assertEqual([(2020, 10, 16), (2020, 10, 14), (2020, 5, 16), (2018, 12, 31)], datumi("ime dat.avi", vrstice))
            self.assertEqual([(2020, 10, 16)], datumi("some other.avi", vrstice))
            self.assertEqual([], datumi("no such file.avi", vrstice))

    def test_najnovejsa(self):
        vrstice = [
            "10/16/2020 ime dat.avi 314236",
            "10/14/2020 ime dat.avi   312353",
            "5/16/2020   ime dat.avi 21532",
            "10/16/2020 some other.avi 314236",
            "10/18/2020 another file.avi 351352",
            "10/18/2018 another file.avi 314236",
        ]
        for i in range(10):
            shuffle(vrstice)
            self.assertEqual(((2020, 10, 16), "ime dat.avi", 314236), najnovejsa("ime dat.avi", vrstice))
            self.assertEqual(((2020, 10, 18), "another file.avi", 351352), najnovejsa("another file.avi", vrstice))
            self.assertEqual(((2020, 10, 16), "some other.avi", 314236), najnovejsa("some other.avi", vrstice))

    def test_odstrani(self):
        from random import shuffle

        f1 = ["10/18/2018 another file.avi 314236"]
        f2 = ["10/18/2020 ime dat.avi 314236"]
        f3 = ["10/18/2020 some other.avi 314236"]
        vrstice = 10 * f1 + 2 * f2 + f3

        self.assertIsNone(odstrani("another file.avi", vrstice[:]), "`odstrani` ne sme vračati ničesar")

        for i in range(10):
            kopija = vrstice[:]
            shuffle(kopija)
            odstrani("another file.avi", kopija)
            self.assertEqual(2 * f2 + f3, sorted(kopija))

        kopija = sorted(vrstice)
        odstrani("another file.avi", kopija)
        self.assertEqual(2 * f2 + f3, sorted(kopija))

        for i in range(10):
            kopija = vrstice[:]
            shuffle(kopija)
            odstrani("ime dat.avi", kopija)
            self.assertEqual(10 * f1 + f3, sorted(kopija))

        kopija = sorted(vrstice)
        odstrani("ime dat.avi", kopija)
        self.assertEqual(10 * f1 + f3, sorted(kopija))

        for i in range(10):
            kopija = vrstice[:]
            shuffle(kopija)
            odstrani("some other.avi", kopija)
            self.assertEqual(10 * f1 + 2 * f2, sorted(kopija))

        kopija = sorted(vrstice)
        odstrani("some other.avi", kopija)
        self.assertEqual(10 * f1 + 2 * f2, sorted(kopija))

        kopija = vrstice[:]
        odstrani("no such file.avi", kopija)
        self.assertEqual(10 * f1 + 2 * f2 + f3, sorted(kopija))


class TestDodatna(unittest.TestCase):
    def test_skupna_dolzina(self):
        vrstice = [
            "10/16/2020 ime dat.avi 1",
            "10/14/2020 ime dat.avi   2",
            "5/16/2020   ime dat.avi 4",
            "12/31/2018   ime dat.avi 8",
            "10/16/2020 some other.avi 16",
            "10/18/2020 another file.avi 32",
            "10/18/2018 another file.avi 64",
        ]
        for i in range(10):
            shuffle(vrstice)
            self.assertEqual(1 + 16 + 32, skupna_dolzina(vrstice))

        vrstice = [
            "10/14/2020 ime dat.avi   1",
            "5/16/2020   ime dat.avi 2",
            "10/16/2020 ime dat.avi 4",
            "12/31/2018   ime dat.avi 8",
            "10/16/2020 some other.avi 16",
            "10/18/2020 another file.avi 32",
            "10/18/2018 another file.avi 64",
        ]
        for i in range(10):
            shuffle(vrstice)
            self.assertEqual(4 + 16 + 32, skupna_dolzina(vrstice))


if __name__ == "__main__":
    unittest.main()
