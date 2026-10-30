'''
Input(s): two strings
Output: return min num of ops to make word1 into word2

Constraints:
0 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.

Approach:
dp -> lcs

Time: O(m * n) - > where m is len of word 1 and n is len of word 2
Space: O(m * n)
'''

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1 = len(word1)
        len2 = len(word2)

        edits = [[0] * (len2 + 1) for _ in range(len1 + 1)]

        # i chars into empty -> del all i
        for i in range(len1 + 1):
            edits[i][0] = i

        # empty into j chars -> ins all j
        for j in range(len2 + 1):
            edits[0][j] = j
    

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    edits[i][j] = edits[i - 1][j - 1]
                else:
                    replaceCost = edits[i -1][j - 1] # change word1's last char into word2's last char
                    deleteCost = edits[i -1][j] # remove word1's last char
                    insertCost = edits[i][j - 1] # add word2's last char to word1
                    edits[i][j] = 1 + min(replaceCost, deleteCost, insertCost)

        return edits[len1][len2]