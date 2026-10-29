'''
Input(s): string
Output: return num of substrings within s that are palindome

Constraints:
1 <= s.length <= 1000
s consists of lowercase English letters.

Approach:
two pointer

Time: O(n^2)
Space: O(1)
'''

class Solution:
    def countSubstrings(self, s: str) -> int:
        totalCount = 0

        def countFrom(left, right):
            found = 0

            while left >= 0 and right < len(s) and s[left] == s[right]:
                found += 1
                left -= 1 # expanding outward
                right += 1
            return found

        for center in range(len(s)):
            totalCount += countFrom(center, center) # odd
            totalCount += countFrom(center, center + 1) # even

        
        return totalCount
