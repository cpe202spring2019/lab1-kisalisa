# Name: Lisa Li
# Assignment: Lab 1
# Course: Gaming 202
# Instructor: Paul Hatalsky
# Term: Spring 2019 


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
        loc3 = Location("SF", 35.3, -120.7)
        loc4 = Location("SF", 35, -120.7)
        loc5 = Location("SF", 35.3, 120.7)
        loc == loc1
        loc != loc2
        loc1 != loc3
        loc != "loc"
        loc3 != loc4
        loc3 != loc5


if __name__ == "__main__":
        unittest.main()
