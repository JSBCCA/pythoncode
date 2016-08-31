import unittest
from double_preceding import double_preceding


class TestDoublePreceding(unittest.TestCase):
    """Tests for double_preceding."""

    def test_double_preceding_none(self):
        """Test nothing."""

        expected = []
        L = []
        double_preceding(L)
        self.assertEqual(expected, L, "Error.")

    def test_double_preceding_one(self):
        """Test one thing."""

        expected = [0]
        L = [2]
        double_preceding(L)
        self.assertEqual(expected, L, "Error.")

    def test_double_preceding_two(self):
        """Test two things."""

        expected = [0, 4]
        L = [2, 3]
        double_preceding(L)
        self.assertEqual(expected, L, "Error.")

    def test_double_preceding_neg(self):
        """Test negative thing."""

        expected = [0]
        L = [-5]
        double_preceding(L)
        self.assertEqual(expected, L, "Error.")

    def test_double_preceding_two_neg(self):
        """Test two negative things."""

        expected = [0, -12]
        L = [-6, -3]
        double_preceding(L)
        self.assertEqual(expected, L, "Error.")

    def test_double_preceding_neg_pos(self):
        """Test positive and negative things."""

        expected = [0, 6, -24]
        L = [3, -12, 1]
        double_preceding(L)
        self.assertEqual(expected, L, "Error.")

    def test_double_preceding_zero(self):
        """Test zero."""

        expected = [0]
        L = [0]
        double_preceding(L)
        self.assertEqual(expected, L, "Error.")


unittest.main()
