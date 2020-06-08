#!/usr/bin/python3
"""contains rectangle tests"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
if __name__ == '__main__':
    unittest.main()


class TestRectangle(unittest.TestCase):
    """class to test rectangle"""
    def test_init(self):
        """init test"""



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
