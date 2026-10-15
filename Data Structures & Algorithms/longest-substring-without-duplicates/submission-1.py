'''
input: string
output: len of longest substring

constraints:
0 <= s.length <= 50,000
s may consist of printable ASCII characters.


time: O(n)
space: O(1)


approach:
init left/right pointers
init var to store results
init var to store seen chars

iterate through string
increment right point as long as we have not seen the char
incrementing results count
if so, remove every element from the left point
increment left pointer
decrement results count


return results

'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        results = 0
        seen = set()

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            seen.add(s[right])
            results = max(results, right - left + 1)

        return results











        