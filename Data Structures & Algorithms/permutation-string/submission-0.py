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

from collections import defaultdict, Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1
        s1_char_count = Counter(s1)
        s1_len = len(s1)

        # s2
        left = 0
        s2_char_count = defaultdict(int)
        

        for right in range(len(s2)):
            substr_len = right - left + 1
            
            s2_char_count[s2[right]] += 1
            
            while (right - left + 1) > s1_len:
                s2_char_count[s2[left]] -= 1
                if s2_char_count[s2[left]] == 0:
                    del s2_char_count[s2[left]]
                left += 1

            if s2_char_count == s1_char_count:
                return True



        return False