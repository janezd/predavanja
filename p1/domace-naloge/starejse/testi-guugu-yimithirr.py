import unittest

class TestGuugu(unittest.TestCase):
    def test_move_distance(self):
        a = Kangaroo()
        b = Kangaroo()
        self.assertEqual(a.distance(), 0)
        self.assertEqual(b.distance(), 0)

        a.move("N5")
        self.assertEqual(a.distance(), 5)
        self.assertEqual(b.distance(), 0)

        a.move("E12")
        self.assertEqual(a.distance(), 13)
        self.assertEqual(b.distance(), 0)

        b.move("S3")
        self.assertEqual(a.distance(), 13)
        self.assertEqual(b.distance(), 3)

        a.move("S21")
        self.assertEqual(a.distance(), 20)
        self.assertEqual(b.distance(), 3)

        a.move("W24")
        self.assertEqual(a.distance(), 20)
        self.assertEqual(b.distance(), 3)

        b.move("N3")
        self.assertEqual(a.distance(), 20)
        self.assertEqual(b.distance(), 0)

    def test_travel(self):
        a = Kangaroo()
        a.travel(["N3", "W4"])
        self.assertEqual(a.distance(), 5)

        b = Kangaroo()
        b.travel([])
        self.assertEqual(b.distance(), 0)

        b.travel(["N100"] * 5)
        self.assertEqual(b.distance(), 500)

        a = Kangaroo()
        from unittest.mock import MagicMock
        a.move = MagicMock()
        a.travel(["N3", "W4"])
        self.assertEqual(a.move.call_count, 2,
                         "method 'travel' must call method 'move'")

    def test_home(self):
        a = Kangaroo()
        a.travel(["N3", "W4", "S1"])
        self.assertEqual(set(a.home()), {"S2", "E4"})

        a = Kangaroo()
        a.travel(["S3", "E4", "N1"])
        self.assertEqual(set(a.home()), {"N2", "W4"})

        a = Kangaroo()
        a.travel(["N1"] * 100 + ["W1"])
        self.assertEqual(set(a.home()), {"S100", "E1"})

        a = Kangaroo()
        a.move("N1")
        self.assertEqual(a.home(), ["S1"])

        a = Kangaroo()
        a.move("E1")
        self.assertEqual(a.home(), ["W1"])

if __name__ == "__main__":
    unittest.main()
