'''
input: two strs
output: bool; True is permutation of s1 exists in s1; else False

constraints:
1 <= s1.length, s2.length <= 10000
both strings contain lowercase letters (26 chars)


time: O(n)
space: O(1)

approach:

if len of s1 > s2; return False

init left/right pointers for sliding window
init var to store char count from s2's subarray
init var to get count of s1

iterate through array
increment and add char from right pointer to subarray

if len of subarray > len of s1 then remove element(s) from left pointer 
if char at left index's count is zero; delete letter from hash map
increment left pointer

if subarray == to s1; return true

otherwise; return False

'''

from collections import Counter, defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        target = Counter(s1)
        window = defaultdict(int) #subarray window
        left = 0

        for right, char in enumerate(s2):
            window[char] += 1

            if (right - left + 1) > len(s1):
                outgoing = s2[left]
                window[outgoing] -= 1

                if window[outgoing] == 0:
                    del window[outgoing]
                
                left += 1

            if window == target:
                return True

        return False





