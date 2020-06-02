#!/usr/bin/python3
"""my_int class"""


class MyInt(int):
    """jokerfied int"""
    def __eq__(self, other):
        """oppo"""
        return super().__ne__(other)
    
    def __ne__(self, other):
       """site"""
       return super().__eq__(other)
