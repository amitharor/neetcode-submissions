'''
Input(s): int
Output: return arry where output[i] is the num of 1's in the binary representation of i

Constraints:
0 <= n <= 1000

Approach:
DP using the ans for i >> 1

Time: O(n)
Space: O(1)
'''

class Solution:
    def countBits(self, n: int) -> List[int]:
        ones = [0] * (n + 1)

        for i in range(1, n+ 1):
            ones[i] = ones[ i >> 1] + (i & 1)

        return ones