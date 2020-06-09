#!/usr/bin/python3
"""base test file"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """test class of Base"""
    def setUp(self):
        """set up"""
        print('setUp')
        self.b1 = Base()
        self.b2 = Base(12)
        self.b3 = Base(12)
        self.b4 = Base()
        self.b5 = Base()

    def tearDown(self):
        print('tearDown')
        del self.b1
        del self.b2
        del self.b3
        del self.b4
        del self.b5

    def test_init(self):
        """test init"""
        print("test_init")
        # b1
        self.assertIsNotNone(self.b1)
        self.assertIsInstance(self.b1, Base)
        self.assertEqual(self.b1.id, 1)
        #b2
        self.assertIsNotNone(self.b2)
        self.assertIsInstance(self.b2, Base)
        self.assertEqual(self.b2.id, 12)
        #b3
        self.assertIsNotNone(self.b3)
        self.assertIsInstance(self.b3, Base)
        self.assertEqual(self.b3.id, 12)
        #b4
        self.assertIsNotNone(self.b4)
        self.assertIsInstance(self.b4, Base)
        self.assertEqual(self.b4.id, 2)
        #b5
        self.assertIsNotNone(self.b5)
        self.assertIsInstance(self.b5, Base)
        self.assertEqual(self.b5.id, 3)

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
