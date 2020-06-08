#!/usr/bin/python3
"""base test file"""
import unittest
from models.base import Base
if __name__ = '__main__':
    unittest.main()


class TestBase(unittest.TestCase):
    """test class of Base"""
    def test_init(self):
        

    def test_module_docstring(self):
        """Module docstring check"""
        print("test_module_docstring")
        result = len(__import__('models.base').__doc__)
        self.assertTrue(result > 0, True)

    def test_class_docstring(self):
        """Class docstring check"""
        print("test_class_docstring")
        result = len(Base.__doc__)
        self.assertTrue(result > 0, True)

    def test_init_docstring(self):
        """Init docstring check"""
        print("test_init_docstring")
        result = len(self.__init__.__doc__)
        self.assertTrue(result > 0, True)        
    
    def test_to_json_string_docstring(self):
        """to_json_string docstring check"""
        print("test_to_json_string_docstring")
        result = len(Base.to_json_string.__doc__)
        self.assertTrue(result > 0, True)

    def test_save_to_file_docstring(self):
        """save_to_file docstring check"""
        print("test_save_to_file_docstring")
        result = len(Base.save_to_file.__doc__)
        self.assertTrue(result > 0, True)

    def test_from_json_string_docstring(self):
        """from_json_string docstring check"""
        print("test_from_json_string_docstring")
        result = len(Base.from_json_string.__doc__)
        self.assertTrue(result > 0, True)

    def test_create_docstring(self):
        """create docstring check"""
        print("test_create_docstring")
        result = len(Base.create.__doc__)
        self.assertTrue(result > 0, True)

    def test_load_from_file_docstring(self):
        """load_from_file docstring check"""
        print("test_load_from_file_docstring")
        result = len(Base.load_from_file.__doc__)
        self.assertTrue(result > 0, True)
