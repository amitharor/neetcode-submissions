'''
Input(s): string, list (str)
Output: bool; return true if string can be split into any combination of words in wordDict

Constraints:
1 <= s.length <= 200
1 <= wordDict.length <= 100
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.

Approach:
dp (bottom up)

Time: O(n * w * t) -> where w is num of words and l is longest word
Space: O(n)
'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        canSplit = [False] * (n + 1)
        canSplit[0] = True # empty string -> nothing to split

        for end in range(1, n + 1):
            for word in wordDict:
                start = end - len(word) #start of word
                if start < 0:
                    continue # word is too long

                if canSplit[start] and s[start:end] == word:
                    canSplit[end] = True
                    break

        return canSplit[n]


