import unittest

class TestIzvoz(unittest.TestCase):
    def test_preberi_podatke(self):
        self.assertIsNone(preberi_podatke(),
                          "Funkcija preberi podatke ne sme vračati ničesar")
        self.assertEqual(len(produkti), 449)
        self.assertEqual(len(drzave), 231)

        preberi_podatke()
        self.assertEqual(len(produkti), 449,
            "Večkratni klic funkcije preberi_podatke spremeni število produktov")
        self.assertEqual(len(drzave), 231,
            "Večkratni klic funkcije preberi_podatke spremeni število držav")

    def test_drzave(self):
        preberi_podatke()
        self.assertSetEqual(set(kaj_izvaza("Slovenia")),
            {'transport equipment', 'manufactured goods', 'chemicals', 'food', 'machinery'})
        self.assertSetEqual(set(kaj_izvaza("Bermuda")),
            {"pharmaceuticals"})
        self.assertSetEqual(set(kaj_izvaza("Gambia, The")),
            {'palm kernels', 'peanut products', 'cotton lint', 'fish'})

    def test_produkti(self):
        preberi_podatke()
        self.assertSetEqual(set(kdo_izvaza("food")),
            {'Eritrea', 'Italy', 'Slovenia', 'Egypt', 'Guam', 'Saint Kitts and Nevis', 'Macedonia', 'United Kingdom', 'Lesotho', 'Antigua and Barbuda', 'Greece', 'Iraq', 'Poland'})
        self.assertSetEqual(set(kdo_izvaza("sand")),
            {'British Virgin Islands'})

    def test_najpodobnejsi(self):
        preberi_podatke()
        self.assertListEqual(najpodobnejsi("Slovenia"),
            ['Croatia', 'Czech Republic', 'Greece', 'Poland', 'United Kingdom'])
        self.assertListEqual(najpodobnejsi("France"),
            ['Austria', 'Bulgaria', 'European Union', 'India', 'Lithuania', 'Macedonia', 'Slovakia'])
        self.assertListEqual(najpodobnejsi("Gibraltar"),
            ['Cayman Islands', 'Greece', 'Mexico', 'Slovenia', 'United Kingdom'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
