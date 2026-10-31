'''
Input(s): int
Output: return num of 1 bits in it's binary representation

Constraints:
0 <= n <= 2^31 - 1 -> 2,147,483,647

Approach:
check the last bit, shift right, repeat

Time: O(1)
Space: O(1)
'''

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n > 0:
            count += n & 1
            n = n >> 1

        return count
        