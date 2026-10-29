'''
Input(s): string
Output: return longest substring of input string that is a palindrome

Constraints:
1 <= s.length <= 1000
s contains only digits and English letters.


Approach:
dp

Time: O(n^2)
Space: O(n^2)
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIndex, resLen = 0, 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True

                    if resLen < (j - i + 1):
                        resIndex = i
                        resLen = j - i + 1

        return s[resIndex: resIndex + resLen]