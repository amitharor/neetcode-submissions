'''
input: two strings

output: bool; return true if two strings are anagram; otherwise false

constraints: 
-> 1 <= s.length, t.length <= 5 * 10^4
-> s and t consist of lowercase English letters.

time: O(n)
space: O(1)

we can use Counter function to count the number of each character
compare the counted strings; if they are the same; return true; otherwise False

'''

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)