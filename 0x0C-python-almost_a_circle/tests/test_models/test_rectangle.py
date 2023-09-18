#!/usr/bin/python3
"""This is the unittest for the Rectangle"""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_initialization(unittest.TestCase):
    """This test the initialization of a rectangle"""

    def test_instance(self):
        rect = Rectangle(2, 3)
        self.assertIsInstance(rect, Base)

    def test_no_arguments(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_argument(self):
        with self.assertRaises(TypeError):
            Rectangle(3)

    def test_2_args(self):
        rect1 = Rectangle(1, 2)
        rect2 = Rectangle(2, 3)
        self.assertEqual(rect1.id, rect2.id - 1)

    def test_3_args(self):
        rect1 = Rectangle(2, 1, 3)
        rect2 = Rectangle(2, 5, 4)
        self.assertEqual(rect1.id, rect2.id - 1)

    def test_4_args(self):
        rect1 = Rectangle(2, 1, 3, 3)
        rect2 = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect1.id, rect2.id - 1)

    def test_5_args(self):
        rect = Rectangle(1, 2, 4, 5, 3)
        self.assertEqual(3, rect.id)

    def test_more_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)


class TestRectangleWidth(unittest.TestCase):
    """This is the test case for With"""

    def test_private(self):
        rect = Rectangle(1, 2)
        with self.assertRaises(AttributeError):
            s = rect.__width

    def test_getter(self):
        rect = Rectangle(1, 3)
        self.assertEqual(1, rect.width)

    def test_setter(self):
        rect = Rectangle(1, 3)
        rect.width = 5
        self.assertEqual(rect.width, 5)

    def test_none(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 1)

    def test_int(self):
        self.assertEqual(Rectangle(1, 2).width, 1)

    def test_string(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("Hello", 2)

    def test_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(1.2, 1)

    def test_complex(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(12), 1)

    def test_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1], 1)

    def test_dictionary(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({'a': 1, 'b': 2}, 1)

    def test_set(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2}, 1)

    def test_tuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2), 1)

    def test_boolean(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 1)

    def test_range(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(23), 1)

    def test_byte(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(b'1231.2', 1)

    def test_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 1)

    def test_nan(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 1)

    def test_infinity(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 1)


class TestRectangleHeight(unittest.TestCase):
    """This is the test case for With"""

    def test_private(self):
        rect = Rectangle(1, 2)
        with self.assertRaises(AttributeError):
            s = rect.__height

    def test_getter(self):
        rect = Rectangle(1, 3)
        self.assertEqual(3, rect.height)

    def test_setter(self):
        rect = Rectangle(1, 3)
        rect.height = 5
        self.assertEqual(rect.height, 5)

    def test_none(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, None)

    def test_zero(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, 0)

    def test_int(self):
        self.assertEqual(Rectangle(1, 2).height, 2)

    def test_string(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, "Hello")

    def test_float(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 1.2)

    def test_complex(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, complex(12))

    def test_list(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, [1])

    def test_dictionary(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, {'a': 1, 'b': 2})

    def test_set(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, {1, 2})

    def test_tuple(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, (1, 2))

    def test_boolean(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, True)

    def test_range(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, range(23))

    def test_byte(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, b'1231.2')

    def test_negative(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -1)

    def test_nan(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float('nan'))

    def test_infinity(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float('inf'))


class TestRectangleX(unittest.TestCase):
    """This is the test case for With"""

    def test_private(self):
        rect = Rectangle(1, 2, 3)
        with self.assertRaises(AttributeError):
            s = rect.__x

    def test_getter(self):
        rect = Rectangle(1, 3, 4)
        self.assertEqual(4, rect.x)

    def test_setter(self):
        rect = Rectangle(1, 3, 1)
        rect.x = 5
        self.assertEqual(rect.x, 5)

    def test_none(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, None)

    def test_zero(self):
        self.assertEqual(Rectangle(1, 2, 0, 0).y, 0)

    def test_int(self):
        self.assertEqual(Rectangle(1, 2, 1).x, 1)

    def test_string(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, 'hi')

    def test_float(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, 1.2)

    def test_complex(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, complex(12))

    def test_list(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, [2])

    def test_dictionary(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {'a': 1, 'b': 2})

    def test_set(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 1, {1, 2})

    def test_tuple(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 1, (1, 2))

    def test_boolean(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 1, True)

    def test_range(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 1, range(23))

    def test_byte(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 1, b'1231.2')

    def test_negative(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 1, -1)

    def test_nan(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, float('nan'))

    def test_infinity(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, float('inf'))


class TestRectangleY(unittest.TestCase):
    """This is the test case for With"""

    def test_private(self):
        rect = Rectangle(1, 2, 2, 3)
        with self.assertRaises(AttributeError):
            s = rect.__y

    def test_getter(self):
        rect = Rectangle(1, 3, 2, 4)
        self.assertEqual(4, rect.y)

    def test_setter(self):
        rect = Rectangle(1, 3, 1, 1)
        rect.y = 5
        self.assertEqual(rect.y, 5)

    def test_none(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, None)

    def test_zero(self):
        self.assertEqual(Rectangle(1, 2, 0, 0).y, 0)

    def test_int(self):
        self.assertEqual(Rectangle(1, 2, 1, 1).y, 1)

    def test_string(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, 'hi')

    def test_float(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, 1.2)

    def test_complex(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, complex(12))

    def test_list(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, [2])

    def test_dictionary(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, {'a': 1, 'b': 2})

    def test_set(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 1, 1, {1, 2})

    def test_tuple(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 1, 1, (1, 2))

    def test_boolean(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 1, 1, True)

    def test_range(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 1, 1, range(23))

    def test_byte(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 1, 1, b'1231.2')

    def test_negative(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 1, 1, -1)

    def test_nan(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, float('nan'))

    def test_infinity(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, float('inf'))


class TestRectangleArea(unittest.TestCase):
    """The unittest class for the area test"""

    def test_norm(self):
        rect = Rectangle(1, 2, 0, 0, 1)
        self.assertEqual(rect.area(), 2)

    def test_with_arg(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(2, 3)
            rect.area(23)

    def test_with_changes(self):
        rect = Rectangle(3, 4)
        rect.width = 5
        rect.height = 5
        self.assertEqual(rect.area(), 25)

    def test_large_numbers(self):
        rect = Rectangle(99999999999999999999999, 999999999999999999)
        self.assertEqual(rect.area(),
                         99999999999999999899999000000000000000001)


class TestRectangleStr(unittest.TestCase):
    """This is the unittest case for the __str__"""

    @staticmethod
    def get_str_res(rect):
        """Returns the str representation of the rectangle"""
        import contextlib
        import io
        cap = io.StringIO()
        with contextlib.redirect_stdout(cap):
            print(rect)
        return cap.getvalue()

    def test_normal(self):
        rect = Rectangle(1, 1, 1, 1, 1)
        self.assertEqual("[Rectangle] (1) 1/1 - 1/1\n",
                         TestRectangleStr.get_str_res(rect))

    def test_change(self):
        rect = Rectangle(1, 1, 1, 1, 1)
        rect.id = 2
        rect.width = 2
        rect.height = 2
        rect.x = 2
        rect.y = 2
        self.assertEqual("[Rectangle] (2) 2/2 - 2/2\n",
                         TestRectangleStr.get_str_res(rect))

    def test_w_and_h(self):
        rect = Rectangle(2, 2)
        self.assertEqual("[Rectangle] ({}) 0/0 - 2/2".format(rect.id),
                         str(rect))

    def test_w_and_h_and_x(self):
        rect = Rectangle(1, 1, 1)
        self.assertEqual("[Rectangle] ({}) 1/0 - 1/1".format(rect.id),
                         str(rect))

    def test_w_and_h_and_x_and_y(self):
        rect = Rectangle(1, 1, 1, 1)
        self.assertEqual(f"[Rectangle] ({rect.id}) 1/1 - 1/1",
                         str(rect))

    def test_w_h_x_y_id(self):
        rect = Rectangle(1, 1, 1, 1, 1)
        self.assertEqual("[Rectangle] (1) 1/1 - 1/1", str(rect))


class TestRectangleDisplay(unittest.TestCase):
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
            Rectangle(2, 3).display(2)

    def test_normal(self):
        rect = Rectangle(2, 4)
        self.assertEqual("##\n##\n##\n##\n",
                         TestRectangleDisplay.get_display_res(rect))

    def test_change(self):
        rect = Rectangle(5, 4, 0, 0, 0)
        rect.width = 1
        rect.height = 1
        self.assertEqual("#\n",
                         TestRectangleDisplay.get_display_res(rect))

    def test_with_x(self):
        rect = Rectangle(1, 2, 1, 0)
        self.assertEqual(" #\n #\n",
                         TestRectangleDisplay.get_display_res(rect))

    def test_with_y(self):
        rect = Rectangle(2, 2, 0, 1)
        self.assertEqual("\n##\n##\n",
                         TestRectangleDisplay.get_display_res(rect))

    def test_with_x_and_y(self):
        rect = Rectangle(2, 2, 2, 2)
        self.assertEqual("\n\n  ##\n  ##\n",
                         TestRectangleDisplay.get_display_res(rect))


class TestRectangleUpdateArgs(unittest.TestCase):
    """This is the unit test case for update function"""

    def test_with_no_args(self):
        rect = Rectangle(1, 1, 1, 1, 1)
        rect.update()
        self.assertEqual("[Rectangle] (1) 1/1 - 1/1", str(rect))

    def test_one_arg(self):
        rect = Rectangle(1, 1)
        rect.update(1)
        self.assertEqual('[Rectangle] (1) 0/0 - 1/1', str(rect))

    def test_2_args(self):
        rect = Rectangle(1, 2)
        rect.update(2, 2)
        self.assertEqual('[Rectangle] (2) 0/0 - 2/2', str(rect))

    def test_3_args(self):
        rect = Rectangle(1, 1, 1, 1, 1)
        rect.update(2, 2, 2)
        self.assertEqual('[Rectangle] (2) 1/1 - 2/2', str(rect))

    def test_4_args(self):
        rect = Rectangle(1, 1, 1, 1, 1)
        rect.update(2, 2, 2, 2)
        self.assertEqual('[Rectangle] (2) 2/1 - 2/2', str(rect))

    def test_5_args(self):
        rect = Rectangle(1, 1, 1, 1, 1)
        rect.update(2, 2, 2, 2, 2)
        self.assertEqual('[Rectangle] (2) 2/2 - 2/2', str(rect))

    def test_more_args(self):
        rect = Rectangle(1, 1, 1, 1, 1)
        rect.update(2, 2, 2, 2, 2, 2)
        self.assertEqual('[Rectangle] (2) 2/2 - 2/2', str(rect))

    def test_double_update(self):
        rect = Rectangle(1, 1, 1, 1, 1)
        rect.update(2, 2, 2, 2, 2)
        rect.update(3, 3, 3, 3, 3)
        self.assertEqual('[Rectangle] (3) 3/3 - 3/3', str(rect))

    def test_none_id(self):
        rect = Rectangle(1, 1, 1, 1, 1)
        rect.update(None, 2, 3)
        self.assertEqual(f'[Rectangle] ({rect.id}) 1/1 - 2/3', str(rect))

    def test_diff_type_w(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(1, 1, 1, 1, 1).update(1, "hi")

    def test_diff_type_h(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 1, 1, 1, 1).update(2, 2, 'hi')

    def test_diff_type_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, 1, 1, 1).update(2, 2, 2, "hi")

    def test_diff_type_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, 1, 1).update(2, 2, 2, 2, "hi")

    def test_0_w(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(1, 1, 1, 1, 1).update(1, 0)

    def test_0_h(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 1, 1, 1, 1).update(1, 1, 0)

    def test_neg_w(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(1, 1, 1, 1, 1).update(1, -1)

    def test_neg_h(self):
        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            Rectangle(1, 1, 1, 1, 1).update(1, 1, -1)

    def test_neg_x(self):
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            Rectangle(1, 1, 1, 1, 1).update(1, 1, 1, -1)

    def test_neg_y(self):
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            Rectangle(1, 1, 1, 1, 1).update(1, 1, 1, 1, -1)

    def test_w_bf_h(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(1, 1).update(1, "hi", "ehlllo")

    def test_w_bf_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(1, 1).update(1, "hi", 1, "ehlllo")

    def test_w_bf_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(1, 1).update(1, "hi", 1, 1, "ehlllo")

    def test_h_bf_x(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 1).update(1, 2, "hi", "ehlllo")

    def test_h_bf_y(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 1).update(1, 2, "hi", 2, "ehlllo")

    def test_x_bf_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1).update(1, 2, 2, "hi", "ehlllo")


class TestRectangleUpdateKwargs(unittest.TestCase):
    """This is the unittest case for the update with key word arguments"""

    def test_no_args(self):
        rect = Rectangle(1, 1, 1, 1, 1)
        rect.update()
        self.assertEqual('[Rectangle] (1) 1/1 - 1/1', str(rect))

    def test_one_arg(self):
        rect = Rectangle(1, 1)
        rect.update(x=1)
        self.assertEqual(f'[Rectangle] ({rect.id}) 1/0 - 1/1', str(rect))

    def test_2_args(self):
        rect = Rectangle(1, 1)
        rect.update(x=3, y=4)
        self.assertEqual(f'[Rectangle] ({rect.id}) 3/4 - 1/1', str(rect))

    def test_3_args(self):
        rect = Rectangle(1, 2)
        rect.update(id=2, x=3, y=5)
        self.assertEqual(f'[Rectangle] (2) 3/5 - 1/2', str(rect))

    def test_4_args(self):
        rect = Rectangle(2, 3)
        rect.update(id=2, width=1, height=1, x=5)
        self.assertEqual(f'[Rectangle] (2) 5/0 - 1/1', str(rect))

    def test_5_args(self):
        rect = Rectangle(1, 1)
        rect.update(id=2, width=2, height=2, x=1, y=1)
        self.assertEqual(f'[Rectangle] (2) 1/1 - 2/2', str(rect))

    def test_more_args(self):
        rect = Rectangle(1, 1)
        rect.update(id=1, width=2, height=2, x=1, y=1, z=1)
        self.assertEqual(f'[Rectangle] (1) 1/1 - 2/2', str(rect))

    def test_unknown_args(self):
        rect = Rectangle(2, 2)
        rect.update(s=2, v=8)
        self.assertEqual(f'[Rectangle] ({rect.id}) 0/0 - 2/2', str(rect))

    def test_id_none(self):
        rect = Rectangle(2, 2)
        rect.update(id=None)
        self.assertEqual(f'[Rectangle] ({rect.id}) 0/0 - 2/2', str(rect))

    def test_diff_type_w(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(1, 1).update(width="ehllo")

    def test_diff_type_h(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, 1).update(height="helli")

    def test_diff_type_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 2).update(x="ff")

    def test_diff_type_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1).update(y="shdlf")

    def test_0_w(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(1, 1).update(width=0)

    def test_0_h(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, 2).update(height=0)

    def test_neg_w(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(1, 2).update(width=-1)

    def test_neg_h(self):
        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            Rectangle(2, 2).update(height=-2)

    def test_neg_x(self):
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            Rectangle(2, 3).update(x=-2)

    def test_neg_y(self):
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            Rectangle(2, 1).update(y=-5)


class TestRectangleToDictionary(unittest.TestCase):
    """This is the test case class for the to_dictionary func"""

    def test_no_arg(self):
        rect = Rectangle(1, 1, 1, 1, 1)
        self.assertDictEqual(
                {'id': 1, 'width': 1, 'height': 1, 'x': 1, 'y': 1},
                rect.to_dictionary())

    def test_1_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 2).to_dictionary(3)

    def test_not_equal(self):
        rect1 = Rectangle(2, 3)
        rect2 = Rectangle(3, 4)
        rect2.update(**rect1.to_dictionary())
        self.assertNotEqual(rect1, rect2)


if __name__ == "__main__":
    unittest.main()
