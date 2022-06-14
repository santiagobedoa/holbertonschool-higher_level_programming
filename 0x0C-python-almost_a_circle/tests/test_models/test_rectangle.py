#!/usr/bin/python3
"""
Unittest for Class Rectangle
"""


from models.rectangle import Rectangle
import unittest


class TetsRectangle_01_attributes(unittest.TestCase):
    """Test cases for the Rectangle class"""

    def test_01_init(self):
        """-----Test for the fisrt rectangle writed-----"""

        r1 = Rectangle(10, 2)
        self.assertNotIsInstance(r1._Rectangle__height, Rectangle)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        self.assertNotIsInstance(r3.height, Rectangle)

    def test_02_init_TypeError(self):
        """-----Test Typeerror the values Must be integers-----"""

        """Tests to TypeErrors"""
        typeErr = ["number", "10", 3.0, [1, 2], {"a": 1}, float("nan"), None]
        msgErrHeight = "height must be an integer"
        for err in typeErr:
            with self.assertRaisesRegex(TypeError, "width must be an integer"):
                Rectangle(err, 10, "4")
            with self.assertRaisesRegex(TypeError, msgErrHeight):
                Rectangle(10, err, "4")
            with self.assertRaisesRegex(TypeError, "x must be an integer"):
                Rectangle(23, 10, err)
            with self.assertRaisesRegex(TypeError, "y must be an integer"):
                Rectangle(2, 10, 3, err)

    def test_03_init_valueError(self):
        """-----Tests to ValueErrors-----"""
        valueErr = [-2, -1024, -1]
        for err in valueErr:
            with self.assertRaisesRegex(ValueError, "width must be > 0"):
                Rectangle(err, 10, 6)
            with self.assertRaisesRegex(ValueError, "height must be > 0"):
                Rectangle(10, err, 2)
            with self.assertRaisesRegex(ValueError, "x must be >= 0"):
                Rectangle(23, 10, err)
            with self.assertRaisesRegex(ValueError, "y must be >= 0"):
                Rectangle(2, 10, 3, err)

        """Width and height must be > 0"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 10, 6)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(7, 0, 6)


class TetsRectangle_01_methods(unittest.TestCase):
    """Test cases for the Rectangle class"""

    def test_04_init_area(self):
        """-----Test area method-----"""

        ra1 = Rectangle(2, 3)
        self.assertEqual(ra1.area(), 6)
        ra2 = Rectangle(1024, 2, 3, 4, 12)
        self.assertEqual(ra2.area(), 2048)

        """Width and height must be > 0"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 10, 6).area()
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(7, 0, 6).area()

    def test_05_init_display(self):
        """-----Display method-----"""

        rd1 = Rectangle(1, 1)
        result1 = "#\n"
        self.assertEqual(rd1.display(), result1)
        rd2 = Rectangle(1, 2)
        result2 = "#\n#\n"
        self.assertEqual(rd2.display(), result2)
        rd3 = Rectangle(2, 1)
        result3 = "##\n"
        self.assertEqual(rd3.display(), result3)
        rd3 = Rectangle(2, 2)
        result3 = "##\n##\n"
        self.assertEqual(rd3.display(), result3)

        """Hangling x and y"""
        rd4 = Rectangle(2, 2, 2, 2)
        result4 = "\n\n  ##\n  ##\n"
        self.assertEqual(rd4.display(), result4)
        rd5 = Rectangle(2, 2, 2, 0)
        result5 = "  ##\n  ##\n"
        self.assertEqual(rd5.display(), result5)
        rd6 = Rectangle(2, 3, 3, 1)
        result6 = "\n   ##\n   ##\n   ##\n"
        self.assertEqual(rd6.display(), result6)

    def test_06_init_str(self):
        """-----Test str method------"""

        rs1 = Rectangle(1, 2, 3, 4, 5)
        str1 = "[Rectangle] (5) 3/4 - 1/2"
        self.assertEqual(rs1.__str__(), str1)

        rs2 = Rectangle(1, 2, 0, 0, 34)
        str2 = "[Rectangle] (34) 0/0 - 1/2"
        self.assertEqual(rs2.__str__(), str2)

    def test_07_init_update(self):
        """Test update method"""

        """only with *args"""
        ru1 = Rectangle(1, 2, 0, 0, 1)
        r1 = "[Rectangle] (1) 0/0 - 1/2"
        self.assertEqual(ru1.__str__(), r1)
        ru1.update(1, 1, 2, 2, 0)
        r2 = "[Rectangle] (1) 2/0 - 1/2"
        self.assertEqual(ru1.__str__(), r2)
        ru1.update(100, 1, 10, 3, 8)
        r2 = "[Rectangle] (100) 3/8 - 1/10"
        self.assertEqual(ru1.__str__(), r2)
        ru1.update(100, 23)
        r2 = "[Rectangle] (100) 3/8 - 23/10"
        self.assertEqual(ru1.__str__(), r2)
        ru1.update()
        r2 = "[Rectangle] (100) 3/8 - 23/10"
        self.assertEqual(ru1.__str__(), r2)

        """With *args and **kwargs"""
        r = Rectangle(1, 2, 0, 0, 3)
        r2 = "[Rectangle] (3) 0/0 - 1/2"
        self.assertEqual(r.__str__(), r2)
        """Case not arguments"""
        r.update()
        r2 = "[Rectangle] (3) 0/0 - 1/2"
        self.assertEqual(r.__str__(), r2)
        r.update(id=100, x=10)
        r2 = "[Rectangle] (100) 10/0 - 1/2"
        self.assertEqual(r.__str__(), r2)
        r.update(id=10, height=137)
        r2 = "[Rectangle] (10) 10/0 - 1/137"
        self.assertEqual(r.__str__(), r2)
        r.update(1, 2, 3, id=100, x=10)
        r2 = "[Rectangle] (1) 10/0 - 2/3"
        self.assertEqual(r.__str__(), r2)
        r.update(113, id=100, x=10)
        r2 = "[Rectangle] (113) 10/0 - 2/3"
        self.assertEqual(r.__str__(), r2)
        r.update(id=100, x=10)
        r2 = "[Rectangle] (100) 10/0 - 2/3"
        self.assertEqual(r.__str__(), r2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(id=100, x="10")


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TetsRectangle_01_attributes("test_1_id"))
    suite.addTest(TetsRectangle_01_attributes("test_2_typeError"))
    suite.addTest(TetsRectangle_01_attributes("test_3_valueError"))
    return suite


if __name__ == "__main__":
    unittest.main(failfast=True, exit=False)
