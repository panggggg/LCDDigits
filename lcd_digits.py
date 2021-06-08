# 0 -> 0
# 1 -> 1
# 2 -> 2
# 3 -> 3
# 4 -> 4
# 5 -> 5
# 6 -> 6
# 7 -> 7
# 8 -> 8
# 9 -> 9
# 910 -> 910


from typing import List


class LCDDigits:
    def create_LCD(self, number):

        list_first_line = ["._.", "...", "._.", "._."]
        list_second_line = ["|.|", "..|", "._|", "._|"]
        list_third_line = ["|_|", "..|", "|_.", "._|"]

        if number >= 10:
            tens_digits = int(number / 10)
            digit = int(number % 10)
            first_line = list_first_line[tens_digits] + list_first_line[digit] + "\n"
            second_line = list_second_line[tens_digits] + list_second_line[digit] + "\n"
            third_line = list_third_line[tens_digits] + list_third_line[digit]
            return first_line + second_line + third_line

        else:

            return "{}\n{}\n{}".format(
                list_first_line[number],
                list_second_line[number],
                list_third_line[number],
            )
