'''
Input(s): two int
Output: return sum of two ints without using + and - operators

Constraints:
-1000 <= a, b <= 1000

Approach:
XOR for the sum without carries + AND shifted left for the carries, repeated until there's no carry

Time: O(1)
Space: O(1)
'''

class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        maxInt = 0x7FFFFFFF

        while b != 0:
            carry = (a & b) << 1
            a = (a ^b) & mask
            b = carry & mask

        return a if a <= maxInt else ~(a ^ mask)