import unittest

class TestWordDict(unittest.TestCase):
    def setUp(self):
        # Pred vsakim testom ustvarimo tri objekte razreda WordDict.
        self.d1 = WordDict([])
        self.d2 = WordDict(
            [('i have', 'Imam'),
            ('He Has', 'ima'),
            ('sHE hAS', 'ima')])
        self.d3 = WordDict(
            [('pRime', [2, 3, 5]),
             ('EVEN', [2, 4, 6]),
             ('Odd', [1, 3, 5]),
             ('Pi', 3.14),
             ('E', 2.71828)])

    def test_keys(self):
        self.assertCountEqual(self.d1.keys(), [])
        self.assertCountEqual(self.d2.keys(),
            ['i have', 'He Has', 'sHE hAS'])
        self.assertCountEqual(self.d3.keys(),
            ['pRime', 'EVEN', 'Odd', 'Pi', 'E'])

    def test_values(self):
        self.assertCountEqual(self.d1.values(), [])
        self.assertCountEqual(self.d2.values(),
            ['Imam', 'ima', 'ima'])
        self.assertCountEqual(self.d3.values(),
            [[2, 3, 5], [2, 4, 6], [1, 3, 5], 3.14, 2.71828])

    def test_items(self):
        self.assertCountEqual(self.d1.items(), [])
        self.assertCountEqual(self.d2.items(),
            [('i have', 'Imam'), ('sHE hAS', 'ima'), ('He Has', 'ima')])
        self.assertCountEqual(self.d3.items(),
            [('pRime', [2, 3, 5]),
            ('EVEN', [2, 4, 6]),
            ('Pi', 3.14),
            ('Odd', [1, 3, 5]),
            ('E', 2.71828)])

    def test_getitem(self):
        self.assertEqual(self.d2['I HAVE'], 'Imam')
        self.assertEqual(self.d3['PRIme'], [2, 3, 5])
        self.assertEqual(self.d3['eVeN'], [2, 4, 6])
        self.assertEqual(self.d3['PI'], 3.14)
        self.assertEqual(self.d3['pi'], 3.14)
        self.assertEqual(self.d3['Pi'], 3.14)

    def test_setitem(self):
        self.d1['C++'] = 'Stroustrup'
        self.d1['Go'] = 'Pike'
        self.assertCountEqual(self.d1.items(),
            [('C++', 'Stroustrup'), ('Go', 'Pike')])
        self.d1['GO'] = 'Thompson'
        self.assertCountEqual(self.d1.items(),
            [('C++', 'Stroustrup'), ('GO', 'Thompson')])
        self.d1['go'] += ', Pike'
        self.assertCountEqual(self.d1.items(),
            [('C++', 'Stroustrup'), ('go', 'Thompson, Pike')])

    def test_len(self):
        self.assertEqual(len(self.d1), 0)
        self.assertEqual(len(self.d2), 3)
        self.assertEqual(len(self.d3), 5)
        self.assertEqual(len(WordDict([('A', 1), ('a', 1)])), 1)

    def test_all(self):
        italian = WordDict([('hvala', 'grazie')])

        self.assertEqual(len(italian), 1)
        italian['nasvIdenje'] = 'Arrivederci'
        italian['IN'] = 'e'
        self.assertEqual(len(italian), 3)

        italian['NASVIDENJE'] = 'arrivederci'
        self.assertEqual(len(italian), 3)

        it = []
        for word in 'nasvidenje in hvala'.split():
            it.append(italian[word])
        self.assertEqual(' '.join(it), 'arrivederci e grazie')

        self.assertCountEqual(italian.items(),
            [('hvala', 'grazie'), ('IN', 'e'), ('NASVIDENJE', 'arrivederci')])

if __name__ == '__main__':
    unittest.main(verbosity=2)
