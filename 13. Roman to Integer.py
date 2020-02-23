"""

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9.
    X can be placed before L (50) and C (100) to make 40 and 90.
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

"""


"""---SOLUTION---"""


class Solution:
    def romanToInt(self, s):

        roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        j = ''
        number = 0
        for i in s:
            if i in roman:
                r = roman.index(i)
                number += numbers[r]
                if (i == "M" and j == 'C') or (i == "D" and j == "C"):
                    number -= 200
                elif (i == "C" and j == "X") or (i == "L" and j == "X"):
                    number -= 20
                elif (i == "X" and j == "I") or (i == "V" and j == "I"):
                    number -= 2
                j = i
        return number

