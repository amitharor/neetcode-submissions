'''
i: list of strings
o: list of list of grouped anagrams

constraints:
1 <= strs.length <= 10000.
0 <= strs[i].length <= 100
strs[i] is made up of lowercase English letters.

edge:

time: O(n * k)
space: O(n)

init defaultdict - list

iterate through list
init var to store count of letters of curr element -> init to list of 26 0s
iterate through each word
count letters and store in count var
append count(tuple) and word into defaultdict

return list of vals from defaultdict

'''

from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        seen = defaultdict(list)


        for word in strs:
            count = [0] * 26
            
            for letter in word:
                count[ord(letter) - ord('a')] +=1

            seen[tuple(count)].append(word)

        return list(seen.values())




