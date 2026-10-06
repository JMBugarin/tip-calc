import unittest
from tip import split_bill


class TestTip(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(split_bill(100, 20, 4), {"tip": 20.0, "total": 120.0, "per_person": 30.0})

    def test_invalid(self):
        with self.assertRaises(ValueError):
            split_bill(10, 15, 0)


if __name__ == "__main__":
    unittest.main()
