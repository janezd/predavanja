import unittest
class DumpTest(unittest.TestCase):
    def test_dump(self):
        n = 100
        self.assertEqual(dump([], n), '[]')
        self.assertEqual(dump([1], n), '[1]')
        self.assertEqual(dump([1, 2, 3, 4, 5], n), '[1, 2, 3, 4, 5]')
        self.assertEqual(dump([[1, 2], 3, 4, 5], n), '[[1, 2], 3, 4, 5]')
        self.assertEqual(dump([[1, 2], 3, [4, 5]], n), '[[1, 2], 3, [4, 5]]')
        self.assertEqual(dump([[[[1]], 2], 3, [4, 5]], n), '[[[[1]], 2], 3, [4, 5]]')
        self.assertEqual(dump([[[[1]], 2], [], 3, [], [4, 5]], n), '[[[[1]], 2], [], 3, [], [4, 5]]')
        self.assertEqual(dump([[[[[[[[[[]]]]]]]]]], n), '[[[[[[[[[[]]]]]]]]]]')
        self.assertEqual(dump([[42, [7, 423]], [[-60, 50, 1, 2, 3]], 2, -3, 4, [[-1, [], 2]], -5, [6, 7], 0], n),
            '[[42, [7, 423]], [[-60, 50, 1, 2, 3]], 2, -3, 4, [[-1, [], 2]], -5, [6, 7], 0]')
        self.assertEqual(dump([1, [2, [3, [4, [5, [6, [7, [8, [9, [10, []]]]]]]]]]], n),
            '[1, [2, [3, [4, [5, [6, [7, [8, [9, [10, []]]]]]]]]]]')

    def test_ellipsis(self):
        self.assertEqual(dump([1, 2, 3, 4, 5], 5), '[1, 2, 3, 4, 5]')
        self.assertEqual(dump([1, 2, 3, 4, 5], 4), '[1, 2, 3, 4, ...]')
        self.assertEqual(dump([1, 2, 3, 4, 5], 0), '[...]')

        xs = [[1, 2, 3, 4, 5], [[1, 2, [1, 2, 3, 4, 5, [1, 2, 3, 4], 7], 4, 5, 6]], 3, 4, 5]
        self.assertEqual(dump(xs, 7), '[[1, 2, 3, 4, 5], [[1, 2, [1, 2, 3, 4, 5, [1, 2, 3, 4], 7], 4, 5, 6]], 3, 4, 5]')
        self.assertEqual(dump(xs, 6), '[[1, 2, 3, 4, 5], [[1, 2, [1, 2, 3, 4, 5, [1, 2, 3, 4], ...], 4, 5, 6]], 3, 4, 5]')
        self.assertEqual(dump(xs, 5), '[[1, 2, 3, 4, 5], [[1, 2, [1, 2, 3, 4, 5, ...], 4, 5, ...]], 3, 4, 5]')
        self.assertEqual(dump(xs, 4), '[[1, 2, 3, 4, ...], [[1, 2, [1, 2, 3, 4, ...], 4, ...]], 3, 4, ...]')
        self.assertEqual(dump(xs, 3), '[[1, 2, 3, ...], [[1, 2, [1, 2, 3, ...], ...]], 3, ...]')
        self.assertEqual(dump(xs, 2), '[[1, 2, ...], [[1, 2, ...]], ...]')
        self.assertEqual(dump(xs, 1), '[[1, ...], ...]')
        self.assertEqual(dump(xs, 0), '[...]')
         

if __name__ == '__main__':
    unittest.main(verbosity=2)
