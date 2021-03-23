import unittest
import random
from collections import defaultdict
from contextlib import contextmanager
from copy import deepcopy
from string import ascii_letters


stiki = {"Ana": {"Berta": {"šola", "sprehod", "žurka"},
                  "Cilka": {"sprehod", "trgovina"}},
          "Berta": {"Dani": {"sprehod"},
                    "Ema": {"šola", "žurka"}},
          "Cilka": {"Fanči": {"sprehod"},
                    "Greta": {"sprehod"}},
          "Dani": {"Helga": {"sprehod", "šola"}},
          "Ema": {"Iva": {"žurka"},
                  "Jana": {"šola", "žurka"}},
          "Greta": {"Klara": {"šola", "žurka"},
                    "Liza": {"trgovina", "šola", "žurka"},
                    "Micka": {"trgovina", "žurka"}},
          "Liza": {"Nina": {"trgovina", "šola"},
                   "Olga": {"šola"}}
          }


@contextmanager
def pokvari(f):
    global stiki
    prevod = defaultdict(
        lambda: "".join(random.choice(ascii_letters) for _ in range(20)))
    prejsnji = deepcopy(stiki)

    def prev_func(*args):
        return f(*[prevod[a] for a in args])

    try:
        stiki = {prevod[ime]: {prevod[okuzenec]:
                                    {prevod[aktivnost] for aktivnost in
                                     aktivnosti}
                                for okuzenec, aktivnosti in okuz_akt.items()}
                  for ime, okuz_akt in stiki.items()}
        yield prev_func
    finally:
        stiki = prejsnji


class Test1Obvezna(unittest.TestCase):
    def test_stevilo_okuzenih(self):
        self.assertEqual(1, stevilo_okuzenih("Helga"))
        self.assertEqual(2, stevilo_okuzenih("Dani"))
        self.assertEqual(3, stevilo_okuzenih("Ema"))
        self.assertEqual(6, stevilo_okuzenih("Berta"))
        self.assertEqual(6, stevilo_okuzenih("Greta"))
        self.assertEqual(8, stevilo_okuzenih("Cilka"))
        self.assertEqual(15, stevilo_okuzenih("Ana"))
        with pokvari(stevilo_okuzenih) as stevilo_okuzenih_p:
            self.assertEqual(1, stevilo_okuzenih_p("Helga"))
            self.assertEqual(2, stevilo_okuzenih_p("Dani"))
            self.assertEqual(3, stevilo_okuzenih_p("Ema"))
            self.assertEqual(6, stevilo_okuzenih_p("Berta"))
            self.assertEqual(6, stevilo_okuzenih_p("Greta"))
            self.assertEqual(8, stevilo_okuzenih_p("Cilka"))
            self.assertEqual(15, stevilo_okuzenih_p("Ana"))

    def test_rekord(self):
        self.assertEqual(0, rekord("Helga"))
        self.assertEqual(1, rekord("Dani"))
        self.assertEqual(2, rekord("Ema"))
        self.assertEqual(2, rekord("Berta"))
        self.assertEqual(2, rekord("Liza"))
        self.assertEqual(3, rekord("Greta"))
        self.assertEqual(3, rekord("Cilka"))
        self.assertEqual(3, rekord("Ana"))
        with pokvari(rekord) as rekord_p:
            self.assertEqual(0, rekord_p("Helga"))
            self.assertEqual(1, rekord_p("Dani"))
            self.assertEqual(2, rekord_p("Ema"))
            self.assertEqual(2, rekord_p("Berta"))
            self.assertEqual(2, rekord_p("Liza"))
            self.assertEqual(3, rekord_p("Greta"))
            self.assertEqual(3, rekord_p("Cilka"))
            self.assertEqual(3, rekord_p("Ana"))


class Test2Dodatna(unittest.TestCase):
    def test_nevarnost(self):
        self.assertEqual(0, nevarnost("Dani", "žurka"))
        self.assertEqual(1, nevarnost("Dani", "sprehod"))
        self.assertEqual(1, nevarnost("Dani", "šola"))
        self.assertEqual(3, nevarnost("Berta", "šola"))
        self.assertEqual(3, nevarnost("Berta", "žurka"))
        self.assertEqual(7, nevarnost("Ana", "žurka"))
        self.assertEqual(8, nevarnost("Ana", "šola"))
        self.assertEqual(6, nevarnost("Ana", "sprehod"))
        self.assertEqual(4, nevarnost("Ana", "trgovina"))
        self.assertEqual(3, nevarnost("Cilka", "trgovina"))
        self.assertEqual(3, nevarnost("Greta", "trgovina"))
        with pokvari(nevarnost) as nevarnost_p:
            self.assertEqual(0, nevarnost_p("Dani", "žurka"))
            self.assertEqual(1, nevarnost_p("Dani", "sprehod"))
            self.assertEqual(1, nevarnost_p("Dani", "šola"))
            self.assertEqual(3, nevarnost_p("Berta", "šola"))
            self.assertEqual(3, nevarnost_p("Berta", "žurka"))
            self.assertEqual(7, nevarnost_p("Ana", "žurka"))
            self.assertEqual(8, nevarnost_p("Ana", "šola"))
            self.assertEqual(6, nevarnost_p("Ana", "sprehod"))
            self.assertEqual(4, nevarnost_p("Ana", "trgovina"))
            self.assertEqual(3, nevarnost_p("Cilka", "trgovina"))
            self.assertEqual(3, nevarnost_p("Greta", "trgovina"))

    def test_okuzbe_zaradi(self):
        self.assertEqual(1, okuzbe_zaradi("Dani", "žurka"))
        self.assertEqual(2, okuzbe_zaradi("Dani", "sprehod"))
        self.assertEqual(2, okuzbe_zaradi("Dani", "šola"))
        self.assertEqual(3, okuzbe_zaradi("Berta", "šola"))
        self.assertEqual(4, okuzbe_zaradi("Berta", "žurka"))
        self.assertEqual(5, okuzbe_zaradi("Ana", "žurka"))
        self.assertEqual(4, okuzbe_zaradi("Ana", "šola"))
        self.assertEqual(7, okuzbe_zaradi("Ana", "sprehod"))
        self.assertEqual(2, okuzbe_zaradi("Ana", "trgovina"))
        self.assertEqual(1, okuzbe_zaradi("Cilka", "trgovina"))
        self.assertEqual(4, okuzbe_zaradi("Greta", "trgovina"))
        with pokvari(okuzbe_zaradi) as okuzbe_zaradi_p:
            self.assertEqual(1, okuzbe_zaradi_p("Dani", "žurka"))
            self.assertEqual(2, okuzbe_zaradi_p("Dani", "sprehod"))
            self.assertEqual(2, okuzbe_zaradi_p("Dani", "šola"))
            self.assertEqual(3, okuzbe_zaradi_p("Berta", "šola"))
            self.assertEqual(4, okuzbe_zaradi_p("Berta", "žurka"))
            self.assertEqual(5, okuzbe_zaradi_p("Ana", "žurka"))
            self.assertEqual(4, okuzbe_zaradi_p("Ana", "šola"))
            self.assertEqual(7, okuzbe_zaradi_p("Ana", "sprehod"))
            self.assertEqual(2, okuzbe_zaradi_p("Ana", "trgovina"))
            self.assertEqual(1, okuzbe_zaradi_p("Cilka", "trgovina"))
            self.assertEqual(4, okuzbe_zaradi_p("Greta", "trgovina"))

    def test_okuzbe_brez(self):
        self.assertEqual(1, okuzbe_brez("Helga", set()))
        self.assertEqual(1, okuzbe_brez("Helga", {"šola"}))
        self.assertEqual(2, okuzbe_brez("Dani", set()))
        self.assertEqual(2, okuzbe_brez("Dani", {"sprehod"}))
        self.assertEqual(2, okuzbe_brez("Dani", {"šola"}))
        self.assertEqual(1, okuzbe_brez("Dani", {"šola", "sprehod"}))

        self.assertEqual(6, okuzbe_brez("Ana", {"sprehod"}))
        self.assertEqual(5, okuzbe_brez("Ana", {"sprehod", "trgovina"}))

        self.assertEqual(5, okuzbe_brez("Greta", {"šola"}))
        self.assertEqual(4, okuzbe_brez("Greta", {"šola", "žurka"}))
        self.assertEqual(1, okuzbe_brez("Greta", {"šola", "žurka", "trgovina"}))


if __name__ == "__main__":
    unittest.main()

