'''
Input(s): two strings
Output: return num of dist subsequences of s which are == t

Constraints:
1 <= s.length, t.length <= 1000
s and t consist of English letters.

Approach:
dp - lcs

Time: O(m * n) -> where m is len of string s and n is len of string t
Space: O(m * n)
'''


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        lenS = len(s)
        lenT = len(t)

        ways = [[0] * (lenT + 1) for _ in range(lenS + 1)]

        for i in range(lenS + 1):
            ways[i][0] = 1 #empty t: one way

        for i in range(1, lenS + 1):
            for j in range(1, lenT + 1):
                skipIt = ways[i - 1][j] # don't use s's last char

                if s[i - 1] == t[j - 1]:
                    useIt = ways[i - 1][j - 1] # match s's last char to t's last char
                    ways[i][j] = skipIt + useIt # two difference choices -> add them
                else:
                    ways[i][j] = skipIt # don't match -> skip
        
        return ways[lenS][lenT]