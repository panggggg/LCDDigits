import unittest
from lcd_digits import LCDDigits


class TestLCDDigits(unittest.TestCase):
    def test_create_LDCDigits_push_0_should_be_return_LCDDigits_0(self):
        # arrange
        first_line = "._.\n"
        second_line = "|.|\n"
        third_line = "|_|"
        expected = first_line + second_line + third_line
        # action
        lcd_digits = LCDDigits()
        actual = lcd_digits.create_LCD(number=0)
        # assert
        self.assertEquals(expected, actual)