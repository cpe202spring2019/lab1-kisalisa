import unittest
from lab1 import *
import lab1

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """tests max_list_iter for lists with unique values, duplicates,
           empty lists, and for max values that are negative, and in the last, first, middle, and 
           when a list is None"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        self.assertIsNone(max_list_iter([]))
        self.assertEqual(max_list_iter([1, 2, 3]), 3)
        self.assertEqual(max_list_iter([1, 3, 2]), 3)
        self.assertEqual(max_list_iter([3, 1, 2]), 3)
        self.assertEqual(max_list_iter([3, 3, 3]), 3)
        self.assertEqual(max_list_iter([3, 3, 1]), 3)
        self.assertEqual(max_list_iter([1, 3, 3]), 3)
        self.assertEqual(max_list_iter([3, 1, 3]), 3)
        self.assertEqual(max_list_iter([0, 0, 0]), 0)
        self.assertEqual(max_list_iter([-1, -2, -3]), -1)

    def test_reverse_rec(self):
        """tests reverse_rec for exception, for random list lengths, if the list
           is empty, and if it has one value"""
        tlist = None
        with self.assertRaises(ValueError):
            reverse_rec(tlist)
        self.assertEqual(reverse_rec([1,2,3]), [3,2,1])
        self.assertEqual(reverse_rec([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])
        self.assertEqual(reverse_rec([0, 9, 8, 7, 6]), [6, 7, 8, 9, 0])
        self.assertEqual(reverse_rec([]), [])
        self.assertEqual(reverse_rec([1]), [1])
        self.assertEqual(reverse_rec([5, 10]), [10, 5])
        self.assertEqual(reverse_rec([3, 3, 3]), [3, 3, 3])


    def test_bin_search(self):
        """tests bin_search for item not found, exception, item at middle of list, item at beginning,
           and item at end"""
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(4, 0, len(list_val) - 1, list_val), 4) # item at middle
        self.assertEqual(bin_search(10, 0, 10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 10) # item at end
        self.assertEqual(bin_search(0, 0, 2, [0, 1, 2]), 0) # item at beginning
        self.assertIsNone(bin_search(1, 0, 2, [0, 0, 0])) # item not in list
        self.assertEqual(bin_search(1, 0, 2, [0, 1, 2]), 1) # item in middle 
        self.assertEqual(bin_search(2, 0, 2, [0, 1, 2]), 2) # item at end
        self.assertEqual(bin_search(-2, 0, 2, [-2, 0, 2]), 0) # item with negative values
        self.assertIsNone(bin_search(0, 0, 0, [])) # empty list
        self.assertEqual(bin_search(0, 0, 0, [0]), 0) # one item list
        self.assertIsNone(bin_search(1, 6, 2, list_val)) # low > high
        self.assertIsNone(bin_search(1, 2, 4, list_val)) # val not in list range
        self.assertIsNone(bin_search(4, 10, 11, list_val)) # low, high not in list
        self.assertIsNone(bin_search(4, 0, 0, [0]))
        tlist = None
        with self.assertRaises(ValueError):
            bin_search(2, 3, 1, tlist)
        

if __name__ == "__main__":
        unittest.main()
