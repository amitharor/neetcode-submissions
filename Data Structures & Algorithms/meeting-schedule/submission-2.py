'''
Input(s): arr (int)
Output: bool; return True if person could add all meetings to their schedule without any conflicts; otherwise False

Constraints:
0 <= intervals.length <= 500
0 <= intervals[i].start < intervals[i].end <= 1,000,000

Approach:
sort by start -> then check each pair of neighbors

Time: O(n log n)
Space: O(n)
'''


"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda interval: interval.start) # sorting by start time

        for i in range(1, len(intervals)):
            previousEnd = intervals[i - 1]
            currentStart = intervals[i]

            if currentStart.start < previousEnd.end: # starts before the last one ends
                return False
        
        return True