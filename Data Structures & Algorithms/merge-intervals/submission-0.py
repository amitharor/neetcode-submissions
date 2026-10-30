'''
Input(s): arr (int)
Output: return non overlapping intervals that cover all the intervals in the input

Constraints:
1 <= intervals.length <= 1000
intervals[i].length == 2
0 <= start <= end <= 1000

Approach:



Time: O(n log n)
Space: O(n)
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda interval: interval[0]) # sort by start
        merged = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = merged[-1][1] # end of the most recent merged interval

            if start <= lastEnd:
                merged[-1][1] = max(lastEnd, end)
            else:
                merged.append([start, end])

        return merged
