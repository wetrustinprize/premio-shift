import unittest

from premioshift.shifter import shift_message

class TestShifter(unittest.TestCase):
    def test_shift(self):
        message = "hello world"
        key = "abc123@"

        final_message = shift_message(message, key, shift=1)

        self.assertEqual(final_message, "igomq xqumf")
    
    def test_shift_to(self):
        message = "hello world"
        key = "abc123@"

        final_message = shift_message(message, key, cur_pos=0, shift_to=1)
        to_message = shift_message(final_message, key, cur_pos=1, shift_to=0)

        self.assertEqual(final_message, "igomq xqumf")
        self.assertEqual(to_message, "hello world")