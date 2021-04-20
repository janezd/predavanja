

import unittest
import random
import os
import warnings


class Test(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)

    def test_razberi_cas(self):
        self.assertEqual(
            13 * 3600 + 12 * 60 + 33.125,
            razberi_cas("13:12:33,125"))

    def test_razberi_interval(self):
        self.assertEqual(
            (13 * 3600 + 12 * 60 + 33.125, 13 * 3600 + 12 * 60 + 37.574),
            razberi_interval("13:12:33,125 --> 13:12:37.574"))

    def test_zapisi_cas(self):
        self.assertEqual(
            "13:12:33,125",
            zapisi_cas(13 * 3600 + 12 * 60 + 33.125)
        )
        self.assertEqual(
            "13:12:33,000",
            zapisi_cas(13 * 3600 + 12 * 60 + 33)
        )

    def test_zapisi_interval(self):
        self.assertEqual(
            razberi_interval("13:12:33,125 --> 13:12:37.574"),
            (13 * 3600 + 12 * 60 + 33.125, 13 * 3600 + 12 * 60 + 37.574))

    def test_paketek(self):
        f = open("podnapisi.srt")
        for exp in (["1", "00:00:02,618 --> 00:00:05,019", "(Finch) We are being watched."],
                    ["2", "00:00:05,021 --> 00:00:07,288", "The government has a secret system,"],
                    ["3", "00:00:07,290 --> 00:00:11,626", "a machine that spies on you", "every hour of every day."],
                    ["4", "00:00:11,628 --> 00:00:14,128", "I designed the machine", "to detect acts of terror,"],
                    ["5", "00:00:14,130 --> 00:00:15,963", "but it sees everything,"],
                    None, None, None):
            self.assertEqual(exp, paketek(f))

    def test_podnapis(self):
        f = open("podnapisi.srt")
        for exp in ((1, 2.618, 5.019, ["(Finch) We are being watched."]),
                    (2, 5.021, 7.288, ["The government has a secret system,"]),
                    (3, 7.290, 11.626, ["a machine that spies on you", "every hour of every day."]),
                    (4, 11.628, 14.128, ["I designed the machine", "to detect acts of terror,"]),
                    (5, 14.130, 15.963, ["but it sees everything,"]),
                    (0, 0, 0, []), (0, 0, 0, []), (0, 0, 0, [])):
            self.assertEqual(exp, podnapis(f))

    def test_zapisi_podnapis(self):
        ime = f"test{random.randint(0, 9999):04}.srt"
        with open(ime, "w") as f:
            zapisi_podnapis(f, 13, 3663.25, 3664.5, ["foo", "bar!"])
            zapisi_podnapis(f, 14, 7263.25, 7264.5, ["baz?"])
        self.assertEqual("""13
01:01:03,250 --> 01:01:04,500
foo
bar!

14
02:01:03,250 --> 02:01:04,500
baz?

""", open(ime).read(), f"Napačna datoteka je shranjena v {ime}")
        os.remove(ime)

    def test_premakni(self):
        ime = f"test{random.randint(0, 9999):04}"
        pop_ime = f"{ime}_popravljena.srt"
        ime += ".srt"
        open(ime, "w").write(open("podnapisi.srt").read())
        premakni(ime, 1.5)
        self.assertEqual("""1
00:00:04,118 --> 00:00:06,519
(Finch) We are being watched.

2
00:00:06,521 --> 00:00:08,788
The government has a secret system,

3
00:00:08,790 --> 00:00:13,126
a machine that spies on you
every hour of every day.

4
00:00:13,128 --> 00:00:15,628
I designed the machine
to detect acts of terror,

5
00:00:15,630 --> 00:00:17,463
but it sees everything,""", open(pop_ime).read().strip())
        os.remove(ime)
        os.remove(pop_ime)


if __name__ == "__main__":
    unittest.main()
