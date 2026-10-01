'''
input: two strings
output: bool; ret T if they are both anagrams; otherwise ret F

constraints:
1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.

time: O(n)
space: O(1) - 26 lowercase letters

edge case: return f if string lens are different

user counter to get frequency map of the two strings
return True if freq count is the same for both strings; otherwise return False

'''

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return Counter(s) == Counter(t)