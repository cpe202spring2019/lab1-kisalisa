import unittest
from location import *


class TestLab1(unittest.TestCase):


    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        loc1 = Location("Paris", 48.9, 2.4)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
        self.assertEqual(repr(loc1),"Location('Paris', 48.9, 2.4)")


    def test_eq(loc):
        loc = Location("SLO", 35.3, -120.7)
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("Paris", 48.9, 2.4)
        loc == loc1
        loc != loc2
        loc != "loc"


if __name__ == "__main__":
        unittest.main()
