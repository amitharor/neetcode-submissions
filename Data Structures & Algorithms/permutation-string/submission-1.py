'''
input: strings s1 and s2
output: bool; true if s2 contains permutation of s1; else False

constraints:
1 <= s1.length, s2.length <= 10000


time: O(n)
space: O(k)

approach:
keep track of the letter freq of s1
init var to store length of s1

init left/right pointers for sliding window
init var to store char count of substring


iterate through s2
count every character count at right index
increment right index


if the substring len > len of s1;
remove elements at left index
increment left pointer

if char freq of current subarray == char freq of s1: return True


return False

'''

from collections import Counter, defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        target = Counter(s1)
        window = defaultdict(int)
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

