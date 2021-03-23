import unittest

class TestOpravljivka(unittest.TestCase):
    def setUp(self):
        self.besedilo = '''Na vratih sta se prva pojavila Ana in Peter, menda
        "slučajno". Peter se je sicer več vrtel okrog Nives. Kasneje sta Ana in
        Peter skupaj sedela na klopci, vendar je bil zraven tudi Benjamin.
        Benjamin in Ana sta skupaj pila čaj. Peter in Tina sta tudi pila čaj.
        Peter in Ana pravzaprav tisti večer sploh nista bila več skupaj. Nives
        in Peter pa. Ja, Nives in Peter. Tina je bila kasneje ob ribniku takrat
        kot Benjamin, le na drugi strani. Sicer pa je Tina prejšnji teden rekla
        Nives, da ima Benjamin lep čop. Benjamin definitivno nima lepega čopa.
        Tone ga ima. Ampak Tone hodi z Nives. Kura. Ana in Tone bi bila za
        skupaj. Ne pa Tone in Nives.'''

    def test_imena(self):
        self.assertEqual(['Na', 'Ana', 'Peter'], poisci_imena('Na vratih sta se prva pojavila Ana in Peter, menda "slučajno".'))
        self.assertEqual([], poisci_imena(''))
        self.assertEqual(['Ana'], poisci_imena('Ana banana.'))
        self.assertEqual(['Ana'], poisci_imena('Ana, banana.'))
        self.assertEqual(['Ana', 'Ana'], poisci_imena('Ana prva in Ana druga.'))
        self.assertEqual(['Ana', 'Berta'], poisci_imena('Ana, Berta in cilka.'))
        self.assertEqual([], poisci_imena('ana, berta in cilka.'))
        self.assertEqual(['Tone', 'Ampak', 'Tone', 'Nives', 'Kura', 'Ana', 'Tone'], poisci_imena('Tone ga ima. Ampak Tone hodi z Nives, Kura, Ana in Tone bi bila za skupaj.'))
        self.assertTrue(len(poisci_imena("PETER in ANA sta še tu.")) in [0,2])

    def test_poisci_pare(self):
        self.assertEqual([['Ana', 'Peter']], poisci_pare('Na vratih sta se prva pojavila Ana in Peter, menda "slučajno".'))
        self.assertEqual([], poisci_pare(''))
        self.assertEqual([['A', 'B']], poisci_pare('A in B.'))
        self.assertEqual([['A', 'B']], poisci_pare('B in A.'))
        self.assertEqual([['B', 'C']], poisci_pare('A in B in C.'))
        self.assertEqual([], poisci_pare('A . B.'))
        self.assertEqual([], poisci_pare('A B C D.'))
        self.assertEqual([['A', 'A']], poisci_pare('A in A.'))
        self.assertEqual([['A', 'B'], ['B', 'C'], ['A', 'B']], poisci_pare('A in B. A in B in C. A. A in B in C in D. B in A.'))
        self.assertEqual([['Ana', 'Peter'], ['Nives', 'Peter'], ['Ana', 'Benjamin'], ['Peter', 'Tina'], ['Ana', 'Peter'], ['Nives', 'Peter'], ['Nives', 'Peter'], ['Benjamin', 'Tina'], ['Nives', 'Tone'], ['Ana', 'Tone'], ['Nives', 'Tone']], poisci_pare(self.besedilo))

    def test_prestej_pare(self):
        self.assertCountEqual([], prestej_pare(''))
        self.assertCountEqual([], prestej_pare('A in B in C in D.'))
        self.assertCountEqual([(1, ['A', 'B'])], prestej_pare('A in B.'))
        self.assertCountEqual([(1, ['B', 'C'])], prestej_pare('A in B in C.'))
        self.assertCountEqual([(2, ['A', 'B'])], prestej_pare('A in B. B in A.'))
        self.assertCountEqual([(1, ['A', 'B']), (1, ['B', 'C'])], prestej_pare('A in B. B in C.'))
        self.assertCountEqual([(2, ['A', 'B']), (1, ['B', 'C'])], prestej_pare('A in B. B in C. B in A.'))
        self.assertCountEqual([(2, ['Ana', 'Peter']), (3, ['Nives', 'Peter']), (1, ['Ana', 'Benjamin']), (1, ['Peter', 'Tina']), (1, ['Benjamin', 'Tina']), (2, ['Nives', 'Tone']), (1, ['Ana', 'Tone'])], prestej_pare(self.besedilo))

    def test_razporedi(self):
        self.assertEqual([], razporedi(''))
        self.assertEqual([['A', 'B']], razporedi('A B.'))
        self.assertEqual([['A', 'B']], razporedi('B A.'))
        self.assertEqual([['A', 'B']], razporedi('A B. B A.'))
        self.assertEqual([['A', 'B']], razporedi('A C. A B. B A.'))
        self.assertEqual([['A', 'C']], razporedi('A C. A B. A C. B A. A C.'))
        self.assertEqual([['A', 'B']], razporedi('A C. A B. B A. B A. B C. B C.'))
        self.assertEqual([['A', 'B'], ['C', 'D']], razporedi('A B. C D. A B.'))
        self.assertEqual([['A', 'B'], ['C', 'D']], razporedi('A B. A B. A B. C D. C D. A E.'))
        self.assertEqual([['A', 'B'], ['C', 'D']], razporedi('A B. A B. A B. C D. C D. A D.'))
        self.assertEqual([['A', 'B'], ['C', 'D'], ['E', 'F']], razporedi('A B. A B. A B. A B. C D. C D. C D. E F. E C. E C.'))
        self.assertEqual([['Nives', 'Peter'], ['Benjamin', 'Tina'], ['Ana', 'Tone']], razporedi(self.besedilo + 'Nives Peter. Nives Peter. Nives Peter. Nives Peter. Ana Peter. Ana Peter. Ana Peter. Ana Peter. Nives Tone. Nives Tone. Nives Tone. Peter Tina. Peter Tina. Peter Tina. Ana Tone. Benjamin Tina. Benjamin Tina.'))

if __name__ == '__main__':
    unittest.main(verbosity=2)
