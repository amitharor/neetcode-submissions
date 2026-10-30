'''
Input(s): array (int)
Output: return min num of rooms required to schedule all meeting without any conflicts

Constraints:
0 <= intervals.length <= 100,000
0 <= intervals[i].start < intervals[i].end <= 1,000,000


Approach:
sort by start -> min heap of room end times

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

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda interval: interval.start) # meetings in start order
        roomEndTimes = []

        for interval in intervals:
            if roomEndTimes and roomEndTimes[0] <= interval.start:
                heapq.heappop(roomEndTimes) # take room that is free

            heapq.heappush(roomEndTimes, interval.end) # this room is busy

        return len(roomEndTimes)