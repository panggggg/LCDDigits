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


class LCDDigits:
    def create_LCD(self, number):
        first_line = "._.\n"
        second_line = "|.|\n"
        third_line = "|_|"
        return first_line + second_line + third_line
