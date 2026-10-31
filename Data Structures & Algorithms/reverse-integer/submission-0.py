'''
Input(s): 32 bit int
Output: return x after reversing each of its digits, return 0 if outside the signed 32 bit range

Constraints:
-2^31 <= x <= 2^31 - 1

Approach:
Recursion

Time: O(1)
Space: O(1)
'''

class Solution:
    def reverse(self, x: int) -> int:
        def rec(n, rev):
        
            if n == 0:
                return rev


            rev = rev * 10 + n % 10
            return rec(n // 10, rev)

        sign = -1 if x < 0 else 1
        x = abs(x)
        reversedNum = rec(x, 0)
        reversedNum *= sign
        if reversedNum < -(1 << 31) or reversedNum > (1 << 31) - 1:
            return 0

        return reversedNum