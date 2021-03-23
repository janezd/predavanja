def dejavnosti_osebe(oseba, obiski):
    vse_dejavnosti = set()
    for oseba1, dejavnost in obiski:
        if oseba1 == oseba:
            vse_dejavnosti.add(dejavnost)
    return vse_dejavnosti


def v_stiku(oseba1, oseba2, obiski):
    skupne = dejavnosti_osebe(oseba1, obiski) & dejavnosti_osebe(oseba2, obiski)
    return len(skupne) != 0


def osumljenci(osebe, zdravi, obiski):
    v_stiku_z_zdravimi = set()
    for oseba in zdravi:
        for osumljenec in osebe:
            if v_stiku(osumljenec, oseba, obiski):
                v_stiku_z_zdravimi.add(osumljenec)
    osebe -= v_stiku_z_zdravimi
    return osebe


skupinica = {"Ana", "Berta", "Cilka", "Dani", "Ema"}
obiski = [
    ("Ana", "kava"), ("Berta", "kava"), ("Cilka", "kava"),
    ("Cilka", "telovadba"), ("Ema", "telovadba"),
    ("Dani", "zdravnik"), ("Ana", "zdravnik")]
print(osumljenci(skupinica, {"Dani", "Ema"}, obiski))


import unittest


class Test(unittest.TestCase):
    def test_osumljenci(self):
        obiski = [
            ("Ana", "kava"), ("Berta", "kava"), ("Cilka", "kava"),
            ("Cilka", "telovadba"), ("Ema", "telovadba"),
            ("Dani", "zdravnik"), ("Ana", "zdravnik")]

        skupinica = {"Ana", "Berta", "Cilka", "Dani", "Ema"}
        self.assertEqual({"Dani", "Ema"}, osumljenci(skupinica, {"Berta"}, obiski))
        self.assertEqual({"Berta"}, osumljenci(skupinica, {"Dani", "Ema"}, obiski))
        self.assertEqual(set(), osumljenci(skupinica, {"Ana", "Ema"}, obiski))
        self.assertEqual({"Ana", "Berta", "Cilka", "Dani", "Ema"}, osumljenci(skupinica, set(), obiski))


if __name__ == "__main__":
    unittest.main()
