'''
input: str
output: len of longest substr with the same char

constraints:
1 <= s.length <= 100,000
0 <= k <= s.length
s consists of only uppercase english characters.

time: O(n)
space: O(k)

approach:
init left/right pointers starting at the beginning
init var to track longest len of substring (result)
init var to track most freq char in our substring


iterate through string
increment right pointer and keep updating most freq char length and keep incrementing as long as the substring len - most freq char >= k; and update result var
otherwise; increment left pointer until substring len - most freq char <= k

return result

'''
from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        result = 0
        max_freq = 0
        char_count = defaultdict(int)

        for right in range(len(s)):
            char_count[s[right]] += 1
            max_freq = max(max_freq, char_count[s[right]])

            while (right - left + 1) - max_freq > k:
                char_count[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)        
                
        return result