import unittest
from day8 import *


class MyTestCase(unittest.TestCase):

    def test_SimpleTestPass(self):
        self.assertEqual(True, True)

    # def test_SimpleTestFail(self):
    #     self.assertEqual(True, False)

    def test_dictionary(self):
        dict1 = {}
        dict1['test1'] = None
        dict1['test2'] = "test number 2"
        dict1[123] = "onetwothree"
        self.assertEqual(dict1['test1'], None)
        self.assertEqual(dict1['test2'], "test number 2")
        self.assertEqual(dict1[123], "onetwothree")






