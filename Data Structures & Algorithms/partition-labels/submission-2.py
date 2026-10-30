'''
Input(s): string (lowercase alphabet - 26)
Output: return list of ints representing size of these substring in the order they appear in string

Constraints:
1 <= s.length <= 100

Approach:
greedy - 

Time: O(n)
Space: O(1)
'''

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {letter: i for i, letter in enumerate(s)}

        partSizes = []
        partStart = 0 # where current partition begins
        partEnd = 0 # current partition must reach at least here

        for i, letter in enumerate(s):
            partEnd = max(partEnd, lastIndex[letter])

            if i == partEnd:
                partSizes.append( i - partStart + 1)
                partStart = i + 1

        
        return partSizes