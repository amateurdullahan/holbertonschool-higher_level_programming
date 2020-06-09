#!/usr/bin/python3
"""contains test file for square"""
import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestSquare(unittest.TestCase):
    """test square class"""
    def setUp(self):
        """set up"""
        print('setUp')
        self.s1 = Square(5)
        self.s2 = Square(5, 10)
        self.s3 = Square(5, 10, 15)
        self.s4 = Square(2, 4, 6, 8)
    
    def tearDown(self):
        """tear down"""
        print('tearDown')
        del self.s1
        del self.s2
        del self.s3
        del self.s4


    def test_init(self):
        """init test"""
        print("test_init")
        
        # s1 tests
        self.assertIsNotNone(self.s1)
        self.assertIsInstance(self.s1, Base)
        self.assertIsInstance(self.s1, Rectangle)
        self.assertIs(type(self.s1), Square)
        self.assertEqual(self.s1.id, 1)
        self.assertEqual(self.s1.width, 5)
        self.assertEqual(self.s1.height, 5)
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s1.y, 0)
        # s2 tests
        self.assertIsNotNone(self.s2)
        self.assertIsInstance(self.s2, Base)
        self.assertIsInstance(self.s2, Rectangle)
        self.assertIs(type(self.s2), Square)
        self.assertEqual(self.s2.id, 2)
        self.assertEqual(self.s2.width, 5)
        self.assertEqual(self.s2.height, 5)
        self.assertEqual(self.s2.x, 10)
        self.assertEqual(self.s2.y, 0)
        # s3 tests
        self.assertIsNotNone(self.s3)
        self.assertIsInstance(self.s3, Base)
        self.assertIsInstance(self.s3, Rectangle)
        self.assertIs(type(self.s3), Square)
        self.assertEqual(self.s3.id, 3)
        self.assertEqual(self.s3.width, 5)
        self.assertEqual(self.s3.height, 5)
        self.assertEqual(self.s3.x, 10)
        self.assertEqual(self.s3.y, 15)
        # s4 tests
        self.assertIsNotNone(self.s4)
        self.assertIsInstance(self.s4, Base)
        self.assertIsInstance(self.s4, Rectangle)
        self.assertIs(type(self.s4), Square)
        self.assertEqual(self.s4.id, 8)
        self.assertEqual(self.s4.width, 2)
        self.assertEqual(self.s2.height, 2)
        self.assertEqual(self.s4.x, 4)
        self.assertEqual(self.s4.y, 6)

        def test_attributes(self):
            """test raised exceptions"""
            print("test_attributes")
            
            # s1
            with self.assertRaises(TypeError):
                self.s1.__init__(None, 2)
            with self.assertRaises(TypeError):
                self.s1.__init__("howdy", 17)
            with self.assertRaises(TypeError):
                self.s1.__init__([1, 2, 3], 12, 13, 14)
            # s2
            with self.assertRaises(TypeError):
                self.s2.__init__(4, False, 2)
            with self.assertRaises(TypeError):
                self.s2.__init__(1, 2, (3, ))
            
            # s3
            with self.assertRaises(ValueError):
                self.s3.__init__(4, -3, 4)
            with self.assertRaises(ValueError):
                self.s3.__init__(0, 0, 0)

            # s4
            with self.assertRaises(TypeError):
                self.s4.__init__(True, 1, 2, 3)
            with self.assertRaises(TypeError):
                self.s4.__init__(1, 2, False, 4)

    def test_area(self):
        """test area method"""
        print("test_area")
        # s1
        self.assertEqual(self.s1.area(), 25)
        # s2
        self.assertEqual(self.s2.area(), 25)
        # s3
        self.assertEqual(self.s3.area(), 25)
        # s4
        self.assertEqual(self.s4.area(), 4)

    def test_display(self):
        """test display method"""
        pass

    def test_str(self):
        """test str method"""
        print("test_str")
        # s1
        self.assertEqual(self.s1.__str__(), "[Square] (1) 0/0 - 5")
        # s2
        self.assertEqual(self.s2.__str__(), "[Square] (2) 10/0 - 5")
        # s3
        self.assertEqual(self.s3.__str__(), "[Square] (3) 10/15 - 5")
        # s4
        self.assertEqual(self.s4.__str__(), "[Square] (8) 4/6 - 2")

    def test_update_args(self):
        """test update method with args"""
        print("test_update_args")
        self.assertEqual(self.s1.__str__(), "[Square] (1) 0/0 - 5")
        self.s1.update(69)
        self.assertEqual(self.s1.__str__(), "[Square] (69) 0/0 - 5")
        self.s1.update(2, 4)
        self.assertEqual(self.s1.__str__(), "[Square] (2) 0/0 - 4")
        self.s1.update(2, 4, 6)
        self.assertEqual(self.s1.__str__(), "[Square] (2) 6/0 - 4")
        self.s1.update(2, 4, 6, 8)
        self.assertEqual(self.s1.__str__(), "[Square] (2) 6/8 - 4")

    def test_update_kwargs(self):
        """test update method with kwargs"""
        print("test_update_kwargs")
        self.s1.update(x=69)
        self.assertEqual(self.s1.__str__(), "[Square] (1) 69/0 - 5")
        self.s1.update(size=2, y=13)
        self.assertEqual(self.s1.__str__(), "[Square] (1) 69/13 - 2")
        self.s1.update(size=7, id=89, y=1)
        self.assertEqual(self.s1.__str__(), "[Square] (89) 69/1 - 7")

    def test_module_docstring(self):
        """Module Docstring Check"""
        print("test_module_docstring")
        result = len(__import__('models.square').__doc__)
        self.assertTrue(result > 0, True)

    def test_class_docstring(self):
        """Class Docstring Test"""
        print("test_class_docstring")
        result = len(Square.__doc__)
        self.assertTrue(result > 0, True)

    def test_init_docstring(self):
        """init Docstring Test"""
        print("test_init_docstring")
        result = len(self.__init__.__doc__)
        self.assertTrue(result > 0, True)

    def test_size_getter_docstring(self):
        """size_getter Docstring Test"""
        print("test_size_getter_docstring")
        result = len(Square.size.__doc__)
        self.assertTrue(result > 0, True)

    def test_x_getter_docstring(self):
        """x_getter Docstring Test"""
        print("test_x_getter_docstring")
        result = len(Square.x.__doc__)
        self.assertTrue(result > 0, True)

    def test_y_getter_docstring(self):
        """y_getter Docstring Test"""
        print("test_y_getter_docstring")
        result = len(Square.y.__doc__)
        self.assertTrue(result > 0, True)

    def test_area_docstring(self):
        """area Docstring Test"""
        print("test_area_docstring")
        result = len(Square.area.__doc__)
        self.assertTrue(result > 0, True)

    def test_display_docstring(self):
        """display Docstring Test"""
        print("test_display_docstring")
        result = len(Square.display.__doc__)
        self.assertTrue(result > 0, True)

    def test_str_docstring(self):
        """str Docstring Test"""
        print("test_str_docstring")
        result = len(Square.__str__.__doc__)
        self.assertTrue(result > 0, True)

    def test_update_docstring(self):
        """update Docstring Test"""
        print("test_update_docstring")
        result = len(Square.update.__doc__)
        self.assertTrue(result > 0, True)

    def test_to_dictionary_docstring(self):
        """to_dictionary Docstring Test"""
        print("test_to_dictionary_docstring")
        result = len(Square.to_dictionary.__doc__)
        self.assertTrue(result > 0, True)
