#!/usr/bin/python3
"""This is the unittest for the Square"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare_initialization(unittest.TestCase):
    """This test the initialization of a Square"""

    def test_instance_of_base(self):
        square = Square(6)
        self.assertIsInstance(square, Base)

    def test_instance_of_rect(self):
        square = Square(4)
        self.assertIsInstance(square, Rectangle)

    def test_no_arguments(self):
        with self.assertRaises(TypeError):
            Square()

    def test_one_argument(self):
        rect1 = Square(3)
        rect2 = Square(4)
        self.assertEqual(rect1.id, rect2.id - 1)

    def test_2_args(self):
        rect1 = Square(1, 2)
        rect2 = Square(2, 3)
        self.assertEqual(rect1.id, rect2.id - 1)

    def test_3_args(self):
        rect1 = Square(2, 1, 3)
        rect2 = Square(2, 5, 4)
        self.assertEqual(rect1.id, rect2.id - 1)

    def test_4_args(self):
        rect1 = Square(2, 1, 3, 3)
        rect2 = Square(1, 2, 3, 4)
        self.assertEqual(rect1.id, 3)
        self.assertEqual(rect2.id, 4)

    def test_5_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 4, 5, 3)


class TestSquareSize(unittest.TestCase):
    """This is the test case for Size"""

    def test_private(self):
        rect = Square(1, 2)
        with self.assertRaises(AttributeError):
            s = rect.__width

    def test_getter(self):
        rect = Square(3)
        self.assertEqual(3, rect.size)

    def test_setter(self):
        rect = Square(1, 3)
        rect.size = 5
        self.assertEqual(rect.size, 5)

    def test_none(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 1)

    def test_int(self):
        self.assertEqual(Square(1).size, 1)

    def test_string(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("Hello")

    def test_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(1.2)

    def test_complex(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(complex(12))

    def test_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1])

    def test_dictionary(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({'a': 1, 'b': 2})

    def test_set(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1, 2})

    def test_tuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 2))

    def test_boolean(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True)

    def test_range(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(range(23))

    def test_byte(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(b'1231.2')

    def test_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)

    def test_nan(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('nan'))

    def test_infinity(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('inf'))


class TestSquareX(unittest.TestCase):
    """This is the test case for X"""

    def test_private(self):
        rect = Square(1, 2, 3)
        with self.assertRaises(AttributeError):
            s = rect.__x

    def test_getter(self):
        rect = Square(1, 4)
        self.assertEqual(4, rect.x)

    def test_setter(self):
        rect = Square(1, 1)
        rect.x = 5
        self.assertEqual(rect.x, 5)

    def test_none(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, None)

    def test_zero(self):
        self.assertEqual(Square(1, 0, 0).y, 0)

    def test_int(self):
        self.assertEqual(Square(1, 1).x, 1)

    def test_string(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, 'hi')

    def test_float(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, 1.2)

    def test_complex(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, complex(12))

    def test_list(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, [2])

    def test_dictionary(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, {'a': 1, 'b': 2})

    def test_set(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, {1, 2})

    def test_tuple(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, (1, 2))

    def test_boolean(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, True)

    def test_range(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, range(23))

    def test_byte(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, b'1231.2')

    def test_negative(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -1)

    def test_nan(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, float('nan'))

    def test_infinity(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, float('inf'))


class TestSquareY(unittest.TestCase):
    """This is the test case for With"""

    def test_private(self):
        rect = Square(1, 2, 3)
        with self.assertRaises(AttributeError):
            s = rect.__y

    def test_getter(self):
        rect = Square(1, 2, 4)
        self.assertEqual(4, rect.y)

    def test_setter(self):
        rect = Square(1, 1, 1)
        rect.y = 5
        self.assertEqual(rect.y, 5)

    def test_none(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, None)

    def test_zero(self):
        self.assertEqual(Square(1, 0, 0).y, 0)

    def test_int(self):
        self.assertEqual(Square(1, 1, 1).y, 1)

    def test_string(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, 'hi')

    def test_float(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, 1.2)

    def test_complex(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, complex(12))

    def test_list(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, [2])

    def test_dictionary(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, {'a': 1, 'b': 2})

    def test_set(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 1, {1, 2})

    def test_tuple(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 1, (1, 2))

    def test_boolean(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 1, True)

    def test_range(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 1, range(23))

    def test_byte(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 1, b'1231.2')

    def test_negative(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 1, -1)

    def test_nan(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, float('nan'))

    def test_infinity(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, float('inf'))


class TestSquareArea(unittest.TestCase):
    """The unittest class for the area test"""

    def test_norm(self):
        rect = Square(2, 0, 0, 1)
        self.assertEqual(rect.area(), 4)

    def test_with_arg(self):
        with self.assertRaises(TypeError):
            rect = Square(2, 3)
            rect.area(23)

    def test_with_changes(self):
        rect = Square(4)
        rect.size = 5
        self.assertEqual(rect.area(), 25)

    def test_large_numbers(self):
        rect = Square(99999999999999999999999)
        self.assertEqual(rect.area(),
                         9999999999999999999999800000000000000000000001)


class TestSquareStr(unittest.TestCase):
    """This is the unittest case for the __str__"""

    @staticmethod
    def get_str_res(rect):
        """Returns the str representation of the Square"""
        import contextlib
        import io
        cap = io.StringIO()
        with contextlib.redirect_stdout(cap):
            print(rect)
        return cap.getvalue()

    def test_normal(self):
        rect = Square(1, 1, 1, 1)
        self.assertEqual("[Square] (1) 1/1 - 1\n",
                         TestSquareStr.get_str_res(rect))

    def test_change(self):
        rect = Square(1, 1, 1, 1)
        rect.id = 2
        rect.size = 2
        rect.x = 2
        rect.y = 2
        self.assertEqual("[Square] (2) 2/2 - 2\n",
                         TestSquareStr.get_str_res(rect))

    def test_w_and_h(self):
        rect = Square(2)
        self.assertEqual("[Square] ({}) 0/0 - 2".format(rect.id),
                         str(rect))

    def test_w_and_h_and_x(self):
        rect = Square(1, 1)
        self.assertEqual("[Square] ({}) 1/0 - 1".format(rect.id),
                         str(rect))

    def test_w_and_h_and_x_and_y(self):
        rect = Square(1, 1, 1)
        self.assertEqual(f"[Square] ({rect.id}) 1/1 - 1",
                         str(rect))

    def test_w_h_x_y_id(self):
        rect = Square(1, 1, 1, 1)
        self.assertEqual("[Square] (1) 1/1 - 1", str(rect))


class TestSquareDisplay(unittest.TestCase):
    """This is the unittest cases for the display function"""

    @staticmethod
    def get_display_res(rect):
        """returns the printed value of the display"""
        import contextlib
        import io
        cap = io.StringIO()
        with contextlib.redirect_stdout(cap):
            rect.display()
        return cap.getvalue()

    def test_with_args(self):
        with self.assertRaises(TypeError):
            Square(2, 3).display(2)

    def test_normal(self):
        rect = Square(2)
        self.assertEqual("##\n##\n",
                         TestSquareDisplay.get_display_res(rect))

    def test_change(self):
        rect = Square(5, 0, 0, 0)
        rect.size = 1
        self.assertEqual("#\n",
                         TestSquareDisplay.get_display_res(rect))

    def test_with_x(self):
        rect = Square(1, 1, 0)
        self.assertEqual(" #\n",
                         TestSquareDisplay.get_display_res(rect))

    def test_with_y(self):
        rect = Square(2, 0, 1)
        self.assertEqual("\n##\n##\n",
                         TestSquareDisplay.get_display_res(rect))

    def test_with_x_and_y(self):
        rect = Square(2, 2, 2)
        self.assertEqual("\n\n  ##\n  ##\n",
                         TestSquareDisplay.get_display_res(rect))


class TestSquareUpdateArgs(unittest.TestCase):
    """This is the unit test case for update function"""

    def test_with_no_args(self):
        rect = Square(1, 1, 1, 1)
        rect.update()
        self.assertEqual("[Square] (1) 1/1 - 1", str(rect))

    def test_one_arg(self):
        rect = Square(1)
        rect.update(1)
        self.assertEqual('[Square] (1) 0/0 - 1', str(rect))

    def test_2_args(self):
        rect = Square(1)
        rect.update(2, 2)
        self.assertEqual('[Square] (2) 0/0 - 2', str(rect))

    def test_3_args(self):
        rect = Square(1, 1, 1, 1)
        rect.update(2, 2, 2)
        self.assertEqual('[Square] (2) 2/1 - 2', str(rect))

    def test_4_args(self):
        rect = Square(1, 1, 1, 1)
        rect.update(2, 2, 2, 2)
        self.assertEqual('[Square] (2) 2/2 - 2', str(rect))

    def test_5_args(self):
        rect = Square(1, 1, 1, 1)
        rect.update(2, 2, 2, 2, 2)
        self.assertEqual('[Square] (2) 2/2 - 2', str(rect))

    def test_more_args(self):
        rect = Square(1, 1, 1, 1)
        rect.update(2, 2, 2, 2, 2, 2)
        self.assertEqual('[Square] (2) 2/2 - 2', str(rect))

    def test_double_update(self):
        rect = Square(1, 1, 1, 1)
        rect.update(2, 2, 2, 2)
        rect.update(3, 3, 3, 3)
        self.assertEqual('[Square] (3) 3/3 - 3', str(rect))

    def test_none_id(self):
        rect = Square(1, 1, 1, 1)
        rect.update(None, 2)
        self.assertEqual(f'[Square] ({rect.id}) 1/1 - 2', str(rect))

    def test_diff_type_w(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(1, 1, 1, 1).update(1, "hi")

    def test_diff_type_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, 1, 1, 1).update(2, 2, "hi")

    def test_diff_type_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, 1, 1).update(2, 2, 2, "hi")

    def test_0_w(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(1, 1, 1, 1).update(1, 0)

    def test_neg_w(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(1, 1, 1, 1).update(1, -1)

    def test_neg_x(self):
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            Square(1, 1, 1, 1).update(1, 1, -1)

    def test_neg_y(self):
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            Square(1, 1, 1, 1).update(1, 1, 1, -1)

    def test_w_bf_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(1).update(1, "hi", "ehlllo")

    def test_w_bf_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(1).update(1, "hi", 1, "ehlllo")

    def test_x_bf_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1).update(1, 2, "hi", "ehlllo")


class TestSquareUpdateKwargs(unittest.TestCase):
    """This is the unittest case for the update with key word arguments"""

    def test_no_args(self):
        rect = Square(1, 1, 1, 1)
        rect.update()
        self.assertEqual('[Square] (1) 1/1 - 1', str(rect))

    def test_one_arg(self):
        rect = Square(1)
        rect.update(x=1)
        self.assertEqual(f'[Square] ({rect.id}) 1/0 - 1', str(rect))

    def test_2_args(self):
        rect = Square(1)
        rect.update(x=3, y=4)
        self.assertEqual(f'[Square] ({rect.id}) 3/4 - 1', str(rect))

    def test_3_args(self):
        rect = Square(1)
        rect.update(id=2, x=3, y=5)
        self.assertEqual(f'[Square] (2) 3/5 - 1', str(rect))

    def test_4_args(self):
        rect = Square(2)
        rect.update(id=2, size=1, x=5)
        self.assertEqual(f'[Square] (2) 5/0 - 1', str(rect))

    def test_5_args(self):
        rect = Square(1)
        rect.update(id=2, size=2, x=1, y=1)
        self.assertEqual(f'[Square] (2) 1/1 - 2', str(rect))

    def test_more_args(self):
        rect = Square(1)
        rect.update(id=1, size=2, height=2, x=1, y=1, z=1)
        self.assertEqual(f'[Square] (1) 1/1 - 2', str(rect))

    def test_unknown_args(self):
        rect = Square(2)
        rect.update(s=2, v=8)
        self.assertEqual(f'[Square] ({rect.id}) 0/0 - 2', str(rect))

    def test_id_none(self):
        rect = Square(2)
        rect.update(id=None)
        self.assertEqual(f'[Square] ({rect.id}) 0/0 - 2', str(rect))

    def test_diff_type_w(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(1).update(size="ehllo")

    def test_diff_type_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2).update(x="ff")

    def test_diff_type_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1).update(y="shdlf")

    def test_0_w(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(1).update(size=0)

    def test_neg_w(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(1).update(size=-1)

    def test_neg_x(self):
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            Square(2).update(x=-2)

    def test_neg_y(self):
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            Square(2, 1).update(y=-5)


class TestSquareToDictionary(unittest.TestCase):
    """This is the unittesst case for the to_dictonary func of the square"""

    def test_no_arg(self):
        square = Square(2, 1, 1, 1)
        self.assertDictEqual(
                {'id': 1, 'size': 2, 'x': 1, 'y': 1},
                square.to_dictionary())

    def test_1_arg(self):
        with self.assertRaises(TypeError):
            Square(2).to_dictionary(2)

    def test_update(self):
        square1 = Square(3, 1, 1, 2)
        square2 = Square(2, 2, 2, 2)
        square2.update(**square1.to_dictionary())
        self.assertNotEqual(square1, square2)


if __name__ == "__main__":
    unittest.main()

