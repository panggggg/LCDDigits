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

        if number >= 100:

            hunreds = int(number / 100)  # 1 <= หลักร้อย
            tens_digits = int((number - (hunreds * 100)) / 10)  # 0 <=  หลักสิบ
            digit = int(number % 10)  # 1 <= หลักหน่วย
            first_line = (
                list_first_line[hunreds]
                + list_first_line[tens_digits]
                + list_first_line[digit]
            )
            second_line = (
                list_first_line[hunreds]
                + list_first_line[tens_digits]
                + list_first_line[digit]
            )
            third_line = (
                list_first_line[hunreds]
                + list_first_line[tens_digits]
                + list_first_line[digit]
            )

            return "{}\n{}\n{}".format(first_line, second_line, third_line)

        if number >= 10:
            tens_digits = int(number / 10)
            digit = int(number % 10)
            return "{}{}\n{}{}\n{}{}".format(
                list_first_line[tens_digits],
                list_first_line[digit],
                list_second_line[tens_digits],
                list_second_line[digit],
                list_third_line[tens_digits],
                list_third_line[digit],
            )

        else:

            return "{}\n{}\n{}".format(
                list_first_line[number],
                list_second_line[number],
                list_third_line[number],
            )
