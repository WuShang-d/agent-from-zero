import unittest

from stats import average_duration


class AverageDurationTests(unittest.TestCase):
    def test_fractional_average(self):
        self.assertEqual(average_duration([1, 2]), 1.5)

    def test_empty_input(self):
        with self.assertRaises(ValueError):
            average_duration([])


if __name__ == "__main__":
    unittest.main()
