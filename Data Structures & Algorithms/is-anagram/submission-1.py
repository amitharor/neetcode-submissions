'''
input: two strings
output: bool; ret T if they are both anagrams; otherwise ret F

constraints:
1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.

time: O(n)
space: O(n)

edge case: return f if string lens are different

sort the strings and compare
return T if match, otherwise return F

'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)