import unittest

from premioshift.shifter import key_to_shifts

class TestKeys(unittest.TestCase):
    def test_conversion(self):
        key = "hello world 123 @"
        key_shifts = key_to_shifts(key)

        self.assertEqual(key_shifts, [8,5,12,12,15,23,15,18,12,4,1,2,3])