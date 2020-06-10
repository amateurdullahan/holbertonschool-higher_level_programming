#!/usr/bin/python3
"""contains rectangle tests"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """class to test rectangle"""
    @classmethod
    def setUpClass(cls):
        """setupclass"""
        print("setupClass")

    @classmethod
    def tearDownClass(cls):
        """teardownclass"""
        print("teardownClass")

    def setUp(self):
        """setup"""
        print("setUp")
        self.r1 = Rectangle(10, 1)
        self.r2 = Rectangle(1, 10)
        self.r3 = Rectangle(1, 2, 3, 4, 5)
        self.r4 = Rectangle(5, 4, 3, 2, 1)

    def tearDown(self):
        """teardown"""
        print("tearDown")
        del self.r1
        del self.r2
        del self.r3
        del self.r4

    def test_ainit(self):
        """init test"""
        print("test_init")
        # r1
        self.assertIsNotNone(self.r1)
        self.assertIsInstance(self.r1, Base)
        self.assertIs(type(self.r1), Rectangle)
        self.assertEqual(self.r1.id, 28)
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r1.height, 1)
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r1.y, 0)
        # r2
        self.assertIsNotNone(self.r2)
        self.assertIsInstance(self.r2, Base)
        self.assertIs(type(self.r2), Rectangle)
        self.assertEqual(self.r2.id, 29)
        self.assertEqual(self.r2.width, 1)
        self.assertEqual(self.r2.height, 10)
        self.assertEqual(self.r2.x, 0)
        self.assertEqual(self.r2.y, 0)
        # r3
        self.assertIsNotNone(self.r3)
        self.assertIsInstance(self.r3, Base)
        self.assertIs(type(self.r3), Rectangle)
        self.assertEqual(self.r3.id, 5)
        self.assertEqual(self.r3.width, 1)
        self.assertEqual(self.r3.height, 2)
        self.assertEqual(self.r3.x, 3)
        self.assertEqual(self.r3.y, 4)
        # r4
        self.assertIsNotNone(self.r4)
        self.assertIsInstance(self.r4, Base)
        self.assertIs(type(self.r4), Rectangle)
        self.assertEqual(self.r4.id, 1)
        self.assertEqual(self.r4.width, 5)
        self.assertEqual(self.r4.height, 4)
        self.assertEqual(self.r4.x, 3)
        self.assertEqual(self.r4.y, 2)

    def test_validate_attr(self):
        """test exceptions"""
        print("test_validate_attr")
        # r1
        with self.assertRaises(TypeError):
            self.r1.__init__("poop", 1)
        with self.assertRaises(TypeError):
            self.r1.__init__([], 12)
        # r2
        with self.assertRaises(TypeError):
            self.r2.__init__(2, False)
        with self.assertRaises(TypeError):
            self.r2.__init__(4, None)
        # r3
        with self.assertRaises(ValueError):
            self.r3.__init__(-3, 12)
        with self.assertRaises(ValueError):
            self.r3.__init__(0, 1)
        # r4
        with self.assertRaises(ValueError):
            self.r4.__init__(4, 0)
        with self.assertRaises(ValueError):
            self.r4.__init__(2, -6)

    def test_display(self):
        """test display"""
        pass

    def test_str(self):
        """test str"""
        print("test_str")
        self.assertEqual(self.r1.__str__(),
                         "[Rectangle] ({}) 0/0 - 10/1".format(self.r1.id))
        self.assertEqual(self.r2.__str__(),
                         "[Rectangle] ({}) 0/0 - 1/10".format(self.r2.id))
        self.assertEqual(self.r3.__str__(),
                         "[Rectangle] ({}) 3/4 - 1/2".format(self.r3.id))
        self.assertEqual(self.r4.__str__(),
                         "[Rectangle] ({}) 3/2 - 5/4".format(self.r4.id))

    def test_area(self):
        """Test area"""
        print("test_area")
        # r1
        self.assertEqual(self.r1.area(), 10)
        # r2
        self.assertEqual(self.r2.area(), 10)
        # r3
        self.assertEqual(self.r3.area(), 2)
        # r4
        self.assertEqual(self.r4.area(), 20)

    def test_update_args(self):
        """Test update args"""
        print("test_update_args")
        self.assertEqual(self.r1.__str__(),
                         "[Rectangle] ({}) 0/0 - 10/1".format(self.r1.id))
        self.r1.update(69)
        self.assertEqual(self.r1.__str__(), "[Rectangle] (69) 0/0 - 10/1")
        self.r1.update(69, 2)
        self.assertEqual(self.r1.__str__(), "[Rectangle] (69) 0/0 - 2/1")
        self.r1.update(69, 2, 3)
        self.assertEqual(self.r1.__str__(), "[Rectangle] (69) 0/0 - 2/3")
        self.r1.update(69, 2, 3, 4)
        self.assertEqual(self.r1.__str__(), "[Rectangle] (69) 4/0 - 2/3")
        self.r1.update(69, 2, 3, 4, 5)
        self.assertEqual(self.r1.__str__(), "[Rectangle] (69) 4/5 - 2/3")

    def test_update_kwargs(self):
        """test update kwargs"""
        print("test_update_kwargs")
        self.assertEqual(self.r1.__str__(),
                         "[Rectangle] ({}) 0/0 - 10/1".format(self.r1.id))
        self.r1.update(id=69)
        self.assertEqual(self.r1.__str__(), "[Rectangle] (69) 0/0 - 10/1")
        self.r1.update(width=2)
        self.assertEqual(self.r1.__str__(), "[Rectangle] (69) 0/0 - 2/1")
        self.r1.update(height=3)
        self.assertEqual(self.r1.__str__(), "[Rectangle] (69) 0/0 - 2/3")
        self.r1.update(x=4)
        self.assertEqual(self.r1.__str__(), "[Rectangle] (69) 4/0 - 2/3")
        self.r1.update(y=5)
        self.assertEqual(self.r1.__str__(), "[Rectangle] (69) 4/5 - 2/3")

    def test_module_doctstring(self):
        """Module docstring check"""
        print("test_module_docstring")
        result = len(__import__('models.rectangle').__doc__)
        self.assertTrue(result > 0, True)

    def test_class_docstring(self):
        """Class docstring check"""
        print("test_class_docstring")
        result = len(Rectangle.__doc__)
        self.assertTrue(result > 0, True)

    def test_init_docstring(self):
        """Init docstring check"""
        print("test_init_docstring")
        result = len(self.__init__.__doc__)
        self.assertTrue(result > 0, True)

    def test_width_getter_docstring(self):
        """width_getter Docstring Test"""
        print("test_width_getter_docstring")
        result = len(Rectangle.width.__doc__)
        self.assertTrue(result > 0, True)

    def test_height_getter_docstring(self):
        """height_getter Docstring Test"""
        print("test_height_getter_docstring")
        result = len(Rectangle.height.__doc__)
        self.assertTrue(result > 0, True)

    def test_x_getter_docstring(self):
        """x_getter Docstring Test"""
        print("test_x_getter_docstring")
        result = len(Rectangle.x.__doc__)
        self.assertTrue(result > 0, True)

    def test_y_getter_docstring(self):
        """y_getter Docstring Test"""
        print("test_y_getter_docstring")
        result = len(Rectangle.y.__doc__)
        self.assertTrue(result > 0, True)

    def test_area_docstring(self):
        """area Docstring Test"""
        print("test_area_docstring")
        result = len(Rectangle.area.__doc__)
        self.assertTrue(result > 0, True)

    def test_display_docstring(self):
        """display Docstring Test"""
        print("test_display_docstring")
        result = len(Rectangle.display.__doc__)
        self.assertTrue(result > 0, True)

    def test_str_docstring(self):
        """str Docstring Test"""
        print("test_str_docstring")
        result = len(Rectangle.__str__.__doc__)
        self.assertTrue(result > 0, True)

    def test_update_docstring(self):
        """update Docstring Test"""
        print("test_update_docstring")
        result = len(Rectangle.update.__doc__)
        self.assertTrue(result > 0, True)

    def test_to_dictionary_docstring(self):
        """to_dictionary Docstring Test"""
        print("test_to_dictionary_docstring")
        result = len(Rectangle.to_dictionary.__doc__)
        self.assertTrue(result > 0, True)

if __name__ == '__main__':
    unittest.main()
