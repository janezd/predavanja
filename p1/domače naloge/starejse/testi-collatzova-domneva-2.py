import unittest
class TestCollatz(unittest.TestCase):
    def test_collatz(self):
        self.assertEqual(collatz(1), [1])
        self.assertEqual(collatz(2), [2, 1])
        self.assertEqual(collatz(3), [3, 10, 5, 16, 8, 4, 2, 1])
        self.assertEqual(collatz(12), [12, 6, 3, 10, 5, 16, 8, 4, 2, 1])
        self.assertEqual(collatz(21), [21, 64, 32, 16, 8, 4, 2, 1])

    def test_collatz_dolzina(self):
        self.assertEqual(collatz_dolzina(1), 1)
        self.assertEqual(collatz_dolzina(2), 2)
        self.assertEqual(collatz_dolzina(3), 8)
        self.assertEqual(collatz_dolzina(12), 10)
        self.assertEqual(collatz_dolzina(100000), 129)

    def test_najdaljsi_stev(self):
        self.assertEqual(najdaljsi_stev(1), 1)
        self.assertEqual(najdaljsi_stev(2), 2)
        self.assertEqual(najdaljsi_stev(3), 3)
        self.assertEqual(najdaljsi_stev(12), 9)
        self.assertEqual(najdaljsi_stev(10000), 6171)


    def test_najdaljsi_dolz(self):
        self.assertEqual(najdaljsi_dolz(1), 1)
        self.assertEqual(najdaljsi_dolz(2), 2)
        self.assertEqual(najdaljsi_dolz(3), 8)
        self.assertEqual(najdaljsi_dolz(12), 20)
        self.assertEqual(najdaljsi_dolz(10000), 262)

    def test_nad_n(self):
        self.assertEqual(nad_n(1), 1)
        self.assertEqual(nad_n(10), 7)
        self.assertEqual(nad_n(100), 27)
        self.assertEqual(nad_n(300), 26623)

    def test_sest_collatz(self):
        self.assertEqual(sest_collatz(100), 84)
        self.assertEqual(sest_collatz(1000), 906)
