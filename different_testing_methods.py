import doctest
import sys
import unittest


def add(a: int, b: int) -> int:
    """Return the addition of a and b
    
    >>> add(44, 33)
    77
    >>> add(0, 0)
    100
    """

    return a + b


class TestFunctions(unittest.TestCase):
    """Can be used in pytest: $ py.test"""

    def test_add_two_numbers(self):
        self.assertEqual(add(44, 33), 77)

    def test_fail(self):
        self.assertEqual(add(0, 0), 100)


def test_add_function():
    """Using pytest: $ py.test"""

    assert add(44, 33) == 77
    assert add(0, 0) == 100


if __name__=='__main__':
    """Also can be used as:
    $ python -m unittest different_testing_methods.py
    $ python -m doctest different_testing_methods.py
    """

    if sys.argv[1] == 'u':
        unittest.main(argv=['first-arg-is-ignored'])
    elif sys.argv[1] == 'd':
        doctest.testmod()