import unittest

from premioshift import Shift

class TestShiftClass(unittest.TestCase):
    def setUp(self):
        self.message = "hello world"
        self.key = "abc123@"
        self.shift = Shift()

    def test_message(self):
        self.shift.set_message("hello world")
        self.assertEqual(self.shift.message, self.message)

    def test_key(self):
        self.shift.set_key(self.key)
        self.assertEqual(self.shift.key, self.key)

    def test_shift(self):
        self.shift.shift(1)
        self.assertNotEqual(self.shift.message, self.message)
        self.assertEqual(self.shift.position, 1)

        self.shift.shift(1, dont_save=True)
        self.assertNotEqual(self.shift.position, 2)