import unittest
from solution import Solution

class TestSortedSquares(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_nums(self):
        self.assertEqual(self.solution.sortedSquares([]), [])

    def test_mixed_nums(self):
        result = self.solution.sortedSquares([-4,-1,0,3,10])
        expected = [0,1,9,16,100]
        self.assertEqual(result, expected)

    def test_positive_nums(self):
        self.assertEqual(self.solution.sortedSquares([1, 2, 3, 4, 5]), [1, 4, 9, 16, 25])

    def test_negative_nums(self):
        self.assertEqual(self.solution.sortedSquares([-10, -5, -2]), [4, 25, 100])

    def test_find_with_positive(self):
        self.assertEqual(self.solution.get_first_non_negative([2, 3, 5]), 0)

    def test_find_with_negative(self):
        self.assertEqual(self.solution.get_first_non_negative([-10, -5, -2]), 3)

    def test_find_with_non_negative(self):
        self.assertEqual(self.solution.get_first_non_negative([0, 1, 2, 3]), 0)

    def test_find_with_mixed(self):
        self.assertEqual(self.solution.get_first_non_negative([-10, -5, 0, 1, 2, 3]), 2)


if __name__ == "__main__":
    unittest.main()