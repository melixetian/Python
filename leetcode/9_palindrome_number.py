"""
LC 9. Palindrome Number
https://leetcode.com/problems/palindrome-number/
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        if x < 0 or x % 10 == 0:
            return False

        original = x
        reversed_number = 0
        while x:
            x, digit = divmod(x, 10)
            reversed_number = reversed_number * 10 + digit

        return reversed_number == original
