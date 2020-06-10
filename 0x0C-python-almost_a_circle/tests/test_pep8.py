#!/usr/bin/python3
"""test pep8"""
import unittest
import pep8


class TestCodeFormat(unittest.TestCase):
    """test pep8"""
    def test_pep8_base(self):
        """test pep8 base.py"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0)

    def test_pep8_rectangle(self):
        """test pep8 rectangle.py"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0)

    def test_pep8_square(self):
        """test pep8 square.py"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0)
