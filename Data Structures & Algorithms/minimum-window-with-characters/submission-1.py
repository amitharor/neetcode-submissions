'''
input: two strs
output: shortest substring containing ever char from t (including dups); else ""

constraints:
1 <= s.length <= 100,000
1 <= t.length <= 100,000
s and t consist of uppercase and lowercase English letters.

time: O(n)
space: O(n + k)

approach:
if len of t > len of s or if either string is empty; return ""

init var for freq count of t
init var to get len of t

init var for sub array (hash map)
init var to count if conditon has been met
init result variable to ""
init var to store min length; initialized to float infinity

init left/right pointers
increment right pointer while incrementing count of letter at right pointer
check if element is in freq count of t and is the same amount; if so, increase count condition var

shrink window while valid
update min window length if smaller than what is currently stored there

check if removing it breaks window; if so, decread count condition var
increment left pointer

return result
'''

from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""

        target = Counter(t)
        window = defaultdict(int)

        result = ''
        
        have = 0
        required = len(target)
        min_len = float('inf')
        left = 0

        for right, char in enumerate(s):
            window[char] += 1

            if char in target and window[char] == target[char]:
                have += 1

            while have == required:
                length = right - left + 1
                if length < min_len:
                    min_len = min(min_len, length)
                    result = s[left:right + 1]

                window[s[left]] -= 1

                if s[left] in target and window[s[left]] < target[s[left]]:
                    have -= 1

                left += 1

        return result