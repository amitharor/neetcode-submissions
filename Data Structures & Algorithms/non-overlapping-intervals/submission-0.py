'''
Input(s): arr (int)
Output: return min num of intervals needed to remove to make the rest of the intervals non overlapping

Constraints:
1 <= intervals.length <= 100,000
intervals[i].length == 2
-50000 <= starti < endi <= 50000

Approach:


Time: O(n log n) 
Space: O(n)
'''


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda interval: interval[1]) #sort by the end
        removed = 0
        lastEnd = intervals[0][1] # end of the last interval

        for start, end in intervals[1:]:
            if start >= lastEnd:
                lastEnd = end # fits after the last kept one
            else:
                removed += 1 # overlap; remove it
                
        return removed