
import unittest
import warnings
import random
import string
from operator import add
from functools import reduce

class PuzzleTestCase(unittest.TestCase):
    muc = r"""
         /\_/\
    ____/ o o \
  /~____  =ø= /
 (______)__m_m)"""

    kosi_muca = [
        [('wJMY', 'w  Y', '2  T', 'Fnyq'), ('YTPO', 'Y  O', 'T  v', 'q625'),
         ('OVfe', 'O  e', 'v__U', '5Yjb'), ('e2k9', 'e  9', 'U__J', 'bmq8'),
         ('9J6c', '9 /c', 'J/ 3', '8v2H'), ('cRH5', 'c\\_5', '3o m', 'H27Q'),
         ('5kC7', '5/\\7', 'mo m', 'QRbK'), ('79jc', '7  c', 'm\\ x', 'K9ZK')],
        [('Fnyq', 'F  q', '8 (z', '4MJn'), ('q625', 'q/~5', 'z__8', 'nc1o'),
         ('5Yjb', '5__b', '8__O', 'oAXf'), ('bmq8', 'b__8', 'O__s', 'fyuX'),
         ('8v2H', '8  H', 's)_P', 'XH00'), ('H27Q', 'H=øQ', 'P_mh', '0Ew4'),
         ('QRbK', 'Q= K', 'h_mO', '41K4'), ('K9ZK', 'K/ K', 'O) a', '40YO')]
    ]

    krava = r"""
                                     /;    ;\
                                   __  \\____//
                                  /{_\_/   `'\____
                                  \___   (o)  (o  }
       _____________________________/          :--'
   ,-,'`@@@@@@@@       @@@@@@         \_    `__\
  ;:(  @@@@@@@@@        @@@             \___(o'o)
  :: )  @@@@          @@@@@@        ,'@@(  `===='
  :: : @@@@@:          @@@@         `@@@:
  :: \  @@@@@:       @@@@@@@)    (  '@@@'
  ;; /\      /`,    @@@@@@@@@\   :@@@@@)
  ::/  )    {_----------------:  :~`,~~;
 ;;'`; :   )                  :  / `; ;
;;;; : :   ;                  :  ;  ; :
`'`' / :  :                   :  :  : :
    )_ \__;      ";"          :_ ;  \_\       `,','
    :__\  \    * `,'*         \  \  :  \   *  8`;'*  *
        `^'     \ :/           `^'  `-^-'   \v/ :  \/
"""

    kosi_krave = [
        [('1b5HCW3', '1     3', 'y     K', 'y     4', 'D     n', 'G     o', 'wXak7Lf'), ('3Nar3Ot', '3     t', 'K     t', '4     y', 'n     V', 'o  ___A', 'fs8Ef8L'), ('tpVTC39', 't     9', 't     g', 'y     I', 'V     4', 'A_____2', 'L3HqdZB'), ('9IHJuv0', '9     0', 'g     Q', 'I     I', '4     E', '2_____c', 'BORyS4Y'), ('0FZXo7p', '0     p', 'Q     R', 'I     R', 'E     L', 'c_____S', 'YZ9jZIh'), ('pa8UE6z', 'p     z', 'R     o', 'R     p', 'L     O', 'S_____s', 'hEz4a2S'), ('z2fqiM0', 'z     0', 'o     S', 'p    /j', 'O    \\6', 's_____y', 'SAKQw9b'), ('0zyBXOF', '0  /; F', 'S__  \\o', 'j{_\\_/F', '6___  1', 'y_/   t', 'bWjos7X'), ('FgB5BpV', 'F   ;\\V', 'o\\____R', "F   `'z", '1 (o) q', 't     b', 'XJikjnl'), ('Vh3qiPx', 'V     x', 'R//   4', 'z\\____N', 'q (o  n', 'b  :--b', 'lOf1Uia'), ('xQcaqz2', 'x     2', '4     h', 'N     C', 'n}    j', "b'    w", 'ain6lCM')],
        [('wXak7Lf', 'w   ,-f', 'S  ;:(0', 'C  :: T', '7  :: r', 'z  :: 8', 'IjJSaDr'), ('fs8Ef8L', "f,'`@@L", '0  @@@4', 'T)  @@H', 'r: @@@x', '8\\  @@I', 'rFYzMBw'), ('L3HqdZB', 'L@@@@@B', '4@@@@@s', 'H@@   x', 'x@@:  S', 'I@@@: b', 'wGiN3QV'), ('BORyS4Y', 'B@    Y', 's@    6', 'x     4', 'S     u', 'b     1', 'VvRhZ9n'), ('YZ9jZIh', 'Y   @@h', '6    @o', '4  @@@5', 'u   @@b', '1 @@@@x', 'nuGacd3'), ('hEz4a2S', 'h@@@@ S', 'o@@   K', '5@@@  X', 'b@@   S', 'x@@@) n', '3xoqLX6'), ('SAKQw9b', 'S     b', 'K     M', 'X     o', 'S     2', 'n   ( j', '6r1GFJy'), ('bWjos7X', 'b   \\_X', 'M     v', "o ,'@@v", '2 `@@@Y', "j '@@@x", 'yQBi57m'), ('XJikjnl', 'X    `l', 'v\\___(H', 'v(  `=0', 'Y:    P', "x'    P", 'mvw9gEu'), ('lOf1Uia', 'l__\\  a', "Ho'o) N", "0===' i", 'P     O', 'P     u', 'uG1USjl'), ('ain6lCM', 'a     M', 'N     5', 'i     N', 'O     W', 'u     q', 'lUZd7RY')],
        [('IjJSaDr', 'I  ;; r', 'o  ::/i', "O ;;'`W", 'f;;;; g', "3`'`' N", 'lz3SKAF'), ('rFYzMBw', 'r/\\   w', 'i  )  s', 'W; :  s', 'g: :  7', 'N/ :  4', 'FYkvB0Q'), ('wGiN3QV', 'w   /`V', 's  {_-f', 's )   E', '7 ;   u', '4:    z', 'QuxLObj'), ('VvRhZ9n', 'V,    n', 'f-----l', 'E     G', 'u     e', 'z     i', 'jfT3GWN'), ('nuGacd3', 'n@@@@@3', 'l-----s', 'G     3', 'e     W', 'i     R', 'N9EwL5L'), ('3xoqLX6', '3@@@@\\6', 's-----y', '3     U', 'W     n', 'R     w', 'LxdVORG'), ('6r1GFJy', '6   :@y', 'y:  :~F', 'U:  / O', 'n:  ; d', 'w:  : b', 'Gg9mkCA'), ('yQBi57m', 'y@@@@)m', 'F`,~~;W', 'O`; ; H', 'd ; : H', 'b : : v', 'AWa0RHL'), ('mvw9gEu', 'm     u', 'W     p', 'H     p', 'H     W', 'v     l', 'LkJJ05O'), ('uG1USjl', 'u     l', 'p     D', 'p     k', 'W     k', 'l     v', 'OTRnBf8'), ('lUZd7RY', 'l     Y', 'D     B', 'k     g', 'k     J', 'v     5', '8wkVWz6')],
        [('lz3SKAF', 'l    )F', '7    :P', 'g     r', 'T     h', 'D     V', '3fK3wxo'), ('FYkvB0Q', 'F_ \\__Q', 'P__\\  D', 'r   `^I', 'h     O', 'V     q', 'o39uUq5'), ('QuxLObj', 'Q;    j', 'D\\    h', "I'    z", 'O     w', 'q     F', '5az8RAa'), ('jfT3GWN', 'j  ";"N', "h* `,'Q", 'z \\ :/j', 'w     D', 'F     p', 'aw5UE1d'), ('N9EwL5L', 'N     L', 'Q*    e', 'j     X', 'D     B', 'p     I', 'dcCiv7B'), ('LxdVORG', 'L     G', 'e     3', 'X     r', 'B     7', 'I     w', 'BR5j6k5'), ('Gg9mkCA', 'G:_ ; A', '3\\  \\ s', "r `^' I", '7     5', 'w     M', '50lp8bM'), ('AWa0RHL', 'A \\_\\ L', 's :  \\y', 'I `-^-f', '5     Y', 'M     c', 'MqwQktc'), ('LkJJ05O', 'L     O', 'y   * k', "f'   \\B", 'Y     m', 'c     w', 'cyDdgEP'), ('OTRnBf8', "O `,',8", "k 8`;'n", 'Bv/ : I', 'm     z', 'w     e', 'PLDFqTP'), ('8wkVWz6', "8'    6", 'n*  * M', 'I \\/  N', 'z     X', 'e     E', 'P8kRmOP')],
    ]

    kos = ("Qm55", "7 _H", "2o\R", "H3cc")

    def shuffled(self, kosi):
        kosi = reduce(add, kosi)
        random.shuffle(kosi)
        return kosi

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)


class Test06(PuzzleTestCase):
    def test_zrcaljen_vod(self):
        self.assertTupleEqual(("cba", "fed", "ihg"), zrcaljen_vod(("abc", "def", "ghi")))
        self.assertTupleEqual(("dcba", "gfed", "jihg", "mlkj"), zrcaljen_vod(("abcd", "defg", "ghij", "jklm")))
        self.assertTupleEqual(("55mQ", "H_ 7", r"R\o2", "cc3H"), zrcaljen_vod(self.kos))


        for n in (10, 50, random.randint(100, 200)):
            kos = [""] * n
            koz = [""] * n
            for i in range(n):
                for j in range(n):
                    c = random.choice(string.ascii_letters)
                    kos[i] += c
                    koz[i] = c + koz[i]
            self.assertTupleEqual(tuple(koz), zrcaljen_vod(tuple(kos)))

    def test_zrcaljen_navp(self):
        self.assertTupleEqual(("ghi", "def", "abc"), zrcaljen_navp(("abc", "def", "ghi")))
        self.assertTupleEqual(("jklm", "ghij", "defg", "abcd"), zrcaljen_navp(("abcd", "defg", "ghij", "jklm")))
        self.assertTupleEqual(("H3cc", "2o\R", "7 _H", "Qm55"), zrcaljen_navp(self.kos))

        for n in (10, 50, random.randint(100, 200)):
            kos = []
            koz = []
            for i in range(n):
                s = "".join(random.choice(string.ascii_letters) for _ in range(n))
                kos.append(s)
                koz.insert(0, s)
            self.assertTupleEqual(tuple(koz), zrcaljen_navp(tuple(kos)))

    def _obrnjena(self):
        for n in (10, 50, random.randint(100, 200)):
            kos = [""] * n
            koz = [""] * n
            for i in range(n):
                for j in range(n):
                    c = random.choice(string.ascii_letters)
                    koz[i] += c
                    kos[-j - 1] += c
        return tuple(kos), tuple(koz)

    def test_obrnjen(self):
        self.assertTupleEqual(("gda", "heb", "ifc"), obrnjen(("abc", "def", "ghi")))
        self.assertTupleEqual(("jgda", "kheb", "lifc", "mjgd"), obrnjen(("abcd", "defg", "ghij", "jklm")))
        self.assertTupleEqual(('H27Q', '3o m', 'c\\_5', 'cRH5'), obrnjen(self.kos))

        kos, koz = self._obrnjena()
        self.assertEqual(koz, obrnjen(kos))

    def test_obnjen_n(self):
        self.assertTupleEqual(("gda", "heb", "ifc"), obrnjen_n(("abc", "def", "ghi"), 1))
        self.assertTupleEqual(("gda", "heb", "ifc"), obrnjen_n(("abc", "def", "ghi"), 5))
        self.assertTupleEqual(("jgda", "kheb", "lifc", "mjgd"), obrnjen_n(("abcd", "defg", "ghij", "jklm"), 1))
        self.assertTupleEqual(("jgda", "kheb", "lifc", "mjgd"), obrnjen_n(("abcd", "defg", "ghij", "jklm"), 5))

        kos, koz = self._obrnjena()
        self.assertTupleEqual(koz, obrnjen_n(kos, 1))
        self.assertTupleEqual(kos, obrnjen_n(koz, 3))
        self.assertTupleEqual(koz, obrnjen_n(kos, 5))
        self.assertTupleEqual(kos, obrnjen_n(koz, 7))
        self.assertTupleEqual(koz, obrnjen_n(kos, 10000000000000001))
        self.assertTupleEqual(kos, obrnjen_n(koz, 10000000000000003))

    def test_stranice(self):
        """
        Koščka sta taka:

        abc   abcd
        def   defg
        ghi   ghij
              jklm"""
        self.assertEqual(
            ['Qm55', '5HRc', 'H3cc', 'Q72H', '55mQ', 'cRH5', 'cc3H', 'H27Q'],
            stranice(self.kos))

        self.assertEqual(
            ["abc", "cfi", "ghi", "adg", "cba", "ifc", "ihg", "gda"],
            stranice(("abc", "def", "ghi"))
        )

        self.assertEqual(
            ["abcd", "dgjm", "jklm", "adgj", "dcba", "mjgd", "mlkj", "jgda"],
            stranice(("abcd", "defg", "ghij", "jklm"))
        )

        for n in (10, 50, random.randint(100, 200)):
            kos = []
            levo = ""
            desno = ""
            for i in range(n):
                s = "".join(random.choice(string.ascii_letters) for _ in range(n))
                if i == 0:
                    gor = s
                levo += s[0]
                desno += s[-1]
                kos.append(s)
            kos = tuple(kos)
            self.assertEqual([gor, desno, s, levo,
                              gor[::-1], desno[::-1], s[::-1], levo[::-1]],
                             stranice(kos))

    def test_obrati(self):
        self.assertEqual(
            {('abc', 'def', 'ghi'),
             ('gda', 'heb', 'ifc'),
             ('ihg', 'fed', 'cba'),
             ('cfi', 'beh', 'adg'),
             ('ghi', 'def', 'abc'),
             ('adg', 'beh', 'cfi'),
             ('cba', 'fed', 'ihg'),
             ('ifc', 'heb', 'gda')},
            obrati(("abc", "def", "ghi")))

        self.assertEqual(
            {('55mQ', 'H_ 7', 'R\\o2', 'cc3H'),
             ('5HRc', '5_\\c', 'm o3', 'Q72H'),
             ('H27Q', '3o m', 'c\\_5', 'cRH5'),
             ('H3cc', '2o\\R', '7 _H', 'Qm55'),
             ('Q72H', 'm o3', '5_\\c', '5HRc'),
             ('Qm55', '7 _H', '2o\\R', 'H3cc'),
             ('cRH5', 'c\\_5', '3o m', 'H27Q'),
             ('cc3H', 'R\\o2', 'H_ 7', '55mQ')},
            obrati(self.kos))

class Test07(PuzzleTestCase):
    def test_preberi_datoteko(self):
        self.assertEqual(
            [('bmq8', 'b__8', 'O__s', 'fyuX'),
             ('Qm55', '7 _H', '2o\\R', 'H3cc'),
             ('cj97', 'c  7', 'x \\m', 'KZ9K'),
             ('KZ9K', 'K /K', 'a )O', 'OY04'),
             ('QRbK', 'Q= K', 'h_mO', '41K4'),
             ('8J99', 'q_ k', 'm_ 2', 'bUee'),
             ('ww2F', 'J  n', 'M  y', 'YYTq'),
             ('XH00', 's)_P', '8  H', '8v2H'),
             ('o855', 'A__Y', 'X__j', 'fObb'),
             ('qqzn', '6/_c', '2~_1', '558o'),
             ('Qm55', 'Ro/k', 'b \\C', 'Km77'),
             ('5vOO', 'Y_ V', 'j_ f', 'bUee'),
             ('YYTq', 'T  6', 'P  2', 'OOv5'),
             ('9J6c', '9 /c', 'J/ 3', '8v2H'),
             ('FF84', 'n  M', 'y (J', 'qqzn'),
             ('HHP0', '2=_E', '7ømw', 'QQh4')],
            preberi_datoteko("muc-puzzle.txt"))
        self.assertEqual(
            [('5az8RAa', 'q     F', 'O     w', "I'    z", 'D\\    h', 'Q;    j', 'QuxLObj'),
             ('MqwQktc', 'M     c', '5     Y', 'I `-^-f', 's :  \\y', 'A \\_\\ L', 'AWa0RHL'),
             ('YcEIQ00', 'Z_    F', '9_    Z', 'j_    X', 'Z_    o', 'I_    7', 'hSLRRpp'),
             ('11yyDGw', 'b     X', '5     a', 'H     k', 'C     7', 'W     L', '33K4nof'),
             ('by6jS00', 'W__{_ z', 'j/___ y', 'o _\\ /B', 's  _ ;X', '7  /\\ O', 'Xt1FoFF'),
             ('IjJSaDr', 'I  ;; r', 'o  ::/i', "O ;;'`W", 'f;;;; g', "3`'`' N", 'lz3SKAF'),
             ('mvw9gEu', 'm     u', 'W     p', 'H     p', 'H     W', 'v     l', 'LkJJ05O'),
             ('wXak7Lf', 'w   ,-f', 'S  ;:(0', 'C  :: T', '7  :: r', 'z  :: 8', 'IjJSaDr'),
             ('LHR0aWA', 'v : : b', 'H : ; d', 'H ; ;`O', 'W;~~,`F', 'm)@@@@y', 'm75iBQy'),
             ('fon4K33', 's     N', '8     a', 'E_    r', 'f_    3', '8_    O', 'LAVyttt'),
             ('yJFG1r6', 'y@:   6', 'F~:  :y', 'O /  :U', 'd ;  :n', 'b :  :w', 'ACkm9gG'),
             ('n9ZhRvV', 'n    ,V', 'l-----f', 'G     E', 'e     u', 'i     z', 'NWG3Tfj'),
             ('mxYvvXX', '7@@@ _7', '5@@@ \\s', "i@@'  o", "B'`,  j", 'Q     W', 'yj2oMbb'),
             ('z2fqiM0', 'z     0', 'o     S', 'p    /j', 'O    \\6', 's_____y', 'SAKQw9b'),
             ('VVRzqbl', 'h /\\  O', '3 /_( f', 'q  _o:1', 'i  _ -U', 'P  _ -i', 'xx4Nnba'),
             ('Q0BvkYF', '4  : /N', '7  : :g', 's  : ;W', 's  )  i', 'w   \\/r', 'wBMzYFr'),
             ('wIxH4LL', 'G@@@@@3', 'i@@@@@H', 'N@: @@q', '3:  @@d', 'Q   @@Z', 'VbSxsBB'),
             ('VQ3NiGw', 'V`/   w', 'f-_{  s', 'E   ) s', 'u   ; 7', 'z    :4', 'jbOLxuQ'),
             ('LLeXBIB', '5     7', 'L     v', 'w     i', 'E     C', '9 *   c', 'NNQjDpd'),
             ('OTRnBf8', "O `,',8", "k 8`;'n", 'Bv/ : I', 'm     z', 'w     e', 'PLDFqTP'),
             ('66yUnwG', 'X\\-   R', 'L@-   O', 'q@-   V', 'o@-   d', 'x@-   x', '33s3WRL'),
             ('S2a4zEh', 'S @@@@h', 'K   @@o', 'X  @@@5', 'S   @@b', 'n )@@@x', '6XLqox3'),
             ('jfT3GWN', 'j  ";"N', "h* `,'Q", 'z \\ :/j', 'w     D', 'F     p', 'aw5UE1d'),
             ('LkJJ05O', 'L     O', 'y   * k', "f'   \\B", 'Y     m', 'c     w', 'cyDdgEP'),
             ('Y4SyROB', 'Y    @B', '6    @s', '4     x', 'u     S', '1     b', 'n9ZhRvV'),
             ('BZdqH3L', '2_____A', '4     V', 'I     y', 'g     t', '9     t', '93CTVpt'),
             ('3fK3wxo', 'D     V', 'T     h', 'g     r', '7    :P', 'l    )F', 'lz3SKAF'),
             ('Q0BvkYF', 'Q__\\ _F', 'D  \\__P', 'I^`   r', 'O     h', 'q     V', '5qUu93o'),
             ('2zqacQx', '2     x', 'h     4', 'C     N', 'j    }n', "w    'b", 'MCl6nia'),
             ('Gg9mkCA', 'G:_ ; A', '3\\  \\ s', "r `^' I", '7     5', 'w     M', '50lp8bM'),
             ('3xb5ohh', 'd@@@@@I', 'c@@@ @Z', 'a@ @  j', 'G@    9', 'u     Z', 'n1u46YY'),
             ('8fBnRTO', 'v     l', 'k     W', 'k     p', 'D     p', 'l     u', 'ljSU1Gu'),
             ('yJFG1r6', 'j (   n', '2     S', 'o     X', 'M     K', 'b     S', 'b9wQKAS'),
             ('aaNiOul', 'i     j', "U )'  S", '1\\o=  U', "f_'=  1", 'O_o=  G', 'llH0PPu'),
             ('POmRk8P', 'E     e', 'X     z', 'N  /\\ I', 'M *  *n', "6    '8", '6zWVkw8'),
             ('BIBXeLL', 'R     x', '5     d', 'j     V', '6     O', 'k     R', '5w7r3GG'),
             ('YcEIQ00', '4_    v', 'S_    u', 'y_    J', 'R_    H', 'O_    I', 'B24Ig99'),
             ('rFYzMBw', '8\\  @@I', 'r: @@@x', 'T)  @@H', '0  @@@4', "f,'`@@L", 'fs8Ef8L'),
             ('lUZd7RY', 'u     q', 'O     W', 'i     N', 'N     5', 'a     M', 'ain6lCM'),
             ('mvw9gEu', "x'    P", 'Y:    P', 'v(  `=0', 'v\\___(H', 'X    `l', 'XJikjnl'),
             ('33s3WRL', 'd@-   5', 'c@-   L', 'a@-   w', 'G@-   E', 'u@-   9', 'nnlGeiN'),
             ('z6EU8ap', 'z     p', 'o     R', 'p     R', 'O     L', 's_____S', 'S2a4zEh'),
             ('lUZd7RY', 'l     Y', 'D     B', 'k     g', 'k     J', 'v     5', '8wkVWz6'),
             ('FgB5BpV', 'F   ;\\V', 'o\\____R', "F   `'z", '1 (o) q', 't     b', 'XJikjnl')],
             preberi_datoteko("krava-puzzle.txt"))

    def test_zbirka_stranic(self):
        self.assertEqual({
            'bmq8': {('8J99', 'q_ k', 'm_ 2', 'bUee'),
                     ('bmq8', 'b__8', 'O__s', 'fyuX')},
            '88sX': {('XH00', 's)_P', '8  H', '8v2H'),
                     ('bmq8', 'b__8', 'O__s', 'fyuX')},
            'fyuX': {('bmq8', 'b__8', 'O__s', 'fyuX')},
            'bbOf': {('o855', 'A__Y', 'X__j', 'fObb'),
                     ('bmq8', 'b__8', 'O__s', 'fyuX')},
            '8qmb': {('8J99', 'q_ k', 'm_ 2', 'bUee'),
                     ('bmq8', 'b__8', 'O__s', 'fyuX')},
            'Xs88': {('XH00', 's)_P', '8  H', '8v2H'),
                     ('bmq8', 'b__8', 'O__s', 'fyuX')},
            'Xuyf': {('bmq8', 'b__8', 'O__s', 'fyuX')},
            'fObb': {('o855', 'A__Y', 'X__j', 'fObb'),
                     ('bmq8', 'b__8', 'O__s', 'fyuX')},
            'Qm55': {('Qm55', 'Ro/k', 'b \\C', 'Km77'),
                     ('Qm55', '7 _H', '2o\\R', 'H3cc')},
            '5HRc': {('Qm55', '7 _H', '2o\\R', 'H3cc')},
            'H3cc': {('9J6c', '9 /c', 'J/ 3', '8v2H'),
                     ('Qm55', '7 _H', '2o\\R', 'H3cc')},
            'Q72H': {('HHP0', '2=_E', '7ømw', 'QQh4'),
                     ('Qm55', '7 _H', '2o\\R', 'H3cc')},
            '55mQ': {('Qm55', 'Ro/k', 'b \\C', 'Km77'),
                     ('Qm55', '7 _H', '2o\\R', 'H3cc')},
            'cRH5': {('Qm55', '7 _H', '2o\\R', 'H3cc')},
            'cc3H': {('9J6c', '9 /c', 'J/ 3', '8v2H'),
                     ('Qm55', '7 _H', '2o\\R', 'H3cc')},
            'H27Q': {('HHP0', '2=_E', '7ømw', 'QQh4'),
                     ('Qm55', '7 _H', '2o\\R', 'H3cc')},
            'cj97': {('cj97', 'c  7', 'x \\m', 'KZ9K')},
            '77mK': {('cj97', 'c  7', 'x \\m', 'KZ9K'),
                     ('Qm55', 'Ro/k', 'b \\C', 'Km77')},
            'KZ9K': {('cj97', 'c  7', 'x \\m', 'KZ9K'),
                     ('KZ9K', 'K /K', 'a )O', 'OY04')},
            'ccxK': {('cj97', 'c  7', 'x \\m', 'KZ9K')},
            '79jc': {('cj97', 'c  7', 'x \\m', 'KZ9K')},
            'Km77': {('cj97', 'c  7', 'x \\m', 'KZ9K'),
                     ('Qm55', 'Ro/k', 'b \\C', 'Km77')},
            'K9ZK': {('cj97', 'c  7', 'x \\m', 'KZ9K'),
                     ('KZ9K', 'K /K', 'a )O', 'OY04')},
            'Kxcc': {('cj97', 'c  7', 'x \\m', 'KZ9K')},
            'KKO4': {('QRbK', 'Q= K', 'h_mO', '41K4'),
                     ('KZ9K', 'K /K', 'a )O', 'OY04')},
            'OY04': {('KZ9K', 'K /K', 'a )O', 'OY04')},
            'KKaO': {('KZ9K', 'K /K', 'a )O', 'OY04')},
            '4OKK': {('QRbK', 'Q= K', 'h_mO', '41K4'),
                     ('KZ9K', 'K /K', 'a )O', 'OY04')},
            '40YO': {('KZ9K', 'K /K', 'a )O', 'OY04')},
            'OaKK': {('KZ9K', 'K /K', 'a )O', 'OY04')},
            'QRbK': {('QRbK', 'Q= K', 'h_mO', '41K4'),
                     ('Qm55', 'Ro/k', 'b \\C', 'Km77')},
            '41K4': {('QRbK', 'Q= K', 'h_mO', '41K4')},
            'QQh4': {('QRbK', 'Q= K', 'h_mO', '41K4'),
                     ('HHP0', '2=_E', '7ømw', 'QQh4')},
            'KbRQ': {('QRbK', 'Q= K', 'h_mO', '41K4'),
                     ('Qm55', 'Ro/k', 'b \\C', 'Km77')},
            '4K14': {('QRbK', 'Q= K', 'h_mO', '41K4')},
            '4hQQ': {('QRbK', 'Q= K', 'h_mO', '41K4'),
                     ('HHP0', '2=_E', '7ømw', 'QQh4')},
            '8J99': {('9J6c', '9 /c', 'J/ 3', '8v2H'),
                     ('8J99', 'q_ k', 'm_ 2', 'bUee')},
            '9k2e': {('8J99', 'q_ k', 'm_ 2', 'bUee')},
            'bUee': {('8J99', 'q_ k', 'm_ 2', 'bUee'),
                     ('5vOO', 'Y_ V', 'j_ f', 'bUee')},
            '99J8': {('9J6c', '9 /c', 'J/ 3', '8v2H'),
                     ('8J99', 'q_ k', 'm_ 2', 'bUee')},
            'e2k9': {('8J99', 'q_ k', 'm_ 2', 'bUee')},
            'eeUb': {('8J99', 'q_ k', 'm_ 2', 'bUee'),
                     ('5vOO', 'Y_ V', 'j_ f', 'bUee')},
            'ww2F': {('ww2F', 'J  n', 'M  y', 'YYTq')},
            'Fnyq': {('ww2F', 'J  n', 'M  y', 'YYTq'),
                     ('FF84', 'n  M', 'y (J', 'qqzn')},
            'YYTq': {('YYTq', 'T  6', 'P  2', 'OOv5'),
                     ('ww2F', 'J  n', 'M  y', 'YYTq')},
            'wJMY': {('ww2F', 'J  n', 'M  y', 'YYTq')},
            'F2ww': {('ww2F', 'J  n', 'M  y', 'YYTq')},
            'qynF': {('ww2F', 'J  n', 'M  y', 'YYTq'),
                     ('FF84', 'n  M', 'y (J', 'qqzn')},
            'qTYY': {('YYTq', 'T  6', 'P  2', 'OOv5'),
                     ('ww2F', 'J  n', 'M  y', 'YYTq')},
            'YMJw': {('ww2F', 'J  n', 'M  y', 'YYTq')},
            'XH00': {('XH00', 's)_P', '8  H', '8v2H')},
            '0PHH': {('HHP0', '2=_E', '7ømw', 'QQh4'),
                     ('XH00', 's)_P', '8  H', '8v2H')},
            '8v2H': {('9J6c', '9 /c', 'J/ 3', '8v2H'),
                     ('XH00', 's)_P', '8  H', '8v2H')},
            '00HX': {('XH00', 's)_P', '8  H', '8v2H')},
            'HHP0': {('HHP0', '2=_E', '7ømw', 'QQh4'),
                     ('XH00', 's)_P', '8  H', '8v2H')},
            'H2v8': {('9J6c', '9 /c', 'J/ 3', '8v2H'),
                     ('XH00', 's)_P', '8  H', '8v2H')},
            'o855': {('o855', 'A__Y', 'X__j', 'fObb'),
                     ('qqzn', '6/_c', '2~_1', '558o')},
            '5Yjb': {('o855', 'A__Y', 'X__j', 'fObb'),
                     ('5vOO', 'Y_ V', 'j_ f', 'bUee')},
            'oAXf': {('o855', 'A__Y', 'X__j', 'fObb')},
            '558o': {('o855', 'A__Y', 'X__j', 'fObb'),
                     ('qqzn', '6/_c', '2~_1', '558o')},
            'bjY5': {('o855', 'A__Y', 'X__j', 'fObb'),
                     ('5vOO', 'Y_ V', 'j_ f', 'bUee')},
            'fXAo': {('o855', 'A__Y', 'X__j', 'fObb')},
            'qqzn': {('qqzn', '6/_c', '2~_1', '558o'),
                     ('FF84', 'n  M', 'y (J', 'qqzn')},
            'nc1o': {('qqzn', '6/_c', '2~_1', '558o')},
            'q625': {('YYTq', 'T  6', 'P  2', 'OOv5'),
                     ('qqzn', '6/_c', '2~_1', '558o')},
            'nzqq': {('qqzn', '6/_c', '2~_1', '558o'),
                     ('FF84', 'n  M', 'y (J', 'qqzn')},
            'o1cn': {('qqzn', '6/_c', '2~_1', '558o')},
            '526q': {('YYTq', 'T  6', 'P  2', 'OOv5'),
                     ('qqzn', '6/_c', '2~_1', '558o')},
            '5kC7': {('Qm55', 'Ro/k', 'b \\C', 'Km77')},
            '7Ck5': {('Qm55', 'Ro/k', 'b \\C', 'Km77')},
            '5vOO': {('YYTq', 'T  6', 'P  2', 'OOv5'),
                     ('5vOO', 'Y_ V', 'j_ f', 'bUee')},
            'OVfe': {('5vOO', 'Y_ V', 'j_ f', 'bUee')},
            'OOv5': {('YYTq', 'T  6', 'P  2', 'OOv5'),
                     ('5vOO', 'Y_ V', 'j_ f', 'bUee')},
            'efVO': {('5vOO', 'Y_ V', 'j_ f', 'bUee')},
            'YTPO': {('YYTq', 'T  6', 'P  2', 'OOv5')},
            'OPTY': {('YYTq', 'T  6', 'P  2', 'OOv5')},
            '9J6c': {('9J6c', '9 /c', 'J/ 3', '8v2H')},
            'c6J9': {('9J6c', '9 /c', 'J/ 3', '8v2H')},
            'FF84': {('FF84', 'n  M', 'y (J', 'qqzn')},
            '4MJn': {('FF84', 'n  M', 'y (J', 'qqzn')},
            '48FF': {('FF84', 'n  M', 'y (J', 'qqzn')},
            'nJM4': {('FF84', 'n  M', 'y (J', 'qqzn')},
            '0Ew4': {('HHP0', '2=_E', '7ømw', 'QQh4')},
            '4wE0': {('HHP0', '2=_E', '7ømw', 'QQh4')}},
        zbirka_stranic(preberi_datoteko("muc-puzzle.txt")))


class Test08(PuzzleTestCase):
    def test_kotni(self):
        for kosi in (self.kosi_muca, self.kosi_krave):
            self.assertEqual(
                {kosi[0][0], kosi[0][-1], kosi[-1][0], kosi[-1][-1]},
                kotni(self.shuffled(kosi))
            )

    def test_robni(self):
        for kosi in (self.kosi_muca, self.kosi_krave):
            self.assertEqual(
                set(kosi[0][1:-1])
                | {v[0] for v in kosi[1:-1]}
                | {v[-1] for v in kosi[1:-1]}
                | set(kosi[-1][1:-1]),
                robni(self.shuffled(kosi))
            )

    def test_prvi_kot(self):
        for kosi, prvi in ((self.kosi_muca, ('79jc', '7  c', 'm\\ x', 'K9ZK')),
                           (self.kosi_krave, ('1b5HCW3', '1     3', 'y     K', 'y     4', 'D     n', 'G     o', 'wXak7Lf'))):
            self.assertTupleEqual(prvi, prvi_kot(self.shuffled(kosi)))


class Test09(PuzzleTestCase):
    def test_preobrni(self):
        for kosi in (self.kosi_muca, self.kosi_krave):
            po_stranicah = zbirka_stranic(self.shuffled(kosi))
            for pred, ta in zip(kosi[0], kosi[0][1:]):
                levo = stranice(pred)[1]
                for kos2 in obrati(ta):
                    self.assertEqual(ta, preobrni(kos2, levo, 1, po_stranicah))
                    kos2 = zrcaljen_vod(kos2)
                    self.assertEqual(ta, preobrni(kos2, levo, 1, po_stranicah))

            for nad, pod in zip(kosi, kosi[1:]):
                gor = stranice(nad[0])[2]
                for kos2 in obrati(pod[0]):
                    self.assertEqual(pod[0], preobrni(kos2, 1, gor, po_stranicah))
                    kos2 = zrcaljen_vod(kos2)
                    self.assertEqual(pod[0], preobrni(kos2, 1, gor, po_stranicah))

                for pred, ta, nad in zip(pod, pod[1:], nad[1:]):
                    levo = stranice(pred)[1]
                    gor = stranice(nad)[2]
                    for kos2 in obrati(ta):
                        self.assertEqual(ta, preobrni(kos2, levo, gor, po_stranicah))
                        kos2 = zrcaljen_vod(kos2)
                        self.assertEqual(ta, preobrni(kos2, levo, gor, po_stranicah))

            kos = kosi[0][0]
            kos2 = obrnjen(kos)
            gor, _1, _2, levo, *_ = stranice(kos2)
            self.assertEqual(kos2, preobrni(kos, levo, gor, po_stranicah))


    def test_vzemi_kos(self):
        for kosi, ime, kot in ((self.kosi_muca, "muc", ("ww2F", "J  n", "M  y", "YYTq")),
                               (self.kosi_krave, "krava", ("11yyDGw", "b     X",  "5     a",  "H     k",  "C     7",  "W     L", "33K4nof"))):
            kosi_dat = preberi_datoteko(ime + "-puzzle.txt")
            po_stranicah = zbirka_stranic(kosi_dat)
            uporabljeni = {kot}
            for pred, ta in zip(kosi[0], kosi[0][1:]):
                levo = stranice(pred)[1]
                self.assertEqual(ta, vzemi_kos(levo, 1, po_stranicah, uporabljeni))

            for nad, pod in zip(kosi, kosi[1:]):
                gor = stranice(nad[0])[2]
                self.assertEqual(pod[0], vzemi_kos(1, gor, po_stranicah, uporabljeni))

                for pred, ta, nad in zip(pod, pod[1:], nad[1:]):
                    levo = stranice(pred)[1]
                    gor = stranice(nad)[2]
                    self.assertEqual(ta, vzemi_kos(levo, gor, po_stranicah, uporabljeni))

class Test10(PuzzleTestCase):
    def assertImgEqual(self, expected, actual):
        def strip_fsp(s):
            return "\n".join(map(str.rstrip,
                                 s.lstrip("\n").rstrip().splitlines()))
        self.assertEqual(strip_fsp(expected), strip_fsp(actual),
                         msg=f"Pričakovano:\n\n{expected}\n\n"
                             f"Dejansko:\n\n{actual}")

    def test_sestavi_koscke(self):
        self.assertEqual(
            self.kosi_muca,
            sestavi_koscke(preberi_datoteko("muc-puzzle.txt"), self.kosi_muca[0][0]))

        self.assertEqual(
            self.kosi_krave,
            sestavi_koscke(preberi_datoteko("krava-puzzle.txt"), self.kosi_krave[0][0]))

    def test_slika(self):
        self.assertImgEqual(self.muc, slika(self.kosi_muca))
        self.assertImgEqual(self.krava, slika(self.kosi_krave))

    def test_sestavljanka(self):
        self.assertImgEqual(
            self.muc,
            sestavljanka(preberi_datoteko("muc-puzzle.txt"), self.kosi_muca[0][0]))
        self.assertImgEqual(
            self.krava, sestavljanka(preberi_datoteko("krava-puzzle.txt"), self.kosi_krave[0][0]))

        zadnji = preberi_datoteko("zadnji-puzzle.txt")
        kot = next(kos for kos in zadnji if kos[0] == "TTwADdOW")
        print(sestavljanka(zadnji, zrcaljen_vod(obrnjen(kot))))


if __name__ == "__main__":
    unittest.main()
