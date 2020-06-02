#!/usr/bin/python3
"""MyList Class"""


class MyList(list):
    """Custom list class"""
    def print_sorted(self):
        """Print sorted list"""
        nu = self.copy()
        nu.sort()
        print(nu)
