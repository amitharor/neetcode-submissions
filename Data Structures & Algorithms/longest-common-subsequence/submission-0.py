'''
Input(s): two strings
Output: return len of longest common subsequence between the two strings, else return 0

Constraints:
1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.

Approach:
dp 

Time: O(m * n) -> len of string 1 and string 2
Space: O(m * n)
'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1 = len(text1)
        len2 = len(text2)
        common = [[0] * (len2 + 1) for _ in range(len1 + 1)]

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    # last chars match; count it, then solve both strs without it
                    common[i][j] = common[i - 1][j - 1] + 1
                else:
                    dropFromText1 = common[i - 1][j]
                    dropFromText2 = common[i][j - 1]
                    common[i][j] = max(dropFromText1, dropFromText2)

        return common[len1][len2]