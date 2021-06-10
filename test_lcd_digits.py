import unittest
from lcd_digits import LCDDigits


class TestLCDDigits(unittest.TestCase):
    def setUp(self):
        self.lcd_digits = LCDDigits()

    def test_create_LDCDigits_push_0_should_be_return_LCDDigits_0(self):
        # arrange
        first_line = "._.\n"
        second_line = "|.|\n"
        third_line = "|_|"
        expected = first_line + second_line + third_line
        # action
        actual = self.lcd_digits.create_LCD(number=0)
        # assert
        self.assertEquals(expected, actual)

    def test_create_LDCDigits_push_1_should_be_return_LCDDigits_1(self):
        # arrange
        first_line = "...\n"
        second_line = "..|\n"
        third_line = "..|"
        expected = first_line + second_line + third_line
        # action
        actual = self.lcd_digits.create_LCD(number=1)
        # assert
        self.assertEquals(expected, actual)

    def test_create_LDCDigits_push_2_should_be_return_LCDDigits_2(self):
        # arrange
        first_line = "._.\n"
        second_line = "._|\n"
        third_line = "|_."
        expected = first_line + second_line + third_line
        # action
        actual = self.lcd_digits.create_LCD(number=2)
        # assert
        self.assertEquals(expected, actual)

    def test_create_LDCDigits_push_3_should_be_return_LCDDigits_3(self):
        # arrange
        first_line = "._.\n"
        second_line = "._|\n"
        third_line = "._|"
        expected = first_line + second_line + third_line
        # action
        actual = self.lcd_digits.create_LCD(number=3)
        # assert
        self.assertEquals(expected, actual)

    def test_create_LDCDigits_push_10_should_be_return_LCDDigits_10(self):
        # arrange
        first_line = "...._.\n"
        second_line = "..||.|\n"
        third_line = "..||_|"
        expected = first_line + second_line + third_line
        # action
        actual = self.lcd_digits.create_LCD(number=10)
        # assert
        self.assertEquals(expected, actual)

    def test_create_LDCDigits_push_11_should_be_return_LCDDigits_11(self):
        # arrange
        first_line = "......\n"
        second_line = "..|..|\n"
        third_line = "..|..|"
        expected = first_line + second_line + third_line
        # action
        actual = self.lcd_digits.create_LCD(number=11)
        # assert
        self.assertEquals(expected, actual)

    def test_create_LDCDigits_push_12_should_be_return_LCDDigits_12(self):
        # arrange
        first_line = "...._.\n"
        second_line = "..|._|\n"
        third_line = "..||_."
        expected = first_line + second_line + third_line
        # action
        actual = self.lcd_digits.create_LCD(number=12)
        # assert
        self.assertEquals(expected, actual)

    def test_create_LDCDigits_push_100_should_be_return_LCDDigits_100(self):
        # arrange
        first_line = "...._.._.\n"
        second_line = "..||.||.|\n"
        third_line = "..||_||_|"
        expected = first_line + second_line + third_line
        # action
        actual = self.lcd_digits.create_LCD(number=100)
        # assert
        self.assertEquals(expected, actual)

    def test_create_LDCDigits_push_101_should_be_return_LCDDigits_102(self):
        # arrange
        first_line = "...._....\n"
        second_line = "..||.|..|\n"
        third_line = "..||_|..|"
        expected = first_line + second_line + third_line
        # action
        actual = self.lcd_digits.create_LCD(number=101)
        # assert
        self.assertEquals(expected, actual)

    def test_create_LDCDigits_push_102_should_be_return_LCDDigits_102(self):
        # arrange
        first_line = "...._.._.\n"
        second_line = "..||.|._|\n"
        third_line = "..||_||_."
        expected = first_line + second_line + third_line
        # action
        actual = self.lcd_digits.create_LCD(number=102)
        # assert
        self.assertEquals(expected, actual)