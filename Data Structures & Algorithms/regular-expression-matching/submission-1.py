'''
Input(s): s (str), p (str)
Output: bool; return True if pattern matches the entire input str, otherwise False

Constraints:
1 <= s.length <= 20
1 <= p.length <= 20
Each appearance of '*', will be preceded by a valid character or '.'.

Approach:
dp

Time: O(m * n) -> m is len of string s and n is len of string p
Space: O(m * n)
'''


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        lenS = len(s)
        lenP = len(p)

        matches = [[False] * (lenP + 1) for _ in range(lenS + 1)]
        matches[0][0] = True # empty matches True

        # empty s can match patterns like a*, a*b -> zero copies of each
        for j in range(2, lenP + 1):
            if p[j - 1] == '*':
                matches[0][j] = matches[0][j - 2]


        for i in range(1, lenS + 1):
            for j in range(1, lenP + 1):
                sChar = s[i - 1]
                pChar = p[j - 1]

                if pChar == '*':
                    repeatedChar = p[j - 2] # the char that '*' applies to
                    zeroCopies = matches[i][j - 2] # skip 'x*' entirely
                    charFits = repeatedChar == sChar or repeatedChar == '.'
                    oneMoreCopy = charFits and matches[i - 1][j] # use s char, keep 'x*'
                    matches[i][j] = zeroCopies or oneMoreCopy
                else:
                    charFits = pChar == sChar or pChar == '.'
                    matches[i][j] = charFits and matches[i - 1][j - 1] # both step back

        return matches[lenS][lenP]