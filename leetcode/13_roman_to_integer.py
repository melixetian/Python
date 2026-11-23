"""
LC 13. Roman to Integer
https://leetcode.com/problems/roman-to-integer/

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

Написать функцию для перевода числа из римской системы в десятичную.
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        previous = 0

        for symbol in reversed(s):
            value = values[symbol]
            total += -value if value < previous else value
            previous = value

        return total
