


import unittest

class Test06(unittest.TestCase):
    def test_slovar_besed(self):
        self.assertEqual(
            {"stavek": 0, "ki": 1, "to": 2, "ni": 3, "ker": 4, "kar": 5},
            slovar_besed("stavek ki to ni ker stavek ni kar to ni")
        )
        self.assertEqual({"bla": 0}, slovar_besed("bla bla bla"))

    def test_stisni_besedilo(self):
        self.assertEqual(
            [0, 1, 2, 3, 4, 0, 3, 5, 2, 3],
            stisni_besedilo("stavek ki to ni ker stavek ni kar to ni",
                            {"ni": 3, "ker": 4, "kar": 5, "stavek": 0, "ki": 1, "to": 2})
        )
        self.assertEqual(
            [6, 1, 2, 3, 4, 6, 3, 5, 2, 3],
            stisni_besedilo("stavek ki to ni ker stavek ni kar to ni",
                            {"beseda": 0, "ki": 1, "to": 2, "ni": 3, "ker": 4, "kar": 5, "stavek": 6})
        )


class Test07(unittest.TestCase):
    def test_obrni_slovar(self):
        self.assertEqual(
            ["stavek", "ki", "to", "ni", "ker", "kar"],
            obrni_slovar({"ni": 3, "ker": 4, "kar": 5, "stavek": 0, "ki": 1, "to": 2})
        )
        self.assertEqual(["bla"], obrni_slovar({"bla": 0}))
        self.assertEqual(["ena", "dva", "tri"],
                         obrni_slovar({"dva": 1, "ena": 0, "tri": 2}))

    def test_raztegni_besedilo(self):
        self.assertEqual(
            "stavek ki to ni ker stavek ni kar to ni",
            raztegni_besedilo([0, 1, 2, 3, 4, 0, 3, 5, 2, 3],
                            {"ni": 3, "ker": 4, "kar": 5, "stavek": 0, "ki": 1, "to": 2})
        )
        self.assertEqual(
            "stavek ki to ni ker stavek ni kar to ni",
            raztegni_besedilo([6, 1, 2, 3, 4, 6, 3, 5, 2, 3],
                            {"beseda": 0, "ki": 1, "to": 2, "ni": 3, "ker": 4, "kar": 5, "stavek": 6})
        )


class Test08(unittest.TestCase):
    def test_razbij_besedilo(self):
        self.assertEqual(
            ["Stavek", " ", "-", " ", "čudna", " ", "reč", ",", " ", "ti", " ", "stavki", "!"],
            razbij_besedilo("Stavek - čudna reč, ti stavki!")
        )
        self.assertEqual(
            ['ASF', '!', ' ', ' ', '(', 'BFO', '#', '!', ')', ' ', '(', 'M', '=', 'M', ')'],
            razbij_besedilo("ASF!  (BFO#!) (M=M)")
        )


class Test09(unittest.TestCase):
    def test_stisni_pravo_besedilo(self):
        self.assertEqual(
            ([0,  1,  2,  1,  3,  1,  4,  1,  5,  1,  6,  1,  7,  1,  8,  1,  9,  1,  10,  11,  1,  12,  1,  5,  1,  9,  1,  13,  1,  14,  1,  15,  1,  16,  1,  17,  11,  1,  18,  1,  19,  1,  5,  1,  20,  1,  21,  1,  22,  1,  14,  1,  23,  1,  24,  25,  1,  26,  1,  27,  1,  28,  1,  21,  1,  29,  11,  1,  30,  1,  31,  1,  5,  1,  32,  1,  21,  1,  33,  1,  34,  1,  35,  1,  5,  1,  21,  1,  36,  1,  37,  1,  38,  1,  39,  1,  40,  25,  1,  41,  1,  42,  1,  43,  1,  5,  1,  44,  1,  45,  11],
             {' ': 1, ',': 25, '.': 11, 'Glava': 30, 'Kot': 0, 'Modrinjak': 7, 'Njegov': 18, 'Nosil': 12, 'bil': 20, 'bila': 32, 'druga': 39, 'dvema': 15, 'gumbi': 28, 'hlače': 13, 'hlačnicama': 17, 'in': 34, 'je': 5, 'jo': 43, 'kadar': 41, 'ker': 26, 'koli': 42, 'kot': 37, 'ljubil': 8, 'možje': 4, 'mu': 31, 'obsijala': 44, 'odpadli': 29, 'plešasta': 33, 'preproste': 9, 'preprostima': 16, 'preprosto': 21, 'profesor': 6, 'reč': 40, 'reči': 10, 'se': 35, 'so': 27, 'spet': 22, 'suknjič': 19, 'svetila': 36, 'svetloba': 45, 'varnostnimi': 23, 'veliki': 3, 'vsaka': 38, 'vsi': 2, 'z': 14, 'zaponkami': 24}),
            stisni_pravo_besedilo("Kot vsi veliki možje je profesor Modrinjak ljubil preproste reči. Nosil je preproste hlače z dvema preprostima hlačnicama. Njegov suknjič je bil preprosto spet z varnostnimi zaponkami, ker so gumbi preprosto odpadli. Glava mu je bila preprosto plešasta in se je preprosto svetila kot vsaka druga reč, kadar koli jo je obsijala svetloba.")
        )
        self.assertEqual(
            ([0, 1, 2, 1, 3, 4, 1, 5, 1, 6, 1, 7, 1, 6, 1, 2, 8],
             {'To': 0, ' ': 1, 'je': 2, 'stavek': 3, ',': 4, 'ker': 5, '-': 6, 'očitno': 7, '.': 8}),
            stisni_pravo_besedilo("To je stavek, ker - očitno - je.")
        )

    def test_raztegni_pravo_besedilo(self):
        self.assertEqual(
            "To je stavek, ker - očitno - je.",
            raztegni_pravo_besedilo(
                [0, 1, 2, 1, 3, 4, 1, 5, 1, 6, 1, 7, 1, 6, 1, 2, 8],
                {'To': 0, ' ': 1, 'je': 2, 'stavek': 3, ',': 4, 'ker': 5,
                 '-': 6, 'očitno': 7, '.': 8})
        )
        self.assertEqual(
            "Kot vsi veliki možje je profesor Modrinjak ljubil preproste reči. Nosil je preproste hlače z dvema preprostima hlačnicama. Njegov suknjič je bil preprosto spet z varnostnimi zaponkami, ker so gumbi preprosto odpadli. Glava mu je bila preprosto plešasta in se je preprosto svetila kot vsaka druga reč, kadar koli jo je obsijala svetloba.",
            raztegni_pravo_besedilo(
                [0, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10, 11,
                 1, 12, 1, 5, 1, 9, 1, 13, 1, 14, 1, 15, 1, 16, 1, 17, 11, 1,
                 18, 1, 19, 1, 5, 1, 20, 1, 21, 1, 22, 1, 14, 1, 23, 1, 24, 25,
                 1, 26, 1, 27, 1, 28, 1, 21, 1, 29, 11, 1, 30, 1, 31, 1, 5, 1,
                 32, 1, 21, 1, 33, 1, 34, 1, 35, 1, 5, 1, 21, 1, 36, 1, 37, 1,
                 38, 1, 39, 1, 40, 25, 1, 41, 1, 42, 1, 43, 1, 5, 1, 44, 1, 45,
                 11],
                {' ': 1, ',': 25, '.': 11, 'Glava': 30, 'Kot': 0,
                 'Modrinjak': 7, 'Njegov': 18, 'Nosil': 12, 'bil': 20,
                 'bila': 32, 'druga': 39, 'dvema': 15, 'gumbi': 28,
                 'hlače': 13, 'hlačnicama': 17, 'in': 34, 'je': 5, 'jo': 43,
                 'kadar': 41, 'ker': 26, 'koli': 42, 'kot': 37, 'ljubil': 8,
                 'možje': 4, 'mu': 31, 'obsijala': 44, 'odpadli': 29,
                 'plešasta': 33, 'preproste': 9, 'preprostima': 16,
                 'preprosto': 21, 'profesor': 6, 'reč': 40, 'reči': 10,
                 'se': 35, 'so': 27, 'spet': 22, 'suknjič': 19, 'svetila': 36,
                 'svetloba': 45, 'varnostnimi': 23, 'veliki': 3, 'vsaka': 38,
                 'vsi': 2, 'z': 14, 'zaponkami': 24}))


class Test10(unittest.TestCase):
    def test_poenostavi_slovar(self):
        self.assertEqual(
            {3: 2, 5: 3, 0: 0, 2: 1},
            poenostavi_slovar(
                {"ni": 3, "ker": 4, "kar": 5, "stavek": 0, "ki": 1, "to": 2},
                {"ni", "stavek", "to", "kar"})
        )

    def test_stisni_bolj(self):
        self.assertEqual(
            ([5, 0, 1, 2, 3, 5, 2, 4, 1, 2],
             {"ki": 0, "to": 1, "ni": 2, "ker": 3,
              "kar": 4, "stavek": 5}),
            stisni_bolj([6, 1, 2, 3, 4, 6, 3, 5, 2, 3],
                        {"beseda": 0, "ki": 1, "to": 2, "ni": 3, "ker": 4,
                         "kar": 5, "stavek": 6})
        )
        self.assertEqual(
            ([5, 0, 2, 1, 3, 5, 1, 4, 2, 1],
             {"ki": 0, "kar": 4, "stavek": 5, "to": 2, "ni": 1, "ker": 3,
              }),
            stisni_bolj([6, 1, 3, 2, 4, 6, 2, 5, 3, 2],
                        {"kar": 5, "stavek": 6, "beseda": 0, "ki": 1,
                         "to": 3, "ni": 2, "ker": 4,
                         })
        )


if __name__ == "__main__":
    unittest.main()

