'''
Input(s): s1, s2, s3 (str)
Output: bool; retrun True if s3 is formed by interleaving S1 and S2, else return False

Constraints:
0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200

Approach:
dp

Time: O(m * n) -> m is len of s1 and n is len of s2
Space: O(m * n)
'''


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        sCombine = s1 + s2

        len1 = len(s1)
        len2 = len(s2)

        # edge case: if lens don't match
        if len1 + len2 != len(s3):
            return False


        canBuild = [[False] * (len2 + 1) for _ in range(len1 + 1)]
        canBuild[0][0] = True

        for i in range(len1 + 1):
            for j in range(len2 + 1):
                nextCharIndex = i + j - 1 # position in s3 of the last char used

                # 1 -> last char came from s1
                if i > 0 and canBuild[i - 1][j] and s1[i - 1] == s3[nextCharIndex]:
                    canBuild[i][j] = True

                # 2 -> last char came from s2
                if j > 0 and canBuild[i][j - 1] and s2[j - 1] == s3[nextCharIndex]:
                    canBuild[i][j] = True


        return canBuild[len1][len2]