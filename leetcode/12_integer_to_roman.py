"""
LC 12. Integer to Roman
https://leetcode.com/problems/integer-to-roman/

В римской системе счисления для обозначения чисел
используются следующие символы:
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

Числа 4, 9, 40, 90, 400 и 900
записываются как вычитание из большего числа меньшего:
IV, IX, XL, XC, CD и CM, соответственно.

Написать функцию для перевода числа из десятичной системы в римскую.
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        numerals = (
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        )
        parts = []
        for value, symbol in numerals:
            count, num = divmod(num, value)
            parts.append(symbol * count)
        return "".join(parts)
