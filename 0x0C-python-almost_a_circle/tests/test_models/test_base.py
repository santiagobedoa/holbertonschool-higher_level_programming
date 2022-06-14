#!/usr/bin/python3
"""
Unittest for Class Base
"""


from models.base import Base
import unittest


class TetsBaseClass(unittest.TestCase):
    """Test cases for the Base class"""

    def test_positive_numbers(self):
        """test number more or equal greather than zero"""
        base1 = Base(1)
        self.assertEqual(base1.id, 1)
        base2 = Base(2)
        self.assertEqual(base2.id, 2)
        base3 = Base(0)
        self.assertEqual(base3.id, 0)

    def test_none_value(self):
        """None value to id"""
        base1 = Base()
        self.assertEqual(base1.id, 1)
        base2 = Base()
        self.assertEqual(base2.id, 2)
        self.assertEqual(Base().id, 3)
        base4 = Base(4)
        self.assertEqual(base4.id, 4)
        base5 = Base()
        self.assertEqual(base4.id, 4)

    def test_negative_numbers(self):
        """test number less than zero"""
        base1 = Base(-1)
        self.assertEqual(base1.id, -1)
        base2 = Base(-1024)
        self.assertEqual(base2.id, -1024)
        base3 = Base(-34)
        self.assertEqual(base3.id, -34)


if __name__ == "__main__":
    unittest.main()
