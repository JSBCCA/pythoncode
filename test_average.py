import unittest
from average_age_test import average


class TestAverage(unittest.TestCase):
    """Tests for average_age_test.average."""

    def test_nothing(self):
        """Test nothing."""

        expected = None
        L = []
        self.assertEqual(expected, average(L), "Error.")

    def test_single(self):
        """Test a single number."""

        expected = 5
        L = [5]
        self.assertEqual(expected, average(L), "Error.")

    def test_none(self):
        """Test a single number."""

        expected = None
        L = [None]
        self.assertEqual(expected, average(L), "Error.")

    def test_two(self):
        """Test two numbers."""

        expected = 75
        L = [50, 100]
        self.assertEqual(expected, average(L), "Error.")

    def test_one_none(self):
        """Test two numbers."""

        expected = 50
        L = [50, None]
        self.assertEqual(expected, average(L), "Error.")

    def test_neg(self):
        """Test a negative number."""

        expected = -75
        L = [-75]
        self.assertEqual(expected, average(L), "Error.")

    def test_two_neg(self):
        """Test two negative numbers."""

        expected = -75
        L = [-50, -100]
        self.assertEqual(expected, average(L), "Error.")

    def test_pos_neg(self):
        """Test a positive and negative number."""

        expected = 0
        L = [-100, 100]
        self.assertEqual(expected, average(L), "Error.")

    def test_neg_none(self):
        """Test a negative number and none."""

        expected = -50
        L = [-50, None]
        self.assertEqual(expected, average(L), "Error.")

    def test_neg_pos_none(self):
        """Test a positive, negative, and None."""

        expected = 0
        L = [-50, 50, None]
        self.assertEqual(expected, average(L), "Error.")

    def test_two_none(self):
        """Test two None."""

        expected = None
        L = [None, None]
        self.assertEqual(expected, average(L), "Error.")


unittest.main()
