'''
Input(s): int
Output: bool; return True if x is palindrome; else False

Constraints:
-(2^31) <= x <= ((2^31) - 1)


Approach:
reverse the int

Time: O(n)
Space: O(1)
'''


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reverse = 0
        num = x

        while num:
            reverse = (reverse * 10) + (num % 10)
            num //= 10

        return reverse == x
            