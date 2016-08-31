import unittest
import prefixes


class TestPrefixes(unittest.TestCase):
    """Tests prefixes."""

    def test_above_freezing_above(self):
        """Test a temperature that is above freezing."""

        expected = True
        actual = temperature.above_freezing(5.2)
        self.assertEqual(expected, actual,
                         "The temperature is above freezing.")


unittest.main()
