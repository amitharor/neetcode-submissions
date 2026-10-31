'''
Input(s): 32 bit unsigned int
Output: reverse the bits of the binary representation of n and return result

Constraints:


Approach:
Bit manipulation

Time: O(1)
Space: O(1)
'''


class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        
        for _ in range(32):
            lastBit = n & 1
            result = (result << 1) | lastBit
            n = n >> 1

        return result