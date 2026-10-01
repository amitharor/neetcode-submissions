'''
i: list of strings
o: list of list of grouped anagrams

constraints:
1 <= strs.length <= 10000.
0 <= strs[i].length <= 100
strs[i] is made up of lowercase English letters.



edge:

time: O(n)
space: O(n)

init defaultdict list to store grouped anagrams

iterate through loop
init var to count to alphabet len
set count to letter freq of current element
append current element at tuple count in defaultdict


return list of vals from defaultdict

'''

from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        seen = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for letter in word:
                count[ord(letter) - ord('a')] += 1

            seen[tuple(count)].append(word)

        return list(seen.values())