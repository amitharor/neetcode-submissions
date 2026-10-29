'''
Input(s): string
Output: return num of ways to decode it

Constraints:
1 <= s.length <= 100
s consists of digits

Approach:
dp

Time: O(n)
Space: O(n)
'''

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        ways = [0] * (n + 1)
        ways[0] = 1

        for i in range(1, n + 1):
            oneDigit = s[i - 1]
            if oneDigit != '0':
                ways[i] += ways[i - 1]

            
            if i >= 2:
                twoDigits = int(s[i - 2: i])
                if 10 <= twoDigits <= 26:
                    ways[i] += ways[i - 2]

        return ways[n]