
import unittest
import random
import string
class TestBarvanje(unittest.TestCase):
    def test_barvanje(self):
        self.assertEqual(
            barvanje([("A3", "zelena")]),
            {"A3": "zelena"})

        self.assertEqual(
            barvanje([("A3", "zelena"),
                      ("B5", "modra")]),
            {"A3": "zelena", "B5": "modra"})

        self.assertEqual(
            barvanje([("A3", "zelena"),
                      ("B5", "modra"),
                      ("G2", "rumena")]),
            {"A3": "zelena", "B5": "modra", "G2": "rumena"})

        self.assertEqual(
            barvanje([("A3", "zelena"),
                      ("B5", "modra"),
                      ("A3", "rumena")]),
            {"A3": "rumena", "B5": "modra"})

        self.assertEqual(
            barvanje([("A3", "zelena"),
                      ("B5", "zelena"),
                      ("A3", "zelena")]),
            {"A3": "zelena", "B5": "zelena"})


    def test_barvanje_eno(self):
        self.assertEqual(
            barvanje_eno([("A3", "zelena")]),
            {"A3": "zelena"})

        self.assertEqual(
            barvanje_eno([("A3", "zelena"),
                          ("B5", "modra")]),
            {"A3": "zelena", "B5": "modra"})

        self.assertEqual(
            barvanje_eno([("A3", "zelena"),
                          ("B5", "modra"),
                          ("A3", "rumena")]),
            {"A3": "zelena", "B5": "modra"})

        self.assertEqual(
            barvanje_eno([("A3", "zelena"),
                          ("B5", "zelena"),
                          ("A3", "zelena")]),
            {"A3": "zelena", "B5": "zelena"})


    def test_prestej_barvo(self):
        sahovnica = {
            "A3": "rumena", "A6": "rumena", "H2": "rumena", "G7": "rumena",
            "C2": "zelena", "C3": "zelena",
            "H6": "modra"
        }
        self.assertEqual(prestej_barvo(sahovnica, "rumena"), 4)
        self.assertEqual(prestej_barvo(sahovnica, "zelena"), 2)
        self.assertEqual(prestej_barvo(sahovnica, "modra"), 1)
        self.assertEqual(prestej_barvo(sahovnica, "rjava"), 0)

        for i in range(5):
            barva1 = "".join(random.sample(string.ascii_lowercase, 20))
            barva2 = "".join(random.sample(string.ascii_lowercase, 20))
            sahovnica = {"A1": barva1}
            self.assertEqual(prestej_barvo(sahovnica, barva1), 1)
            self.assertEqual(prestej_barvo(sahovnica, barva2), 0)

    def test_pobarvanih_polj(self):
        sahovnica = {
            "A3": "rumena", "A6": "rumena", "H2": "rumena", "G7": "rumena",
            "C2": "zelena", "C3": "zelena",
            "H6": "modra"
        }
        self.assertEqual(pobarvanih_polj(sahovnica), 7)
        self.assertEqual(pobarvanih_polj({"A3": "rumena"}), 1)
        self.assertEqual(pobarvanih_polj({}), 0)

    def test_nepobarvanih_polj(self):
        sahovnica = {
            "A3": "rumena", "A6": "rumena", "H2": "rumena", "G7": "rumena",
            "C2": "zelena", "C3": "zelena",
            "H6": "modra"
        }
        self.assertEqual(nepobarvanih_polj(sahovnica), 57)
        self.assertEqual(nepobarvanih_polj({"A3": "rumena"}), 63)
        self.assertEqual(nepobarvanih_polj({}), 64)

    def test_polja_po_barvi(self):
        sahovnica = {
            "A3": "rumena", "A6": "rumena", "H2": "rumena", "G7": "rumena",
            "C2": "zelena", "C3": "zelena",
            "H6": "modra"
        }
        self.assertEqual(polja_po_barvi(sahovnica, "rumena"), {"A3", "A6", "H2", "G7"})
        self.assertEqual(polja_po_barvi(sahovnica, "zelena"), {"C2", "C3"})
        self.assertEqual(polja_po_barvi(sahovnica, "modra"), {"H6"})
        self.assertEqual(polja_po_barvi(sahovnica, "rjava"), set())

        for i in range(5):
            barva1 = "".join(random.sample(string.ascii_lowercase, 20))
            barva2 = "".join(random.sample(string.ascii_lowercase, 20))
            barva3 = "".join(random.sample(string.ascii_lowercase, 20))
            sahovnica = {"A1": barva1, "A4": barva1, "C4": barva2}
            self.assertEqual(polja_po_barvi(sahovnica, barva1), {"A1", "A4"})
            self.assertEqual(polja_po_barvi(sahovnica, barva2), {"C4"})
            self.assertEqual(polja_po_barvi(sahovnica, barva3), set())


    def test_prestej_barve(self):
        sahovnica = {
            "A3": "rumena", "A6": "rumena", "H2": "rumena", "G7": "rumena",
            "C2": "zelena", "C3": "zelena",
            "H6": "modra"
        }
        self.assertEqual(prestej_barve(sahovnica),
                         {"rumena": 4, "zelena": 2, "modra": 1})

    def test_polja_po_barvah(self):
        sahovnica = {
            "A3": "rumena", "A6": "rumena", "H2": "rumena", "G7": "rumena",
            "C2": "zelena", "C3": "zelena",
            "H6": "modra"
        }
        self.assertEqual(polja_po_barvah(sahovnica),
                         {"rumena": {"A3", "A6", "H2", "G7"},
                          "zelena": {"C2", "C3"},
                          "modra": {"H6"}})

if __name__ == "__main__":
    unittest.main()
