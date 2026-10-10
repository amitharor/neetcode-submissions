'''
input: array strings
DefaultDict, 
output: grouped anagrams into sub lists

constraints: 
1 <= strs.length <= 10000.
0 <= strs[i].length <= 100
strs[i] is made up of lowercase English letters. (26 lowercase letters)


time: O(n * m)
space: O(n)

approach:

create a default dict to store all anagrams
iterate through lists
get the freq count of the letters of current work (becomes our key) and add to dict

return list of values from dict
'''

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for char in s:
                count[ord(char) - ord('a')] += 1

            grouped[tuple(count)].append(s)

        return list(grouped.values())
