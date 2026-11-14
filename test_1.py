
"""
CS 1001 - Lab Programming 4: Searching Algorithms

Starter unit tests for day1.py.

Run with: python -m unittest test_1.py
"""

import unittest

from day1 import find, is_descending, index_of_largest, largest_between


class TestFind(unittest.TestCase):
    def test_first_occurrence(self):
        self.assertEqual(1, find([4, 9, 2, 9, 5], 9))

    def test_target_absent(self):
        self.assertEqual(None, find([4, 9, 2, 9, 5], 7))

    def test_target_at_beginning(self):
        self.assertEqual(0, find([4, 9, 2, 9, 5], 4))

    def test_target_at_end(self):
        self.assertEqual(4, find([4, 9, 2, 9, 5], 5))

    def test_empty_list(self):
        self.assertEqual(None, find([], 9))

    def test_single_element(self):
        self.assertEqual(0, find([9], 9))

    def test_input_unchanged(self):
        values = [4, 9, 2, 9, 5]
        original = values.copy()

        find(values, 9)

        self.assertEqual(original, values)


class TestIsDescending(unittest.TestCase):
    def test_strictly_descending(self):
        self.assertEqual(True, is_descending([9.0, 7.0, 4.0, 1.0]))

    def test_equal_adjacent_values(self):
        self.assertEqual(False, is_descending([9.0, 7.0, 7.0, 1.0]))

    def test_empty_list(self):
        self.assertEqual(True, is_descending([]))

    def test_single_element(self):
        self.assertEqual(True, is_descending([5.0]))

    def test_two_elements_descending(self):
        self.assertEqual(True, is_descending([5.0, 3.0]))

    def test_two_elements_not_descending(self):
        self.assertEqual(False, is_descending([3.0, 5.0]))

    def test_violation_at_beginning(self):
        self.assertEqual(False, is_descending([9.0, 10.0, 7.0, 4.0]))

    def test_violation_at_end(self):
        self.assertEqual(False, is_descending([9.0, 7.0, 4.0, 5.0]))


class TestIndexOfLargest(unittest.TestCase):
    def test_largest_in_middle(self):
        self.assertEqual(1, index_of_largest([4, 9, 2, 7]))

    def test_first_of_repeated_largest(self):
        self.assertEqual(1, index_of_largest([4, 9, 2, 9]))

    def test_largest_at_beginning(self):
        self.assertEqual(0, index_of_largest([10, 4, 2, 7]))

    def test_largest_at_end(self):
        self.assertEqual(3, index_of_largest([4, 2, 7, 10]))

    def test_negative_values(self):
        self.assertEqual(1, index_of_largest([-8, -3, -10, -5]))

    def test_single_element(self):
        self.assertEqual(0, index_of_largest([5]))

    def test_empty_list(self):
        self.assertEqual(None, index_of_largest([]))

    def test_input_unchanged(self):
        values = [4, 9, 2, 7]
        original = values.copy()

        index_of_largest(values)

        self.assertEqual(original, values)


class TestLargestBetween(unittest.TestCase):
    def test_inclusive_range(self):
        self.assertEqual(4, largest_between([8, 3, 12, 7, 15, 4], 1, 4))

    def test_lower_greater_than_upper(self):
        self.assertEqual(None, largest_between([8, 3, 12, 7], 3, 1))

    def test_one_index_range(self):
        self.assertEqual(2, largest_between([8, 3, 12, 7], 2, 2))

    def test_entire_list(self):
        self.assertEqual(4, largest_between([8, 3, 12, 7, 15, 4], 0, 5))

    def test_lower_below_zero(self):
        self.assertEqual(2, largest_between([8, 3, 12, 7], -2, 2))

    def test_upper_beyond_list(self):
        self.assertEqual(2, largest_between([8, 3, 12, 7], 1, 10))

    def test_range_entirely_above_list(self):
        self.assertEqual(None, largest_between([8, 3, 12, 7], 10, 12))

    def test_range_entirely_below_list(self):
        self.assertEqual(None, largest_between([8, 3, 12, 7], -5, -1))

    def test_empty_list(self):
        self.assertEqual(None, largest_between([], 0, 5))

    def test_repeated_largest(self):
        self.assertEqual(1, largest_between([5, 9, 9, 2], 0, 3))

    def test_negative_values(self):
        self.assertEqual(1, largest_between([-8, -3, -10], 0, 2))

    def test_input_unchanged(self):
        values = [8, 3, 12, 7, 15, 4]
        original = values.copy()

        largest_between(values, 1, 4)

        self.assertEqual(original, values)


if __name__ == "__main__":
    unittest.main()
