import unittest

class TestUnikati(unittest.TestCase):
    def test_01_unikati(self):
        s = [5, 4, 1, 4, 4, 4, 4, 4, 3]
        self.assertEqual(unikati(s), [5, 4, 1, 3])
        self.assertEqual(s, [5, 4, 1, 4, 4, 4, 4, 4, 3])

        s = [1, 1, 1, 1, 1]
        self.assertEqual(unikati(s), [1])
        self.assertEqual(s, [1, 1, 1, 1, 1])

        s = ["Ana", "Ana", "Berta"]
        self.assertEqual(unikati(s), ["Ana", "Berta"])
        self.assertEqual(s, ["Ana", "Ana", "Berta"])

        s = []
        self.assertEqual(unikati(s), [])

    def test_02_ocisti(self):
        s = [5, 4, 1, 4, 4, 4, 4, 4, 3]
        self.assertIsNone(ocisti(s))
        self.assertEqual(s, [5, 4, 1, 3])

        s = [1, 1, 1, 1, 1]
        self.assertIsNone(ocisti(s))
        self.assertEqual(s, [1])

        s = ["Ana", "Ana", "Berta"]
        self.assertIsNone(ocisti(s))
        self.assertEqual(s, ["Ana", "Berta"])

        s = []
        self.assertIsNone(ocisti(s))
        self.assertEqual(s, [])

    def test_03_podvoji(self):
        s = [5, 1, 3, 1, 4]
        self.assertIsNone(podvoji(s))
        self.assertEqual(s, [5, 5, 1, 1, 3, 3, 1, 1, 4, 4])

        s = [1]
        self.assertIsNone(podvoji(s))
        self.assertEqual(s, [1, 1])

        s = ["Ana", 7, (4, 2)]
        self.assertIsNone(podvoji(s))
        self.assertEqual(s, ["Ana", "Ana", 7, 7, (4, 2), (4, 2)])

        s = []
        self.assertIsNone(podvoji(s))
        self.assertEqual(s, [])

if __name__ == "__main__":
    unittest.main()
