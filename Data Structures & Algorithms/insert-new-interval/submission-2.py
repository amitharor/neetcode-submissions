'''
Input(s): arr of non overlapping intervals (int), interval (int)
Output: return intervals after adding new interval

Constraints:
0 <= intervals.length <= 10000
newInterval.length == intervals[i].length == 2
0 <= start <= end <= 100000

Approach:
interval search

Time: O(n)
Space: O(1)
'''


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []
        newStart, newEnd = newInterval
        i = 0
        n = len(intervals)

        # intervals that end before new one starts
        while  i < n and intervals[i][1] < newStart:
            merged.append(intervals[i])
            i += 1

        # intervals that start before the new one ends
        while i < n and intervals[i][0] <= newEnd:
            newStart = min(newStart, intervals[i][0]) # widen to left
            newEnd = max(newEnd, intervals[i][1]) # widen to right
            i += 1
        merged.append([newStart, newEnd]) # the merged new interval

        # everything left starts after the new one ends
        while i < n:
            merged.append(intervals[i])
            i += 1

        return merged