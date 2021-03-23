import unittest
import copy

class TestKuhar(unittest.TestCase):
    normal_pairs = [
        (["pivo", (3, "sok"), (2, "kava")], ["pivo", "sok", "sok", "sok", "kava", "kava"]) ,
        (["pivo", "sok", "kava"], ["pivo", "sok", "kava"]),
        ([(15, "pivo")], ["pivo"]*15),
        (["kava"], ["kava"]),
        (["kava", "sok", (3, "kava")], ["kava", "sok"] + ["kava"]*3),
        (["kava", (3, "sok")], ["kava", "sok", "sok", "sok"]),
        ([(3, "sok"), "kava"], ["sok", "sok", "sok", "kava"]),
        ([], []),
    ]
    abnormal_pairs = [
        (["kava", "kava"], ["kava", "kava"]),
        (["kava", (3, "kava")], ["kava"]*4),
    ]

    def test_expanded(self):
        for s, res in copy.deepcopy(self.normal_pairs + self.abnormal_pairs):
            s2 = s[:]
            t = expanded(s)
            self.assertListEqual(t, res)
            self.assertListEqual(s, s2, "Funkcija expanded ne sme spreminjati seznama")

    def test_expand(self):
        for s, res in copy.deepcopy(self.normal_pairs + self.abnormal_pairs):
            t = expand(s)
            self.assertListEqual(s, res)
            self.assertIsNone(t, "Funkcija expand ne sme vračati rezultata")

    def test_implode(self):
        for res, s in copy.deepcopy(self.normal_pairs):
            t = implode(s)
            self.assertIsNone(t, "Funkcija implode ne sme vračati rezultata")
            self.assertListEqual(s, res)

    def test_imploded(self):
        for res, s in copy.deepcopy(self.normal_pairs):
            s2 = s[:]
            t = imploded(s)
            self.assertListEqual(t, res)
            self.assertListEqual(s, s2, "Funkcija imploded ne sme spreminjati seznama")

if __name__ == '__main__':
    unittest.main(verbosity=2)
